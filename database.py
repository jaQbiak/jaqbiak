import os
import dotenv
import psycopg2


dotenv.load_dotenv()


class Database(object):
    def connect_to_database(self):
        return psycopg2.connect(
            host=os.environ['HOST'],
            database=os.environ['DATABASE'],
            user=os.environ['USERNAME'],
            password=os.environ['PASSWORD']
        )