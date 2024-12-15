import pytest

@pytest.mark.smoke         #created own marker smoke
def test_login():
    print("login done")

@pytest.mark.regression
def test_addProduct():
    print("add product")

@pytest.mark.smoke
def test_logout():
        print("Logout done")