import sqlite3
import PIL


def get_all_items_names():
    with sqlite3.connect('db/database.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT module_id, module_name FROM modules"""
        cursor.execute(query)
        result = dict(cursor)
        all_data = {}
        all_data['sootvetstviye'] = {result[k]: k for k in result}
        all_data['names'] = [i for i in result.values()]
        return all_data


def clear_data():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        # выполнить запрос SQL DELETE для удаления всех строк из таблицы
        cursor.execute('DELETE FROM modules_in_case')
        # сделать фиксацию изменений в базе данных
        db.commit()


def read_data():
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        cursor.execute('SELECT module_id, module_amount, row_id FROM modules_in_case WHERE COALESCE(module_id, "") != "" AND COALESCE(module_amount, "") != "" AND COALESCE(row_id, "") != ""')
        rows = cursor.fetchall()
        return rows


print(read_data())


def insert_data(data):
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = '''INSERT INTO modules_in_case (module_id, module_amount, row_id)
                 VALUES (?, ?, ?)'''
        cursor.executemany(query, data)
        db.commit()


def get_data_from(info_comb_entry):
    print(info_comb_entry)
    data = []
    for i in info_comb_entry:
        if i[0].winfo_exists() and i[1].winfo_exists():
            data.append((i[0].get(), i[1].get(), i[2]))
    return sorted(data, key=lambda x: x[2])





