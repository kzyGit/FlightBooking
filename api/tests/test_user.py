import json
from api.models.user import User
from .base import BaseTestcase
from django.urls import reverse


class UserTestcase(BaseTestcase):
    """ Test user model """

    def test_user_model_can_save_new_user(self):
        self.assertTrue(isinstance(self.user, User))

    def signup(self, data):
        return self.client.post(
            reverse('signup'),
            data=json.dumps(data),
            content_type="application/json"
        )

    def login(self, data):
        return self.client.post(
            reverse('login'),
            data=json.dumps(data),
            content_type="application/json"
        )

    def test_user_cannot_signup_with_duplicate_email(self):
        self.new_user['email'] = 'kezzyangiro@gmail.com'
        response = self.signup(self.new_user)
        self.assertIn(
            'Email already registered, kindly select a different email',
            response.data['email'])

    def test_signup_password_strength(self):
        self.new_user['password'] = "k"
        response = self.signup(self.new_user)
        self.assertIn(
            'Ensure password has a letter, a number and atleast 4 characters long',
            response.data)

    def test_successful_user_signup(self):
        response = self.signup(self.new_user)
        self.assertEquals('User Signed Up successfully',
                          response.data['message'])

    def test_user_login_with_invalid_credentials(self):
        self.login_user['password'] = 'wrong'
        response = self.login(self.login_user)
        self.assertEqual('Invalid Login credentials', response.data['message'])

    def test_successful_user_login(self):
        response = self.login(self.login_user)
        self.assertEqual('User logged in successfully', response.data['message'])
        self.assertIn('token', response.data)
