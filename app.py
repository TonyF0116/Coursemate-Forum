from forum import create_app
from forum.db import db

from sqlalchemy import *


app = create_app()
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # engine = create_engine("sqlite:///forum_raw.db")
    # connection = engine.connect()
    # connection.execute('DROP TABLE IF EXISTS Project')
    # connection.execute('''CREATE TABLE Project (id INT PRIMARY KEY,
    #                                             title VARCHAR(50),
    #                                             group_leader VARCHAR(10),
    #                                             description VARCHAR(255),
    #                                             project_start_date DATE,
    #                                             project_end_date DATE);''')
    # connection.close()

    app.run(debug=True)
