requests = []

def add_req():
    requests.append({'dest': input("Куда: "), 'flight': input("Рейс: "), 'name': input("ФИО: "), 'date': input("Дата: ")})

def del_req():
    global requests
    f = input("Рейс для удаления: ")
    requests = [r for r in requests if r['flight'] != f]

def find_req():
    f = input("Рейс: ")
    d = input("Дата: ")
    for r in requests:
        if r['flight'] == f and r['date'] == d:
            print(r)

def show_all():
    print(requests)

def main():
    while True:
        c = input("1. Добавить 2. Удалить 3. Найти 4. Все 5. Выход\nВыбор: ")
        if c == '1': add_req()
        elif c == '2': del_req()
        elif c == '3': find_req()
        elif c == '4': show_all()
        elif c == '5': break

if __name__ == '__main__':
    main()