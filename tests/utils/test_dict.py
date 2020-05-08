"""Tests for util/dict.

Tests must be written in order in which they are defined in kalam.utils.dict
"""

import kalam.utils.dict as dict_util


def test_dict_all_value_in_list() -> None:
    """Test dict_all_value_in_list."""
    test_dict = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": {
            "dict_key1": "dict_value1",
            "dict_key2": "dict_value2",
            "dict_key3": {"dict_dict_key1": "dict_dict_value1"},
        },
        "key5": "value5",
    }

    expected_result = [
        "value1",
        "value2",
        "value3",
        "dict_value1",
        "dict_value2",
        "dict_dict_value1",
        "value5",
    ]
    test_result = dict_util.dict_all_value_in_list(test_dict)
    assert test_result == expected_result
