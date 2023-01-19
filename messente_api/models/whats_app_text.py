# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services.  * Send and receive SMS, Viber, WhatsApp and Telegram messages. * Manage contacts and groups. * Fetch detailed info about phone numbers. * Blacklist phone numbers to make sure you're not sending any unwanted messages.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from messente_api.configuration import Configuration


class WhatsAppText(object):
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
        'preview_url': 'bool',
        'body': 'str'
    }

    attribute_map = {
        'preview_url': 'preview_url',
        'body': 'body'
    }

    def __init__(self, preview_url=True, body=None, local_vars_configuration=None):  # noqa: E501
        """WhatsAppText - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._preview_url = None
        self._body = None
        self.discriminator = None

        if preview_url is not None:
            self.preview_url = preview_url
        self.body = body

    @property
    def preview_url(self):
        """Gets the preview_url of this WhatsAppText.  # noqa: E501

        Whether to display link preview if the message contains a hyperlink  # noqa: E501

        :return: The preview_url of this WhatsAppText.  # noqa: E501
        :rtype: bool
        """
        return self._preview_url

    @preview_url.setter
    def preview_url(self, preview_url):
        """Sets the preview_url of this WhatsAppText.

        Whether to display link preview if the message contains a hyperlink  # noqa: E501

        :param preview_url: The preview_url of this WhatsAppText.  # noqa: E501
        :type preview_url: bool
        """

        self._preview_url = preview_url

    @property
    def body(self):
        """Gets the body of this WhatsAppText.  # noqa: E501

        Plaintext content for WhatsApp, can contain URLs, emojis and formatting  # noqa: E501

        :return: The body of this WhatsAppText.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this WhatsAppText.

        Plaintext content for WhatsApp, can contain URLs, emojis and formatting  # noqa: E501

        :param body: The body of this WhatsAppText.  # noqa: E501
        :type body: str
        """
        if self.local_vars_configuration.client_side_validation and body is None:  # noqa: E501
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WhatsAppText):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhatsAppText):
            return True

        return self.to_dict() != other.to_dict()
