import mysql.connector


class MySQLConnector:
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 3306
        self.user = 'user'
        self.password = 'password'
        db = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password
        )
        print(
            "MySQL connection ID for db1: {0}"
            .format(db1.connection_id)
        )
        db1.close()


if __name__ == '__main__':
    MySQLConnector()
