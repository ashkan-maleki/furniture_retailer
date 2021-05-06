from dataclasses import dataclass
from typing import NewType, NamedTuple
from collections import namedtuple
import pytest


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


class Money(NamedTuple):
    currency: str
    value: int


Line = namedtuple('Line', ['sku', 'qty'])


class A:
    pass


def test_equality():
    assert Money('gbp', 10) == Money('gbp', 10)
    assert Name('Harry', 'Percival') == Name('Harry', 'Percival')
    assert Line("RED-CHAIR", 5) == Line("RED-CHAIR", 5)
    assert A() != A()


fiver = Money('gbp', 5)
tenner = Money('gbp', 10)


def add(self: Money, other: Money) -> Money:
    if self.currency == other.currency:
        return Money(self.currency, self.value + other.value)
    else:
        raise ValueError


def subtract(self: Money, other: Money) -> Money:
    if self.currency == other.currency:
        return Money(self.currency, self.value - other.value)
    else:
        raise ValueError


Money.__add__ = add
Money.__sub__ = subtract


def can_add_money_values_for_the_same_currency():
    assert fiver + fiver == tenner
    print(fiver + fiver)


def can_substract_money_values():
    assert tenner - fiver == fiver
    print(tenner - fiver)


def adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money('usd', 10) + Money('gbp', 1)


def multiply(self: Money, other: int) -> Money:
    if isinstance(other, Money):
        raise TypeError
    else:
        return Money(self.currency, self.value * other)


Money.__mul__ = multiply


def can_multiply_money_by_a_number():
    assert fiver * 5 == Money('gbp', 25)
    print(fiver * 5)


def multiplying_two_money_values_is_an_error():
    with pytest.raises(TypeError):
        tenner * fiver


# multiplying_two_money_values_is_an_error()

class C:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"C({self.x})"

    def __hash__(self):
        # print(hash(self.x))
        return hash(self.x)

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.x == other.x
        )


class B:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return f"C({self.x})"

    def __hash__(self):
        return hash('self.x')

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self.x == other.x
        )


def test_hash_and_equality():
    d = dict()
    s = set()
    c = C(1)
    d[c] = 42
    s.add(c)
    print(d, s)

    print(c in s and c in d)  # c is in both!

    c.x = 2
    print(c in s or c in d)  # c is in neither!?

    print(d, s)

    cc = C(1)

    print(cc in s or cc in d)  # c is in neither!?
    print(cc == c)
    print(hash(cc))
    print(hash(c))
    print(hash(cc) == hash(c))
    print(d, s)
    # butit's right there!


def test_hash_and_equality2():
    d = dict()
    s = set()
    c = C(1)
    d[c] = 42
    s.add(c)
    print(d, s)

    print(c in s and c in d)  # c is in both!

    c.x = 2
    print(c in s or c in d)  # c is in neither!?

    print(d, s)
    # butit's right there!


test_hash_and_equality()
