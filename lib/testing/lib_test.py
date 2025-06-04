# lib/testing/lib_test.py
from lib.functions import (
    greet_programmer,
    greet,
    greet_with_default,
    add,
    halve,
)

def test_greet_programmer(capsys):
    greet_programmer()
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello, programmer!"

def test_greet(capsys):
    greet("Ibrahim")
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello, Ibrahim!"

def test_greet_with_default(capsys):
    greet_with_default()
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello, programmer!"

    greet_with_default("Fatuma")
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello, Fatuma!"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_halve():
    assert halve(10) == 5
    assert halve(5) == 2.5
