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
    
class Merge(Resource):
    def put(self):
        try:
            r=request.json
            ticket_id=r.get('ticket_id')
            topic_id=r.get('topic_id')
            t=Ticket.query.filter_by(id=ticket_id).first()
            t.merged=topic_id
            db.session.commit()
            return jsonify({"message":"Merged Ticket with Topic"})
        except:
            abort(404,message="Failed to Merge the Ticket")

class ResolveTicket(Resource):
    def put(self):
        try:
            r=request.json
            id=r.get('ticket_id')
            t=Ticket.query.filter_by(id=id).first()
            t.resolved=True
            db.session.commit()
            return jsonify({"message":"Resolved Ticket"})
        except:
            abort(404,message="Failed to Resolve Ticket")

class ResolveTopic(Resource):
    def put(self):
        try:
            r=request.json
            resolution=r.get('resolution')
            topic_id=r.get('topic_id')
            data={
                "raw":resolution,
                "topic_id":topic_id
            }
            response = requests.post(f'http://localhost:4200/posts.json',json=data, headers=headers)
            if response.status_code==200:
                r=response.json
                id=r.get('id')
                t=Topic.query.filter_by(topic_id=topic_id).first()
                t.solution_post_id=id
                db.session.commit()
                return jsonify({"message":"Resolved Topic"})
            else:
                abort(404,message="Failed to post the resolution")
            
        except:
            abort(404,message="Failed to Resolve Topic")


class StaffProfile(Resource):
    #@token_required
    def get(self):
        try:
            id=2
            #id=user.id
            user=User.query.filter_by(id=id).first()
            d = {
                'username': user.username,
                'email': user.email,
                'role': user.role,
                'discourse_id': user.discourse_id,
                'status': user.status,
                'notification': user.notification,
                'email_notif': user.email_notif,
                'webhook_notif': user.webhook_notif
                }   
            return jsonify({"data": d})
        except:
            abort(401,message="Failed to fetch user details")

class AllottedCategory(Resource):
    #@token_required
    def get(self):
        try:
            id=2
            #id=user.id
            cat=CategoryAllotted.query.filter_by(staff_id=id , is_approved=1).all()
            cat_list=[]
            for c in cat:
                d = {
                    'staff_id':c.staff_id,
                    'category':c.category
                    }   
                cat_list.append(d)
            return jsonify({"data": cat_list})
        except:
            abort(401,message="Failed to fetch alloted category")

class Respond(Resource):
    #@token_required
    def post(self):
        try:
            '''
            {
            "ticket_id":"",
            "responder":"", //staff_id here
            "response":""  //response here
            }
            '''
            r=request.json
            d =Response(
                ticket_id= r['ticket_id'],
                responder= r['responder'],
                response= r['response']
            )
            db.session.add(d)
            db.session.commit()   
            return jsonify({"message": "successfully responded"})
        except:
            abort(401,message="Failed to add response")

class RequestFAQ(Resource):
    #@token_required
    def post(self):
        try:
            '''
            {
            "topic_id":"",
            "solution_post_id":""
            }
            '''
            r=request.json
            d = FAQ(
                topic_id= r['topic_id'],
                solution_post_id= r['solution_post_id']
            ) 
            db.session.add(d)
            db.session.commit()
            return jsonify({"message": "faq request is added successfully"})
        except:
            abort(401,message="Failed to add faq request")

class RequestCategory(Resource):
    #@token_required
    def post(self):
        try:
            '''
            {
            "staff_id":"",
            "category":""
            }
            '''
            r=request.json
            d = CategoryAllotted(
                staff_id= r['staff_id'],
                category= r['category']
            )   
            db.session.add(d)
            db.session.commit()
            return jsonify({"message": "category request is added successfully"})
        except:
            abort(401,message="Failed to add category")

class UpdateSetting(Resource):
    #@token_required
    def patch(self):
        try: 
            '''
            {
            "user_id":   ,
            "notification":  , //1 for ON 0 for OFF
            "email_notif":  ,  //1 for ON 0 for OFF
            "webhook_notif":  //1 for ON 0 for OFF
            }
            '''
            r=request.json
            #id=user.id
            id=r['user_id']
            user=User.query.filter_by(id=id).first()
            if(r['notification'] is not None):
               user.notification=r['notification']
            if(r['email_notif'] is not None):
                user.email_notif=r['email_notif']
            if(r['webhook_notif'] is not None):
                user.webhook_notif=r['webhook_notif']
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "settings updates successfully"})
        except:
            abort(401,message="Failed to update settings")
# @app.route("/users", methods=["GET"])
# @token_required
# def get_users(current_user):
#     print(current_user,current_user.id,current_user.email)
#     users = User.query.all()
#     results = [
#         {
#             "user_id": user.id,
#             "user_name": user.username,
#             "name": user.name,
#             "email_id": user.email,
#             "role_id": user.id
#         } for user in users]

#     return jsonify(results)
