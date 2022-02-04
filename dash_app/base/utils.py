import os
import yaml
import logging.config
import logging


def setup_logging(path='dash_app/logging.yaml', default_level=logging.INFO):
    """
    reading the log config file, a YAML file, and creating the loggers
    """
    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)
            except Exception as e:
                print(e)
                print('Error in logging config')
    else:
        print(path)
        logging.basicConfig(level=default_level)
        print('Failed to load the configuration...')
