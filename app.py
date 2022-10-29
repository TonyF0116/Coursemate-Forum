from forum import create_app
from forum.db import db


app = create_app()
db.init_app(app)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
