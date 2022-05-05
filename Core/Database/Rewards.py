from Core.Logger import Logger
import sqlite3


class RewardsDatabase:
    FILE = "rewards.db"

    def __init__(self, **kwargs):
        self._connector = sqlite3.connect(kwargs.get('file', RewardsDatabase.FILE), check_same_thread=False)
        self._logger = kwargs.get('logger', Logger())
        self._migration()

    def __del__(self):
        self._connector.close()

    def _migration(self):
        self._logger.log("[+] Trying to create Accounts Table.")
        rewards_table = '''
                    CREATE TABLE IF NOT EXISTS rewards(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        account_id INTEGER NOT NULL,
                        current_day INTEGER NOT NULL DEFAULT 0,
                        visitor INTEGER DEFAULT 0,
                        mbox INTEGER DEFAULT 0,
                        talking INTEGER DEFAULT 0,
                        daily_gems INTEGER DEFAULT 0,
                        dive INTEGER DEFAULT 0,
                        daily_visit INTEGER DEFAULT 0,
                        photo INTEGER DEFAULT 0,
                        last_spin_time TIMESTAMP DEFAULT 0,
                        reward_day TIMESTAMP DEFAULT 0,
                        FOREIGN KEY(account_id) REFERENCES accounts(id)
                    );
                '''
        try:
            self._logger.log("[+] rewards table has been created successfully.")
            self._connector.execute(rewards_table)
        except Exception as e:
            self._logger.log(f"[+] Unable to create rewards table\n\t [-] error: {e}", True)

    def insert(self, account_id, **kwargs):
        try:
            self._logger.log("[+] Trying to insert reward info into database.")
            fields = ','.join(['account_id'] + list(kwargs.keys()))
            selector = ','.join(['?' for x in range(len(kwargs) + 1)])
            query = f'INSERT OR IGNORE INTO rewards({fields}) VALUES ({selector})'
            with self._logger.locker:
                cursor = self._connector.cursor()
                cursor.execute(query, [account_id] + list(kwargs.values()))
                self._connector.commit()
                cursor.close()
            self._logger.log("[+] reward info has been saved successfully.")
            return True
        except Exception as e:
            self._logger.log(f"[-] Unable to insert reward's info\n\t [-] error: {e}", True)
        return False

    def selectAll(self):
        try:
            self._logger.log("[+] Trying to retrieve rewards info.")
            accounts = []
            cursor = self._connector.cursor()
            query = "SELECT * FROM rewards"
            cursor.execute(query)
            for row in cursor.fetchall():
                accounts.append({
                    'id': row[0],
                    'account_id': row[1],
                    'current_day': row[2],
                    'visitor': row[3],
                    'mbox': row[4],
                    'talking': row[5],
                    'daily_gems': row[6],
                    'dive': row[7],
                    'daily_visit': row[8],
                    'photo': row[9],
                    'last_spin_time': int(row[10]),
                    'reward_day': int(row[11])
                })
            self._logger.log("[+] rewards info has been retrieved successfully")
            return accounts
        except Exception as e:
            self._logger.log(f"[-] Unable to retrieve rewards info.\n\t [-] error: {e}", True)
        return None

    def update(self, account_id, **kwargs):
        self._logger.log(f"[+] trying to fetch reward's info\n\t [+] account id: {account_id}")
        try:
            update_builder = ', '.join([f"{key} = ?" for key in kwargs.keys()])
            query = f"UPDATE rewards SET {update_builder} WHERE account_id = ?"
            with self._logger.locker:
                cursor = self._connector.cursor()
                cursor.execute(query, [account_id] + list(kwargs.values()))
                self._connector.commit()
                cursor.close()
            self._logger.log("[+] reward's info has been updated successfully.")
            return True
        except Exception as e:
            self._logger.log(f"[-] unable to update reward's info\n\t [-] error: {e}", True)
        return False

    def select(self, **kwargs):
        self._logger.log(f"[+] trying to get reward with\n\t [+] params: {kwargs}")
        try:
            if not kwargs:
                raise Exception("Unable to select record without params")

            selector = ' AND '.join([f"{key} = ?" for key in kwargs.keys()])
            query = f"SELECT * FROM rewards WHERE {selector}"
            cursor = self._connector.cursor()
            cursor.execute(query, tuple(kwargs.values()))
            reward_info = cursor.fetchone()
            cursor.close()
            self._logger.log("[+] reward's info has been fetched successfully")
            return {
                'id': reward_info[0],
                'account': reward_info[1],
                'current_day': reward_info[2],
                'visitor': reward_info[3],
                'mbox': reward_info[4],
                'talking': reward_info[5],
                'daily_gems': reward_info[6],
                'dive': reward_info[7],
                'daily_visit': reward_info[8],
                'photo': reward_info[9],
                'last_spin_time': reward_info[10],
                'reward_day': reward_info[11]
            }
        except Exception as e:
            self._logger.log(f"[-] unable to fetch reward's info\n\t [-] error: {e}", True)
        return {}


if __name__ == "__main__":
    database = RewardsDatabase()
    database.insert(1)
    database.update(1, visitor=1)
    print(database.select(account_id=1))
