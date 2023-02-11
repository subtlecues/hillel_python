import sqlite3

tables = {
    'vacancy': {
        'position_name': '',
        'company': '',
        'description': '',
        'contacts_id': '',
        'comment': '',
    }
}


def select_info(qry):
    conn = sqlite3.connect('vacancy_db.db')
    c = conn.cursor()
    c.execute(qry)
    result = c.fetchall()
    conn.close()
    return result


def insert_info(table_name, data):
    columns = ', '.join(data.keys())
    placeholders = ':' + ', :'.join(data.keys())
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, columns, placeholders)
    conn = sqlite3.connect('vacancy_db.db')
    c = conn.cursor()
    c.execute(query, data)
    conn.commit()
    conn.close()
