
import sqlalchemy as sa
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin



from app import db, app

class Free_Cars(db.Model, UserMixin):  
    __tablename__ = 'free_cars'

    id = db.Column(db.Integer, primary_key=True)    
    model = db.Column(db.String(40), nullable=False)
    number = db.Column(db.String(250), nullable=False)
    reserve = db.Column(db.String(100), nullable=False)

class Cars(db.Model, UserMixin):  
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)    
    phone = db.Column(db.String(40), nullable=False)
    sms = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(100), nullable=False)
    fuel_level = db.Column(db.String(100), nullable=False)

    
    
    def check_password(self, sms: str):
        return self.sms == sms


    



    


