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


class DB:

    def __enter__(self):
        self.conn = sqlite3.connect('vacancy_db.db')
        self.c = self.conn.cursor()
        return self

    def query(self,qry):
        self.c.execute(qry)
        result = self.c.fetchall()
        return result

    def insert(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ':' + ', '.join(data.keys())
        query = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, columns, placeholders)
        self.c.execute(query, data)
        self.conn.commit()

    def close(self):
        self.c.close()
        self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.c.close()
        self.conn.close()

#
# def select_info(list_qry):
#     conn = sqlite3.connect('vacancy_db.db')
#     c = conn.cursor()
#
#     results = []
#
#     for qry in list_qry:
#         c.execute(qry)
#         result = c.fetchall()
#         results.append(result)
#     conn.close()
#     return results

#
# def insert_info(table_name, data):
#     columns = ', '.join(data.keys())
#     placeholders = ':' + ', :'.join(data.keys())
#     query = 'INSERT INTO %s (%s) VALUES (%s)' % (table_name, columns, placeholders)
#     conn = sqlite3.connect('vacancy_db.db')
#     c = conn.cursor()
#     c.execute(query, data)
#     conn.commit()
#     conn.close()
