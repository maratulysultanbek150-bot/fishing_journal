from storage import save_journal, journal_load
import datetime


def proverka(data):
    return data == ""


def main():
    fish_data = dict()
    while True:
        print("""Выбери действия:
    1.Записать улов
    2.Посмотреть весь журнал
    3.Выход""")

        try:
            response = int(input("Ответ:"))
        except ValueError:
            print("Ошибка. Напиши число от 1 до 3")
            continue

        if response == 1:
            fish = input("Вид рыбы:").strip()
            if proverka(fish):
                print("Нельзя пустую строку, попробуй снова")
                continue
            fish_data["fish_type"] = fish

            try:
                weight = float(input("Вес рыбы:"))
            except ValueError:
                print("Ошибка, напиши число с точкой")
            fish_data["fish_weight"] = weight

        elif response == 2:
            print(journal_load())

        elif response == 3:
            break


main()
