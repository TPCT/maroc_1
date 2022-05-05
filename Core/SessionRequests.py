from requests import Session
from warnings import simplefilter
import time
simplefilter('ignore')


class SessionRequests:
    def __init__(self, **kwargs):
        self._headers = kwargs.get('headers', {})
        self._session = kwargs.get('session', Session())
        self._session.headers.update(self._headers)
        self.proxies = self._session.proxies

    def request(self, *args, **kwargs):
        self._session.headers['user-agent'] = str(time.time())
        # while True:
        response = self._session.request(*args, **kwargs, verify=False, timeout=10)
        try:
            self._session.headers["X-Avkn-Jwtsession"] = response.headers["X-Avkn-Jwtsession"]
        except:
            pass
            # if response.status_code == 200:
            #     break
            # time.sleep(60)
        return response
