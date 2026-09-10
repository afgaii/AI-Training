import logging

# Configure the logger
logging.basicConfig(
                    filename='app.log',
                    level=logging.INFO)

logging.info("Logger is configured and ready to use.")

logger = logging.getLogger("my_logger")