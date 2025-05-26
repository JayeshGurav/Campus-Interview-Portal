import os

class Config:
    # COMMENT: Change secret key for production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://enrolluser:enrollpass@localhost/campus_interview'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # COMMENT: Adjust these values as needed
    ADMIN_EMAIL = 'admin@campus.edu'
    STUDENT_ROLE = 'student'
    ADMIN_ROLE = 'admin'