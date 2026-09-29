import json
import os


class MultiLanguage:
    def __init__(self, default_lang="zh-CN"):
        self.lang_data = {}
        self.current_lang = default_lang
        self.lang_folder = "./lang/"

    def load_language(self, lang_code):
        file_path = os.path.join(self.lang_folder, f"{lang_code}.json")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.lang_data = json.load(f)
            self.current_lang = lang_code
            return True
        except Exception as e:
            print(f"Load language failed: {e}")
            return False

    def get_text(self, key):
        return self.lang_data.get(key, f"[{key}]")


if __name__ == "__main__":
    lang = MultiLanguage()

    lang.load_language("zh-CN")
    print(lang.get_text("msg_welcome"))

    lang.load_language("zh-HK")
    print(lang.get_text("msg_welcome"))

    lang.load_language("zh-TW")
    print(lang.get_text("msg_welcome"))

    lang.load_language("zh-MO")
    print(lang.get_text("msg_welcome"))

    lang.load_language("zh-classic")
    print(lang.get_text("msg_welcome"))

    lang.load_language("en-GB")
    print(lang.get_text("msg_welcome"))

    lang.load_language("en-US")
    print(lang.get_text("msg_welcome"))

    lang.load_language("ja")
    print(lang.get_text("msg_welcome"))

    lang.load_language("ko")
    print(lang.get_text("msg_welcome"))
