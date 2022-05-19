from Core.Requests.Account import Login, Register
from Core.Requests.Rewards import Rewards
from Core.Database.Accounts import AccountsDatabase
from Core.SessionRequests import SessionRequests
from Core.Logger import Logger
from Core.Proxy import Proxy
from time import time, sleep
from threading import Thread, Lock, Event
from random import randint


if __name__ == "__main__":
    blocker = Event()
    logger = Logger(locker=Lock())
    proxy_handler = Proxy(logger=logger, protocol='socks4', timeout=1000)

    fail = 0
    success = 0

    account_database = AccountsDatabase(logger=logger)

    def getUpdateAccountInfo(login_handler, account):
        while True:
            account_info = login_handler.getAccountInfoResponse()
            if account_info:
                break
            sleep(5)
        account_info['last_update_time'] = time()
        account_database.update(account['email'], **account_info)

    def gemsClaimer(account):
        if (time() - account['last_update_time']) // (24 * 3600) >= 4:
            account_session = SessionRequests(proxy_handler=proxy_handler, logger=logger)
            login_handler = Login(account_session=account_session, proxy_handler=proxy_handler, logger=logger)
            login_info = login_handler.login(login_token=account['login_token'])

            if login_info:
                rewards_handler = Rewards(account_session=account_session,
                                          logger=logger, session_token=login_info['session_token'])
                rewards_handler.collectGemsResponse()
                getUpdateAccountInfo(login_handler, account)

    def rewardsClaimer(account):
        if (time() - account['last_update_time']) // (24 * 3600) >= 10:
            account_session = SessionRequests(proxy_handler=proxy_handler, logger=logger)
            login_handler = Login(account_session=account_session, proxy_handler=proxy_handler, logger=logger)
            login_info = login_handler.login(login_token=account['login_token'])

            if login_info:
                rewards_handler = Rewards(account_session=account_session,
                                          logger=logger, session_token=login_info['session_token'])
                rewards_handler.spinRewardsResponse()
                current_day = login_handler.getCurrentDate()
                while current_day <= 42:
                    if rewards_handler.claimDailyGiftsResponse(current_day):
                        break

                while True:
                    if rewards_handler.claimXpBoostingResponse():
                        getUpdateAccountInfo(login_handler, account)
                        break
            blocker.set()

                # getUpdateAccountInfo(login_handler, account)

    def accountCreator():
        global fail, success
        account_session = SessionRequests(proxy_handler=proxy_handler, logger=logger)
        account_generator = Register(logger=logger, account_session=account_session)
        account_login = Login(logger=logger, account_session=account_session)
        rewards = Rewards(logger=logger, account_session=account_session)

        account_info = account_generator.createAccount(f"{time() + randint(1, 1000000000000)}@avkngeeks.com",
                                                       f"{time() + randint(1, 1000000000000)}@a")
        logger.log(f"account_info: {account_info}")
        if account_info:
            rewards.setSessionToken(session_token=account_generator.session_token)

            while not rewards.getOneTimeRewardsResponse():
                continue

            while not rewards.bypassDailyLimitResponse():
                continue

            levels = account_login.getAccountInfoResponse()

            if levels:
                account_info.update(levels if levels else {})
                account_database.insert(**account_info)
                success += 1
                return

        fail += 1


    def wrapper():
        # proxy_key = input('Proxy scrape key: ')

        print("Welcome to TPCT AVKN life bot\n\t"
              "[+] press 1 for creating the accounts\n\t"
              "[+] press 2 for making watcher thread\n\t"
              "[+] press 3 for gems watcher thread\n\t")
        choice = input("-> ")
        if choice == "1":
            threads_count = input("[+] please enter threads count to start: ")
            if threads_count.isdigit():
                while True:
                    threads_pool = []
                    for i in range(int(threads_count)):
                        thread = Thread(target=accountCreator, daemon=True)
                        thread.start()
                        threads_pool.append(thread)

                    for thread in threads_pool:
                        thread.join()
            pass
        elif choice == "2":
            accounts = account_database.selectAll()
            accounts.reverse()
            threads_count = input("[+] please enter threads count to start: ")
            if threads_count.isdigit():
                while True:
                    threads_pool = []
                    for account in accounts:
                        thread = Thread(target=rewardsClaimer, daemon=True, args=(account,),
                                        name=account['id'])
                        thread.start()
                        threads_pool.append(thread)

                        if len(threads_pool) >= int(threads_count):
                            blocker.clear()
                        blocker.wait()

                    # threads_pool.append(thread)
                    # start_time = time()
                    # for i in range(0, len(accounts), int(threads_count)):
                    #     threads_pool = []
                    #     start_time_1 = time()
                    #
                    #     for thread in threads_pool:
                    #         thread.join() if thread.is_alive() else None
                    #     logger.log(
                    #         f"failed: {fail}, success: {success}, time elapsed: {time() - start_time_1}")
                    #
                    # operation_time = time() - start_time
                    # sleep_time = 6*3600 - operation_time
                    # logger.log(f"time elapsed: {operation_time}")
                    # sleep(sleep_time) if sleep_time > 0 else None
        elif choice == "3":
            accounts = account_database.selectAll()
            threads_count = input("[+] please enter threads count to start: ")
            if threads_count.isdigit():
                while True:
                    start_time = time()
                    for i in range(0, len(accounts), int(threads_count)):
                        threads_pool = []
                        start_time_1 = time()
                        for account in accounts[i: i + int(threads_count)]:
                            thread = Thread(target=gemsClaimer, daemon=True, args=(account,),
                                            name=account['id'])
                            thread.start()
                            threads_pool.append(thread)
                        for thread in threads_pool:
                            thread.join() if thread.is_alive() else None
                        logger.log(
                            f"failed: {fail}, success: {success}, time elapsed: {time() - start_time_1}")
                    operation_time = time() - start_time
                    sleep_time = 6*3600 - operation_time
                    logger.log(f"time elapsed: {operation_time}")
                    sleep(sleep_time) if sleep_time > 0 else None

    wrapper()
