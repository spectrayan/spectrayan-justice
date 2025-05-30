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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from generated.models.problem_detail_errors_inner import ProblemDetailErrorsInner
from typing import Optional, Set
from typing_extensions import Self

class ProblemDetail(BaseModel):
    """
    ProblemDetail
    """ # noqa: E501
    type: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="A URI reference that identifies the problem type.")
    status: Optional[Annotated[int, Field(le=599, strict=True, ge=100)]] = Field(default=None, description="The HTTP status code generated by the origin server for this occurrence of the problem.")
    title: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="A short, human-readable summary of the problem type. It should not change from occurrence to occurrence of the problem, except for purposes of localization.")
    detail: Annotated[str, Field(strict=True, max_length=4096)] = Field(description="A human-readable explanation specific to this occurrence of the problem.")
    instance: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(default=None, description="A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced.")
    code: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="An API specific error code aiding the provider team understand the error based on their own potential taxonomy or registry.")
    errors: Optional[Annotated[List[ProblemDetailErrorsInner], Field(max_length=1000)]] = Field(default=None, description="An array of error details to accompany a problem details response.")
    __properties: ClassVar[List[str]] = ["type", "status", "title", "detail", "instance", "code", "errors"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProblemDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProblemDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "status": obj.get("status"),
            "title": obj.get("title"),
            "detail": obj.get("detail"),
            "instance": obj.get("instance"),
            "code": obj.get("code"),
            "errors": [ProblemDetailErrorsInner.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None
        })
        return _obj


