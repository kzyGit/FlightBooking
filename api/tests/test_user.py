from django.test import TestCase
from ..models.user import User

class UserModel(TestCase):
    def test_model_can_Save_new_user(self):
        user = User.objects.create_user(
            first_name='Kezzy',
            middle_name='Awuor',
            sur_name='Angiro',
            email='kezzyangiro@gmail.com',
            id_or_passport=31487132,
            password='kzy',
            nationality='Kenyan'
        )
        print("*** ",user )

