from Core.Payloads import RewardsPayloads
from Core.Urls import RewardsUrls
from Core.Logger import Logger


class Rewards:
    def __init__(self, account_session, **kwargs):
        self._logger = kwargs.get('logger', Logger())
        self._session = account_session
        self._session_token = kwargs.get("session_token", None)

    def setSessionToken(self, session_token):
        self._session.setProxy()
        self._session_token = session_token

    def getOneTimeRewardsResponse(self):
        self._logger.log("[+] trying to get daily rewards")
        response = None
        try:
            for payload in RewardsPayloads.createRewardsPayload():
                response = self._session.request('post', RewardsUrls.onetime_rewards,
                                                 json=payload,
                                                 headers={'X-Avkn-Jwtsession': self._session_token})
                self._logger.log(f"[+] Response has been retrieved\n\t [+] response: {response.text}\n\t "
                                 f"[+] status code: {response.status_code}\n\t "
                                 f"[+] payload: {payload}")
            self._logger.log("[+] daily rewards has been retrieved successfully")
            return True
        except Exception as e:
            self._logger.log('[-] an error occurred while trying to get one time award.\n\t '
                             f'[-] error: {e}\n\t '
                             f'[-] response: {response.text if response else None}\n\t '
                             f'[-] status code: {response.status_code if response else -1}', True)
            return False

    def bypassDailyLimitResponse(self):
        self._logger.log("[+] trying to bypass gifting limit")
        response = None
        try:
            response = self._session.request('post', RewardsUrls.gift_limit,
                                             json=RewardsPayloads.createBypassGiftingLimitPayload(),
                                             headers={'X-Avkn-Jwtsession': self._session_token})
            self._logger.log('[+] bypassing gifting limit response has been retrieved\n\t '
                             f'[+] response: {response.text}\n\t ' 
                             f'[+] status code: {response.status_code}')
            return True
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to bypass gift limit\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)
        return False

    def claimDailyGiftsResponse(self, current_day):
        self._logger.log(f"[+] trying to claim day {current_day} gift")
        response = None
        try:
            response = self._session.request('post', RewardsUrls.daily_reward,
                                             json=RewardsPayloads.createDailyRewardPayload(current_day),
                                             headers={'X-Avkn-Jwtsession': self._session_token})
            self._logger.log('[+] claiming daily gift response has been retrieved\n\t '
                             f'[+] response: {response.text}\n\t ' 
                             f'[+] status code: {response.status_code}')
            return response.status_code in (200, 417)
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to claim daily gift\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)
        return False

    def claimXpBoostingResponse(self):
        self._logger.log(f"[+] trying to claim xp boosting gift")
        response = None
        try:
            for retries, payload in RewardsPayloads.createDailyXpBoostingPayload():
                for i in range(retries):
                    response = self._session.request('post', RewardsUrls.xp_boosting,
                                                     json=payload,
                                                     headers={'X-Avkn-Jwtsession': self._session_token})
                    self._logger.log('[+] claiming xp boosting response has been retrieved\n\t '
                                     f'[+] response: {response.text}\n\t '
                                     f'[+] status code: {response.status_code}\n\t '
                                     f'[+] payload: {payload}')

                    response_json = response.json()
                    if 'lkwd' not in response_json:
                        break
            return True
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to claim xp boosting gift\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)
        return False

    def spinRewardsResponse(self):
        self._logger.log(f"[+] trying to claim spin boosting gift")
        response = None
        try:
            for i in range(1):
                response = self._session.request('post', RewardsUrls.spin_1,
                                                 json=RewardsPayloads.createSpinRewardsPayload(),
                                                 headers={'X-Avkn-Jwtsession': self._session_token})

                self._logger.log('[+] claiming spin reward response has been retrieved\n\t '
                                 f'[+] response: {response.text}\n\t '
                                 f'[+] status code: {response.status_code}\n\t '
                                 f'[+] payload: {RewardsPayloads.createSpinRewardsPayload()}\n\t '
                                 f'[+] endpoint: {RewardsUrls.spin_1}')

                if not response.text or not response.json()['config']:
                    return None

            for i in range(1):
                response = self._session.request('post', RewardsUrls.spin_2,
                                                 json=RewardsPayloads.createSpinRewardsPayload(),
                                                 headers={'X-Avkn-Jwtsession': self._session_token})

                self._logger.log('[+] claiming spin reward response has been retrieved\n\t '
                                 f'[+] response: {response.text}\n\t '
                                 f'[+] status code: {response.status_code}\n\t '
                                 f'[+] payload: {RewardsPayloads.createSpinRewardsPayload()}\n\t '
                                 f'[+] endpoint: {RewardsUrls.spin_2}')

                if not response.text:
                    return None
            return True
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to spin reward gift\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)
        return False

    def collectGemsResponse(self):
        self._logger.log(f"[+] trying to claim gems gift")
        response = None
        try:
            for payload in RewardsPayloads.createGemsCollectPayload():
                for i in range(10):
                    response = self._session.request('post', RewardsUrls.gems,
                                                     json=payload,
                                                     headers={'X-Avkn-Jwtsession': self._session_token})

                    self._logger.log('[+] claiming gems reward response has been retrieved\n\t '
                                     f'[+] response: {response.text}\n\t '
                                     f'[+] status code: {response.status_code}\n\t '
                                     f'[+] payload: {payload}\n\t '
                                     f'[+] endpoint: {RewardsUrls.gems}')

                    if 'balance' not in response.text:
                        break
            return True
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to collect gems reward gift\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)
        return False