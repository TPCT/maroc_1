from requests import Session
from warnings import simplefilter
from random import shuffle, choice
from Core.Logger import Logger
from time import sleep, time
simplefilter('ignore')


class SessionRequests:
    def __init__(self, **kwargs):
        self._session = kwargs.pop('session', Session())
        self._proxies = kwargs.pop('proxies', [])
        self._session.headers.update(kwargs.pop('headers', {}))
        self._logger = kwargs.pop('logger', Logger())
        self._proxy = None
        self._current_proxy = None
        self.setProxy()

    def setProxy(self):
        proxy = {}
        if self._proxies:
            shuffle(self._proxies)
            proxy_string = choice(self._proxies)
            proxy['http'] = proxy_string
            proxy['https'] = proxy_string
            self._current_proxy = proxy_string

        if self._proxy == proxy:
            sleep(5)

        self._proxy = proxy
        self._session.proxies = proxy
        self._logger.log("[+] the proxy has been set\n\t "
                         f"[+] proxy: {self._proxy}")

    def _request(self, *args, **kwargs):
        response = None
        try:
            self._session.headers['user-agent'] = str(time())
            response = self._session.request(*args, **kwargs, verify=False, timeout=5)
            if response.status_code in (429, 419, 403):
                self.setProxy()
        except Exception as e:
            if self._current_proxy and self._current_proxy in self._proxies:
                self._proxies.remove(self._current_proxy)
        return response

    def request(self, *args, **kwargs):
        infinite = kwargs.pop('infinite', True)
        while True:
            response = self._request(*args, **kwargs)
            if not response or response.status_code in (429, 419, 403):
                self._logger.log("[-] the last response has been blocked.\n\t "
                                 f"[-] endpoint: {args[1]}\n\t "
                                 f"[-] payload: {kwargs.get('json', kwargs.get('data', None))}\n\t "
                                 f"[-] proxy: {self._proxy}\n\t "
                                 f"[-] response: {response.text if response else response}")
                self.setProxy()
                if infinite:
                    continue
            return response
