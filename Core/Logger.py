from threading import currentThread, enumerate, Lock
from time import strftime
from textwrap import fill


class Logger:
    def __init__(self, locker=None, width=500):
        self.logger = print
        self.locker = locker if locker else Lock()
        self.width = width

    def _log(self, message, isError=False):
        self.logger(
            fill(f"[{' +' if not isError else ' -'} {strftime('%Y/%m/%d %H:%M:%S')}]"
                 f"[{currentThread().name} / {len(enumerate())}] {message}",
                 self.width, subsequent_indent="\t", replace_whitespace=False))

    def log(self, message, isError=False):
        if self.locker:
            with self.locker:
                self._log(message, isError)
        else:
            self._log(message, isError)

    def addLogger(self, logger):
        self.logger = logger