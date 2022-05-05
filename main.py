from Core.Requests.Account import Login, Register
from Core.Requests.Rewards import Rewards
from Core.Database.Accounts import AccountsDatabase
from Core.Database.Rewards import RewardsDatabase
from Core.SessionRequests import SessionRequests
from Core.Logger import Logger
from Core.Proxy import Proxy
from time import time, sleep
from threading import Thread, Lock
from random import randint

if __name__ == "__main__":
    logger = Logger(locker=Lock())
    proxy = Proxy(logger=logger, protocol='socks4', timeout=1000)
    proxies = proxy.getProxyList()

    fail = 0
    success = 0

    account_database = AccountsDatabase(logger=logger)
    rewards_database = RewardsDatabase(logger=logger)

    def rewardsClaimer(account):
        global fail, success
        session = SessionRequests(proxies=proxies)
        login_handler = Login(session=session, proxies=proxies, logger=logger)
        rewards_handler = Rewards(session=session, proxies=proxies, logger=logger)
        login_info = login_handler.login(login_token=account['login_token'])
        rewards_database.insert(account['id'], reward_day=time())
        rewards_info = rewards_database.select(account_id=account['id'])
        if login_info:
            rewards_handler.setSessionToken(login_info['session_token'])
            if rewards_handler.claimDailyGiftsResponse(rewards_info['current_day']):
                rewards_database.update(account['id'], current_day=rewards_info['current_day'] + 1)

            if rewards_handler.claimXpBoostingResponse():
                rewards_database.update(account['id'], visitor=rewards_info['visitor'] + 1,
                                        mbox=rewards_info['mbox'] + 1, talking=rewards_info['talking'] + 1,
                                        daily_gems=rewards_info['daily_gems'] + 1, dive=rewards_info['dive'] + 1,
                                        daily_visit=rewards_info['daily_visit'] + 1, photo=rewards_info['photo'] + 1)

            if rewards_handler.spinRewardsResponse():
                rewards_database.update(account['id'], last_spin_time=time())

            if rewards_handler.collectGemsResponse():
                pass

            account_info = login_handler.getAccountInfoResponse(login_token=login_info['login_token'])
            account_database.update(account['email'], **account_info)
            success += 1
        else:
            fail += 1


    def accountCreator():
        global fail, success
        account_generator = Register(logger=logger, proxies=proxies)
        account_login = Login(logger=logger, proxies=proxies)
        account_info = account_generator.createAccount(f"{time() * randint(1, 1000000000000)}@avkngeeks.com",
                                                       f"{time() * randint(1, 1000000000000)}@a")
        if account_info:
            levels = account_login.getAccountInfoResponse(login_token=account_info['login_token'])
            account_info.update(levels if levels else {})

        status = account_database.insert(**account_info)
        success += 1 if status else 0
        fail += 0 if status else 1

    def wrapper():
        print("Welcome to TPCT AVKN life bot\n\t"
              "[+] press 1 for creating the accounts\n\t"
              "[+] press 2 for making watcher thread")
        choice = input("-> ")
        if choice == "1":
            threads_count = input("[+] please enter threads count to start: ")
            if threads_count.isdigit():
                while True:
                    threads_pool = []
                    for i in range(int(threads_count)):
                        thread = Thread(target=accountCreator)
                        thread.start()
                        threads_pool.append(thread)

                    for thread in threads_pool:
                        thread.join()
        elif choice == "2":
            accounts = account_database.selectAll()
            threads_count = input("[+] please enter threads count to start: ")
            if threads_count.isdigit():
                while True:
                    start_time = time()
                    for i in range(0, len(accounts), int(threads_count)):
                        threads_pool = []
                        start_time_1 = time()
                        for account in accounts[i: i + int(threads_count)]:
                            thread = Thread(target=rewardsClaimer, daemon=True, args=(account,),
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
    # start_time = time()
    # for i in range(0, len(accounts), 5):
    #     threads_pool = []
    #     start_time_1 = time()
    #     for account in accounts[i: i + 5]:
    #         thread = Thread(target=rewardsClaimer, daemon=True, args=(account, ), name=account['id'])
    #         thread.start()
    #         threads_pool.append(thread)
    #
    #     for thread in threads_pool:
    #         thread.join() if thread.is_alive() else None
    #     logger.log(f"failed: {fail}, success: {success}, total accounts: {counter}, time elapsed: {time() - start_time_1}")
    #
    # print(f"total taken time for creating 1000 account {time() - start_time}")