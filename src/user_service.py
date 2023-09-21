from src.csv_file_handler import CSVFileHandler


class UserService:
    """
        Service which respond for all communications between users
        storing users, retrieving and so on.
    """

    def __init__(self, handler: CSVFileHandler):
        self.handler = handler

    def check_user_exist(self):
        pass

    def get_user_by_id(self, id: int):
        pass

    def add_user(self, user_data: list) -> None:
        user_data_save = {
            'id': user_data[0],
            'user_name': user_data[1],
            'first_name': user_data[2],
            'last_name': user_data[3],
            'user_type': user_data[4]
        }
        self.handler.write_row(user_data_save)

