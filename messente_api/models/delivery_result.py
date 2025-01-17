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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from messente_api.models.channel import Channel
from messente_api.models.error_code_omnichannel_machine import ErrorCodeOmnichannelMachine
from messente_api.models.price_info import PriceInfo
from messente_api.models.status import Status
from typing import Optional, Set
from typing_extensions import Self

class DeliveryResult(BaseModel):
    """
    A delivery report
    """ # noqa: E501
    status: Optional[Status] = None
    channel: Optional[Channel] = None
    message_id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the message")
    error: Optional[StrictStr] = Field(default=None, description="Human-readable description of what went wrong, *null* in case of success or if the message has not been processed yet")
    err: Optional[ErrorCodeOmnichannelMachine] = None
    timestamp: Optional[datetime] = Field(default=None, description="When this status was received by Omnichannel API")
    price_info: Optional[PriceInfo] = None
    sender: Optional[StrictStr] = Field(default=None, description="the sender of the message")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["status", "channel", "message_id", "error", "err", "timestamp", "price_info", "sender"]

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
        """Create an instance of DeliveryResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price_info
        if self.price_info:
            _dict['price_info'] = self.price_info.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeliveryResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "channel": obj.get("channel"),
            "message_id": obj.get("message_id"),
            "error": obj.get("error"),
            "err": obj.get("err"),
            "timestamp": obj.get("timestamp"),
            "price_info": PriceInfo.from_dict(obj["price_info"]) if obj.get("price_info") is not None else None,
            "sender": obj.get("sender")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


