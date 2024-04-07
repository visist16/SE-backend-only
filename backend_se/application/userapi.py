from flask_restful import Resource, request, abort
from flask import jsonify
from datetime import datetime
from dateutil import tz, parser
from application.models import *
from application.models import  db
from application.routes import token_required
from application.workers import celery
from celery import chain
from application.tasks import send_email, response_notification
from datetime import datetime, timedelta
import jwt
from .config import Config
from werkzeug.exceptions import HTTPException 
from application import index

class Login(Resource):
    def post(self):
        if request.is_json:
            email = request.json["email"]
            password = request.json["password"]
        else:
            email = request.form["email"]
            password = request.form["password"]
        test = User.query.filter_by(email_id=email).first()
        # print(test)
        if (test is None):
            abort(409,message="User does not exist")
        elif (test.password == password):
            token = jwt.encode({
                'user_id': test.user_id,
                'exp': datetime.now() + timedelta(minutes=80)
            }, Config.SECRET_KEY, algorithm="HS256")
            # access_token = create_access_token(identity=email)
            # print(token)
            return jsonify({"message":"Login Succeeded!", "token":token,"user_id":test.user_id,"role":test.role_id})
        else:
            abort(401, message="Bad Email or Password")
  

class YourTickets(Resource):
    # @token_required
    def get(self):
        r=request.json
        creator=r.get('user_id')
        ticket=Ticket.query.filter_by(creator=creator).all()
        result=[]
        for t in ticket:
            d={}
            d['id']=t.id
            d['title']=t.title
            d['description']=t.description
            d['date']=str(t.date)
            d['category']=t.category
            d['tags']=t.tags
            d['offensive']=t.offensive
            d['escalated']=t.escalated
            d['resolved']=t.resolved
            d['merged']=t.merged
            result.append(d)
            return jsonify({"data": result})
     
class NewTicket(Resource):       
    # @token_required
    def post(self):
        try:
            data=request.json
            ticket=Ticket(title=data['title'],
                        description=data['description'],
                        date=datetime.now(),
                        creator=data['creator'],
                        category=data['category'],
                        tags=data['tags'])
            db.session.add(ticket)
            db.session.commit()
            return jsonify({'message':'Ticket created successfully'})
        except:
            abort(401,message="Failed to create ticket")
        
class UserProfile(Resource):
    # @token_required
    def get(self):
        try:
            r=request.json
            id=r.get('user_id')
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