import sys
import yaml
DEFAULT_CONFIG_PATH = '/examples/1.yml'

class MinmlNlp(object):
    """docstring for MinmlNlp"""
    def __init__(self, config_path):
        self.config_path = config_path

    def run(self):
        print('running nlp config: {}'.format(self.config_path))

def main(config_path):
    mnlp = MinmlNlp(config_path)
    mnlp.run()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main(DEFAULT_CONFIG_PATH)
    else:
        main(sys.argv[1])
