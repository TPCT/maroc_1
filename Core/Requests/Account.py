from Core.Logger import Logger
from Core.Urls import AccountUrls
from Core.Payloads import AccountPayloads
from Core.SessionRequests import SessionRequests
from random import choice


class Login:
    def __init__(self, **kwargs):
        self._logger = kwargs.get('logger', Logger())
        self._session = kwargs.get('session', SessionRequests(proxies=kwargs.get('proxies', []), logger=self._logger))
        self._email = None
        self._password = None
        self._login_token = None
        self._session_token = None

    def _resetData(self):
        self._email = None
        self._password = None
        self._login_token = None
        self._session_token = None

    def _emailLoginResponse(self, email, password):
        self._email = email
        self._password = password
        self._logger.log(f"[+] trying to login To the Account using email: {self._email}, password: {self._password}")
        response = None
        try:
            response = self._session.request('post', AccountUrls.login,
                                             json=AccountPayloads.createLoginPayload(self._email, self._password),
                                             infinite=False)
            response_json = response.json()
            if response_json['error']:
                self._logger.log(f"[-] unable to login to the account\n\t "
                                 f"[-] error: {response_json['error']}\n\t "
                                 f"[-] response: {response.text}\n\t "
                                 f"[-] status code: {response.status_code}", True)
                return None
            self._login_token = response.json()['login_token']
            self._session_token = response.headers['X-Avkn-Jwtsession']
            self._logger.log("[+] Account has been logged in successfully.\n\t "
                             f"[+] response: {response.text}\n\t "
                             f"[+] status code: {response.status_code}")
            return {
                'login_token': self._login_token,
                'session_token': self._session_token
            }
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to login to account\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)

    def _tokenLoginResponse(self, token):
        self._login_token = token
        self._logger.log(f"[+] trying to login To the Account using login token")
        response = None
        try:
            response = self._session.request('post', AccountUrls.login,
                                             json=AccountPayloads.createTokenLoginPayload(self._login_token),
                                             infinite=False)
            response_json = response.json()
            if response_json['error']:
                self._logger.log(f"[-] unable to login to the account\n\t "
                                 f"[-] error: {response_json['error']}\n\t "
                                 f"[-] response: {response.text}\n\t "
                                 f"[-] status code: {response.status_code}", True)
                return None
            self._session_token = response.headers['X-Avkn-Jwtsession']
            self._logger.log("[+] Account has been logged in successfully.\n\t "
                             f"[+] response: {response.text}\n\t "
                             f"[+] status code: {response.status_code}")
            return {
                'login_token': self._login_token,
                'session_token': self._session_token
            }
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to login to account\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)

    def _getAccountsLevel(self):
        response = None
        try:
            self._logger.log("[+] trying to get xp, level info")
            response = self._session.request('post', AccountUrls.level, json={},
                                             headers={'X-Avkn-Jwtsession': self._session_token}, infinite=False)
            self._logger.log("[+] info has been retrieved successfully\n\t "
                             f"[+] response: {response.text}\n\t "
                             f"[+] status code: {response.status_code}"
                             )
            response_json = response.json()['lkwd']['avakinlife']
            return {
                'level': response_json['level'],
                'xp': response_json['xp']
            }
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to get account's level.\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)
            return None

    def _getAccountsBalance(self):
        response = None
        try:
            self._logger.log("[+] trying to get coins, gems info")
            response = self._session.request('post', AccountUrls.balance, json={},
                                             headers={'X-Avkn-Jwtsession': self._session_token}, infinite=False)
            self._logger.log("[+] info has been retrieved successfully\n\t "
                             f"[+] response: {response.text}\n\t "
                             f"[+] status code: {response.status_code}"
                             )
            response_json = response.json()['balance']
            return {
                'coins': response_json['coins'],
                'gems': response_json['gems']
            }
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to get account's balance.\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)
            return None

    def getAccountInfoResponse(self, **kwargs):
        try:
            self.login(**kwargs)
            self._logger.log("[+] trying to get account's info")
            info = {}
            level = self._getAccountsLevel()
            balance = self._getAccountsBalance()
            info.update(level if level else {})
            info.update(balance if balance else {})
            return info
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to get accounts info.\n\t "
                             f"[-] error: {e}\n\t ", True)

    def login(self, **kwargs):
        self._resetData()
        if 'login_token' in kwargs:
            return self._tokenLoginResponse(kwargs['login_token'])
        elif 'email' in kwargs and 'password' in kwargs:
            return self._emailLoginResponse(kwargs['email'], kwargs['password'])
        else:
            raise Exception('invalid login credentials please enter email,password or login_token to login')


