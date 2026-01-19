from .libs import json


def json_read(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.loads(file.read())
    except FileNotFoundError:
        print("找不到檔案")
        return {}
    except Exception as e:
        print(f"{path} - 例外錯誤:", e)
        return {}


def json_parse(text: str) -> dict:
    try:
        return json.loads(text)
    except Exception as e:
        print(f"{text} - 例外錯誤:", e)
        return {}


def json_write(path: str, data: dict) -> None:
    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(json.dumps(data, indent=4, separators=(",", ":"), ensure_ascii=False))
    except FileNotFoundError:
        print("找不到檔案")
    except Exception as e:
        print(f"{path} - 例外錯誤:", e)
