# -*- coding: utf-8 -*-
import logging

#Get logger from django config.
defLogger = logging.getLogger('platform')

def chkDict(dict, keys=[]):
    errorKey = []
    try:
        for key in keys:
            if key not in dict:
                errorKey.append(key)
    except Exception, e:
        errorMsg = "Unknow error."
        defLogger.error(errorMsg)
        defLogger.exception(str(e))
        status = 9003
        return {'status': status,
                'msg': errorMsg,
                'result': '',
               }

    if len(errorKey) > 0:
        keys = ",".join(errorKey)
        msg = "No found key in POST data: {0}".format(keys)
        status = 9000
    else:
        msg = "All keys are in POST data."
        status = 0

    return {'status': status,
            'msg': msg,
            'result': '',
           }
