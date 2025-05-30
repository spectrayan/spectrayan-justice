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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from generated.models.address import Address
from generated.models.court_type import CourtType
from generated.models.phone import Phone
from typing import Optional, Set
from typing_extensions import Self

class Court(BaseModel):
    """
    Court
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique document id auto generated")
    created_by: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The principal that created the entity containing the field.", alias="createdBy")
    created_at: Optional[datetime] = Field(default=None, description="The date and time the entity containing the field was created.", alias="createdAt")
    updated_by: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="The principal that recently modified the entity containing the field.", alias="updatedBy")
    updated_at: Optional[datetime] = Field(default=None, description="The date the entity containing the field was recently modified.", alias="updatedAt")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Name of the court")
    type: CourtType
    jurisdiction: StrictStr = Field(description="Jurisdiction of the court")
    address: Optional[Address] = None
    phone_number: Optional[Phone] = Field(default=None, alias="phoneNumber")
    email: Optional[StrictStr] = Field(default=None, description="Court's email address")
    __properties: ClassVar[List[str]] = ["id", "createdBy", "createdAt", "updatedBy", "updatedAt", "name", "type", "jurisdiction", "address", "phoneNumber", "email"]

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
        """Create an instance of Court from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_by",
            "created_at",
            "updated_by",
            "updated_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of phone_number
        if self.phone_number:
            _dict['phoneNumber'] = self.phone_number.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Court from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "createdBy": obj.get("createdBy"),
            "createdAt": obj.get("createdAt"),
            "updatedBy": obj.get("updatedBy"),
            "updatedAt": obj.get("updatedAt"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "jurisdiction": obj.get("jurisdiction"),
            "address": Address.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "phoneNumber": Phone.from_dict(obj["phoneNumber"]) if obj.get("phoneNumber") is not None else None,
            "email": obj.get("email")
        })
        return _obj


