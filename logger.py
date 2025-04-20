import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup a logger with a specific name and log file.

    Args:
        name (str): The name of the logger.
        log_file (str): The file where logs will be written.
        level (int): The logging level. Default is logging.INFO.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers
    file_handler = logging.FileHandler(log_file)
    stream_handler = logging.StreamHandler()

    # Create formatters and add them to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

def log_message(logger, message, level=logging.INFO):
    """Function to log a message with a specific logging level.

    Args:
        logger (logging.Logger): The logger instance.
        message (str): The message to log.
        level (int): The logging level. Default is logging.INFO.
    """
    if level == logging.DEBUG:
        logger.debug(message)
    elif level == logging.INFO:
        logger.info(message)
    elif level == logging.WARNING:
        logger.warning(message)
    elif level == logging.ERROR:
        logger.error(message)
    elif level == logging.CRITICAL:
        logger.critical(message)
    else:
        logger.info(message)