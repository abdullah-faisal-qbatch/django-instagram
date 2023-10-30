import unittest
import requests


class Fixture(unittest.TestCase):
    pass

# class to write the test cases using given when then approach


class TestStrategies(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = self._Fixture()

    def test_get_valid_access_and_refresh_token_with_valid_username_and_valid_password(self):
        """
        This test case is designed to check whether we are getting access token and refresh token with valid username and valid password
        """
        self.fixture.given_valid_credentials_for_login()
        self.fixture.when_requested_for_login()
        self.fixture.then_access_token_and_refresh_token_received_for_login()

    def test_get_access_token_and_refresh_token_with_valid_password_and_invalid_username(self):
        """
        This test case is designed to check whether we are not getting access token and refresh token with valid password and invalid username
        """
        self.fixture.given_invalid_credentials_for_login("null", "123")
        self.fixture.when_requested_for_login()
        self.fixture.then_access_token_and_refresh_token_not_received_for_login()

    def test_get_access_token_and_refresh_token_with_valid_username_and_invalid_password(self):
        """
        This test case is designed to check whether we are not getting access token and refresh token with valid username and invalid password
        """
        self.fixture.given_invalid_credentials_for_login("john", "1234")
        self.fixture.when_requested_for_login()
        self.fixture.then_access_token_and_refresh_token_not_received_for_login()

    def test_get_access_token_and_refresh_token_with_invalid_username_and_invalid_password(self):
        """
        This test case is designed to check whether we are not getting access token and refresh token with invalid username and invalid password
        """
        self.fixture.given_invalid_credentials_for_login(
            "some-random-guy", "1234")
        self.fixture.when_requested_for_login()
        self.fixture.then_access_token_and_refresh_token_not_received_for_login()

    def test_new_user_created_with_valid_credentials(self):
        """
        This test case is designed to check whether we are getting valid credentails in return when we have created new user
        """
        self.fixture.given_valid_credentials_for_sign_up()
        self.fixture.when_requested_for_sign_up()
        self.fixture.then_user_credentials_are_returned()

    def test_new_user_not_created_with_username_already_exists(self):
        """
        This test case is designed to check whether we are not getting valid credentails in return when we have created new user that already exists
        """
        self.fixture.given_valid_credentials_for_sign_up()
        self.fixture.when_requested_for_sign_up()
        self.fixture.then_user_credentials_are_not_returned()

    def test_new_user_not_created_when_passwords_are_not_matched(self):
        """
        This test case is designed to check whether we are not getting valid credentails in return when we have created new user whow passwords don't match
        """
        self.fixture.given_invalid_credentials_for_sign_up(
            "mike", "12345678!!", "12345678!", "mike@gmail.com", 1, 2)
        self.fixture.when_requested_for_sign_up()
        self.fixture.then_passwords_validation_error_is_returned()

    def test_new_user_not_created_when_email_is_not_unique(self):
        """
        This test case is designed to check whether we are not getting valid credentails in return when we have created new user whow email is not unique
        """
        self.fixture.given_invalid_credentials_for_sign_up(
            "mike", "12345678!!", "12345678!", "chris@site.com", 1, 2)
        self.fixture.when_requested_for_sign_up()
        self.fixture.then_email_validation_error_is_returned()

    class _Fixture(Fixture):
        def then_email_validation_error_is_returned(self):
            self.assertEqual(self.response.get('email')[0],
                             "This field must be unique.")

        def then_passwords_validation_error_is_returned(self):
            self.assertEqual(self.response.get('password')[0],
                             "Password fields didn't match.")

        def given_invalid_credentials_for_sign_up(self, username, password, password2, email, first_name, last_name):
            self.username = username
            self.password = password
            self.password2 = password2
            self.email = email
            self.first_name = first_name
            self.last_name = last_name

        def given_valid_credentials_for_sign_up(self):
            self.username = "chris"
            self.password = "12345678!"
            self.password2 = "12345678!"
            self.email = "chris@site.com"
            self.first_name = 1
            self.last_name = 2

        def when_requested_for_sign_up(self):
            response = requests.post(
                "http://127.0.0.1:8081/auth/register/", data={"username": self.username, "password": self.password, "password2": self.password2, "email": self.email, "first_name": self.first_name, "last_name": self.last_name})
            self.response = response.json()

        def then_user_credentials_are_returned(self):
            self.assertEqual(self.response.get('username'), self.username)
            self.assertEqual(self.response.get('email'), self.email)
            self.assertEqual(self.response.get('first_name'), self.first_name)
            self.assertEqual(self.response.get('last_name'), self.last_name)

        def then_user_credentials_are_not_returned(self):
            self.assertEqual(self.response.get('username')[0],
                             "A user with that username already exists.")

        def given_valid_credentials_for_login(self):
            self.username = "john"
            self.password = "123"

        def given_invalid_credentials_for_login(self, username, password):
            self.username = username
            self.password = password

        def when_requested_for_login(self):
            response = requests.post(
                "http://127.0.0.1:8081/auth/login/", data={"username": self.username, "password": self.password})
            self.response = response.json()

        def then_access_token_and_refresh_token_received_for_login(self):
            self.assertEqual(len(self.response.get('refresh')), 253)
            self.assertEqual(len(self.response.get('access')), 252)

        def then_access_token_and_refresh_token_not_received_for_login(self):
            self.assertEqual(self.response.get('refresh'), None)
            self.assertEqual(self.response.get('access'), None)


if __name__ == '__main__':
    unittest.main()
