import sys
from detect import iszkowebism
from decode import decode, decodewithescape


def fromfile(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        sys.stderr.write('usage: python run.py <file>\n')
        sys.exit(1)
    src = fromfile(sys.argv[1])
    if not iszkowebism(src):
        sys.stderr.write('not zkowebism\n')
        sys.exit(2)
    out = decode(src)
    if out is None:
        out = decodewithescape(src)
    if out is None:
        sys.stderr.write('decode failed\n')
        sys.exit(3)
    sys.stdout.write(out)
    sys.stdout.write('\n')


if __name__ == '__main__':
    main()
