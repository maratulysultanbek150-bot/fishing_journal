from json import load, dump
import datetime

FILE = 'журнал.json'

def journal_load(data):
    with open(FILE , 'r', encoding='utf-8') as f:
        return load(f)
    

def save_journal(data):
    with open(FILE, 'w', encoding="utf-8") as f:
            dump(data, f, ensure_ascii=False, indent=4)
    

def main():
    while True:        
        print('''Выбери действия:ыыыыы
        1.Записать улов
        2.Посмотреть весь журнал
        3.Выход''')
        try:
             response = int(input())
        except ValueError:
             print('Ошибка. Напиши число от 1 до 3')
             continue
        if response == 1:
             