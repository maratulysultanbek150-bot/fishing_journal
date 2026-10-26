from storage import save_journal, journal_load
import datetime


def proverka(data):
    return not data.strip()


def main():
    fish_data = {}
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
                weight = float(input("Вес рыбы (кг):"))
            except ValueError:
                print("Ошибка, напиши число с точкой")
            fish_data["fish_weight"] = weight

            location = input("Место пойманной рыбы:").strip()
            if proverka(location):
                print("Нельзя пустую строку, попробуй снова")
                continue
            fish_data["location"] = location

            date = input("Внести текущую дату?(д/н)").strip()
            if ("", "да", "д", "y", "yes") in date:
                fish_data["date"] = datetime.date.today().strftime("%d.%m.%Y")
            else:
                date_2 = input("Введите дату(Д.М.Г):").strip()
                fish_data["date"] = date_2

            data = input("Еще подробности(приманка, погода, проводка и т.д.):").strip()
            if proverka(data):
                print("Нельзя пустую строку, попробуй снова")
                continue
            fish_data["comment"] = data

            save_journal(fish_data)
            print("Данные успешно сохранены")

        elif response == 2:
            print(journal_load())

        elif response == 3:
            break


main()
