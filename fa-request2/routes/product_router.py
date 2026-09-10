from fastapi import APIRouter
router=APIRouter(prefix='/products')

from models.product import ProductModel


products=[
    {'pid':101,'pname':'Marker Pen','price':30,'category':'Stationary'},
    {'pid':102,'pname':'Lenovo Mouse','price':400,'category':'Electronics'},
    {'pid':103,'pname':'ThinkPad','price':108000,'category':'Electronics'},
    {'pid':104,'pname':'Water Bottle','price':10,'category':'Groceries'},
    {'pid':105,'pname':'Dell Inspiron','price':150000,'category':'Electronics'},
    {'pid':106,'pname':'Mac Book Pro','price':183000,'category':'Electronics'},
    {'pid':107,'pname':'Stappler','price':35,'category':'Stationary'},
    {'pid':108,'pname':'R Pen','price':10,'category':'Stationary'},
    {'pid':109,'pname':'Parker Pen','price':200,'category':'Stationary'},
    {'pid':110,'pname':'Meta Rayban','price':40000,'category':'Electronics'}
]




@router.post("/create")
def create_product(product:ProductModel):
  products.append(product)
  return {'msg':'new product created successfully'}


@router.get("/read")
def get_product():
  return products

'''
usage: fetch products between min price to max price
rest API url :http://127.0.0.1:8000/products/range?min=500max=50000
Method type:get
required fields:none
acess type:public
'''
@router.get("/range")
def get_products_filter(min:int,max:int):
  return list(filter(lambda product:min<=product['price']<=max,products))
