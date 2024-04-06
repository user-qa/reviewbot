import random

import psycopg2 as psql

from main import config


class DATABASE:
    def __init__(self):
        self.conn = psql.connect(
            database=config.DB_NAME,
            password=config.DB_PASS,
            user=config.DB_USER,
            host=config.DB_HOST
        )

        self.cursor = self.conn.cursor()

    def create_tables(self):
        user_table = """
        Create table if not exists users(
        id Serial primary key,
        chat_id bigint unique,
        full_name varchar(55),
        phone_number varchar(13),
        location_name varchar(50)
        )
        """

        photos = """create table if not exists photos(
        id serial primary key,
        chat_id bigint references users(chat_id),
        photo_id text unique,
        status boolean default false
        )"""

        likes = """create table if not exists likes (
        id serial primary key,
        chat_id bigint,
        photo_id text references photos(photo_id),
        is_like boolean default false
        )"""

        self.cursor.execute(user_table)
        self.cursor.execute(photos)
        self.cursor.execute(likes)

        self.conn.commit()

    def get_user_chat_id(self, chat_id):
        query = f"select * from users where chat_id = '{chat_id}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def add_user(self, data: dict):
        chat_id = data['chat_id']
        full_name = data['full_name']
        phone_number = data['phone_number']
        location_name = data['location']
        query = f"""insert into users(chat_id, full_name, phone_number, location_name) values ({chat_id}, '{full_name}', '{phone_number}', '{location_name}')"""
        self.cursor.execute(query)
        self.conn.commit()

    def add_user_photo(self, data):
        chat_id = data['chat_id']
        photo = data['photo']
        query = f"insert into photos(chat_id, photo_id, status) values('{chat_id}', '{photo}', true)"
        self.cursor.execute(query)
        self.conn.commit()

    def get_photo_by_chat_id(self, chat_id):
        query = f"select * from photos where chat_id = {chat_id} and status = true"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result

    def get_random_photo(self, chat_id):
        query = f"select * from photos where chat_id != {chat_id} and status = true"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        if results:
            return random.choice(results)

    def get_liked_and_disliked_photos(self, photo_id):
        query_liked = f"select count(*) from likes where photo_id = '{photo_id}' and is_like = true"
        query_dislike = f"select count(*) from likes where photo_id = '{photo_id}' and is_like = false"

        self.cursor.execute(query_liked)
        number_of_likes = self.cursor.fetchone()
        self.cursor.execute(query_dislike)
        number_of_dislikes = self.cursor.fetchone()

        return number_of_likes, number_of_dislikes
