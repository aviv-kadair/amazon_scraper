"""
Create our database for the amazon project
Author: Serah
"""
import mysql.connector
import config
from Logging import logger
import sys


sys.path.append('../')
DB_FILENAME = config.DB_FILENAME


def create_db():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='Abensour1'
    )

    logger.info("\n*** Connection was created successfully. ***\n")

    conn = db.cursor()
    conn.execute(f"DROP DATABASE IF EXISTS {config.DB_FILENAME}" )
    conn.execute(f"CREATE DATABASE IF NOT EXISTS {config.DB_FILENAME}")
    db.commit()
    logger.info("\n*** Database was created successfully. ***\n")


def connect_to_db(host='localhost', user='root', psw='Abensour1'):
    db = mysql.connector.connect(
        host=host,
        user=user,
        passwd=psw,
        database=config.DB_FILENAME)
    return db


def create_tables():
    db = connect_to_db()
    conn = db.cursor(buffered=True)

    try:
        conn.execute(config.TABLE1)
        db.commit()
        conn.execute(config.TABLE2)
        db.commit()
        conn.execute(config.TABLE3)
        db.commit()
        conn.execute(config.TABLE4)
        db.commit()
        conn.execute(config.KEY_TABLE1)
        conn.execute(config.KEY_TABLE2)
        db.commit()
        logger.info("\n*** Created tables successfully ***\n")
    except Exception as e:
        logger.error(f'{e} ')

    finally:
        db.close()

