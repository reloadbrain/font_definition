import mysql.connector


class CustomException(Exception):
    pass


class UseDatabase:
    def __init__(self, config: dict) -> None:
        self.conf = config

    def __enter__(self) -> 'cursor':
        try:
            self.conn = mysql.connector.connect(**self.conf)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as error:
            raise CustomException(error)
        except mysql.connector.errors.ProgrammingError as error:
            raise Exception(error)

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise Exception(exc_val)
        elif exc_type:
            raise exc_type(exc_val)
