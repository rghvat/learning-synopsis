'''
different logging object
different levels of logger ?
different levels of handler ?

by the use of handler we can write error logs to error file, debug to debug file

debug - logging verbose details
info  - trivial information, handling requests or server state changed
warning - 
error  - io error, exception, network issue
critical -  memory full, 

__name__ is current module name in python, it makes configuaration of module easy.

logging module follows hierachy design, levels of hireachy indicated by dots.


A traceback is a stack trace from the point of an exception handler down the call chain to the point where the exception was raised.
log TB also.   exc_info = True


'''

import logging

logging.basicConfig(level = logging.INFO)

records = {'name':'raghav', 'occupation':'b tech'}

logging.info('%s', records)