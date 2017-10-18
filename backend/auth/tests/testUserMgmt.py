from unittest import TestCase
from django.test import Client
from auth.models import User
import json

class GetUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def tearDown(self):
        user = User.objects.get(userName="test")
        user.delete()

    def testGetUser(self):
        userDataHandler = User(userName='test', 
                nickName='nicktest', 
                email='test@test.com', 
                phoneNum='11111111111', 
                comment='')
        userDataHandler.save()

        response = self.client.post('/omservice/usermgmt/user/', {'uid': '1'})

        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)

        #self.assertEqual(data['msg'], 0)
        #self.assertEqual(data['result'], 0)

        self.assertEqual(data['status'], 0)
