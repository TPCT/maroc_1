from requests import Session
from warnings import simplefilter
from Core.Logger import Logger
from time import time
simplefilter('ignore')


class SessionRequests:
    def __init__(self, **kwargs):
        self._session = kwargs.pop('session', Session())
        self._proxy_handler = kwargs.pop('proxy_handler', None)
        self._session.headers.update(kwargs.pop('headers', {}))
        self._logger = kwargs.pop('logger', Logger())
        self._proxy = None
        self._current_proxy = None

    def setProxy(self):
        proxy = {}
        if self._proxy_handler:
            proxy_string = self._proxy_handler.getProxy()
            proxy['http'] = proxy_string
            proxy['https'] = proxy_string
            self._current_proxy = proxy_string

        self._proxy = proxy
        self._session.proxies = proxy
        self._logger.log("[+] the proxy has been set\n\t "
                         f"[+] proxy: {self._proxy}")

    def _request(self, *args, **kwargs):
        response = None
        try:
            self._session.headers['user-agent'] = str(time())
            response = self._session.request(*args, **kwargs, verify=False, timeout=10)
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to make request\n\t "
                             f"[-] error: {e}")
        return response

    def request(self, *args, **kwargs):
        response = self._request(*args, **kwargs)
        if response is None or response.status_code in (429, 419, 403):
            self._logger.log("[-] the last response has been blocked.\n\t "
                             f"[-] endpoint: {args[1]}\n\t "
                             f"[-] payload: {kwargs.get('json', kwargs.get('data', None))}\n\t "
                             f"[-] proxy: {self._proxy}\n\t "
                             f"[-] response: {response.text if response else response}\n\t ")
            self.setProxy()
        return response
