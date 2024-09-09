from datetime import datetime
from app.lib.decorators.singleton_decorator import Singleton
from app.lib.console_printer import ConsolePrinter as Print
import logging


@Singleton
class ConsoleLogger:
    def __init__(self):
        self.__logger = logging.getLogger()
        self.__logger.setLevel(logging.DEBUG)

        # begin - Console Handler
        self.__console_handler = logging.StreamHandler()
        self.__console_handler.setLevel(logging.DEBUG)
        self.__console_handler.addFilter(lambda record: self.__console_filter_function(record))  # Custom Console Filter
        self.__logger.addHandler(self.__console_handler)
        # end- Console Handler

        # begin - File Handler
        '''
        self.__file_handler = logging.FileHandler('system.log')
        self.__file_handler.setLevel(logging.DEBUG)
        self.__logger.addHandler(self.__file_handler)
        '''
        # end - File Handler

    @staticmethod
    def __console_filter_function(record) -> bool:
        if record.levelno == logging.DEBUG:
            Print.print_underline(record.msg)

        if record.levelno == logging.INFO:
            Print.print_purple(record.msg)

        if record.levelno == logging.WARNING:
            Print.print_orange(record.msg)

        if record.levelno == logging.ERROR:
            Print.print_red(record.msg)

        if record.levelno == logging.CRITICAL:
            Print.print_red(record.msg)

        return False

    def log(self, log="", level=logging.INFO):
        import inspect
        frame = inspect.currentframe().f_back
        current_date_time = datetime.now()
        log_level_str = logging.getLevelName(level)
        class_name = frame.f_globals.get('__name__')
        function_name = frame.f_code.co_name
        message = f"{current_date_time.strftime('%Y-%m-%d %H:%M:%S')} {str.upper(log_level_str)} - {class_name}.{function_name}"
        if log:
            message += f" ::: {log}"

        self.__logger.log(level, message)
        return message
