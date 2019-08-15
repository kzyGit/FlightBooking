from rest_framework.test import APITestCase, APIClient
from api.models.user import User


class BaseTestcase(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = User.objects.create_user(
            first_name='Kezzy',
            middle_name='Awuor',
            sur_name='Angiro',
            email='kezzyangiro@gmail.com',
            id_or_passport=31487132,
            password='kzy1',
            nationality='Kenyan'
        )

        self.new_user = {
            "first_name": "Ann",
            "middle_name": "Mukami",
            "sur_name": "Moinde",
            "email": "ann@gmail.com",
            "id_or_passport": 12345,
            "password": "ann1",
            "nationality": "Kenyan"
        }

        self.login_user = {
            "email": "kezzyangiro@gmail.com",
            "password": "kzy1"
        }
