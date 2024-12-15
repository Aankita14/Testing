import pytest
import sys

@pytest.mark.parametrize("username,password",
                       [
                              ("selenium","webdriver"),
                              ("python","pytest"),
                              ("ankita","bundiwale"),
                              ("API","Postman"),


                        ]

                         )
def test_login(username,password):
    print(username)
    print(password)