from typing import Any, Callable

Grid = list[list[int | str | None]]
Roi = tuple[slice, slice]
Convolution = Callable[[Grid, Roi], Any]


def center(grid: Grid, roi: Roi) -> int | str | None:
    x, y = roi
    x_center = (x.start + x.stop - 1) // 2
    y_center = (y.start + y.stop - 1) // 2
    return grid[y_center][x_center]


def sum_grid(grid: Grid, roi: Roi | None = None) -> int | float:
    x, y = roi if roi is not None else (slice(None), slice(None))
    return sum(item for row in grid[y] for item in row[x] if isinstance(item, (int, float)))


def count(grid: Grid, roi: Roi | None = None) -> int | float:
    return count_if(grid, True, roi)


def count_if(grid: Grid, value: int | str | bool, roi: Roi | None = None) -> int | float:
    x, y = roi if roi is not None else (slice(None), slice(None))
    return sum(1 for row in grid[y] for item in row[x] if item == value)


def convolve(
    grid: list[list[int | str]],
    fn: Convolution,
    nbh: int | tuple[int, int] = 3,
    wrap: bool = False,
    fill: int | str | None = None,
    initial: int | str = 0,
    update: bool = False,
    debug: bool = False,
):
    # dimensions
    height, width = len(grid), len(grid[0])
    w, h = (nbh, nbh) if isinstance(nbh, int) else nbh

    # source grid with
    if wrap:
        source = _make_wrapped_source(grid, w, h)
    else:
        source = _make_padded_source(grid, w, h, fill)

    # result grid
    result = [[initial] * width for _ in range(height)]

    # convolution
    for cy in range(height):
        y_slice = slice(cy, cy + h)
        for cx in range(width):
            x_slice = slice(cx, cx + w)
            if update:
                result[cy][cx], grid[cy][cx] = fn(source, (x_slice, y_slice))
            else:
                result[cy][cx] = fn(source, (x_slice, y_slice))
            if debug:
                _debug_step(source, (x_slice, y_slice), result[cy][cx])

    return result


def _make_padded_source(grid, kw, kh, fill):
    width = len(grid)
    kw_half, kh_half = kw // 2, kh // 2
    padded_w = width + kw - 1

    # top margin row(s)
    source = [[fill] * padded_w for _ in range(kh_half)]

    # data rows with left/right margins
    for row in grid:
        source.append([fill] * kw_half + list(row) + [fill] * kw_half)

    # bottom margin row(s)
    source.extend([[fill] * padded_w for _ in range(kh_half)])

    return source


def _make_wrapped_source(grid, kw, kh):
    source = []
    height, width = len(grid), len(grid[0])
    kw_half, kh_half = kw // 2, kh // 2
    for dy in range(-kh_half, height + kh_half):
        src_row = grid[dy % height]
        row = []
        for dx in range(-kw_half, width + kw_half):
            row.append(src_row[dx % width])
        source.append(row)
    return source


def _debug_step(source, roi, result):
    print()
    x, y = roi
    print(f"({x.start}, {y.start}): {center(source, roi)} => {result}")
    for row in source[y]:
        cells = [v if v is not None else " " for v in row[x]]
        if all(isinstance(c, str) and len(c) == 1 for c in cells):
            print(f" [{''.join(cells)}]")
        elif all(isinstance(c, int) and 0 <= c < 10 for c in cells):
            print(f" [{''.join(str(c) for c in cells)}]")
        else:
            print(f" [{' '.join(str(c) for c in cells)}]")
