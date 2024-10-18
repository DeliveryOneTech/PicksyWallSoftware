import os
import datetime
from app.lib.app_config_context import AppConfigContext


class Utils:

    @staticmethod
    def read_all_app_config():
        return AppConfigContext().read_all_app_config()

    @staticmethod
    def get_value_from_app_config(key):
        return AppConfigContext().get_value_from_app_config(key)

    @staticmethod
    def upsert_app_config(key: str, value: object):
        return AppConfigContext().upsert_app_config(key, value)

    @staticmethod
    def update_all_app_config(content: str):
        return AppConfigContext().update_all_app_config(content)

    @staticmethod
    def get_the_folder_path_on_home(folder_name, create_if_not_exist=False):
        home = os.path.expanduser("~").replace("\\", "/")
        path = os.path.join(home, folder_name)
        if create_if_not_exist and not os.path.exists(path):
            os.makedirs(path)
        return path

    @staticmethod
    def get_current_date_time_str() -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
