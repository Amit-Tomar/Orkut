from src import db
from src.model import User, Post

class SeedDev():
  def run(self, app):
    with app.app_context():
        from faker import Faker

        fake = Faker()

        for i in range(5):
            user = User(username=fake.name(),email=fake.email())
            print("Adding user: %s" % user)
            db.session.add(user)

            for j in range(10):
                post = Post(body=fake.text(50),author=user)
                print("Adding post: %s" % post)
                db.session.add(user)

            db.session.commit()