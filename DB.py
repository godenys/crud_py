import pymysql


class DB:

    def __init__(self):
        self.connection = pymysql.connect(host='localhost', user='root', passwd='1', db='crud_py')
        self.myCursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def get_all(self, table):
        self.myCursor.execute("SELECT * FROM `%s` WHERE `deleted`=0;" % table)
        data = self.myCursor.fetchall()
        self.myCursor.close()
        self.connection.close()
        return data

    def find(self, table, id):
        self.myCursor.execute("SELECT * FROM `%s` WHERE `id`=%d;" % (table, int(id)))
        data = self.myCursor.fetchone()
        self.myCursor.close()
        self.connection.close()
        return data

    def store(self, table, data):
        keys = map(lambda x: '`{}`'.format(x), data.keys())
        string_of_keys = ', '.join(keys)
        values = map(lambda x: "'{}'".format(x), data.values())
        placeholders = ', '.join(values)
        self.myCursor.execute("INSERT INTO `%s`(%s) VALUES(%s);" % (table, string_of_keys, placeholders))
        self.connection.commit()
        self.connection.close()

    def update(self, table, id, data):
        fields = ''
        for item in data:
            fields += '`'+item+'`' + "='" + data[item] + "',"
        fields = fields[:-1]
        self.myCursor.execute("UPDATE `%s` SET %s WHERE `id`=%d;" % (table, fields, int(id)))
        self.connection.commit()
        self.connection.close()

    def remove(self, table, id):
        self.myCursor.execute("UPDATE `%s` SET `deleted`=1 WHERE `id`=%d;" % (table, int(id)))
        self.connection.commit()
        self.connection.close()
