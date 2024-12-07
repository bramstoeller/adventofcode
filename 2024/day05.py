# Advent of Code 2024, Day 5
# https://adventofcode.com/2024/day/5


# Part One
def load_data(file_name):
    rule_data, update_data = open(file_name, "r").read().split("\n\n")
    rules = [list(map(int, line.split("|"))) for line in rule_data.strip().split("\n")]
    rules_dict = {page: [b for a, b in rules if a == page] for page in set(x for x, _ in rules)}
    updates = (list(map(int, line.split(","))) for line in update_data.strip().split("\n"))
    return rules_dict, updates


def is_valid_update(update, rules):
    return all(all(r not in update[:i] for r in rules.get(page, [])) for i, page in enumerate(update))


def part_1(file_name):
    rules, updates = load_data(file_name)
    valid_updates = (update for update in updates if is_valid_update(update, rules))
    return sum(update[len(update) // 2] for update in valid_updates)


# Part Two
class PageCompare:
    def __init__(self, page, rules):
        self.page = page
        self.rules = rules.get(page, [])

    def __lt__(self, other):
        return self.page in other.rules


def correct_updates(updates, rules):
    return (sorted(update, key=lambda page: PageCompare(page, rules)) for update in updates)


def part_2(file_name):
    rules, updates = load_data(file_name)
    invalid_updates = (update for update in updates if not is_valid_update(update, rules))
    corrected_updates = correct_updates(invalid_updates, rules)
    return sum(update[len(update) // 2] for update in corrected_updates)


if __name__ == "__main__":
    print("1. Example:", part_1("data/day05-example.txt"), "=? 143")
    print("1. Answer:", part_1("data/day05-data.txt"))
    print("2. Example:", part_2("data/day05-example.txt"), "=? 123")
    print("2. Answer:", part_2("data/day05-data.txt"))
