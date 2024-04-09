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


class CreateCategory(Resource):
    #CREATE A CATEGORY
    #can be restricted to admin later
    def post(self):

        r=request.json

        data = {
            "name": r.get('name'),
            "color": r.get('color'),
            "text_color": "f0fcfd",
            "allow_badges": "true",
            "topic_featured_links_allowed": "true",
            "permissions": {
                "everyone": 1,
                "staff": 0
            },
            "search_priority": 0,
            "form_template_ids": []
            }
        
        x = requests.post("http://localhost:4200/categories.json", json=data,headers=headers)
        if x.status_code==200:
            return jsonify({"message":"Category created successfully"})
        else:
            abort(404,message="Failed to create Category")

class EditCategory(Resource):
    #UPDATE A CATEGORY
    #can be restricted to admin later
    def patch(self):

        r=request.json
        id=r.get('id')
        del r['id']
    
        x = requests.put(f'http://localhost:4200/categories/{id}.json', json=r,headers=headers)
        if x.status_code==200:
            return jsonify({"message":"Category updated successfully"})
        else:
            abort(404,message="Failed to update Category")
