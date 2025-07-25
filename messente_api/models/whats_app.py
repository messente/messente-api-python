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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from messente_api.models.whats_app_audio import WhatsAppAudio
from messente_api.models.whats_app_document import WhatsAppDocument
from messente_api.models.whats_app_image import WhatsAppImage
from messente_api.models.whats_app_sticker import WhatsAppSticker
from messente_api.models.whats_app_template import WhatsAppTemplate
from messente_api.models.whats_app_text import WhatsAppText
from messente_api.models.whats_app_video import WhatsAppVideo
from typing import Optional, Set
from typing_extensions import Self

class WhatsApp(BaseModel):
    """
    WhatsApp message content.   Only one of \"text\", \"image\", \"document\" or \"audio\" can be provided
    """ # noqa: E501
    sender: Optional[StrictStr] = Field(default=None, description="Phone number or alphanumeric sender name")
    validity: Optional[StrictInt] = Field(default=None, description="After how many minutes this channel is   considered as failed and the next channel is attempted")
    ttl: Optional[StrictInt] = Field(default=None, description="After how many seconds this channel is considered as failed and the next channel is attempted.       Only one of \"ttl\" and \"validity\" can be used.")
    template: Optional[WhatsAppTemplate] = None
    channel: Optional[StrictStr] = Field(default='whatsapp', description="The channel used to deliver the message")
    text: Optional[WhatsAppText] = None
    image: Optional[WhatsAppImage] = None
    video: Optional[WhatsAppVideo] = None
    audio: Optional[WhatsAppAudio] = None
    document: Optional[WhatsAppDocument] = None
    sticker: Optional[WhatsAppSticker] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["sender", "validity", "ttl", "template", "channel", "text", "image", "video", "audio", "document", "sticker"]

    @field_validator('channel')
    def channel_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['whatsapp']):
            raise ValueError("must be one of enum values ('whatsapp')")
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
        """Create an instance of WhatsApp from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of template
        if self.template:
            _dict['template'] = self.template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of text
        if self.text:
            _dict['text'] = self.text.to_dict()
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video
        if self.video:
            _dict['video'] = self.video.to_dict()
        # override the default output from pydantic by calling `to_dict()` of audio
        if self.audio:
            _dict['audio'] = self.audio.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document
        if self.document:
            _dict['document'] = self.document.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sticker
        if self.sticker:
            _dict['sticker'] = self.sticker.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WhatsApp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sender": obj.get("sender"),
            "validity": obj.get("validity"),
            "ttl": obj.get("ttl"),
            "template": WhatsAppTemplate.from_dict(obj["template"]) if obj.get("template") is not None else None,
            "channel": obj.get("channel") if obj.get("channel") is not None else 'whatsapp',
            "text": WhatsAppText.from_dict(obj["text"]) if obj.get("text") is not None else None,
            "image": WhatsAppImage.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "video": WhatsAppVideo.from_dict(obj["video"]) if obj.get("video") is not None else None,
            "audio": WhatsAppAudio.from_dict(obj["audio"]) if obj.get("audio") is not None else None,
            "document": WhatsAppDocument.from_dict(obj["document"]) if obj.get("document") is not None else None,
            "sticker": WhatsAppSticker.from_dict(obj["sticker"]) if obj.get("sticker") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


