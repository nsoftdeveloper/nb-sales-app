from pydantic import BaseModel
from typing import Optional

class Category(BaseModel):
    id_category: int
    category: str
    sub_category: str
    description: Optional[str] = None