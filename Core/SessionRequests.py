from requests import Session
from warnings import simplefilter
import time
from random import shuffle, choice
simplefilter('ignore')


class SessionRequests:
    def __init__(self, **kwargs):
        self._session = kwargs.pop('session', Session())
        self._proxies = kwargs.pop('proxies', [])
        self._session.headers.update(kwargs.pop('headers', {}))
        self.proxies = self._session.proxies

    def _request(self, *args, **kwargs):
        proxy = {}
        self._session.headers['user-agent'] = str(time.time())
        if self._proxies:
            shuffle(self._proxies)
            proxy_string = choice(self._proxies)
            proxy['http'] = proxy_string
            proxy['https'] = proxy_string
        response = self._session.request(*args, **kwargs, verify=False, timeout=10,
                                         proxies=proxy if proxy else self._session.proxies)
        try:
            self._session.headers["X-Avkn-Jwtsession"] = response.headers["X-Avkn-Jwtsession"]
        except:
            pass
        return response

    def request(self, *args, **kwargs):
        while True:
            response = self._request(*args, **kwargs)
            if response.status_code in (419, 403):
                continue
            return response
