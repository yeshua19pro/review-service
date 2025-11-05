from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from utils.time import utc_now_iso


#ENUM TYPES FOR REVIEW EVENTS
class ReviewEventTypes(str, Enum):
    REVIEW_CREATE_SUCCESS = "reviews.create_review" # event for worker


# BASE MODEL FOR REVIEW EVENT
class BaseReviewEvent(BaseModel):
    book_id: str
    event_type: ReviewEventTypes
    rating: float


# EVENT BUILDER FUNCTION

def build_review_event(rating: float, book_id: str) -> dict:
    return BaseReviewEvent(
        event_type=ReviewEventTypes.REVIEW_CREATE_SUCCESS,
        rating= rating,
        book_id = book_id
    ).model_dump()


