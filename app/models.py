from typing import List

from pydantic import BaseModel


class Request(BaseModel):
    data: List[int]
