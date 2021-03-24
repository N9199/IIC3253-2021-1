#!/usr/bin/python3
import re
import mmap
import sys
import subprocess

with open(sys.argv[1], 'r') as f:
    content = f.read()
    content_new = re.sub(
        r'(\\begin\{prob\}\n)(.|\n)*?(\\end\{prob\})', r'\1\n\3', content,
        flags=re.M)
    content_new = re.sub(
        r'(\\begin\{sol\}\n)(.|\n)*?(\\end\{sol\})', r'\1\n\3', content_new,
        flags=re.M)

with open(sys.argv[1], 'w') as f:
    print(content_new, file=f)

