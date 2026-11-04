from storage import save_journal, journal_load
import datetime


def proverka(data):
    return not data.strip()


def main():
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
            fish_data = {}
            fish = input("Вид рыбы:").strip()
            if proverka(fish):
                print("Нельзя пустую строку, попробуй снова")
                continue
            fish_data["fish_type"] = fish

            try:
                weight = float(input("Вес рыбы (кг):"))
            except ValueError:
                print("Ошибка, напиши число с точкой")
                continue
            fish_data["fish_weight"] = weight

            location = input("Место пойманной рыбы:").strip()
            if proverka(location):
                print("Нельзя пустую строку, попробуй снова")
                continue
            fish_data["location"] = location

            date_input = (
                input("Внести текущую дату? (Enter — да, иначе любая буква): ")
                .strip()
                .lower()
            )
            if not date_input or date_input == ("да", "д", "y", "yes"):
                fish_data["date"] = datetime.date.today().strftime("%d.%m.%Y")
            else:
                fish_data["date"] = input("Введите дату (ДД.ММ.ГГГГ): ").strip()

            data = input("Еще подробности(приманка, погода, проводка и т.д.):").strip()
            fish_data["comment"] = data

            save_journal(fish_data)
            print("Данные успешно сохранены")

        elif response == 2:
            print(journal_load())

        elif response == 3:
            break

        else:
            print("Ошибка. Такого пункта нет, выберите число от 1 до 3.")
            continue


main()
