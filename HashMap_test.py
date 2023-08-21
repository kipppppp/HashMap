
# BASIC TESTING

from hash_map_sc import *
from hash_map_oa import *
from GIVEN_DATA_STRUCTURES import *

# ------------------- Linked List HashMap ---------------------------------- #


def test_put_sc():
    """
    Tests put(), resize(), table_load() empty_buckets(), get_size(),
    get_capacity().
    Adds random values, then periodically checks actual output against
    expected output.
    """
    m = HashMapSC(53, hash_function_1)
    output1 = [39, 0.47, 25, 53]
    output2 = [39, 0.94, 50, 53]
    output3 = [82, 0.70, 75, 107]
    output4 = [79, 0.93, 100, 107]
    output5 = [184, 0.56, 125, 223]
    output6 = [181, 0.67, 150, 223]
    counter = 0
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            counter += 1
            test = [m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity()]
            if counter == 1:
                assert test == output1
            elif counter == 2:
                assert test == output2
            elif counter == 3:
                assert test == output3
            elif counter == 4:
                assert test == output4
            elif counter == 5:
                assert test == output5
            elif counter == 6:
                assert test == output6


def test_clear_sc():
    """
    Adds a value to a HashMap of a given size, then clears the object.
    """
    m = HashMapSC(53, hash_function_1)
    assert m.get_size() == 0
    assert m.get_capacity() == 53
    m.put("test_key", "test_value")
    assert m.get_size() == 1
    assert m.get_capacity() == 53

    m.clear()
    assert m.get_size() == 0
    assert m.get_capacity() == 53


def test_get_sc():
    """
    Tries getting a value from an empty HashMap, then adds a key/value and
    tries again.
    """
    m = HashMapSC(31, hash_function_1)
    assert m.get("test_key") is None
    m.put("test_key", "test_value")
    assert m.get("test_key") == "test_value"


def test_contains_key_sc():
    """
    Checks for a key in an empty HashMap, then adds two keys one at a time
    and checks for each key.
    """
    m = HashMapSC(53, hash_function_1)
    assert m.contains_key("test_key1") is False
    m.put("test_key1", "test_value1")
    assert m.contains_key("test_key1") is True
    assert m.contains_key("test_key2") is False
    m.put("test_key2", "test_value2")
    assert m.contains_key("test_key2") is True


def test_remove_sc():
    """
    Checks for a key in an empty Hashmap, adds the key and checks
    again, then removes the key and checks again.
    """
    m = HashMapSC(52, hash_function_1)
    assert m.contains_key("test_key") is False
    m.put("test_key", "test_value")
    assert m.contains_key("test_key") is True
    m.remove("test_key")
    assert m.contains_key("test_key") is False


def test_get_keys_and_values_sc():
    """
    Creates a HashMap using set values and compares the output of keys and
    values to the expected output.
    """
    m = HashMapSC()
    target = [('1', '10'), ('2', '20'), ('3', '30'), ('4', '40'), ('5', '50')]
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    assert sorted(list(m.get_keys_and_values())) == target


def test_find_mode_sc():
    """
    Tests mode and frequency output on a set DynamicArray.
    """
    da = DynamicArray(['1', '2', '3', '1', '6', '7', '1', '10'])
    mode, frequency = find_mode(da)
    mode = list(mode)
    assert mode == ['1']
    assert frequency == 3

# ------------------- Open Addressing HashMap ------------------------------ #


def test_put_oa():
    """
    Tests put(), resize(), table_load() empty_buckets(), get_size(),
    get_capacity().
    Adds random values, then periodically checks actual output against
    expected output.
    """
    m = HashMapOA(53, hash_function_1)
    output1 = [28, 0.47, 25, 53]
    output2 = [57, 0.47, 50, 107]
    output3 = [148, 0.34, 75, 223]
    output4 = [123, 0.45, 100, 223]
    output5 = [324, 0.28, 125, 449]
    output6 = [299, 0.33, 150, 449]
    counter = 0
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            counter += 1
            test = [m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity()]
            if counter == 1:
                assert test == output1
            elif counter == 2:
                assert test == output2
            elif counter == 3:
                assert test == output3
            elif counter == 4:
                assert test == output4
            elif counter == 5:
                assert test == output5
            elif counter == 6:
                assert test == output6


def test_clear_oa():
    """
    Adds a value to a HashMap of a given size, then clears the object.
    """
    m = HashMapOA(101, hash_function_1)
    assert m.get_size() == 0
    assert m.get_capacity() == 101
    m.put("test_key", "test_value")
    assert m.get_size() == 1
    assert m.get_capacity() == 101

    m.clear()
    assert m.get_size() == 0
    assert m.get_capacity() == 101


def test_get_oa():
    """
    Tries getting a value from an empty HashMap, then adds a key/value and
    tries again.
    """
    m = HashMapOA(31, hash_function_1)
    assert m.get("test_key") is None
    m.put("test_key", "test_value")
    assert m.get("test_key") == "test_value"


def test_contains_key_oa():
    """
    Checks for a key in an empty HashMap, then adds two keys one at a time
    and checks for each key.
    """
    m = HashMapOA(31, hash_function_1)
    assert m.contains_key("test_key1") is False
    m.put("test_key1", "test_value1")
    assert m.contains_key("test_key1") is True
    assert m.contains_key("test_key2") is False
    m.put("test_key2", "test_value2")
    assert m.contains_key("test_key2") is True


def test_remove_oa():
    """
    Checks for a key in an empty Hashmap, adds the key and checks
    again, then removes the key and checks again.
    """
    m = HashMapOA(53, hash_function_1)
    assert m.contains_key("test_key") is False
    m.put("test_key", "test_value")
    assert m.contains_key("test_key") is True
    m.remove("test_key")
    assert m.contains_key("test_key") is False


def test_get_keys_and_values_oa():
    """
    Creates a HashMap using set values and compares the output of keys and
    values to the expected output.
    """
    m = HashMapOA(53, hash_function_1)
    target = [('1', '10'), ('2', '20'), ('3', '30'), ('4', '40'), ('5', '50')]
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    assert sorted(list(m.get_keys_and_values())) == target
