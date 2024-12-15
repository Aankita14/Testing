import pytest
import sys

@pytest.mark.skip
def test_login():
    print("login done")

@pytest.mark.skipif(sys.version_info>(1,1),reason="Python version not supported")
def test_addProduct():
    print("add product")

@pytest.mark.xfail
def test_logout():
    #assert True
    assert False
    print("Logout done")

def test_closeApplication():
    assert True
    print("Close the app")



#Execution command:  pytest_Test_markers2.py