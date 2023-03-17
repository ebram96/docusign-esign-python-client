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


class Recipients(object):
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
        'agents': 'list[Agent]',
        'carbon_copies': 'list[CarbonCopy]',
        'certified_deliveries': 'list[CertifiedDelivery]',
        'current_routing_order': 'str',
        'editors': 'list[Editor]',
        'error_details': 'ErrorDetails',
        'in_person_signers': 'list[InPersonSigner]',
        'intermediaries': 'list[Intermediary]',
        'notaries': 'list[NotaryRecipient]',
        'participants': 'list[Participant]',
        'recipient_count': 'str',
        'seals': 'list[SealSign]',
        'signers': 'list[Signer]',
        'witnesses': 'list[Witness]'
    }

    attribute_map = {
        'agents': 'agents',
        'carbon_copies': 'carbonCopies',
        'certified_deliveries': 'certifiedDeliveries',
        'current_routing_order': 'currentRoutingOrder',
        'editors': 'editors',
        'error_details': 'errorDetails',
        'in_person_signers': 'inPersonSigners',
        'intermediaries': 'intermediaries',
        'notaries': 'notaries',
        'participants': 'participants',
        'recipient_count': 'recipientCount',
        'seals': 'seals',
        'signers': 'signers',
        'witnesses': 'witnesses'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """Recipients - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._agents = None
        self._carbon_copies = None
        self._certified_deliveries = None
        self._current_routing_order = None
        self._editors = None
        self._error_details = None
        self._in_person_signers = None
        self._intermediaries = None
        self._notaries = None
        self._participants = None
        self._recipient_count = None
        self._seals = None
        self._signers = None
        self._witnesses = None
        self.discriminator = None

        setattr(self, "_{}".format('agents'), kwargs.get('agents', None))
        setattr(self, "_{}".format('carbon_copies'), kwargs.get('carbon_copies', None))
        setattr(self, "_{}".format('certified_deliveries'), kwargs.get('certified_deliveries', None))
        setattr(self, "_{}".format('current_routing_order'), kwargs.get('current_routing_order', None))
        setattr(self, "_{}".format('editors'), kwargs.get('editors', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('in_person_signers'), kwargs.get('in_person_signers', None))
        setattr(self, "_{}".format('intermediaries'), kwargs.get('intermediaries', None))
        setattr(self, "_{}".format('notaries'), kwargs.get('notaries', None))
        setattr(self, "_{}".format('participants'), kwargs.get('participants', None))
        setattr(self, "_{}".format('recipient_count'), kwargs.get('recipient_count', None))
        setattr(self, "_{}".format('seals'), kwargs.get('seals', None))
        setattr(self, "_{}".format('signers'), kwargs.get('signers', None))
        setattr(self, "_{}".format('witnesses'), kwargs.get('witnesses', None))

    @property
    def agents(self):
        """Gets the agents of this Recipients.  # noqa: E501

        A complex type defining the management and access rights of a recipient assigned assigned as an agent on the document.  # noqa: E501

        :return: The agents of this Recipients.  # noqa: E501
        :rtype: list[Agent]
        """
        return self._agents

    @agents.setter
    def agents(self, agents):
        """Sets the agents of this Recipients.

        A complex type defining the management and access rights of a recipient assigned assigned as an agent on the document.  # noqa: E501

        :param agents: The agents of this Recipients.  # noqa: E501
        :type: list[Agent]
        """

        self._agents = agents

    @property
    def carbon_copies(self):
        """Gets the carbon_copies of this Recipients.  # noqa: E501

        A complex type containing information about recipients who should receive a copy of the envelope, but does not need to sign it.  # noqa: E501

        :return: The carbon_copies of this Recipients.  # noqa: E501
        :rtype: list[CarbonCopy]
        """
        return self._carbon_copies

    @carbon_copies.setter
    def carbon_copies(self, carbon_copies):
        """Sets the carbon_copies of this Recipients.

        A complex type containing information about recipients who should receive a copy of the envelope, but does not need to sign it.  # noqa: E501

        :param carbon_copies: The carbon_copies of this Recipients.  # noqa: E501
        :type: list[CarbonCopy]
        """

        self._carbon_copies = carbon_copies

    @property
    def certified_deliveries(self):
        """Gets the certified_deliveries of this Recipients.  # noqa: E501

        A complex type containing information on a recipient the must receive the completed documents for the envelope to be completed, but the recipient does not need to sign, initial, date, or add information to any of the documents.  # noqa: E501

        :return: The certified_deliveries of this Recipients.  # noqa: E501
        :rtype: list[CertifiedDelivery]
        """
        return self._certified_deliveries

    @certified_deliveries.setter
    def certified_deliveries(self, certified_deliveries):
        """Sets the certified_deliveries of this Recipients.

        A complex type containing information on a recipient the must receive the completed documents for the envelope to be completed, but the recipient does not need to sign, initial, date, or add information to any of the documents.  # noqa: E501

        :param certified_deliveries: The certified_deliveries of this Recipients.  # noqa: E501
        :type: list[CertifiedDelivery]
        """

        self._certified_deliveries = certified_deliveries

    @property
    def current_routing_order(self):
        """Gets the current_routing_order of this Recipients.  # noqa: E501

          # noqa: E501

        :return: The current_routing_order of this Recipients.  # noqa: E501
        :rtype: str
        """
        return self._current_routing_order

    @current_routing_order.setter
    def current_routing_order(self, current_routing_order):
        """Sets the current_routing_order of this Recipients.

          # noqa: E501

        :param current_routing_order: The current_routing_order of this Recipients.  # noqa: E501
        :type: str
        """

        self._current_routing_order = current_routing_order

    @property
    def editors(self):
        """Gets the editors of this Recipients.  # noqa: E501

        A complex type defining the management and access rights of a recipient assigned assigned as an editor on the document.  # noqa: E501

        :return: The editors of this Recipients.  # noqa: E501
        :rtype: list[Editor]
        """
        return self._editors

    @editors.setter
    def editors(self, editors):
        """Sets the editors of this Recipients.

        A complex type defining the management and access rights of a recipient assigned assigned as an editor on the document.  # noqa: E501

        :param editors: The editors of this Recipients.  # noqa: E501
        :type: list[Editor]
        """

        self._editors = editors

    @property
    def error_details(self):
        """Gets the error_details of this Recipients.  # noqa: E501

        Array or errors.  # noqa: E501

        :return: The error_details of this Recipients.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this Recipients.

        Array or errors.  # noqa: E501

        :param error_details: The error_details of this Recipients.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def in_person_signers(self):
        """Gets the in_person_signers of this Recipients.  # noqa: E501

        Specifies a signer that is in the same physical location as a DocuSign user who will act as a Signing Host for the transaction. The recipient added is the Signing Host and new separate Signer Name field appears after Sign in person is selected.  # noqa: E501

        :return: The in_person_signers of this Recipients.  # noqa: E501
        :rtype: list[InPersonSigner]
        """
        return self._in_person_signers

    @in_person_signers.setter
    def in_person_signers(self, in_person_signers):
        """Sets the in_person_signers of this Recipients.

        Specifies a signer that is in the same physical location as a DocuSign user who will act as a Signing Host for the transaction. The recipient added is the Signing Host and new separate Signer Name field appears after Sign in person is selected.  # noqa: E501

        :param in_person_signers: The in_person_signers of this Recipients.  # noqa: E501
        :type: list[InPersonSigner]
        """

        self._in_person_signers = in_person_signers

    @property
    def intermediaries(self):
        """Gets the intermediaries of this Recipients.  # noqa: E501

        Identifies a recipient that can, but is not required to, add name and email information for recipients at the same or subsequent level in the routing order (until subsequent Agents, Editors or Intermediaries recipient types are added).  # noqa: E501

        :return: The intermediaries of this Recipients.  # noqa: E501
        :rtype: list[Intermediary]
        """
        return self._intermediaries

    @intermediaries.setter
    def intermediaries(self, intermediaries):
        """Sets the intermediaries of this Recipients.

        Identifies a recipient that can, but is not required to, add name and email information for recipients at the same or subsequent level in the routing order (until subsequent Agents, Editors or Intermediaries recipient types are added).  # noqa: E501

        :param intermediaries: The intermediaries of this Recipients.  # noqa: E501
        :type: list[Intermediary]
        """

        self._intermediaries = intermediaries

    @property
    def notaries(self):
        """Gets the notaries of this Recipients.  # noqa: E501

          # noqa: E501

        :return: The notaries of this Recipients.  # noqa: E501
        :rtype: list[NotaryRecipient]
        """
        return self._notaries

    @notaries.setter
    def notaries(self, notaries):
        """Sets the notaries of this Recipients.

          # noqa: E501

        :param notaries: The notaries of this Recipients.  # noqa: E501
        :type: list[NotaryRecipient]
        """

        self._notaries = notaries

    @property
    def participants(self):
        """Gets the participants of this Recipients.  # noqa: E501

          # noqa: E501

        :return: The participants of this Recipients.  # noqa: E501
        :rtype: list[Participant]
        """
        return self._participants

    @participants.setter
    def participants(self, participants):
        """Sets the participants of this Recipients.

          # noqa: E501

        :param participants: The participants of this Recipients.  # noqa: E501
        :type: list[Participant]
        """

        self._participants = participants

    @property
    def recipient_count(self):
        """Gets the recipient_count of this Recipients.  # noqa: E501

          # noqa: E501

        :return: The recipient_count of this Recipients.  # noqa: E501
        :rtype: str
        """
        return self._recipient_count

    @recipient_count.setter
    def recipient_count(self, recipient_count):
        """Sets the recipient_count of this Recipients.

          # noqa: E501

        :param recipient_count: The recipient_count of this Recipients.  # noqa: E501
        :type: str
        """

        self._recipient_count = recipient_count

    @property
    def seals(self):
        """Gets the seals of this Recipients.  # noqa: E501

          # noqa: E501

        :return: The seals of this Recipients.  # noqa: E501
        :rtype: list[SealSign]
        """
        return self._seals

    @seals.setter
    def seals(self, seals):
        """Sets the seals of this Recipients.

          # noqa: E501

        :param seals: The seals of this Recipients.  # noqa: E501
        :type: list[SealSign]
        """

        self._seals = seals

    @property
    def signers(self):
        """Gets the signers of this Recipients.  # noqa: E501

        A complex type containing information about the Signer recipient.  # noqa: E501

        :return: The signers of this Recipients.  # noqa: E501
        :rtype: list[Signer]
        """
        return self._signers

    @signers.setter
    def signers(self, signers):
        """Sets the signers of this Recipients.

        A complex type containing information about the Signer recipient.  # noqa: E501

        :param signers: The signers of this Recipients.  # noqa: E501
        :type: list[Signer]
        """

        self._signers = signers

    @property
    def witnesses(self):
        """Gets the witnesses of this Recipients.  # noqa: E501

          # noqa: E501

        :return: The witnesses of this Recipients.  # noqa: E501
        :rtype: list[Witness]
        """
        return self._witnesses

    @witnesses.setter
    def witnesses(self, witnesses):
        """Sets the witnesses of this Recipients.

          # noqa: E501

        :param witnesses: The witnesses of this Recipients.  # noqa: E501
        :type: list[Witness]
        """

        self._witnesses = witnesses

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
        if issubclass(Recipients, dict):
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
        if not isinstance(other, Recipients):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Recipients):
            return True

        return self.to_dict() != other.to_dict()
