import logging
import json

#Get logger from django config.
defLogger = logging.getLogger('platform')
reqLogger = logging.getLogger('request')


#Format request data.
def fmtRequest(request):
    defLogger.info(request)
    if not request.POST:
        mateData = request.META

        try:
            rawData = mateData.get('wsgi.input', {})
        except ValueError:
            errorMsg = "No found key \'wsgi.input\': "
            defLogger.exception(errorMsg)
            rawData = {}
            return rawData

        try:
            contentLen = mateData.get('CONTENT_LENGTH', 0)
        except ValueError:
            errorMsg = "No found key \'CONTENT_LENGTH\': "
            defLogger.exception(errorMsg)
            contentLen = 0

        data = json.loads(rawData.read(contentLen))
    else:
        data = request.POST

    defLogger.info("Request Data:" + str(data))

    return data
