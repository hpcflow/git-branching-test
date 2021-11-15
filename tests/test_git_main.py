from git_branching_test import main


def test_hello():
    assert main.hello("bob", number=1) == "hello bob!"
