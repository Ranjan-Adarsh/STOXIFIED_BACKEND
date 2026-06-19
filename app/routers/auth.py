from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserOut, Token
from app.services.users import create_user, get_user_by_username
from app.core.security import create_access_token, verify_password

router = APIRouter(prefix = "/auth",tags=["Auth"])

@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate):
    return create_user(user.username, user.email, user.full_name, user.password)

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}
