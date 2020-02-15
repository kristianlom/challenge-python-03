# Resolve the problem!!
import io
import re


def run():
    with io.open("encoded.txt", "r", encoding='utf-8') as f:
        y = re.compile('[a-z]').findall(f.readline())
        print(''.join(y))


if __name__ == '__main__':
    run()
