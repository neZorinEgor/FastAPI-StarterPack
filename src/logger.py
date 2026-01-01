import json
import logging
import logging.config
from pathlib import Path


def init_logger(config_path: Path):
    """
    Docstring for init_logger
    
    :param config_path: Description
    :type config_path: str
    """
    with open(config_path, "r") as config_file:
        config_data = json.loads(config_file.read())
    logging.config.dictConfig(config_data)

