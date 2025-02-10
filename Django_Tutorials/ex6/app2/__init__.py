# # app2 = sessions
#
# '''
#     session is used to store info about user in server side
#
#     step 1 - config session setting in setting .py
#         SESSION_ENGINE = django.contribute.sessions.backends.db
#         SESSION_EXPIRE_AT_BROWSER_CLOSE = True
#
#     step 2 config setting.py in middleware
#         MIDDLEWARE = [djnago.contrib.sessions.middleware.SessionMiddleware]
#
#     step 3 handling sessions
#         adding - request.sessions[key] = value
#         getting - request.sessions.get(key)
#         deleting - del request.session[key]