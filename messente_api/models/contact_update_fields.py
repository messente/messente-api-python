# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services.  * Send and receive SMS, Viber, WhatsApp and Telegram messages. * Manage contacts and groups. * Fetch detailed info about phone numbers. * Blacklist phone numbers to make sure you're not sending any unwanted messages.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.

    The version of the OpenAPI document: 2.0.0
    Contact: messente@messente.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ContactUpdateFields(BaseModel):
    """
    A container for fields of a contact
    """ # noqa: E501
    email: Optional[StrictStr] = Field(default=None, description="The email of the contact")
    first_name: Optional[StrictStr] = Field(default=None, description="The first name of the contact", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="The last name of the contact", alias="lastName")
    company: Optional[StrictStr] = Field(default=None, description="The company of the contact")
    title: Optional[StrictStr] = Field(default=None, description="The title of the contact")
    custom: Optional[StrictStr] = Field(default=None, description="The first custom field")
    custom2: Optional[StrictStr] = Field(default=None, description="The second custom field")
    custom3: Optional[StrictStr] = Field(default=None, description="The third custom field")
    custom4: Optional[StrictStr] = Field(default=None, description="The fourth custom field")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["email", "firstName", "lastName", "company", "title", "custom", "custom2", "custom3", "custom4"]

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
        """Create an instance of ContactUpdateFields from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['firstName'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['lastName'] = None

        # set to None if company (nullable) is None
        # and model_fields_set contains the field
        if self.company is None and "company" in self.model_fields_set:
            _dict['company'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if custom (nullable) is None
        # and model_fields_set contains the field
        if self.custom is None and "custom" in self.model_fields_set:
            _dict['custom'] = None

        # set to None if custom2 (nullable) is None
        # and model_fields_set contains the field
        if self.custom2 is None and "custom2" in self.model_fields_set:
            _dict['custom2'] = None

        # set to None if custom3 (nullable) is None
        # and model_fields_set contains the field
        if self.custom3 is None and "custom3" in self.model_fields_set:
            _dict['custom3'] = None

        # set to None if custom4 (nullable) is None
        # and model_fields_set contains the field
        if self.custom4 is None and "custom4" in self.model_fields_set:
            _dict['custom4'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContactUpdateFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "company": obj.get("company"),
            "title": obj.get("title"),
            "custom": obj.get("custom"),
            "custom2": obj.get("custom2"),
            "custom3": obj.get("custom3"),
            "custom4": obj.get("custom4")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


