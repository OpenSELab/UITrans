import json
import orjson

filepath = r"D:\Codes\ArkTS\dashbook\entry\src\main\resources/base/element/string.json"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()
print(content)
print(orjson.loads(content))