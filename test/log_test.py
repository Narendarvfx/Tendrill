import logging
import logging.handlers

logger = logging.getLogger('myLogger')
logger.setLevel(logging.DEBUG)

# Add handler to the logger
handler = logging.handlers.SysLogHandler(address=('192.168.10.15', 514))

# Add formatter to the handler
formatter = logging.Formatter('Python: { "loggerName":"%(name)s", "asciTime":"%(asctime)s", "pathName":"%(pathname)s", "logRecordCreationTime":"%(created)f", "functionName":"%(funcName)s", "levelNo":"%(levelno)s", "lineNo":"%(lineno)d", "time":"%(msecs)d", "levelName":"%(levelname)s", "message":"%(message)s"}')

handler.formatter = formatter
logger.addHandler(handler)
for _ in range(100):
    logger.debug("Test Message")