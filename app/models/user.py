from main import db


def insert():
    user = User()
    user.id = "1234"
    user.username = "5678"
    user.email = "12345"
    db.session.add(user)
    db.session.commit()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
