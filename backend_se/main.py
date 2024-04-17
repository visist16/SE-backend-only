from application import app, api, celery

from application.apiuser import *
from application.apistaff import *
from application.apiadmin import * 
from application.apigeneral import *
from application.ticketapi import *

# Login APIs

api.add_resource(Login,'/login')

# User APIs

api.add_resource(UserProfile, '/api/user/profile')
api.add_resource(YourTickets, '/api/user/tickets')
api.add_resource(NewTicket, '/api/user/newticket')
api.add_resource(Recommendations, '/api/user/recommendations')
api.add_resource(MatchTopic, '/api/user/match')
api.add_resource(FAQs, '/api/user/faqs')

# Staff APIs

api.add_resource(CreateTopic, '/api/staff/createtopic')
api.add_resource(EditTopic, '/api/staff/edittopic')
api.add_resource(Merge, '/api/staff/merge')
api.add_resource(ResolveTopic, '/api/staff/resolvetopic')
api.add_resource(ResolveTicket, '/api/staff/resolveticket')
api.add_resource(StaffProfile, '/api/staff/profile')
api.add_resource(AllottedCategory, '/api/staff/category')
api.add_resource(Respond, '/api/staff/respond')
api.add_resource(RequestFAQ, '/api/staff/requestfaq')
api.add_resource(RequestCategory, '/api/staff/requestcategory')
api.add_resource(UpdateSetting, '/api/staff/updatesetting')

# Admin APIs

api.add_resource(CreateCategory, '/api/admin/createcategory')
api.add_resource(EditCategory, '/api/admin/editcategory')
api.add_resource(AdminHome, '/api/admin/home')
api.add_resource(AdminGetRequest,'/api/admin/admingetrequest')
api.add_resource(AdminPostRequest,'/api/admin/adminpostrequest')
api.add_resource(RevokeStaff,'/api/admin/revokestaff')
api.add_resource(RevokeCategory,'/api/admin/revokecategory')
api.add_resource(AddStaff,'/api/admin/addstaff')
api.add_resource(BlockUser,'/api/admin/blockuser')

# Discourse APIs

api.add_resource(Verification, '/api/discourse/self_account/activate')
api.add_resource(Registration, '/api/discourse/register')

# Notification APIs

api.add_resource(Notifications, '/api/notifications')

# Topics APIs

api.add_resource(Topics, '/api/topics')

# Categories APIs

api.add_resource(Categories, '/api/categories')

from application.routes import *

if __name__ == '__main__':
  app.run(debug=True,port=5000)