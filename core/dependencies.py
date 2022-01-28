from database.database import SessionLocal
from parser.sites import *


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_parser(page):
    if page.type == 1:
        to_parse = Mangakakalot(page.link)
    elif page.type == 2:
        to_parse = Readmanganato(page.link)
    return to_parse
