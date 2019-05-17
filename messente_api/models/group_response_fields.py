# coding: utf-8

"""
    Messente API

    [Messente](https://messente.com) is a global provider of messaging and user verification services. Use Messente API library to send and receive SMS, Viber and WhatsApp messages, blacklist phone numbers to make sure you're not sending any unwanted messages, manage contacts and groups.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class GroupResponseFields(object):
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
        'id': 'str',
        'name': 'str',
        'created_on': 'str',
        'contacts_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_on': 'createdOn',
        'contacts_count': 'contactsCount'
    }

    def __init__(self, id=None, name=None, created_on=None, contacts_count=None):  # noqa: E501
        """GroupResponseFields - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._name = None
        self._created_on = None
        self._contacts_count = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.created_on = created_on
        self.contacts_count = contacts_count

    @property
    def id(self):
        """Gets the id of this GroupResponseFields.  # noqa: E501

        Id string in uuid format  # noqa: E501

        :return: The id of this GroupResponseFields.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupResponseFields.

        Id string in uuid format  # noqa: E501

        :param id: The id of this GroupResponseFields.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this GroupResponseFields.  # noqa: E501


        :return: The name of this GroupResponseFields.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupResponseFields.


        :param name: The name of this GroupResponseFields.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_on(self):
        """Gets the created_on of this GroupResponseFields.  # noqa: E501

        format %Y-%m-%dT%H:%M:%S.%fZ  # noqa: E501

        :return: The created_on of this GroupResponseFields.  # noqa: E501
        :rtype: str
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this GroupResponseFields.

        format %Y-%m-%dT%H:%M:%S.%fZ  # noqa: E501

        :param created_on: The created_on of this GroupResponseFields.  # noqa: E501
        :type: str
        """

        self._created_on = created_on

    @property
    def contacts_count(self):
        """Gets the contacts_count of this GroupResponseFields.  # noqa: E501


        :return: The contacts_count of this GroupResponseFields.  # noqa: E501
        :rtype: int
        """
        return self._contacts_count

    @contacts_count.setter
    def contacts_count(self, contacts_count):
        """Sets the contacts_count of this GroupResponseFields.


        :param contacts_count: The contacts_count of this GroupResponseFields.  # noqa: E501
        :type: int
        """
        if contacts_count is None:
            raise ValueError("Invalid value for `contacts_count`, must not be `None`")  # noqa: E501

        self._contacts_count = contacts_count

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
        if not isinstance(other, GroupResponseFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
