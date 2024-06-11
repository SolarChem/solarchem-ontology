import configparser
import os

parser = configparser.ConfigParser()

conf_file = os.path.join(os.path.dirname(__file__), 'settings.conf')
parser.read(conf_file)