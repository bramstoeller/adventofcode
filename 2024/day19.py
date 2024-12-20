# Advent of Code 2024, Day 19
# https://adventofcode.com/2024/day/19
import re


# Part One
def load_data(file_name):
    data = open(file_name, "r").read()
    towels, patterns = data.split("\n\n")
    towels = list(towels.strip().split(", "))
    patterns = [line.strip() for line in patterns.strip().split("\n")]
    return towels, patterns


def can_form(word, other_words):
    if len(word) == 0:
        return True
    for w in other_words:
        if word.startswith(w):
            if can_form(word[len(w):], other_words):
                return True
    return False


def reduce_list(strings):
    result = []
    for word in strings:
        other_words = [w for w in strings if w != word]
        if not can_form(word, other_words):
            result.append(word)
    return result


def fn_1(towels, patterns):
    towels = reduce_list(towels)
    regex = re.compile(r'(' + "|".join(towels) + r')+')
    matches = {p for p in patterns if regex.fullmatch(p)}
    return matches


def part_1(file_name):
    return len(fn_1(*load_data(file_name)))


# Part Two

def all_can_form(word, other_words):
    if len(word) == 0:
        return [[]]
    matches = []
    for w in other_words:
        if word.startswith(w):
            matches += [[w] + m for m in all_can_form(word[len(w):], other_words)]
    return matches


def count_can_form(word, other_words):
    if len(word) == 0:
        return 1
    matches = 0
    for w in other_words:
        if word.startswith(w):
            matches += count_can_form(word[len(w):], other_words)
    return matches


def count_can_form_grouped(word, other_words):
    if len(word) == 0:
        return 1
    matches = 0
    for n, word_set in other_words:
        if word[:n] in word_set:
            matches += count_can_form_grouped(word[n:], other_words)
    return matches


def group_towels(towels):
    grouped = {}
    for p in towels:
        n = len(p)
        if n not in grouped:
            grouped[n] = set()
        grouped[n].add(p)
    return list((n, frozenset(towel_set)) for n, towel_set in grouped.items())


def towel_tree(towels):
    tree = {}
    for t in towels:
        node = tree
        for i in range(len(t)):
            c = ord(t[i])
            if c not in node:
                node[c] = {}
            node = node[c]
        node[0] = {}
    return tree


def in_tree(tree, word):
    node = tree
    for c in word:
        if c not in node:
            return False
        node = node[c]
    return 0 in node


def count_can_form_in_tree(word, tree):
    if len(word) == 0:
        return 1
    matches = 0
    for n in range(1, min(9, len(word) + 1)):
        if in_tree(tree, word[:n]):
            matches += count_can_form_in_tree(word[n:], tree)
    return matches


def print_tree(tree, indent=0):
    for k, v in tree.items():
        print(" " * indent + (chr(k) if k != 0 else "0"))
        print_tree(v, indent + 1)


def fn_2a(towels, patterns):
    matches = 0
    for i, p in enumerate(patterns):
        n = count_can_form(p, towels)
        matches += n
    return matches


def fn_2b(towels, patterns):
    matches = 0
    towels = group_towels(towels)
    for i, p in enumerate(patterns):
        n = count_can_form_grouped(p, towels)
        matches += n
    return matches


def fn_2c(towels, patterns):
    matches = 0
    towels = towel_tree(towels)
    for i, p in enumerate(patterns):
        p = [ord(c) for c in p]
        n = count_can_form_in_tree(p, towels)
        matches += n
    return matches


def part_2_comparison(file_name):
    data = load_data(file_name)
    start = time.time()
    fn_2a(*data)
    print("A:", time.time() - start)
    start = time.time()
    fn_2b(*data)
    print("B:", time.time() - start)
    start = time.time()
    fn_2c(*data)
    print("C:", time.time() - start)
    return fn_2c(*data)
def part_2(file_name):
    data = load_data(file_name)
    return fn_2b(*data)


import time

if __name__ == "__main__":
    print("1. Example:", part_1("data/day19-example.txt"), "=? 6")
    print("1. Answer:", part_1("data/day19-data.txt"))
    print("2. Example:", part_2("data/day19-example.txt"), "=? 16")
    print("2. Example:", part_2_comparison("data/day19-example2.txt"))
    # print("2. Answer:", part_2("data/day19-data.txt"))
