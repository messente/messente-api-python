# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services.  * Send and receive SMS, Viber, WhatsApp and Telegram messages. * Manage contacts and groups. * Fetch detailed info about phone numbers. * Blacklist phone numbers to make sure you're not sending any unwanted messages.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from messente_api.configuration import Configuration


class Viber(object):
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
        'sender': 'str',
        'validity': 'int',
        'text': 'str',
        'image_url': 'str',
        'button_url': 'str',
        'button_text': 'str',
        'channel': 'str'
    }

    attribute_map = {
        'sender': 'sender',
        'validity': 'validity',
        'text': 'text',
        'image_url': 'image_url',
        'button_url': 'button_url',
        'button_text': 'button_text',
        'channel': 'channel'
    }

    def __init__(self, sender=None, validity=None, text=None, image_url=None, button_url=None, button_text=None, channel='viber', local_vars_configuration=None):  # noqa: E501
        """Viber - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sender = None
        self._validity = None
        self._text = None
        self._image_url = None
        self._button_url = None
        self._button_text = None
        self._channel = None
        self.discriminator = None

        if sender is not None:
            self.sender = sender
        if validity is not None:
            self.validity = validity
        if text is not None:
            self.text = text
        if image_url is not None:
            self.image_url = image_url
        if button_url is not None:
            self.button_url = button_url
        if button_text is not None:
            self.button_text = button_text
        if channel is not None:
            self.channel = channel

    @property
    def sender(self):
        """Gets the sender of this Viber.  # noqa: E501

        Phone number or alphanumeric sender name  # noqa: E501

        :return: The sender of this Viber.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this Viber.

        Phone number or alphanumeric sender name  # noqa: E501

        :param sender: The sender of this Viber.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def validity(self):
        """Gets the validity of this Viber.  # noqa: E501

        After how many minutes this channel is considered as failed and the next channel is attempted  # noqa: E501

        :return: The validity of this Viber.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this Viber.

        After how many minutes this channel is considered as failed and the next channel is attempted  # noqa: E501

        :param validity: The validity of this Viber.  # noqa: E501
        :type: int
        """

        self._validity = validity

    @property
    def text(self):
        """Gets the text of this Viber.  # noqa: E501

        Plaintext content for Viber  # noqa: E501

        :return: The text of this Viber.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Viber.

        Plaintext content for Viber  # noqa: E501

        :param text: The text of this Viber.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def image_url(self):
        """Gets the image_url of this Viber.  # noqa: E501

        URL for the embedded image    Valid combinations:    1) image_url,    2) text, image_url, button_url, button_text  # noqa: E501

        :return: The image_url of this Viber.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this Viber.

        URL for the embedded image    Valid combinations:    1) image_url,    2) text, image_url, button_url, button_text  # noqa: E501

        :param image_url: The image_url of this Viber.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def button_url(self):
        """Gets the button_url of this Viber.  # noqa: E501

        URL of the button, must be specified along with ''text'', ''button_text'' and ''image_url'' (optional)  # noqa: E501

        :return: The button_url of this Viber.  # noqa: E501
        :rtype: str
        """
        return self._button_url

    @button_url.setter
    def button_url(self, button_url):
        """Sets the button_url of this Viber.

        URL of the button, must be specified along with ''text'', ''button_text'' and ''image_url'' (optional)  # noqa: E501

        :param button_url: The button_url of this Viber.  # noqa: E501
        :type: str
        """

        self._button_url = button_url

    @property
    def button_text(self):
        """Gets the button_text of this Viber.  # noqa: E501

        Must be specified along with ''text'', ''button_url'', ''button_text'', ''image_url'' (optional)  # noqa: E501

        :return: The button_text of this Viber.  # noqa: E501
        :rtype: str
        """
        return self._button_text

    @button_text.setter
    def button_text(self, button_text):
        """Sets the button_text of this Viber.

        Must be specified along with ''text'', ''button_url'', ''button_text'', ''image_url'' (optional)  # noqa: E501

        :param button_text: The button_text of this Viber.  # noqa: E501
        :type: str
        """

        self._button_text = button_text

    @property
    def channel(self):
        """Gets the channel of this Viber.  # noqa: E501

        The channel used to deliver the message  # noqa: E501

        :return: The channel of this Viber.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this Viber.

        The channel used to deliver the message  # noqa: E501

        :param channel: The channel of this Viber.  # noqa: E501
        :type: str
        """
        allowed_values = ["viber"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and channel not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `channel` ({0}), must be one of {1}"  # noqa: E501
                .format(channel, allowed_values)
            )

        self._channel = channel

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
        if not isinstance(other, Viber):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Viber):
            return True

        return self.to_dict() != other.to_dict()
