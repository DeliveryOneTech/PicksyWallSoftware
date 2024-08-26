import os
import json
from app.mutexs.app_config_context_mutex import SingletonAppConfigContextMutex


class AppConfigContext:
    def __init__(self):
        self.app_config_context_mutex = SingletonAppConfigContextMutex.getInstance()

    def read_all_app_config(self):
        try:
            self.app_config_context_mutex.lock()
            with open("./appconfig.json") as f:
                return json.load(f)
        except Exception as e:
            print(e)
            return None
        finally:
            self.app_config_context_mutex.unlock()

    def get_value_from_app_config(self, key):
        return self.read_all_app_config()[key]

    def upsert_app_config(self, key: str, value: object):
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
        try:
            self.app_config_context_mutex.lock()
            # if appconfig.json does not exist, create it
            if not os.path.exists("./appconfig.json"):
                return False, "Application config file does not exist."

            content = self.read_all_app_config()
            content[key] = value

            with open("./appconfig.json", "w") as f:
                json.dump(content, f, indent=4)
                f.close()

            return True, None
        except Exception as e:
            print(e)
            return False, str(e)
        finally:
            self.app_config_context_mutex.unlock()

    def update_all_app_config(self, content: str):
        """
        This method updates the appconfig.json file with the given content.
        The content should be a valid JSON string.

        :param content:
        :return:
        """
        try:
            self.app_config_context_mutex.lock()
            # pre-validation for json
            try:
                json.loads(content)
            except json.JSONDecodeError as e:
                return False, f"Invalid JSON content: {content}"

            with open("./appconfig.json", "w") as f:
                f.write(content)
                f.close()

            return True, None
        except Exception as e:
            print(e)
            return False, str(e)
        finally:
            self.app_config_context_mutex.unlock()


class SingletonAppConfigContext(AppConfigContext):
    __instance = None

    def __new__(cls):
        if SingletonAppConfigContext.__instance is None:
            SingletonAppConfigContext.__instance = AppConfigContext()
        return SingletonAppConfigContext.__instance
