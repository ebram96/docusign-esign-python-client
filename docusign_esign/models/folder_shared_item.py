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


class FolderSharedItem(object):
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
        'folder_id': 'str',
        'name': 'str',
        'owner': 'UserInfo',
        'parent_folder_id': 'str',
        'parent_folder_uri': 'str',
        'shared': 'str',
        'shared_groups': 'list[MemberGroupSharedItem]',
        'shared_users': 'list[UserSharedItem]',
        'uri': 'str',
        'user': 'UserInfo'
    }

    attribute_map = {
        'error_details': 'errorDetails',
        'folder_id': 'folderId',
        'name': 'name',
        'owner': 'owner',
        'parent_folder_id': 'parentFolderId',
        'parent_folder_uri': 'parentFolderUri',
        'shared': 'shared',
        'shared_groups': 'sharedGroups',
        'shared_users': 'sharedUsers',
        'uri': 'uri',
        'user': 'user'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """FolderSharedItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error_details = None
        self._folder_id = None
        self._name = None
        self._owner = None
        self._parent_folder_id = None
        self._parent_folder_uri = None
        self._shared = None
        self._shared_groups = None
        self._shared_users = None
        self._uri = None
        self._user = None
        self.discriminator = None

        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('folder_id'), kwargs.get('folder_id', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('owner'), kwargs.get('owner', None))
        setattr(self, "_{}".format('parent_folder_id'), kwargs.get('parent_folder_id', None))
        setattr(self, "_{}".format('parent_folder_uri'), kwargs.get('parent_folder_uri', None))
        setattr(self, "_{}".format('shared'), kwargs.get('shared', None))
        setattr(self, "_{}".format('shared_groups'), kwargs.get('shared_groups', None))
        setattr(self, "_{}".format('shared_users'), kwargs.get('shared_users', None))
        setattr(self, "_{}".format('uri'), kwargs.get('uri', None))
        setattr(self, "_{}".format('user'), kwargs.get('user', None))

    @property
    def error_details(self):
        """Gets the error_details of this FolderSharedItem.  # noqa: E501

        Array or errors.  # noqa: E501

        :return: The error_details of this FolderSharedItem.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this FolderSharedItem.

        Array or errors.  # noqa: E501

        :param error_details: The error_details of this FolderSharedItem.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def folder_id(self):
        """Gets the folder_id of this FolderSharedItem.  # noqa: E501

          # noqa: E501

        :return: The folder_id of this FolderSharedItem.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this FolderSharedItem.

          # noqa: E501

        :param folder_id: The folder_id of this FolderSharedItem.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def name(self):
        """Gets the name of this FolderSharedItem.  # noqa: E501

          # noqa: E501

        :return: The name of this FolderSharedItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderSharedItem.

          # noqa: E501

        :param name: The name of this FolderSharedItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this FolderSharedItem.  # noqa: E501

        Information about the user who owns the folder.  # noqa: E501

        :return: The owner of this FolderSharedItem.  # noqa: E501
        :rtype: UserInfo
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this FolderSharedItem.

        Information about the user who owns the folder.  # noqa: E501

        :param owner: The owner of this FolderSharedItem.  # noqa: E501
        :type: UserInfo
        """

        self._owner = owner

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this FolderSharedItem.  # noqa: E501

          # noqa: E501

        :return: The parent_folder_id of this FolderSharedItem.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this FolderSharedItem.

          # noqa: E501

        :param parent_folder_id: The parent_folder_id of this FolderSharedItem.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def parent_folder_uri(self):
        """Gets the parent_folder_uri of this FolderSharedItem.  # noqa: E501

          # noqa: E501

        :return: The parent_folder_uri of this FolderSharedItem.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_uri

    @parent_folder_uri.setter
    def parent_folder_uri(self, parent_folder_uri):
        """Sets the parent_folder_uri of this FolderSharedItem.

          # noqa: E501

        :param parent_folder_uri: The parent_folder_uri of this FolderSharedItem.  # noqa: E501
        :type: str
        """

        self._parent_folder_uri = parent_folder_uri

    @property
    def shared(self):
        """Gets the shared of this FolderSharedItem.  # noqa: E501

        When set to **true**, this custom tab is shared.  # noqa: E501

        :return: The shared of this FolderSharedItem.  # noqa: E501
        :rtype: str
        """
        return self._shared

    @shared.setter
    def shared(self, shared):
        """Sets the shared of this FolderSharedItem.

        When set to **true**, this custom tab is shared.  # noqa: E501

        :param shared: The shared of this FolderSharedItem.  # noqa: E501
        :type: str
        """

        self._shared = shared

    @property
    def shared_groups(self):
        """Gets the shared_groups of this FolderSharedItem.  # noqa: E501

          # noqa: E501

        :return: The shared_groups of this FolderSharedItem.  # noqa: E501
        :rtype: list[MemberGroupSharedItem]
        """
        return self._shared_groups

    @shared_groups.setter
    def shared_groups(self, shared_groups):
        """Sets the shared_groups of this FolderSharedItem.

          # noqa: E501

        :param shared_groups: The shared_groups of this FolderSharedItem.  # noqa: E501
        :type: list[MemberGroupSharedItem]
        """

        self._shared_groups = shared_groups

    @property
    def shared_users(self):
        """Gets the shared_users of this FolderSharedItem.  # noqa: E501

          # noqa: E501

        :return: The shared_users of this FolderSharedItem.  # noqa: E501
        :rtype: list[UserSharedItem]
        """
        return self._shared_users

    @shared_users.setter
    def shared_users(self, shared_users):
        """Sets the shared_users of this FolderSharedItem.

          # noqa: E501

        :param shared_users: The shared_users of this FolderSharedItem.  # noqa: E501
        :type: list[UserSharedItem]
        """

        self._shared_users = shared_users

    @property
    def uri(self):
        """Gets the uri of this FolderSharedItem.  # noqa: E501

          # noqa: E501

        :return: The uri of this FolderSharedItem.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this FolderSharedItem.

          # noqa: E501

        :param uri: The uri of this FolderSharedItem.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def user(self):
        """Gets the user of this FolderSharedItem.  # noqa: E501

        Information about the user associated with the folder.  # noqa: E501

        :return: The user of this FolderSharedItem.  # noqa: E501
        :rtype: UserInfo
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this FolderSharedItem.

        Information about the user associated with the folder.  # noqa: E501

        :param user: The user of this FolderSharedItem.  # noqa: E501
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
        if issubclass(FolderSharedItem, dict):
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
        if not isinstance(other, FolderSharedItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderSharedItem):
            return True

        return self.to_dict() != other.to_dict()
