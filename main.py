import sys
from nlp.cli import main
from nlp.cli import DEFAULT_CONFIG_PATH


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(DEFAULT_CONFIG_PATH)
    else:
        main(sys.argv[1])
