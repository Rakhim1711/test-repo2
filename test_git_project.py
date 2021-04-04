import pytest

def function_one(x):
    return x +1

def function_two(x):
    return x + 20


@pytest.mark.company
@pytest.mark.one
def test_case_one():
    assert function_one(10) == 11

@pytest.mark.company
@pytest.mark.two
def test_case_two():
    assert function_two(20) == 40


