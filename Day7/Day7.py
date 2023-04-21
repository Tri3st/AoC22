"""Day 7"""
from Day7.DirTree import DirTree
from MyMods.ReadDataFile import read_data
import re

data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split("\n")


def part1():
	my_dir = DirTree()
	my_dir.command("$ ls")
	my_dir.command("dir a")
	my_dir.command("14848514 b.txt")
	my_dir.command("8504156 c.dat")
	my_dir.command("dir d")
	print(my_dir)


def part2():
	pass
