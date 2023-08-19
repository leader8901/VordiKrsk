import sqlite3

"""CREATE TABLE vordi_user_info (
    id        DOUBLE        PRIMARY KEY
                            NOT NULL,
    user_id   VARCHAR (100) NOT NULL,
    user_data VARCHAR (200) NOT NULL
);"""


class SQLighter:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    """Добавляем нового подписчика"""

    def add_user_state(self, user_id, user_data):
        print(user_id, user_data)
        with self.connection:
            return self.cursor.execute(
                "INSERT OR REPLACE INTO `vordi_user_info` (`user_id`,`user_data`) VALUES(?,?)",
                (user_id, user_data))

    # удалить предыдущую историю меню для этого пользователя
    def delete_user_state(self, user_id, user_data):
        print(user_id, user_data)
        with self.connection:
            return self.cursor.execute("DELETE FROM vordi_user_info WHERE user_id=? AND user_data=?",
                                       (user_id, user_data))

    # добавить текущее название меню в историю меню
    def add_menu_user_state(self, user_id, current_menu):
        print(user_id, current_menu)
        with self.connection:
            return self.cursor.execute("UPDATE INTO vordi_user_info (user_id,  user_data) VALUES (?, ?)",
                                       (user_id, current_menu))

    def get_menu_user_state(self, user_id):
        # retrieve user_data from database
        with self.connection:
            self.cursor.execute("SELECT user_data FROM vordi_user_info WHERE user_id=?", (user_id,))
            return self.cursor.fetchone()[0]

    def update_user_set(self, user_id, current_menu):
        # retrieve user_data from database
        with self.connection:
            self.cursor.execute("UPDATE vordi_user_info SET user_data=? WHERE user_id=?", (user_id,))
            return self.cursor.fetchone()[0]
