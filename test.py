#!/usr/bin/env python
# coding: utf-8
import re
import os


def revise_readme(readme_path="README.md"):
    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("README-NEW.md", "w", encoding="utf-8") as f:
        for line in lines:
            if line[0] == "*" or line[0] == "-":
                if line[2] == "h":
                    pat = re.compile(r'[(](.*?)[)]', re.S)
                    name = re.findall(pat, line)
                    if len(name) > 0:
                        line_list = line.split("(")
                        if line[0] == "*":
                            line = "* " + name[0] + ": " + line_list[0][2:] + "\n"
                        else:
                            line = "- " + name[0] + ": " + line_list[0][2:] + "\n"
            f.write(line)
    os.rename(readme_path, "README_OLD.md")
    os.rename("README-NEW.md", readme_path)

if __name__ == "__main__":
    revise_readme()
