# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class UserSharedItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error_details': 'ErrorDetails',
        'shared': 'str',
        'user': 'UserInfo'
    }

    attribute_map = {
        'error_details': 'errorDetails',
        'shared': 'shared',
        'user': 'user'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UserSharedItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_details = None
        self._shared = None
        self._user = None
        self.discriminator = None

        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('shared'), kwargs.get('shared', None))
        setattr(self, "_{}".format('user'), kwargs.get('user', None))

    @property
    def error_details(self):
        """Gets the error_details of this UserSharedItem.  # noqa: E501

        Array or errors.  # noqa: E501

        :return: The error_details of this UserSharedItem.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this UserSharedItem.

        Array or errors.  # noqa: E501

        :param error_details: The error_details of this UserSharedItem.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def shared(self):
        """Gets the shared of this UserSharedItem.  # noqa: E501

        When set to **true**, this custom tab is shared.  # noqa: E501

        :return: The shared of this UserSharedItem.  # noqa: E501
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this UserSharedItem.

        When set to **true**, this custom tab is shared.  # noqa: E501

        :param shared: The shared of this UserSharedItem.  # noqa: E501
        :type: str
        """

        self._shared = shared

    @property
    def user(self):
        """Gets the user of this UserSharedItem.  # noqa: E501

        The user whose sharing information is being requested.  # noqa: E501

        :return: The user of this UserSharedItem.  # noqa: E501
        :rtype: UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserSharedItem.

        The user whose sharing information is being requested.  # noqa: E501

        :param user: The user of this UserSharedItem.  # noqa: E501
        :type: UserInfo
        """

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(UserSharedItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserSharedItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserSharedItem):
            return True

        return self.to_dict() != other.to_dict()
