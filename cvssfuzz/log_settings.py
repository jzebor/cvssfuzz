import logging.config

# logger settings. you can change these values if you want.
logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': {
        'cvssfuzz': {  # Replace 'cvssfuzz' with your package name
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': False
        }
    },
    'root': {
        'handlers': ['default'],
        'level': 'INFO'
    }
}

def setup_logging():
    """Just setup the logging. Parking function here for now."""
    logging.config.dictConfig(logging_config)