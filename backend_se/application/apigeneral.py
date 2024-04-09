from flask_restful import Resource, request, abort
import requests
from flask import jsonify
from datetime import datetime
from dateutil import tz, parser
from application.models import *
from application.models import db
from application.routes import token_required
from application.workers import celery
from celery import chain
from application.tasks import send_email, response_notification
from datetime import datetime, timedelta
import jwt
from .config import Config
from werkzeug.exceptions import HTTPException 
from application import index

API_TOKEN="77a052969dae8a3d77c97021a8b53ef18d191761a4079c0487f255eadfcfcaff"
USER="21f1007034"                ##Just configured only for Unit Testing

headers = {
            "Api-key": API_TOKEN,
            "Api-Username": USER
        }

class Categories(Resource): 
    # LIST ALL CATEGORIES
    def get(self):
       x=requests.get("http://localhost:4200/categories.json")
       return x.json()
    
class Topics(Resource):

    #GET ALL TOPICS BY EITHER CATEGORY ID OR CATEGORY SLUG
    def get(self):
        r=request.json
        slug=r.get('slug')
        id=r.get('id')
        
        response = requests.get(f'http://localhost:4200/c/{slug}/{id}.json', headers=headers)
        return response.json()



class Notifications(Resource):
    #GET ALL NOTIFICATIONS BY USER ID
    def get(self):
        
        response = requests.get(f'http://localhost:4200/notifications.json',headers=headers)
        return response.json()
    

    
