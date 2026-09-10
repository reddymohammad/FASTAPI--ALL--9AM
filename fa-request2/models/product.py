from pydantic import BaseModel

class ProductModel(BaseModel):
  pid:int
  pname:str
  price:float
  category:str