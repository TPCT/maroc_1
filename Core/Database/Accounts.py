from Core.Logger import Logger
import sqlite3


class AccountsDatabase:
    FILE = "accounts.db"

    def __init__(self, **kwargs):
        self._connector = sqlite3.connect(kwargs.get('file', AccountsDatabase.FILE), check_same_thread=False)
        self._logger = kwargs.get('logger', Logger())
        self._migration()

    def __del__(self):
        self._connector.close()

    def _migration(self):
        self._logger.log("[+] Trying to create Accounts Table.")
        accounts_table = '''
                    CREATE TABLE IF NOT EXISTS accounts(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        login_token TEXT NOT NULL,
                        session_token TEXT DEFAULT NULL,
                        xp INTEGER NOT NULL DEFAULT 0,
                        level INTEGER NOT NULL DEFAULT 1,
                        coins INTEGER NOT NULL DEFAULT 0,
                        gems INTEGER NOT NULL DEFAULT 0
                    );
                '''
        try:
            self._logger.log("[+] Accounts table has been created successfully.")
            self._connector.execute(accounts_table)
        except Exception as e:
            self._logger.log(f"[+] Unable to create accounts table\n\t [-] error: {e}", True)

    def insert(self, email, password, login_token, **kwargs):
        try:
            if not (email or password or login_token):
                self._logger.log("[-] unable to save the account\n\t "
                                 "[-] error: insufficient data", True)
                return None

            self._logger.log("[+] Trying to save accounts info into database.")
            keys_builder = ','.join([key for key in ['email', 'password', 'login_token'] + list(kwargs.keys())])
            values_builder = ','.join(['?' for value in range(len(kwargs.values()) + 3)])
            query = f'''
                        INSERT OR IGNORE INTO accounts(
                                             {keys_builder}
                        ) VALUES ({values_builder})
                    '''
            with self._logger.locker:
                cursor = self._connector.cursor()
                cursor.execute(query, [email, password, login_token] + list(kwargs.values()))
                self._connector.commit()
                cursor.close()
            self._logger.log("[+] Account info has been saved successfully.")
            return True
        except Exception as e:
            self._logger.log(f"[-] Unable to save Account's info\n\t [-] error: {e}", True)
        return False

    def selectAll(self):
        try:
            self._logger.log("[+] Trying to retrieve accounts info.")
            accounts = []
            cursor = self._connector.cursor()
            query = "SELECT * FROM Accounts"
            cursor.execute(query)
            for row in cursor.fetchall():
                accounts.append({
                    'id': row[0],
                    'email': row[1],
                    'password': row[2],
                    'login_token': row[3],
                    'session_token': row[4],
                    'xp': row[5],
                    'level': row[6],
                    'coins': row[7],
                    'gems': row[8]
                })
            self._logger.log("[+] Accounts info has been retrieved successfully")
            return accounts
        except Exception as e:
            self._logger.log(f"[-] Unable to retrieve accounts info.\n\t [-] error: {e}", True)
        return None

    def update(self, email, **kwargs):
        self._logger.log(f"[+] trying to fetch account's info\n\t [+] email: {email}")
        try:
            update_builder = ', '.join([f"{key} = '{value}'" for key, value in kwargs.items()])
            query = f"UPDATE accounts SET {update_builder} WHERE email = '{email}'"
            with self._logger.locker:
                cursor = self._connector.cursor()
                cursor.execute(query)
                self._connector.commit()
                cursor.close()
            self._logger.log("[+] account's info has been updated successfully.")
            return True
        except Exception as e:
            self._logger.log(f"[-] unable to update account's info\n\t [-] error: {e}", True)
        return False

    def select(self, **kwargs):
        self._logger.log(f"[+] trying to get account with\n\t [+] params: {kwargs}")
        try:
            if not kwargs:
                raise Exception("Unable to select record without params")

            selector = ' AND '.join([f"{key} = ?" for key in kwargs.keys()])
            cursor = self._connector.cursor()
            query = f"SELECT * FROM accounts WHERE {selector}"
            cursor.execute(query, tuple(kwargs.values()))
            account_info = cursor.fetchone()
            cursor.close()
            self._logger.log("[+] Account's info has been fetched successfully")
            return {
                'id': account_info[0],
                'email': account_info[1],
                'password': account_info[2],
                'login_token': account_info[3],
                'session_token': account_info[4],
                'xp': account_info[5],
                'level': account_info[6],
                'coins': account_info[7],
                'gems': account_info[8]
            }
        except Exception as e:
            self._logger.log(f"[-] unable to fetch account's info\n\t [-] error: {e}", True)
        return []


if __name__ == "__main__":
    database = AccountsDatabase()
    database.insert("akjhdlaskjd@gmail.com", "alkjklajdkls", "ajksdoiqwuoikhjalkdasd")
    print(database.selectAll())