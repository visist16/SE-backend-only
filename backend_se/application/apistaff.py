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

class CreateTopic(Resource):
    #CREATE A TOPIC FROM LOCAL TICKET
    #RESTRICTED TO STAFF
    def post(self):
        r=request.json
        id=r.get('ticket_id')
        cat_id=r.get('cat_id')
        #CATEGORY FIELD WILL BE ADDED TO TICKET TABLE SOON!!!!
        t=Ticket.query.filter_by(ticket_id=id).first()
        data = {
            "title":t.title,
            "raw":t.description,
            "category":cat_id
        }
        
        response = requests.post(f'http://localhost:4200/posts.json',json=data, headers=headers)
        return response.json()
    
class EditTopic(Resource):
    #EDIT AN EXISTING TOPIC
    def patch(self):
        r=request.json
        id=r.get('topic_id')
        title=r.get('title')
        category_id=r.get('category_id')

        data = {
            "topic":{
            "title":title,
            "category_id":category_id
        }
        }
        response = requests.put(f'http://localhost:4200/t/-/{id}.json',json=data, headers=headers)
        return response.json()
