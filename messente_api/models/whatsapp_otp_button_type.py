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
import json
from enum import Enum
from typing_extensions import Self


class WhatsappOtpButtonType(str, Enum):
    """
    Type of the OTP button
    """

    """
    allowed enum values
    """
    COPY_CODE = 'copy_code'
    ONE_TAP = 'one_tap'
    ZERO_TAP = 'zero_tap'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WhatsappOtpButtonType from a JSON string"""
        return cls(json.loads(json_str))


