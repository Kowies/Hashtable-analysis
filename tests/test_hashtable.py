"""Tests for hashtableanalysis.hashtable.hashtable"""

from hashtableanalysis.hashtable.hashtable import Hashtable


def test_hashtable_add():
    hashtable = Hashtable()
    string = 'Ambroży'

    assert string not in hashtable 
    hashtable.add(string)
    assert string in hashtable


def test_hashtable_discard():
    hashtable = Hashtable()
    string = 'Ambroży'

    assert string not in hashtable 
    hashtable.discard(string)
    assert string not in hashtable

    hashtable.add(string)
    assert string in hashtable
    hashtable.discard(string)
    assert string not in hashtable
    hashtable.discard(string)
    assert string not in hashtable


def test_hashtable_len():
    hashtable = Hashtable()
    string_1 = 'Ambroży'
    string_2 = 'Kleks'

    assert len(hashtable) == 0
    hashtable.add(string_1)
    assert len(hashtable) == 1
    hashtable.add(string_2)
    assert len(hashtable) == 2

    hashtable.discard(string_1)
    assert len(hashtable) == 1
    hashtable.discard(string_1)
    assert len(hashtable) == 1

    hashtable.discard(string_2)
    assert len(hashtable) == 0
    hashtable.discard(string_2)
    assert len(hashtable) == 0