from pydantic import BaseModel


class AddPageRequest(BaseModel):
    link: str
    type: int


class DeletePageRequest(BaseModel):
    id: int


class CheckRequest(BaseModel):
    message: str