from typing import Any
from pydantic import BaseModel

class IRequestResponse(BaseModel):
    message: str
    data: Any