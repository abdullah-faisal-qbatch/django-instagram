valid_login_credentials = {
    "username": "john",
    "password": "123"
}

invalid_username_valid_password = {
    "username": "null",
    "password": "123"
}


valid_username_invalid_password = {
    "username": "john",
    "password": "1234"
}


invalid_username_invalid_password = {
    "username": "some-random-guy",
    "password": "1234"
}

valid_credentials_sign_up = {
    "username": "chris",
    "password": "12345678!",
    "confirm_password": "12345678!",
    "email": "chris@site.com",
    "first_name": 1, "last_name": 2
}

invalid_credentials_sign_up_passwords_not_match = {
    "username": "mathew",
    "password": "12345678!!",
    "confirm_password": "12345678!",
    "email": "mike@gmail.com",
    "first_name": 1, "last_name": 2

}

invalid_credentials_sign_up_emails_not_unique = {
    "username": "chris",
    "password": "12345678!",
    "confirm_password": "12345678!",
    "email": "chris@site.com",
    "first_name": 1, "last_name": 2

}
