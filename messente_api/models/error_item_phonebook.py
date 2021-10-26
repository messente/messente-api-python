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


class ErrorItemPhonebook(object):
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
        'title': 'ErrorTitlePhonebook',
        'detail': 'str',
        'code': 'ErrorCodePhonebook'
    }

    attribute_map = {
        'title': 'title',
        'detail': 'detail',
        'code': 'code'
    }

    def __init__(self, title=None, detail=None, code=None, local_vars_configuration=None):  # noqa: E501
        """ErrorItemPhonebook - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._detail = None
        self._code = None
        self.discriminator = None

        self.title = title
        self.detail = detail
        self.code = code

    @property
    def title(self):
        """Gets the title of this ErrorItemPhonebook.  # noqa: E501


        :return: The title of this ErrorItemPhonebook.  # noqa: E501
        :rtype: ErrorTitlePhonebook
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ErrorItemPhonebook.


        :param title: The title of this ErrorItemPhonebook.  # noqa: E501
        :type title: ErrorTitlePhonebook
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this ErrorItemPhonebook.  # noqa: E501

        Free form more detailed description of the error  # noqa: E501

        :return: The detail of this ErrorItemPhonebook.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorItemPhonebook.

        Free form more detailed description of the error  # noqa: E501

        :param detail: The detail of this ErrorItemPhonebook.  # noqa: E501
        :type detail: str
        """
        if self.local_vars_configuration.client_side_validation and detail is None:  # noqa: E501
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

    @property
    def code(self):
        """Gets the code of this ErrorItemPhonebook.  # noqa: E501


        :return: The code of this ErrorItemPhonebook.  # noqa: E501
        :rtype: ErrorCodePhonebook
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorItemPhonebook.


        :param code: The code of this ErrorItemPhonebook.  # noqa: E501
        :type code: ErrorCodePhonebook
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

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
        if not isinstance(other, ErrorItemPhonebook):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorItemPhonebook):
            return True

        return self.to_dict() != other.to_dict()
