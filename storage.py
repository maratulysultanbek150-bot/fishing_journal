from json import load, dump, JSONDecodeError

FILE = "data.json"


def journal_load():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            journal = load(f)
        return journal if isinstance(journal, list) else []

    except (FileNotFoundError, JSONDecodeError):
        return []


def save_journal(data):
    journal_data = journal_load()

    journal_data.append(data)

    with open(FILE, "w", encoding="utf-8") as f:
        dump(journal_data, f, ensure_ascii=False, indent=4)
