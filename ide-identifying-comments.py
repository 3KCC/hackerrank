# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

pattern = '//.*(?:\n|\r|$)|/\*(?:.|\n|\r)*?\*/'

s = ''
for line in sys.stdin:
    s += line

founds = re.findall(pattern, s)
for f in founds:
    print re.sub('\n\s+', '\n', f).strip()