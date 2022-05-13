import os.path
from Core.Logger import Logger
from random import shuffle


class Proxy:
    PROXY_URL = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol={protocol}&timeout={" \
                "timeout}&country={country}&ssl={ssl}&anonymity={anonymity} "

    def __init__(self, **kwargs):
        self._logger = kwargs.get('logger', Logger())
        self._protocol = kwargs.get('protocol', 'socks4')
        timeout = kwargs.get('timeout', 1000)
        country = kwargs.get('country', 'all')
        ssl = kwargs.get('ssl', 'all')
        anonymity = kwargs.get('anonymity', 'all')
        self._proxy_url = Proxy.PROXY_URL.format(**{'protocol': self._protocol, 'timeout': timeout,
                                                    'country': country, 'ssl': ssl, 'anonymity': anonymity})
        self._proxies = []
        self._current_counter = 0
        self._proxies_count = 0
        self._readProxies()

    def _readProxies(self):
        self._logger.log("trying to get proxy list from proxy scrape")
        try:
            api_response = open(os.path.dirname(__file__) + '/proxies', 'r+').read()
            for line in api_response.split():
                self._proxies.append(f"{self._protocol if self._protocol != 'http' else 'https'}://{line}")
            shuffle(self._proxies)
            self._proxies_count = len(self._proxies)
            self._logger.log("[+] proxy list has been fetched successfully\n\t "
                             f"[+] proxy type: {self._protocol}\n\t "
                             f"[+] proxy list count: {self._proxies_count}")
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to fetch proxy list\n\t "
                             f"[-] error: {e}")

    def getProxy(self):
        if self._proxies:
            self._current_counter = self._current_counter if self._proxies_count - 1 > self._current_counter else 0
            selector = self._current_counter
            self._current_counter += 1
            return self._proxies[selector]
        return None

    # def getProxyList(self):
    #     self._logger.log("trying to get proxy list from proxy scrape")
    #     try:
    #         api_response = open(os.path.dirname(__file__) + '/proxies', 'r+').read()
    #         # api_response = get(self._proxy_url).text
    #         for line in api_response.split():
    #             self._proxies.append(f"{self._protocol if self._protocol != 'http' else 'https'}://{line}")
    #         shuffle(self._proxies)
    #         self._logger.log("[+] proxy list has been fetched successfully\n\t "
    #                          f"[+] proxy type: {self._protocol}\n\t "
    #                          f"[+] proxy list count: {len(self._proxies)}")
    #     except Exception as e:
    #         self._logger.log("[-] an error occurred while trying to fetch proxy list\n\t "
    #                          f"[-] error: {e}")
    #     return self._proxies


if __name__ == "__main__":
    proxy = Proxy()
    proxy.getProxyList()