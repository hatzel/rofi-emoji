#!/usr/bin/env python3
import emoji_data_python
from sys import argv
from subprocess import call

if len(argv) == 1:
    for k, v in emoji_data_python.emoji_short_names.items():
        print(" ".join(v.short_name.split("_")), v.char, sep="\t")
else:
    name, emoji = argv[1].split("\t")
    codepoints = [ord(c) for c in emoji]
    for c in codepoints:
        call(["xdotool", "key", "U" + hex(c)[2:]])
