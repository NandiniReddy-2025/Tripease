from app import create_app
from models import db, User

app = create_app()
with app.app_context():
    admin = User(username='admin', email='admin@gmail.com', is_admin=True)
    admin.set_password('tester')  # Replace with a strong password
    db.session.add(admin)
    db.session.commit()
    print('Admin user created!')