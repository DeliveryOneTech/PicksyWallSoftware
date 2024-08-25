import json
import logging
import os
import datetime
from app.lib.system_logger import SingletonSystemLogger


class Utils:

    @staticmethod
    def read_all_app_config():
        with open("./appconfig.json") as f:
            return json.load(f)

    @staticmethod
    def get_value_from_app_config(key):
        return Utils.read_all_app_config()[key]

    @staticmethod
    def upsert_app_config(key: str, value: object):
        """
        This method updates the appconfig.json file with the given key and value.
        If the key does not exist, it creates a new key-value pair.
        Else, it updates the value of the existing key.

        Upsert = Update + Insert
        Upsert keyword is used as a method name because it is a common term in the database world.

        :param key:
        :param value:
        :return:
        """
        singleton_system_logger = SingletonSystemLogger()

        # if appconfig.json does not exist, create it
        if not os.path.exists("./appconfig.json"):
            singleton_system_logger.log("Application config file does not exist.", level=logging.CRITICAL)
            return False, "Application config file does not exist."

        content = Utils.read_all_app_config()
        content[key] = value

        with open("./appconfig.json", "w") as f:
            json.dump(content, f, indent=4)
            f.close()

        singleton_system_logger.log(f"Application config file is updated. Key: {key}, Value: {value}")
        return True, None

    @staticmethod
    def update_all_app_config(content: str):
        singleton_system_logger = SingletonSystemLogger()

        # pre-validation for json
        try:
            json.loads(content)
        except json.JSONDecodeError as e:
            singleton_system_logger.log(f"Invalid JSON content: {content}", level=logging.CRITICAL)
            return False, f"Invalid JSON content: {content}"

        with open("./appconfig.json", "w") as f:
            f.write(content)
            f.close()

        singleton_system_logger.log("Application config file is updated. This update is for all content.")
        return True, None

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
