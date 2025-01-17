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
from messente_api.models.whats_app_currency import WhatsAppCurrency
from messente_api.models.whats_app_datetime import WhatsAppDatetime
from messente_api.models.whats_app_media import WhatsAppMedia
from typing import Optional, Set
from typing_extensions import Self

class WhatsAppParameter(BaseModel):
    """
    Whatsapp component parameter.
    """ # noqa: E501
    type: StrictStr = Field(description="Type of the parameter.")
    text: Optional[StrictStr] = Field(default=None, description="A text.")
    currency: Optional[WhatsAppCurrency] = None
    date_time: Optional[WhatsAppDatetime] = None
    image: Optional[WhatsAppMedia] = None
    document: Optional[WhatsAppMedia] = None
    video: Optional[WhatsAppMedia] = None
    coupon_code: Optional[StrictStr] = Field(default=None, description="A coupon code.")
    payload: Optional[StrictStr] = Field(default=None, description="A payload.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "text", "currency", "date_time", "image", "document", "video", "coupon_code", "payload"]

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
        """Create an instance of WhatsAppParameter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of date_time
        if self.date_time:
            _dict['date_time'] = self.date_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict['document'] = self.document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video
        if self.video:
            _dict['video'] = self.video.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WhatsAppParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "text": obj.get("text"),
            "currency": WhatsAppCurrency.from_dict(obj["currency"]) if obj.get("currency") is not None else None,
            "date_time": WhatsAppDatetime.from_dict(obj["date_time"]) if obj.get("date_time") is not None else None,
            "image": WhatsAppMedia.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "document": WhatsAppMedia.from_dict(obj["document"]) if obj.get("document") is not None else None,
            "video": WhatsAppMedia.from_dict(obj["video"]) if obj.get("video") is not None else None,
            "coupon_code": obj.get("coupon_code"),
            "payload": obj.get("payload")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


