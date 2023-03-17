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


class FolderItemV2(object):
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
        'completed_date_time': 'str',
        'created_date_time': 'str',
        'envelope_id': 'str',
        'envelope_uri': 'str',
        'expire_date_time': 'str',
        'folder_id': 'str',
        'folder_uri': 'str',
        'is21_cfr_part11': 'str',
        'last_modified_date_time': 'str',
        'owner_name': 'str',
        'recipients': 'Recipients',
        'recipients_uri': 'str',
        'sender_company': 'str',
        'sender_email': 'str',
        'sender_name': 'str',
        'sender_user_id': 'str',
        'sent_date_time': 'str',
        'status': 'str',
        'subject': 'str',
        'template_id': 'str',
        'template_uri': 'str'
    }

    attribute_map = {
        'completed_date_time': 'completedDateTime',
        'created_date_time': 'createdDateTime',
        'envelope_id': 'envelopeId',
        'envelope_uri': 'envelopeUri',
        'expire_date_time': 'expireDateTime',
        'folder_id': 'folderId',
        'folder_uri': 'folderUri',
        'is21_cfr_part11': 'is21CFRPart11',
        'last_modified_date_time': 'lastModifiedDateTime',
        'owner_name': 'ownerName',
        'recipients': 'recipients',
        'recipients_uri': 'recipientsUri',
        'sender_company': 'senderCompany',
        'sender_email': 'senderEmail',
        'sender_name': 'senderName',
        'sender_user_id': 'senderUserId',
        'sent_date_time': 'sentDateTime',
        'status': 'status',
        'subject': 'subject',
        'template_id': 'templateId',
        'template_uri': 'templateUri'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """FolderItemV2 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._completed_date_time = None
        self._created_date_time = None
        self._envelope_id = None
        self._envelope_uri = None
        self._expire_date_time = None
        self._folder_id = None
        self._folder_uri = None
        self._is21_cfr_part11 = None
        self._last_modified_date_time = None
        self._owner_name = None
        self._recipients = None
        self._recipients_uri = None
        self._sender_company = None
        self._sender_email = None
        self._sender_name = None
        self._sender_user_id = None
        self._sent_date_time = None
        self._status = None
        self._subject = None
        self._template_id = None
        self._template_uri = None
        self.discriminator = None

        setattr(self, "_{}".format('completed_date_time'), kwargs.get('completed_date_time', None))
        setattr(self, "_{}".format('created_date_time'), kwargs.get('created_date_time', None))
        setattr(self, "_{}".format('envelope_id'), kwargs.get('envelope_id', None))
        setattr(self, "_{}".format('envelope_uri'), kwargs.get('envelope_uri', None))
        setattr(self, "_{}".format('expire_date_time'), kwargs.get('expire_date_time', None))
        setattr(self, "_{}".format('folder_id'), kwargs.get('folder_id', None))
        setattr(self, "_{}".format('folder_uri'), kwargs.get('folder_uri', None))
        setattr(self, "_{}".format('is21_cfr_part11'), kwargs.get('is21_cfr_part11', None))
        setattr(self, "_{}".format('last_modified_date_time'), kwargs.get('last_modified_date_time', None))
        setattr(self, "_{}".format('owner_name'), kwargs.get('owner_name', None))
        setattr(self, "_{}".format('recipients'), kwargs.get('recipients', None))
        setattr(self, "_{}".format('recipients_uri'), kwargs.get('recipients_uri', None))
        setattr(self, "_{}".format('sender_company'), kwargs.get('sender_company', None))
        setattr(self, "_{}".format('sender_email'), kwargs.get('sender_email', None))
        setattr(self, "_{}".format('sender_name'), kwargs.get('sender_name', None))
        setattr(self, "_{}".format('sender_user_id'), kwargs.get('sender_user_id', None))
        setattr(self, "_{}".format('sent_date_time'), kwargs.get('sent_date_time', None))
        setattr(self, "_{}".format('status'), kwargs.get('status', None))
        setattr(self, "_{}".format('subject'), kwargs.get('subject', None))
        setattr(self, "_{}".format('template_id'), kwargs.get('template_id', None))
        setattr(self, "_{}".format('template_uri'), kwargs.get('template_uri', None))

    @property
    def completed_date_time(self):
        """Gets the completed_date_time of this FolderItemV2.  # noqa: E501

        Specifies the date and time this item was completed.  # noqa: E501

        :return: The completed_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._completed_date_time

    @completed_date_time.setter
    def completed_date_time(self, completed_date_time):
        """Sets the completed_date_time of this FolderItemV2.

        Specifies the date and time this item was completed.  # noqa: E501

        :param completed_date_time: The completed_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._completed_date_time = completed_date_time

    @property
    def created_date_time(self):
        """Gets the created_date_time of this FolderItemV2.  # noqa: E501

        Indicates the date and time the item was created.  # noqa: E501

        :return: The created_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._created_date_time

    @created_date_time.setter
    def created_date_time(self, created_date_time):
        """Sets the created_date_time of this FolderItemV2.

        Indicates the date and time the item was created.  # noqa: E501

        :param created_date_time: The created_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._created_date_time = created_date_time

    @property
    def envelope_id(self):
        """Gets the envelope_id of this FolderItemV2.  # noqa: E501

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :return: The envelope_id of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._envelope_id

    @envelope_id.setter
    def envelope_id(self, envelope_id):
        """Sets the envelope_id of this FolderItemV2.

        The envelope ID of the envelope status that failed to post.  # noqa: E501

        :param envelope_id: The envelope_id of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._envelope_id = envelope_id

    @property
    def envelope_uri(self):
        """Gets the envelope_uri of this FolderItemV2.  # noqa: E501

        Contains a URI for an endpoint that you can use to retrieve the envelope or envelopes.  # noqa: E501

        :return: The envelope_uri of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._envelope_uri

    @envelope_uri.setter
    def envelope_uri(self, envelope_uri):
        """Sets the envelope_uri of this FolderItemV2.

        Contains a URI for an endpoint that you can use to retrieve the envelope or envelopes.  # noqa: E501

        :param envelope_uri: The envelope_uri of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._envelope_uri = envelope_uri

    @property
    def expire_date_time(self):
        """Gets the expire_date_time of this FolderItemV2.  # noqa: E501

        The date and time the envelope is set to expire.  # noqa: E501

        :return: The expire_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._expire_date_time

    @expire_date_time.setter
    def expire_date_time(self, expire_date_time):
        """Sets the expire_date_time of this FolderItemV2.

        The date and time the envelope is set to expire.  # noqa: E501

        :param expire_date_time: The expire_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._expire_date_time = expire_date_time

    @property
    def folder_id(self):
        """Gets the folder_id of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The folder_id of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this FolderItemV2.

          # noqa: E501

        :param folder_id: The folder_id of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._folder_id = folder_id

    @property
    def folder_uri(self):
        """Gets the folder_uri of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The folder_uri of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._folder_uri

    @folder_uri.setter
    def folder_uri(self, folder_uri):
        """Sets the folder_uri of this FolderItemV2.

          # noqa: E501

        :param folder_uri: The folder_uri of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._folder_uri = folder_uri

    @property
    def is21_cfr_part11(self):
        """Gets the is21_cfr_part11 of this FolderItemV2.  # noqa: E501

        When set to **true**, indicates that this module is enabled on the account.  # noqa: E501

        :return: The is21_cfr_part11 of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._is21_cfr_part11

    @is21_cfr_part11.setter
    def is21_cfr_part11(self, is21_cfr_part11):
        """Sets the is21_cfr_part11 of this FolderItemV2.

        When set to **true**, indicates that this module is enabled on the account.  # noqa: E501

        :param is21_cfr_part11: The is21_cfr_part11 of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._is21_cfr_part11 = is21_cfr_part11

    @property
    def last_modified_date_time(self):
        """Gets the last_modified_date_time of this FolderItemV2.  # noqa: E501

        The date and time the item was last modified.  # noqa: E501

        :return: The last_modified_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_date_time

    @last_modified_date_time.setter
    def last_modified_date_time(self, last_modified_date_time):
        """Sets the last_modified_date_time of this FolderItemV2.

        The date and time the item was last modified.  # noqa: E501

        :param last_modified_date_time: The last_modified_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._last_modified_date_time = last_modified_date_time

    @property
    def owner_name(self):
        """Gets the owner_name of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The owner_name of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this FolderItemV2.

          # noqa: E501

        :param owner_name: The owner_name of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

    @property
    def recipients(self):
        """Gets the recipients of this FolderItemV2.  # noqa: E501

        An array of powerform recipients.  # noqa: E501

        :return: The recipients of this FolderItemV2.  # noqa: E501
        :rtype: Recipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this FolderItemV2.

        An array of powerform recipients.  # noqa: E501

        :param recipients: The recipients of this FolderItemV2.  # noqa: E501
        :type: Recipients
        """

        self._recipients = recipients

    @property
    def recipients_uri(self):
        """Gets the recipients_uri of this FolderItemV2.  # noqa: E501

        Contains a URI for an endpoint that you can use to retrieve the recipients.  # noqa: E501

        :return: The recipients_uri of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._recipients_uri

    @recipients_uri.setter
    def recipients_uri(self, recipients_uri):
        """Sets the recipients_uri of this FolderItemV2.

        Contains a URI for an endpoint that you can use to retrieve the recipients.  # noqa: E501

        :param recipients_uri: The recipients_uri of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._recipients_uri = recipients_uri

    @property
    def sender_company(self):
        """Gets the sender_company of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The sender_company of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sender_company

    @sender_company.setter
    def sender_company(self, sender_company):
        """Sets the sender_company of this FolderItemV2.

          # noqa: E501

        :param sender_company: The sender_company of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sender_company = sender_company

    @property
    def sender_email(self):
        """Gets the sender_email of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The sender_email of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this FolderItemV2.

          # noqa: E501

        :param sender_email: The sender_email of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sender_email = sender_email

    @property
    def sender_name(self):
        """Gets the sender_name of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The sender_name of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sender_name

    @sender_name.setter
    def sender_name(self, sender_name):
        """Sets the sender_name of this FolderItemV2.

          # noqa: E501

        :param sender_name: The sender_name of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sender_name = sender_name

    @property
    def sender_user_id(self):
        """Gets the sender_user_id of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The sender_user_id of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sender_user_id

    @sender_user_id.setter
    def sender_user_id(self, sender_user_id):
        """Sets the sender_user_id of this FolderItemV2.

          # noqa: E501

        :param sender_user_id: The sender_user_id of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sender_user_id = sender_user_id

    @property
    def sent_date_time(self):
        """Gets the sent_date_time of this FolderItemV2.  # noqa: E501

        The date and time the envelope was sent.  # noqa: E501

        :return: The sent_date_time of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._sent_date_time

    @sent_date_time.setter
    def sent_date_time(self, sent_date_time):
        """Sets the sent_date_time of this FolderItemV2.

        The date and time the envelope was sent.  # noqa: E501

        :param sent_date_time: The sent_date_time of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._sent_date_time = sent_date_time

    @property
    def status(self):
        """Gets the status of this FolderItemV2.  # noqa: E501

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :return: The status of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FolderItemV2.

        Indicates the envelope status. Valid values are:  * sent - The envelope is sent to the recipients.  * created - The envelope is saved as a draft and can be modified and sent later.  # noqa: E501

        :param status: The status of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def subject(self):
        """Gets the subject of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The subject of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this FolderItemV2.

          # noqa: E501

        :param subject: The subject of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def template_id(self):
        """Gets the template_id of this FolderItemV2.  # noqa: E501

        The unique identifier of the template. If this is not provided, DocuSign will generate a value.   # noqa: E501

        :return: The template_id of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this FolderItemV2.

        The unique identifier of the template. If this is not provided, DocuSign will generate a value.   # noqa: E501

        :param template_id: The template_id of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def template_uri(self):
        """Gets the template_uri of this FolderItemV2.  # noqa: E501

          # noqa: E501

        :return: The template_uri of this FolderItemV2.  # noqa: E501
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        """Sets the template_uri of this FolderItemV2.

          # noqa: E501

        :param template_uri: The template_uri of this FolderItemV2.  # noqa: E501
        :type: str
        """

        self._template_uri = template_uri

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
        if issubclass(FolderItemV2, dict):
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
        if not isinstance(other, FolderItemV2):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderItemV2):
            return True

        return self.to_dict() != other.to_dict()
