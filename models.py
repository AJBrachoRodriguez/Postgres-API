from pydantic import BaseModel
from datetime import date

class Movies(BaseModel):
    id: int
    db_name : str
    author : str
    description: str
    release_date: date

class Movies_Update(BaseModel):
    id_to_update : int
    db_name_to_update : str
    author_updated : str
    description_updated : str
    release_date_updated : date

class Movies_Delete(BaseModel):
    id_to_delete : int
    db_name_to_delete : str
#    author_deleted : str
#    description_deleted : str
#    release_date_delete : date
 
