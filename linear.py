requests = []
while True:
    print("1. Добавить 2. Удалить 3. Найти 4. Все 5. Выход")
    c = input("Выбор: ")
    if c == '1':
        requests.append({'dest': input("Куда: "), 'flight': input("Рейс: "), 'name': input("ФИО: "), 'date': input("Дата: ")})
    elif c == '2':
        f = input("Рейс для удаления: ")
        requests = [r for r in requests if r['flight'] != f]
    elif c == '3':
        f = input("Рейс: ")
        d = input("Дата: ")
        for r in requests:
            if r['flight'] == f and r['date'] == d:
                print(r)
    elif c == '4':
        print(requests)
    elif c == '5':
        break