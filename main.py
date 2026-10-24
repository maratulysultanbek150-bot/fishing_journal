from json import load, dump
import datetime

FILE = "журнал.json"


def proverka(data):
    return data == ""


def journal_load(data):
    with open(FILE, "r", encoding="utf-8") as f:
        return load(f)


def save_journal(data):
    with open(FILE, "w", encoding="utf-8") as f:
        dump(data, f, ensure_ascii=False, indent=4)


def main():
    fish_data = dict()
    while True:
        print("""Выбери действия:
    1.Записать улов
    2.Посмотреть весь журнал
    3.Выход""")
        try:
            response = int(input())
        except ValueError:
            print("Ошибка. Напиши число от 1 до 3")
            continue
        if response == 1:
            fish = input("Вид рыбы:").strip()
            if proverka(fish):
                print("Нельзя пустую строку, попробуй снова")
                continue
            fish_data.update(fish_type=fish)
            try:
                weight = float(input())
            except ValueError:
                print("Ошибка, напиши число с точкой")

            fish_data.update(fish_weight=weight)
        if response == 3:
            break


main()