class Register:
    def __init__(self, **kwargs):
        self._logger = kwargs.get('logger', Logger())
        self._session = kwargs.get('session', SessionRequests(proxies=kwargs.get('proxies', []), logger=self._logger))
        self._email = None
        self._password = None
        # self._pre_session = None
        self._character_token = None
        self._username_token = None
        self._login_token = None
        self._session_token = None

    # def _preSessionResponse(self):
    #     self._logger.log("[+] trying to retrieve pre_session token.")
    #     response = None
    #     try:
    #         response = self._session.request('post', AccountUrls.pre_session, json={})
    #         response_json = response.json()
    #         self._pre_session = response_json['pre_session']
    #         self._logger.log('[+] pre_session token has been retrieved successfully\n\t '
    #                          f"[+] user id: {response_json['user_id']}\n\t "
    #                          f'[+] status code: {response.status_code}')
    #         return self._pre_session
    #     except Exception as e:
    #         self._logger.log("[-] an error occurred while trying to retrieve pre_session token.\n\t "
    #                          f"[-] error: {e}\n\t "
    #                          f"[-] response: {response.text if response else None}\n\t "
    #                          f"[-] status code: {response.status_code if response else -1}", True)

    def _characterTokenResponse(self):
        self._logger.log("[+] trying to retrieve character key token")
        response = None
        try:
            response = self._session.request('post', AccountUrls.old_key_token, json={}, infinite=False)
            if response:
                response_json = response.json()
                character = choice(response_json['configs'])
                self._character_token = character['signature']
                self._logger.log("[+] character token has been retrieved successfully.\n\t "
                                 f"[+] character uuid: {character['uuid']}\n\t "
                                 f"[+] status code: {response.status_code}")
                return self._character_token
        except Exception as e:
            self._logger.log("[-] an error occurred while trying to retrieve old token.\n\t "
                             f"[-] error: {e}\n\t "
                             f"[-] response: {response.text if response else None}\n\t "
                             f"[-] status code: {response.status_code if response else -1}", True)

    def _usernameTokenResponse(self):
        self._logger.log("[+] trying to get username token")
        response = None
        try:
            response = self._session.request('post', AccountUrls.username_key_token, json={}, infinite=False)
            if response:
                response_json = response.json()
                username = choice(response_json['usernames'])
                self._username_token = username['signature']
                self._logger.log("[+] username token has been retrieved successfully\n\t "
                                 f"[+] username: {username['username']}\n\t "
                                 f"[+] status code: {response.status_code}")
                return self._username_token
        except Exception as e:
            self._logger.log('[-] an error occurred while trying to retrieve username token.\n\t '
                             f'[-] error: {e}\n\t '
                             f'[-] response: {response.text if response else None}\n\t '
                             f'[-] status code: {response.status_code if response else -1}', True)

    def _accountTokenResponse(self):
        self._logger.log("[+] trying to get account generation token")
        response = None
        try:
            response = self._session.request('post', AccountUrls.register,
                                             json=AccountPayloads.createAccountTokenPayload(
                                                 "",
                                                 self._character_token,
                                                 self._username_token
                                             ), infinite=False)
            if response:
                response_json = response.json()
                self._login_token = response_json['login_token']
                self._session_token = response_json['session_token']
                user = response_json['user']
                self._logger.log("[+] account generation token has been retrieved successfully\n\t "
                                 f"[+] user id: {user['user_id']}\n\t "
                                 f"[+] status code: {response.status_code}")
                return {
                    'login_token': self._login_token,
                    'session_token': self._session_token
                }
        except Exception as e:
            self._logger.log('[-] an error occurred while trying to retrieve username token.\n\t '
                             f'[-] error: {e}\n\t '
                             f'[-] response: {response.text if response else None}\n\t '
                             f'[-] status code: {response.status_code if response else -1}', True)

    def _createAccountResponse(self):
        self._logger.log("[+] trying to create account")
        response = None
        try:
            response = self._session.request('post', AccountUrls.set_profile,
                                             json=AccountPayloads.createAccountPayload(self._email, self._password),
                                             headers={
                                                 "X-Avkn-Jwtsession": self._session_token
                                             }, infinite=False)
            if response:
                response_json = response.json()
                if response_json['error'] is None:
                    self._logger.log(f"Account with email: {self._email} and password: {self._password} "
                                     f"has been created successfully.")
                    return {'email': self._email, 'password': self._password}
                raise Exception(response_json['error'])
        except Exception as e:
            self._logger.log('[-] an error occurred while trying to create the account.\n\t '
                             f'[-] error: {e}\n\t '
                             f'[-] response: {response.text if response else None}\n\t '
                             f'[-] status code: {response.status_code if response else -1}', True)

    def _resetData(self):
        self._email = None
        self._password = None
        # self._pre_session = None
        self._character_token = None
        self._username_token = None
        self._login_token = None
        self._session_token = None

    @property
    def session(self):
        return self._session

    @property
    def session_token(self):
        return self._session_token

    @property
    def login_token(self):
        return self._login_token

    def createAccount(self, email, password):
        self._resetData()

        self._email = email
        self._password = password

        steps = [
            self._characterTokenResponse,
            self._usernameTokenResponse,
            self._accountTokenResponse,
            self._createAccountResponse,
        ]

        for step in steps:
            if not step():
                return None

        return {
            'email': self._email,
            'password': self._password,
            'login_token': self._login_token,
            'session_token': self._session_token
        }
