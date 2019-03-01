# coding: utf-8

"""
    Messente Combined API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


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

    def __init__(self, title=None, detail=None, code=None):  # noqa: E501
        """ErrorItemPhonebook - a model defined in OpenAPI"""  # noqa: E501

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
        :type: ErrorTitlePhonebook
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this ErrorItemPhonebook.  # noqa: E501

        Free form more detailed description of the error.  # noqa: E501

        :return: The detail of this ErrorItemPhonebook.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorItemPhonebook.

        Free form more detailed description of the error.  # noqa: E501

        :param detail: The detail of this ErrorItemPhonebook.  # noqa: E501
        :type: str
        """
        if detail is None:
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
        :type: ErrorCodePhonebook
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

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
        if not isinstance(other, ErrorItemPhonebook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
