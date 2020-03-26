import sys

with open(sys.argv[1], 'rt', encoding='utf8') as f:
    for line in f:
        sys.stdout.write(line)
