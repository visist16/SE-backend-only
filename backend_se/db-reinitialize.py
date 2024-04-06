from application import app
from application.models import *

db.drop_all()
db.create_all()