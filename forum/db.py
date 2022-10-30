from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# For using sqlalchemy ORM
db = SQLAlchemy()

# "mysql+pymysql://username:password@host:port/database"
engine = create_engine(
    "mysql+pymysql://root:qwerty12@coursepartnermatcher.cpzyc87uemgs.us-east-2.rds.amazonaws.com/CoursePartnerMatcher")
