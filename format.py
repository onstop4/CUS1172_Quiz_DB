#!/usr/bin/env python3
import json

with open("db.json", "r+") as file:
    j = json.load(file)
    file.seek(0)
    json.dump(j, file, separators=(",", ":"))
    file.truncate()
