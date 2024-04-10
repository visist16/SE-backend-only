from application import app, api, celery

from application.apiuser import *
from application.apistaff import *
from application.apiadmin import * 
from application.apigeneral import *
from application.ticketapi import *


api.add_resource(TicketAPI, '/api/ticket')
api.add_resource(UserAPI,'/api/user')
api.add_resource(FAQApi, '/api/faq', '/api/faq/<int:ticket_id>')
api.add_resource(ResponseAPI_by_ticket, '/api/respTicket') #For getting responses with ticket_id
api.add_resource(ResponseAPI_by_response_id, '/api/respResp') #For getting responses with response_id
api.add_resource(ResponseAPI_by_user, '/api/respUser') #For getting responses with user id.
api.add_resource(TicketAll, '/api/ticketAll') #For getting all tickets
api.add_resource(getResolutionTimes, '/api/getResolutionTimes') # For getting resolution times of support agents, only accessible to managers.
api.add_resource(flaggedPostAPI, '/api/flaggedPosts') #For getting the flagged posts.
api.add_resource(getResponseAPI_by_ticket,'/api/getResponseAPI_by_ticket') #Only for getting the responses by ticket ID
api.add_resource(ImportResourceUser,'/api/importUsers')
api.add_resource(TicketDelete,'/api/ticket/<int:ticket_id>')
api.add_resource(UserDelete,'/api/user/<int:user_id>') 
api.add_resource(ResponseAPI_by_responseID_delete, '/api/respRespDel/<int:responder_id>/<int:response_id>')

########################GENERAL APIS###################################

api.add_resource(Notifications, '/api/notifications')
api.add_resource(Topics, '/api/topics')
api.add_resource(Categories, '/api/categories')
#discourse apis from ajeet
api.add_resource(Verification, '/api/discourse/self_account/activate')
api.add_resource(Registration, '/api/discourse/register')
# api.add_resource(Sitaram, '/api/discourse/sitaram_user')
# api.add_resource(Discourse_post, '/api/discourse/sitaram_post1')
api.add_resource(Login,'/login')

########################USER APIS######################################

api.add_resource(UserProfile, '/api/user/profile')
api.add_resource(YourTickets, '/api/user/tickets')
api.add_resource(NewTicket, '/api/user/newticket')
api.add_resource(Recommendations, '/api/user/recommendations')
api.add_resource(MatchTopic, '/api/user/match')

########################STAFF APIS#####################################

api.add_resource(CreateTopic, '/api/staff/createtopic')
api.add_resource(EditTopic, '/api/staff/edittopic')

########################ADMIN APIS#####################################

api.add_resource(CreateCategory, '/api/admin/createcategory')
api.add_resource(EditCategory, '/api/admin/editcategory')

from application.routes import *
if __name__ == '__main__':
  # Run the Flask app
  app.run(debug=True)