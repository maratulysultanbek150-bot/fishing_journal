from json import load, dump

FILE = "журнал.json"


def journal_load():
    with open(FILE, "r", encoding="utf-8") as f:
        journal = load(f)
        return f"Все записи: {journal}"


def save_journal(data):
    with open(FILE, "w", encoding="utf-8") as f:
        dump(data, f, ensure_ascii=False, indent=4)
