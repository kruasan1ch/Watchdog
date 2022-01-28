from fastapi import Request, Depends, APIRouter
from config import templates
from sqlalchemy.orm import Session
from core.dependencies import get_db, get_parser
from database.models import Page
from core.custom_requests import *
from core.enums import PageTypes
from parser.sites import Mangakakalot, Readmanganato
from datetime import datetime

router = APIRouter()


@router.get("/")
async def root(request: Request, db: Session = Depends(get_db)):
    pages = db.query(Page).all()
    updated = []
    for page in pages:
        if page.last_check is not None and page.last_update is not None and page.last_check == page.last_update.date():
            updated.append(page)

    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "page_types": PageTypes,
        "updated": updated,
        "pages": pages
    })


@router.post("/add_page")
async def add(add_page_request: AddPageRequest, db: Session = Depends(get_db)):
    page = Page()
    page.link = add_page_request.link
    page.type = add_page_request.type
    to_parse = get_parser(page)
    page.name = to_parse.get_name()
    db.add(page)
    db.commit()

    return {
        "message": "ok"
    }


@router.post("/del_page")
async def delete(add_page_request: DeletePageRequest, db: Session = Depends(get_db)):
    page = db.query(Page).filter(Page.id == add_page_request.id).first()
    db.delete(page)
    db.commit()

    return {
        "message": "ok"
    }


@router.post("/check")
async def check(request: CheckRequest, db: Session = Depends(get_db)):
    pages = db.query(Page).all()
    for page in pages:
        to_parse = get_parser(page)
        parsed = to_parse.parse()
        if len(parsed) != 0:
            if page.last_chapter is not None and page.last_chapter != parsed[0][0] or page.last_chapter is None:
                page.last_chapter = parsed[0][0]
                page.last_update = datetime.now()
            elif page.last_chapter == parsed[0][0]:
                continue
        page.last_check = datetime.now().date()
    db.commit()
