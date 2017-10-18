# -*- coding: utf-8 -*-
#from django.core.exceptions import MultipleObjectsReturned
from auth.models import User
import logging
import json

#Get logger from django config.
defLogger = logging.getLogger('platform')
reqLogger = logging.getLogger('request')

def _fmtUserData(data):
    fmt = []
    if len(data) == 0:
        return fmt
    for d in data:
        userData = {'id': d.id,
                    'userName': d.userName,
                    'nickName': d.nickName,
                    'email': d.email,
                    'phoneNum': d.phoneNum,
                    'comment': d.comment,
                    'createTimestamp': str(d.createTimestamp),
                    'updateTimestamp': str(d.updateTimestamp)
                   }
        fmt.append(userData)
    return fmt

def _getUser(uid=None, userName=None):
    userData = []
    user='null'
    userDataHandler = None
    try:
        if uid is not None:
            userDataHandler = User.objects.get(id=uid)
            user = uid
        elif userName is not None:
            userDataHandler = User.objects.get(userName=userName)
            user = userName
        else:
            raise TypeError('_getUser() takes at least 1 argument (0 given)')
        uid = userDataHandler.id
        uName = userDataHandler.userName
        userData = _fmtUserData([userDataHandler, ])
        getUserMsg = "Get \'%s\''s UID is %d" % (uName, uid)
        status = 0
    except User.DoesNotExist, e:
        getUserMsg = "User \'{0}\' does not exist.".format(user)
        status = 1001
    except Exception, e:
        errorMsg = "Unknown Error: %s" % str(e)
        defLogger.error(errorMsg)
        defLogger.exception(errorMsg)
        status = 9003
        msg = {'status': status, 
               'msg': errorMsg,
               'result': ''
              }
        returnMsg = "Search User \'{0}\' and return data: {1}".format(user, 
                                                              json.dumps(msg))
        defLogger.error(returnMsg)
        return msg

    defLogger.info(getUserMsg)

    retInfo = {'status': status,
              'result': userData,
              'msg': getUserMsg,
              'object': userDataHandler
              }

    return retInfo

#def _getMultiUser(userName=[], uid=[]):
#    userData = []
#    if len(userName) != 0:
#        for uname in userName:
#            info = _getUser(userName=uname)
#            userData.append(info)
#    elif len(uid) != 0:
#        for id in uid:
#            info = _getUser(uid=id)
#            userData.append(info)
#
#    return userData


def _getAllUser():
    try:
        userDataHandler = User.objects.all()
    except Exception, e:
        errorMsg = "Unknown Error: %s" % str(e)
        defLogger.error(errorMsg)
        defLogger.exception(errorMsg)
        status = 9003
        msg = {'status': status, 
               'msg': errorMsg,
               'result': ''
              }
        returnMsg = "Get all users faild and return data: {0}".format(
                                                              json.dumps(msg))
        defLogger.error(returnMsg)

        return msg

    getUserMsg = "Get all data successfully."
    userData = _fmtUserData(userDataHandler)

    retInfo = {'status': status,
              'result': userData,
              'msg': getUserMsg,
              'object': userDataHandler
              }

    return retInfo

def getUser(uid=None, userName=None):
    if uid is not None:
        return _getUser(uid=uid)
    elif userName is not None:
        return _getUser(userName=userName)
    else:
        return _getAllUser()
