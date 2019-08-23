# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services. Use Messente API library to send and receive SMS, Viber, WhatsApp and Telegram messages, blacklist phone numbers to make sure you're not sending any unwanted messages, manage contacts and groups.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.0.2
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class WhatsAppDocument(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'caption': 'str',
        'content': 'str'
    }

    attribute_map = {
        'caption': 'caption',
        'content': 'content'
    }

    def __init__(self, caption=None, content=None):  # noqa: E501
        """WhatsAppDocument - a model defined in OpenAPI"""  # noqa: E501

        self._caption = None
        self._content = None
        self.discriminator = None

        if caption is not None:
            self.caption = caption
        self.content = content

    @property
    def caption(self):
        """Gets the caption of this WhatsAppDocument.  # noqa: E501

        Description for the document  # noqa: E501

        :return: The caption of this WhatsAppDocument.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this WhatsAppDocument.

        Description for the document  # noqa: E501

        :param caption: The caption of this WhatsAppDocument.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def content(self):
        """Gets the content of this WhatsAppDocument.  # noqa: E501

        Base64-encoded image  # noqa: E501

        :return: The content of this WhatsAppDocument.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this WhatsAppDocument.

        Base64-encoded image  # noqa: E501

        :param content: The content of this WhatsAppDocument.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WhatsAppDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
