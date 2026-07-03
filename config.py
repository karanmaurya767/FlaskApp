# class Config:
#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:CdBnaxGcyrmtORIlFCJxPFivvOdNBVDb@thomas.proxy.rlwy.net:49527/railway"

#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = "00110101"




import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:00110101@localhost/flask_login"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv("SECRET_KEY", "00110101")




# class Config:
#     SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:00110101@localhost/flask_login"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = "00110101"