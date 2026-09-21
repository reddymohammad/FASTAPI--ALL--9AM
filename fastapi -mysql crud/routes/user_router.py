from fastapi import APIRouter,HTTPException
router=APIRouter(prefix='/users')
users_db = [
{"user_id": 102, "name": "Bob", "email": "bob@example.com"},
{"user_id": 103, "name": "Charlie", "email": "charlie@example.com"},
{"user_id": 101, "name": "Alice", "email": "alice@example.com"},
{"user_id": 104, "name": "David", "email": "david@example.com"}
]


'''
usage:Users Root Request
Rest API URL: http://127.0.0.1:8000/users/
Method Type:GET
Required Fields:None
Access Type:public
'''
@router.get("/")
def users_root():
    return {'msg':'User Router Root Request'}


'''
usage:find user by user id
Rest API URL: http://127.0.0.1:8000/users/101
Method Type:GET
Required Fields:None
Access Type:public
'''
@router.get("/{user_id}")
def get_user(user_id:int):
    for user in users_db:
        if user['user_id']==user_id:
            return user 
    raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
