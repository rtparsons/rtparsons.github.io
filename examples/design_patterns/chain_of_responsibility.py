from abc import ABC, abstractclassmethod


class LogHandler(ABC):
    next = None

    @abstractclassmethod
    def handle(self, log: str, log_level: str) -> None:
        pass


class DebugLogHandler(LogHandler):
    def __init__(self, next: LogHandler) -> None:
        self.next = next

    def handle(self, log: str, log_level: str) -> None:
        if log_level == 'DEBUG':
            print(f'DEBUG: {log}')
            return

        if self.next:
            self.next.handle(log, log_level)


class InfoLogHandler(LogHandler):
    def __init__(self, next: LogHandler) -> None:
        self.next = next

    def handle(self, log: str, log_level: str) -> None:
        if log_level == 'INFO':
            print(f'INFO: {log}')
            return

        if self.next:
            self.next.handle(log, log_level)


class ErrorLogHandler(LogHandler):
    def __init__(self, next: LogHandler) -> None:
        self.next = next

    def handle(self, log: str, log_level: str) -> None:
        if log_level == 'ERROR':
            print(f'ERROR: {log}')
            return

        if self.next:
            self.next.handle(log, log_level)

debug_handler = DebugLogHandler(None)
info_handler = InfoLogHandler(debug_handler)
handler = ErrorLogHandler(info_handler)

handler.handle('log string for debug', 'DEBUG')
handler.handle('log string for info', 'INFO')
handler.handle('log string for error', 'ERROR')
handler.handle('log string for no match', '???')
