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


class WhatsApp(object):
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
        'text': 'WhatsAppText',
        'image': 'WhatsAppImage',
        'document': 'WhatsAppDocument',
        'audio': 'WhatsAppAudio',
        'channel': 'str'
    }

    attribute_map = {
        'sender': 'sender',
        'validity': 'validity',
        'text': 'text',
        'image': 'image',
        'document': 'document',
        'audio': 'audio',
        'channel': 'channel'
    }

    def __init__(self, sender=None, validity=None, text=None, image=None, document=None, audio=None, channel='whatsapp'):  # noqa: E501
        """WhatsApp - a model defined in OpenAPI"""  # noqa: E501

        self._sender = None
        self._validity = None
        self._text = None
        self._image = None
        self._document = None
        self._audio = None
        self._channel = None
        self.discriminator = None

        if sender is not None:
            self.sender = sender
        if validity is not None:
            self.validity = validity
        if text is not None:
            self.text = text
        if image is not None:
            self.image = image
        if document is not None:
            self.document = document
        if audio is not None:
            self.audio = audio
        if channel is not None:
            self.channel = channel

    @property
    def sender(self):
        """Gets the sender of this WhatsApp.  # noqa: E501

        Phone number or alphanumeric sender name  # noqa: E501

        :return: The sender of this WhatsApp.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this WhatsApp.

        Phone number or alphanumeric sender name  # noqa: E501

        :param sender: The sender of this WhatsApp.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def validity(self):
        """Gets the validity of this WhatsApp.  # noqa: E501

        After how many minutes this channel is   considered as failed and the next channel is attempted  # noqa: E501

        :return: The validity of this WhatsApp.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this WhatsApp.

        After how many minutes this channel is   considered as failed and the next channel is attempted  # noqa: E501

        :param validity: The validity of this WhatsApp.  # noqa: E501
        :type: int
        """

        self._validity = validity

    @property
    def text(self):
        """Gets the text of this WhatsApp.  # noqa: E501


        :return: The text of this WhatsApp.  # noqa: E501
        :rtype: WhatsAppText
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this WhatsApp.


        :param text: The text of this WhatsApp.  # noqa: E501
        :type: WhatsAppText
        """

        self._text = text

    @property
    def image(self):
        """Gets the image of this WhatsApp.  # noqa: E501


        :return: The image of this WhatsApp.  # noqa: E501
        :rtype: WhatsAppImage
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this WhatsApp.


        :param image: The image of this WhatsApp.  # noqa: E501
        :type: WhatsAppImage
        """

        self._image = image

    @property
    def document(self):
        """Gets the document of this WhatsApp.  # noqa: E501


        :return: The document of this WhatsApp.  # noqa: E501
        :rtype: WhatsAppDocument
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this WhatsApp.


        :param document: The document of this WhatsApp.  # noqa: E501
        :type: WhatsAppDocument
        """

        self._document = document

    @property
    def audio(self):
        """Gets the audio of this WhatsApp.  # noqa: E501


        :return: The audio of this WhatsApp.  # noqa: E501
        :rtype: WhatsAppAudio
        """
        return self._audio

    @audio.setter
    def audio(self, audio):
        """Sets the audio of this WhatsApp.


        :param audio: The audio of this WhatsApp.  # noqa: E501
        :type: WhatsAppAudio
        """

        self._audio = audio

    @property
    def channel(self):
        """Gets the channel of this WhatsApp.  # noqa: E501

        The channel used to deliver the message  # noqa: E501

        :return: The channel of this WhatsApp.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this WhatsApp.

        The channel used to deliver the message  # noqa: E501

        :param channel: The channel of this WhatsApp.  # noqa: E501
        :type: str
        """
        allowed_values = ["whatsapp"]  # noqa: E501
        if channel not in allowed_values:
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
        if not isinstance(other, WhatsApp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
