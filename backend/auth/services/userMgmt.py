# -*- coding: utf-8 -*-
#from django.core.exceptions import MultipleObjectsReturned
from auth.models import User
from auth.services import exceptions
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

def getUser(uid=None, userName=None):
    userData = []
    user='null'
    userDataHandler = None

    if uid is None and userName is None:
        raise TypeError('getUser() takes at least 1 argument (0 given)')

    try:
        if uid is not None:
            userDataHandler = User.objects.get(id=uid)
            user = uid
        elif userName is not None:
            userDataHandler = User.objects.get(userName=userName)
            user = userName
        uid = userDataHandler.id
        uName = userDataHandler.userName
        userData = _fmtUserData([userDataHandler, ])
        getUserMsg = "Get \'%s\''s UID is %d" % (uName, uid)
        status = 0
        defLogger.info(getUserMsg)
        result = {'userdata': userData,
                  'handler': userDataHandler
                 }
    except User.DoesNotExist, e:
        getUserMsg = "User (\'{0}\') does not exist.".format(user)
        raise exceptions.UserDoesNotExist(getUserMsg)
    except Exception, e:
        getUserMsg = ("An unknown error occurred " 
                     "while getting user {0}: {1}".format(user,str(e)))
        raise exceptions.UnknownError(e)

    retInfo = {'status': status,
               'result': result,
               'msg': getUserMsg,
              }

    return retInfo

def _getMultiUser(userName=[], uid=[]):
    userData = []
    if len(userName) != 0:
        for uname in userName:
            info = getUser(userName=uname)
            userData.append(info)
    elif len(uid) != 0:
        for id in uid:
            info = getUser(uid=id)
            userData.append(info)

    return userData


def getAllUser():
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
    retInfo = None
    try:
        if uid is not None:
            retInfo = getUser(uid=uid)
        elif userName is not None:
            retInfo = getUser(userName=userName)
        else:
            retInfo = getAllUser()
    except exceptions.UserMgmtDoesNotExsit, e:
        status = 1001
        getUserMsg = str(e)
        defLogger.info(getUserMsg)
    except exceptions.UnknownError, e:
        status = 9003
        getUserMsg = str(e)
        defLogger.error(getUserMsg)
        defLogger.exception(getUserMsg)

    if retInfo is None:
        retInfo = {'status': status,
                   'result': '',
                   'msg': getUserMsg,
                  }
    else:
       del(retInfo['result']['handler'])

    return retInfo

def addUser(userName,
            email,
            phoneNum,
            nickName='',
            comment='',
            ):
    try:
        userDataHandler = User(userName=userName, 
                               nickName=nickName,
                               email=email,
                               phoneNum=phoneNum,
                               comment=comment)
        userDataHandler.save()
        status = 0
        addUserMsg = "Create user data successfully."
    except Exception, e:
        addUserMsg = "Failed to create user data (Unknown error): {0}".format(
                                                                    str(e))
        raise exceptions.UnknownError(addUserMsg)

    return {'status': status,
           'msg': addUserMsg,
           'result': ''
           }

def addUserCNTLR(userName,
            email,
            phoneNum,
            nickName='',
            comment='',):
    try:
        getUser(userName=userName)
        status = 1048
        addUserMsg = "User (\'{0}\') has existed.".format(userName)
        defLogger.error(addUserMsg)
        return {'status': status,
                'msg': addUserMsg,
                'result': ''
               }
    except exceptions.UserMgmtDoesNotExsit:
        pass
    except exceptions.UnknownError, e:
        status = 9003
        getUserMsg = str(e)
        defLogger.error(getUserMsg)
        defLogger.exception(getUserMsg)
        return {'status': status,
                'msg': addUserMsg,
                'result': ''
               }

    try:
        addUserMsg = addUser(userName=userName, 
                             nickName=nickName,
                             email=email,
                             phoneNum=phoneNum,
                             comment=comment)
    except exceptions.UnknownError, e:
        status = 9003
        addUserMsg = str(e)
        defLogger.error(str(e))
        defLogger.exception(str(e))

    return {'status': status,
           'msg': addUserMsg,
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

