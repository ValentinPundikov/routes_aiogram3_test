import re
import sqlite3


# ПОРАБОТАТЬ С ЗАПРОСАМИ ПРАВИЛЬНО!!!

class sql_request:
    def __init__(self):
        self.con = sqlite3.connect("metanit.db")
        self.cursor = self.con.cursor()

    def repl(self,data):
        result = str(data)
        result = re.sub("['|)|(|,]", "", result)
        return result

    # Создание БД
    def create_db(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT,name TEXT, phone TEXT, lat FLOAT, lon FLOAT, role BOOL, locked BOOL);")
        self.con.commit()

    def set_id(self,user_id):
        self.cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        data = self.cursor.fetchone()
        if data is None:
            self.cursor.execute(
                "INSERT INTO  users (id)  VALUES (?)",(user_id,))
            self.con.commit()
        # Получение чистой строки
        # else:
        #     result = str(data)
        #     data_1 = re.sub("['|)|(|,]", "",result)
        #     print(data_1)


    def set_or_update_username(self,user_id,message):
        self.cursor.execute(
            "UPDATE users SET name=? WHERE id = ? ", (message, user_id,))
        self.con.commit()


    def set_or_update_number(self,user_id,number):
        self.cursor.execute("SELECT phone FROM users WHERE id = ?", (user_id,))
        data = self.cursor.fetchone()
        data = self.repl(data)
        if data == "None" or data != "None":
            self.cursor.execute(
                "UPDATE users SET phone = ? WHERE id = ? ", (number,user_id,))
            self.con.commit()


    def set_or_update_lat_lon(self,user_id,lat,lon):
        self.cursor.execute("SELECT lat FROM users WHERE id = ?", (user_id,))
        latitude = self.cursor.fetchone()
        self.cursor.execute("SELECT lon FROM users WHERE id = ?", (user_id,))
        longitude = self.cursor.fetchone()
        latitude = self.repl(latitude)
        longitude = self.repl(longitude)
        if (latitude != "None" and longitude != "None") or (latitude == "None" and longitude == "None"):
            self.cursor.execute(
                "UPDATE users SET lat = ?,lon=? WHERE id = ? ", (lat,lon,user_id,))
            self.con.commit()

    def get_id(self,user_id):
        self.cursor.execute("SELECT id FROM users WHERE id = ?", (user_id,))
        id_of_user = self.cursor.fetchone()
        id_of_user = self.repl(id_of_user)
        return id_of_user

    def get_phone(self,user_id):
        self.cursor.execute("SELECT phone FROM users WHERE id = ?", (user_id,))
        phone_of_user = self.cursor.fetchone()
        phone_of_user = self.repl(phone_of_user)
        return phone_of_user

    def set_or_update_phone(self,user_id,message):
        self.cursor.execute("UPDATE users SET phone = ? WHERE id = ?",(message,user_id,))
        return True

    def get_lat_lon(self,user_id,lat_lon):
        self.cursor.execute(f"SELECT {lat_lon} FROM users WHERE id = ?", (user_id,))
        lat = self.cursor.fetchone()
        lat = self.repl(lat)
        return lat

    def standart_role_for_user(self,user_id):
        self.cursor.execute("UPDATE users SET role = ? WHERE id = ?",(0,user_id,))
        return True

    def set_role(self,user_id, status):
        self.cursor.execute("UPDATE users SET role = ? WHERE id = ?", (status, user_id,))
        self.con.commit()
        return True

    def get_role(self,user_id):
        self.cursor.execute("SELECT role FROM users WHERE id = ?", (user_id,))
        role_id = self.cursor.fetchone()
        role_id = self.repl(role_id)
        if role_id == "0":
            return "Ваша роль = 0"
        else:
            return "Ваша роль = 1"

    def delete_user(self,user_id):
        # DELETE FROM имя_таблицы WHERE [условие];
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        return f"Пользователь с ID {user_id} удален из базы данных."

    def check_lock(self,user_id):
        self.cursor.execute("SELECT lock FROM users WHERE id = ?", (user_id,))
        lock_status = self.cursor.fetchone()
        lock_status = self.repl(lock_status)
        return lock_status

    def get_my_info(self,user_id):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        my_status = self.cursor.fetchall()
        return my_status

    # ПОРАБОТАТЬ НАД ФУНКЦИЕЙ ЕЩЕ! НЕПРАВИЛЬНЫЙ ВЫВОД.
    def get_all_users(self):
        self.cursor.execute("SELECT id FROM users")

        # Получаем результат сделанного запроса
        results = self.cursor.fetchall()
        results = self.repl(results)
        return results

    def unlock_lock_user(self,user_id,boool):
        self.cursor.execute("UPDATE users SET role = ? WHERE id = ?", (boool,user_id,))









sql = sql_request()
# sql.create_db()
# i = 0
# while i < 10:
#     sql.set_id(i)
#     i+=1
#
#
#
# ss = sql.get_all_users()
#
# sql.set_or_update_number(321,73483)
# sql.set_or_update_lat_lon(321,111.2,121.4)
# sqll = sql.get_lat_lon(321,"lat")
# sqll1 = sql.get_lat_lon(321,"lon")
# print(sqll + " " + sqll1)
data = sql.get_id(11)
print(data)