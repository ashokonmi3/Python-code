"""
Logging Demo 1
Logging Levels

DEBUG
INFO
WARNING (default level)
ERROR
CRITICAL
"""
# =====================================
# Default mode : Warning
# import logging
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')
# x=10
# logging.debug("hi ",x)
# =====================
# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# =====================================
# Some of the commonly used parameters for basicConfig() are the following:
# level: The root logger will be set to the specified severity level.
# filename: This specifies the file.
# filemode: If filename is given, the file is opened in this mode. The default is a, which means append.
# format: This is the format of the log message.
# default mode for file is append mode
#
# import logging
# logging.basicConfig(filename="test.log", level=logging.DEBUG)
# logging.warning("warning message")
# logging.info("info message")
# logging.error("error message")
# =========================
# import logging
# name = 'John'
# logging.error('%s raised an error', name)
# =================

# Capturing Stack Traces
# The logging module also allows you to capture the full stack traces in an
# application.
# Exception information can be captured if the exc_info parameter is passed as True,
# and the logging functions are called like this:

# import logging
#
# a = 5
# b = 0
#
# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)
#   logging.error("Exception occurred")

# =====================

# If exc_info is not set to True, the output of the above program would not
# tell us anything about the exception, which, in a real-world scenario, might 
# not be as simple as a ZeroDivisionError

# import logging
# a = 5
# b = 0
#
# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=False)
# =====================
 # if you’re logging from an exception handler, use the logging.exception() method,
# which logs a message with
# level ERROR and adds exception information to the message.
# To put it more simply, calling logging.exception()
# is like calling logging.error(exc_info=True).
# But since this method always dumps
# exception information, it should only be called from an exception handler. Take a look at this example:

# import logging
#
# a = 5
# b = 0
# try:
#   c = a / b
# except Exception as e:
#   logging.exception("Exception occurred") #logging.error(exc_info=True).

# ==========================
#default logger named root, which is used by the logging module whenever its functions are called directly

# import logging
#
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will get logged to a file')
# logging.info("info message")
# logging.error("error message")
# =======================
# Logging Format
# https://docs.python.org/3/library/logging.html#logrecord-attributes
# https://docs.python.org/3/library/time.html#time.strftime

# import logging
#
# logging.basicConfig(filename='app.log', filemode='w',format='%(asctime)s: %(levelname)s: %(message)s',
#                     datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.WARNING)
# logging.warning("warning message")
# logging.info("info message")
# logging.error("error message")

# =================
# The most commonly used classes defined in the logging module are the following:
#
# Logger: This is the class whose objects will be used in the application code directly to call
# the functions.
#
# LogRecord: Loggers automatically create LogRecord objects that have all the information
# related to the event being logged, like the name of the logger, the function,
# the line number, the message, and more.
#
# Handler: Handlers send the LogRecord to the required output destination,
# like the console or a file. Handler is a base for subclasses like StreamHandler,
# FileHandler, SMTPHandler, HTTPHandler, and more.
# These subclasses send the logging outputs to corresponding destinations,
# like sys.stdout or a disk file.
#
# Formatter: This is where you specify the format of the output by specifying a
# string format that lists out the attributes that the output should contain.
#
# import logging
#
# logger = logging.getLogger('example_logger')
# logger.warning('This is a warning')

# =======================
# Handlers come into the picture when you want to configure your own loggers and send the
# logs to multiple places when they are generated. Handlers send the log messages to configured
# destinations like the standard output stream or a file or over HTTP or to your email via SMTP.

# The name of the logger corresponding to the __name__ variable is logged as __main__,
# which is the name Python assigns to the module where execution starts.
# If this file is imported by some other module, then the __name__ variable would correspond to its name
#
# import logging
#
# logger = logging.getLogger('simple_example')
# logger.setLevel(logging.DEBUG)
# # create file handler which logs even debug messages
# fh = logging.FileHandler('spam.log')
# fh.setLevel(logging.DEBUG)
# # create console handler with a higher log level
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# # create formatter and add it to the handlers
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# ch.setFormatter(formatter)
# fh.setFormatter(formatter)
# # add the handlers to logger
# logger.addHandler(ch)
# logger.addHandler(fh)
#
# # 'application' code
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')

