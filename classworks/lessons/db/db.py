import sqlite3
from pprint import pprint

def create():
    cur.execute(
    """
    CREATE TABLE if not exists names(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lastname TEXT,
    firstname TEXT,
    twoname TEXT)
    """)
    con.commit()
    return 'Done'

def insert(l, f, t):
    cur.execute(
    """
    INSERT INTO names(lastname, firstname, twoname) VALUES (?, ?, ?)
    """, (l, f, t))
    con.commit()
    return 'Done'

def delete(n):
    cur.execute(
    """
    DELETE FROM names WHERE id = (?)
    """, (int(n),))
    con.commit()
    return 'Done'

def view():
    res = cur.execute(
    """
    SELECT * FROM names
    """)
    return res.fetchall()

def sorting(z='firstname'):
    res = cur.execute(
    """
    SELECT * FROM names ORDER BY {}
    """.format(z))
    return res.fetchall()
    

if __name__ == '__main__':
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    create()
    print('Приветствуем!\n\nВведите i чтобы создать нового пользователя.\n'
          'Введите d чтобы удалить пользователя.\n'
          'Введите v чтобы посмотреть пользователей.\n'
          'Введите s чтобы отсортировать пользователей.\n\n')
    while True:
        c = input()
        if c.strip() == 'i':
            l = input('Введите фамилию: ')
            f = input('Введите имя: ')
            t = input('Ввелиие Отчество: ')
            pprint(insert(l, f, t))
        elif c.strip() == 'd':
            n = input('Введите id пользователя: ')
            pprint(delete(n))
        elif c.strip() == 'v':
            pprint(view())
        elif c.strip() == 's':
            n = input('Введите поле для сортировки.\n\n'
                      '"l" - сортировка по фамилии\n'
                      '"f" - сортировка по имени\n'
                      '"t" - сортировка по отчеству\n\n')
            if n == 'l':
                pprint(sorting('lastname'))
            elif n == 'f':
                pprint(sorting('firstname'))
            elif n == 't':
                pprint(sorting('twoname'))
            else:
                print('Поле ввода не соответствует критерию.')
        else:
            print('Поле ввода не соответствует критерию.')






