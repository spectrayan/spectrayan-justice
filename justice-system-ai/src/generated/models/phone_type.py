# coding: utf-8

"""
    Justice system APIs

    This is the OpenAPI Specification for justice system APIs. It provides a comprehensive suite of functionalities to interact with our platform. It is designed to be easy to use and integrate with various application environments. 

    The version of the OpenAPI document: 1.0.0
    Contact: admin@spectrayan.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PhoneType(str, Enum):
    """
    The type of phone number.
    """

    """
    allowed enum values
    """
    HOME = 'Home'
    WORK = 'Work'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PhoneType from a JSON string"""
        return cls(json.loads(json_str))


