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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from messente_api.models.mobile_network import MobileNetwork
from typing import Optional, Set
from typing_extensions import Self

class SyncNumberLookupResult(BaseModel):
    """
    Info about a phone number
    """ # noqa: E501
    number: StrictStr = Field(description="Phone number in e.164 format")
    roaming: Optional[StrictBool] = Field(default=None, description="Indicates if a number is roaming")
    ported: Optional[StrictBool] = Field(default=None, description="Indicates if a number is ported")
    roaming_network: Optional[MobileNetwork] = Field(default=None, alias="roamingNetwork")
    current_network: Optional[MobileNetwork] = Field(default=None, alias="currentNetwork")
    original_network: Optional[MobileNetwork] = Field(default=None, alias="originalNetwork")
    ported_network: Optional[MobileNetwork] = Field(default=None, alias="portedNetwork")
    status: Optional[StrictStr] = Field(default=None, description="Status of the phone number")
    error: Optional[Any] = Field(default=None, description="Indicates if any error occurred while handling the request")
    __properties: ClassVar[List[str]] = ["number", "roaming", "ported", "roamingNetwork", "currentNetwork", "originalNetwork", "portedNetwork", "status", "error"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ON', 'OFF', 'INVALID', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('ON', 'OFF', 'INVALID', 'UNKNOWN')")
        return value

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
        """Create an instance of SyncNumberLookupResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of roaming_network
        if self.roaming_network:
            _dict['roamingNetwork'] = self.roaming_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_network
        if self.current_network:
            _dict['currentNetwork'] = self.current_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_network
        if self.original_network:
            _dict['originalNetwork'] = self.original_network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ported_network
        if self.ported_network:
            _dict['portedNetwork'] = self.ported_network.to_dict()
        # set to None if roaming (nullable) is None
        # and model_fields_set contains the field
        if self.roaming is None and "roaming" in self.model_fields_set:
            _dict['roaming'] = None

        # set to None if ported (nullable) is None
        # and model_fields_set contains the field
        if self.ported is None and "ported" in self.model_fields_set:
            _dict['ported'] = None

        # set to None if roaming_network (nullable) is None
        # and model_fields_set contains the field
        if self.roaming_network is None and "roaming_network" in self.model_fields_set:
            _dict['roamingNetwork'] = None

        # set to None if current_network (nullable) is None
        # and model_fields_set contains the field
        if self.current_network is None and "current_network" in self.model_fields_set:
            _dict['currentNetwork'] = None

        # set to None if original_network (nullable) is None
        # and model_fields_set contains the field
        if self.original_network is None and "original_network" in self.model_fields_set:
            _dict['originalNetwork'] = None

        # set to None if ported_network (nullable) is None
        # and model_fields_set contains the field
        if self.ported_network is None and "ported_network" in self.model_fields_set:
            _dict['portedNetwork'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SyncNumberLookupResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "roaming": obj.get("roaming"),
            "ported": obj.get("ported"),
            "roamingNetwork": MobileNetwork.from_dict(obj["roamingNetwork"]) if obj.get("roamingNetwork") is not None else None,
            "currentNetwork": MobileNetwork.from_dict(obj["currentNetwork"]) if obj.get("currentNetwork") is not None else None,
            "originalNetwork": MobileNetwork.from_dict(obj["originalNetwork"]) if obj.get("originalNetwork") is not None else None,
            "portedNetwork": MobileNetwork.from_dict(obj["portedNetwork"]) if obj.get("portedNetwork") is not None else None,
            "status": obj.get("status"),
            "error": obj.get("error")
        })
        return _obj


