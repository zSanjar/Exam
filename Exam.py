# Sanjar Ziyovuddinov   group --> N47


# 1-masala

import psycopg2

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        host='localhost',
                        port=5432,
                        password='0123')

cur = conn.cursor()

# create_table_query = """
# CREATE TABLE IF NOT EXISTS Product (
# id SERIAL PRIMARY KEY,
# name VARCHAR(255) NOT NULL,
# price INTEGER NOT NULL,
# color VARCHAR(255) NOT NULL,
# image VARCHAR(255) NOT NULL
# );"""
#
# cur.execute(create_table_query)
# conn.commit()
# cur.close()
# conn.close()

# -----------------------------------------------------------------
# 2-masala


def insert_product():
    name = input('Enter Product Name: ')
    price = input('Enter Product Price: ')
    color = input('Enter Product Color: ')
    image = input('Enter Product Image: ')
    data = [name, price, color, image]
    insert_product_ = """
    INSERT INTO Product (name, price, color, image)
    VALUES(%s, %s, %s, %s);"""
    cur.execute(insert_product_, data)
    conn.commit()
# insert_product()


def select_product():
    select_product_ = """ 
    SELECT * FROM Product;
    """
    cur.execute(select_product_)

    select = cur.fetchall()
    print(select)

# select_product()


def delete_product():

    id = input('Enter Product ID: ')
    delete_product_ = """
    DELETE FROM Product WHERE id = %s;
    """
    cur.execute(delete_product_, id)
    conn.commit()

# delete_product()


def update_product():
    id = input('Enter Product ID: ')
    name = input('Enter new Product Name: ')
    price = input('Enter new Product Price: ')
    color = input('Enter new Product Color: ')
    image = input('Enter new Product Image: ')
    update_product_ = """
    UPDATE Product SET name = %s, price = %s, color = %s, image = %s WHERE id = %s;
    """
    data = (name, price, color, image, id)
    cur.execute(update_product_, data)
    conn.commit()

# update_product()


# --------------------------------------------------------------------------------------
# 3-masala
# import string
#
# my_alphabet = string.ascii_lowercase
# class Alphabet:
#     def __init__(self):
#         self.letters = string.ascii_lowercase
#         self._index = 0
#     def __iter__(self):
#
#         return self
#
#     def __next__(self):
#         if self._index < len(self.letters):
#             item = self.letters[self._index]
#             self._index += 1
#             return item
#         else:
#             raise StopIteration
#
# # Test qilish
# alphabet = Alphabet()
# for letter in alphabet:
#     print(letter)

# -----------------------------------------------------------------------------------

# 4-masala


# import threading
# import time
# def print_numbers():
#         for number in range(1, 5):
#             print(number)
#             time.sleep(1)
#
# def print_letters():
#     for letter in ('A', 'B', 'C', 'D', 'E', 'F'):
#         print(letter)
#
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()


# ------------------------------------------------------------------

# 5-masala

class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        name = self.name
        price = self.price
        color = self.color
        image = self.image
        data = (name, price, color, image)
        insert_product = """
        INSERT INTO Product (name, price, color, image)
        VALUES(%s, %s, %s, %s);
        """
        cur.execute(insert_product, data)
        conn.commit()




# -----------------------------------------------------------------

# 6-masala

# db = {'port': 5432,
#       'host': 'localhost',
#       'user': 'postgres',
#       'password': '0123',
#       'database': 'postgres'
#       }
#
#
# class DBConnect:
#     def __enter__(self):
#         self.conn = psycopg2.connect(**db)
#         self.cur = self.conn.cursor()
#         print(self.cur.fetchall())
#         return self.conn
#
#     def __exit__(self):
#
#             self.cur.close()
#             self.conn.close()
#

# ------------------------------------------------------------------------------------------------

# 7-masala

# import requests
#
# url = 'https://dummyjson.com/products/'
#
# r = requests.get(url)
#
#
# create_table_products = """create table products(
#         id serial primary key ,
#         title varchar(255) ,
#         description text ,
#         price int,
#         discountPercentage float,
#         rating float ,
#         stock int
# );"""
#
# cur = conn.cursor()
# cur.execute(create_table_products_query)
# conn.commit()
#
#
#
# insert_into = """insert into products (title, description, price,
# discountPercentage, rating, stock)
#
#     values (%s,%s,%s,%s,%s,%s);
#
# """
#
# for product in r.json()['products']:
#     cur.execute(insert_into_query, (
#         product['title'], product['description'],
#         product['price'], product['discountPercentage'], product['rating'],
#         product['stock']))
#     conn.commit()