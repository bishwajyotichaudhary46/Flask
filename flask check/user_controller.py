from app import app
from model import model
obj = model()


@app.route("/user/signup")
def signup_controller():
    return obj.user_signup_model()