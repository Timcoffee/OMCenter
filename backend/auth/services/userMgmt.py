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
        defLogger.info(getUserMsg)
    except User.DoesNotExist, e:
        status = 1001
        getUserMsg = "User \'{0}\' does not exist.".format(user)
        userDataHandler = ''
        defLogger.info(getUserMsg)
    except Exception, e:
        getUserMsg = "Unknown Error: %s" % str(e)
        defLogger.error(getUserMsg)
        defLogger.exception(getUserMsg)
        status = 9003

    retInfo = {'status': status,
              'result': userData,
              'msg': getUserMsg,
              'object': userDataHandler
              }

    return retInfo

def _getMultiUser(userName=[], uid=[]):
    userData = []
    if len(userName) != 0:
        for uname in userName:
            info = _getUser(userName=uname)
            userData.append(info)
    elif len(uid) != 0:
        for id in uid:
            info = _getUser(uid=id)
            userData.append(info)

    return userData


def _getAllUser():
    try:
        userDataHandler = User.objects.all()
        status = 0
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

def getUserCNTLR(uid=None, userName=None):
    if uid is not None:
        return _getUser(uid=uid)
    elif userName is not None:
        return _getUser(userName=userName)
    else:
        return _getAllUser()

def addUserCNTLR(userName,
            email,
            phoneNum,
            nickName='',
            comment='',):
    userData = getUserCNTLR(userName=userName)
    if userData['status'] == 0:
        errorMsg = "User (\'{0}\') has existed.".format(userName)
        defLogger.error(errorMsg)
        status = 1048
        return {'status': status,
                'msg': errorMsg,
                'result': ''
               }

    try:
        userDataHandler = User(userName=userName, 
                               nickName=nickName,
                               email=email,
                               phoneNum=phoneNum,
                               comment=comment)
        userDataHandler.save()
        msg = "Create user data successfully."
        defLogger.info(msg)
        status = 0
    except Exception, e:
        msg = "Failed to create user data (Unknown error)."
        defLogger.error(msg)
        defLogger.exception(str(e))
        status = 9003

    return {'status': status,
           'msg': msg,
           'result': ''
           }

def _delMultiUsers(uid=[]):
    pass

def  delUserCNTLR(uid):
    userData = getUserCNTLR(uid=uid)
    if userData['status'] == 1001:
        msg = "User does not exist."
        status = 0
    elif userData['status'] == 0:
        userDataHandler = userData['object']
        try:
            userName = userDataHandler.userName
            userDataHandler.delete()
            msg = "Delete user(\'{0}\') successfully.".format(userName)
            status = 0
            defLogger.info(msg)
        except Exception, e:
            msg = "Failed to delete user data (Unknown error)."
            defLogger.error(msg)
            defLogger.exception(str(e))
            status = 9003
    else:
        msg = "Failed to get user data."
        defLogger.error(msg)
        status = userData['status']

    return {"status": status,
            "msg": msg,
            "result": ""
           }

def updUserCNTLR(uid, 
                 userName,
                 email,
                 phoneNum,
                 nickName,
                 comment):
    userData = getUserCNTLR(uid=uid)
    if userData['status'] == 0:
        userDataHandler = userData['object']
        try:
            userDataHandler.userName = userName
            userDataHandler.email = email
            userDataHandler.phoneNum = phoneNum
            userDataHandler.nickName = nickName
            userDataHandler.comment = comment
            userDataHandler.save()
            msg = "Update user(\'{0}\') successfully.".format(userName)
            status = 0
            defLogger.info(msg)
        except Exception, e:
            msg = "Failed to update user data (Unknown error)."
            defLogger.error(msg)
            defLogger.exception(str(e))
            status = 9003

        return {'status': status,
                'msg': msg,
                'result': ''
               }
    else:
        return userData

