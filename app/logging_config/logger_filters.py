import logging

class WarningErrorCritical(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in ('WARNING', 'ERROR', 'CRITICAL')

class DebugInfo(logging.Filter):

    def filter(self, record: logging.LogRecord) -> bool:
        return record.levelname in ('DEBUG', 'INFO')