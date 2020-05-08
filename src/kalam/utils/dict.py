"""Utility operations related to dictionary."""

from typing import List


def dict_all_value_in_list(d: dict) -> List[str]:
    """Recursively reads all the value in the dictionary.

    Args:
        d: A dictionary.

    Returns:
        A list of all values.
    """
    all_values: List[str] = []
    for _, value in d.items():
        if isinstance(value, dict):
            all_values = all_values + dict_all_value_in_list(value)
        else:
            all_values.append(value)
    return all_values
