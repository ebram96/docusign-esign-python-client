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


class UserAuthorization(object):
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
        'agent_user': 'AuthorizationUser',
        'authorization_id': 'str',
        'created': 'str',
        'created_by': 'str',
        'end_date': 'str',
        'modified': 'str',
        'modified_by': 'str',
        'permission': 'str',
        'principal_user': 'AuthorizationUser',
        'start_date': 'str'
    }

    attribute_map = {
        'agent_user': 'agentUser',
        'authorization_id': 'authorizationId',
        'created': 'created',
        'created_by': 'createdBy',
        'end_date': 'endDate',
        'modified': 'modified',
        'modified_by': 'modifiedBy',
        'permission': 'permission',
        'principal_user': 'principalUser',
        'start_date': 'startDate'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """UserAuthorization - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agent_user = None
        self._authorization_id = None
        self._created = None
        self._created_by = None
        self._end_date = None
        self._modified = None
        self._modified_by = None
        self._permission = None
        self._principal_user = None
        self._start_date = None
        self.discriminator = None

        setattr(self, "_{}".format('agent_user'), kwargs.get('agent_user', None))
        setattr(self, "_{}".format('authorization_id'), kwargs.get('authorization_id', None))
        setattr(self, "_{}".format('created'), kwargs.get('created', None))
        setattr(self, "_{}".format('created_by'), kwargs.get('created_by', None))
        setattr(self, "_{}".format('end_date'), kwargs.get('end_date', None))
        setattr(self, "_{}".format('modified'), kwargs.get('modified', None))
        setattr(self, "_{}".format('modified_by'), kwargs.get('modified_by', None))
        setattr(self, "_{}".format('permission'), kwargs.get('permission', None))
        setattr(self, "_{}".format('principal_user'), kwargs.get('principal_user', None))
        setattr(self, "_{}".format('start_date'), kwargs.get('start_date', None))

    @property
    def agent_user(self):
        """Gets the agent_user of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The agent_user of this UserAuthorization.  # noqa: E501
        :rtype: AuthorizationUser
        """
        return self._agent_user

    @agent_user.setter
    def agent_user(self, agent_user):
        """Sets the agent_user of this UserAuthorization.

          # noqa: E501

        :param agent_user: The agent_user of this UserAuthorization.  # noqa: E501
        :type: AuthorizationUser
        """

        self._agent_user = agent_user

    @property
    def authorization_id(self):
        """Gets the authorization_id of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The authorization_id of this UserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._authorization_id

    @authorization_id.setter
    def authorization_id(self, authorization_id):
        """Sets the authorization_id of this UserAuthorization.

          # noqa: E501

        :param authorization_id: The authorization_id of this UserAuthorization.  # noqa: E501
        :type: str
        """

        self._authorization_id = authorization_id

    @property
    def created(self):
        """Gets the created of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The created of this UserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this UserAuthorization.

          # noqa: E501

        :param created: The created of this UserAuthorization.  # noqa: E501
        :type: str
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The created_by of this UserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UserAuthorization.

          # noqa: E501

        :param created_by: The created_by of this UserAuthorization.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def end_date(self):
        """Gets the end_date of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The end_date of this UserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this UserAuthorization.

          # noqa: E501

        :param end_date: The end_date of this UserAuthorization.  # noqa: E501
        :type: str
        """

        self._end_date = end_date

    @property
    def modified(self):
        """Gets the modified of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The modified of this UserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this UserAuthorization.

          # noqa: E501

        :param modified: The modified of this UserAuthorization.  # noqa: E501
        :type: str
        """

        self._modified = modified

    @property
    def modified_by(self):
        """Gets the modified_by of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The modified_by of this UserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this UserAuthorization.

          # noqa: E501

        :param modified_by: The modified_by of this UserAuthorization.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def permission(self):
        """Gets the permission of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The permission of this UserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this UserAuthorization.

          # noqa: E501

        :param permission: The permission of this UserAuthorization.  # noqa: E501
        :type: str
        """

        self._permission = permission

    @property
    def principal_user(self):
        """Gets the principal_user of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The principal_user of this UserAuthorization.  # noqa: E501
        :rtype: AuthorizationUser
        """
        return self._principal_user

    @principal_user.setter
    def principal_user(self, principal_user):
        """Sets the principal_user of this UserAuthorization.

          # noqa: E501

        :param principal_user: The principal_user of this UserAuthorization.  # noqa: E501
        :type: AuthorizationUser
        """

        self._principal_user = principal_user

    @property
    def start_date(self):
        """Gets the start_date of this UserAuthorization.  # noqa: E501

          # noqa: E501

        :return: The start_date of this UserAuthorization.  # noqa: E501
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this UserAuthorization.

          # noqa: E501

        :param start_date: The start_date of this UserAuthorization.  # noqa: E501
        :type: str
        """

        self._start_date = start_date

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
        if issubclass(UserAuthorization, dict):
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
        if not isinstance(other, UserAuthorization):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserAuthorization):
            return True

        return self.to_dict() != other.to_dict()
