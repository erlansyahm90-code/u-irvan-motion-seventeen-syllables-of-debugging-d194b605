import os

ENTRY = "Cursor blinks at three\nthe log file says nothing new\nI am the bug now"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
