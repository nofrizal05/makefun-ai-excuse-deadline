import os

LINE = "I missed the deadline because I spent six hours fact-checking my own apology for missing the deadline."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
