import logging
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler


def init_logging():
    stream_handler = StreamHandler()
    timed_file_handler = TimedRotatingFileHandler(
        filename="logs/all.log",
        when="midnight",
        interval=1,
        backupCount=7,
    )

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S %z",
        handlers=[stream_handler, timed_file_handler],
    )
