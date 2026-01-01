import json
import logging
import logging.config


def init_logger(config_path: str):
    """
    Docstring for init_logger
    
    :param config_path: Description
    :type config_path: str
    """
    with open(config_path, "r") as config_file:
        config_data = json.loads(config_file.read())
    logging.config.dictConfig(config_data)
    
