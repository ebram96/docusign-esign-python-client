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


class EnvelopePublishTransaction(object):
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
        'apply_connect_settings': 'str',
        'envelope_count': 'str',
        'envelope_level_error_rollups': 'list[EnvelopePublishTransactionErrorRollup]',
        'envelope_publish_transaction_id': 'str',
        'error_count': 'str',
        'file_level_errors': 'list[str]',
        'no_action_required_envelope_count': 'str',
        'processed_envelope_count': 'str',
        'processing_status': 'str',
        'results_uri': 'str',
        'submission_date': 'str',
        'submitted_by_user_info': 'UserInfo',
        'submitted_for_publishing_envelope_count': 'str'
    }

    attribute_map = {
        'apply_connect_settings': 'applyConnectSettings',
        'envelope_count': 'envelopeCount',
        'envelope_level_error_rollups': 'envelopeLevelErrorRollups',
        'envelope_publish_transaction_id': 'envelopePublishTransactionId',
        'error_count': 'errorCount',
        'file_level_errors': 'fileLevelErrors',
        'no_action_required_envelope_count': 'noActionRequiredEnvelopeCount',
        'processed_envelope_count': 'processedEnvelopeCount',
        'processing_status': 'processingStatus',
        'results_uri': 'resultsUri',
        'submission_date': 'submissionDate',
        'submitted_by_user_info': 'submittedByUserInfo',
        'submitted_for_publishing_envelope_count': 'submittedForPublishingEnvelopeCount'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """EnvelopePublishTransaction - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._apply_connect_settings = None
        self._envelope_count = None
        self._envelope_level_error_rollups = None
        self._envelope_publish_transaction_id = None
        self._error_count = None
        self._file_level_errors = None
        self._no_action_required_envelope_count = None
        self._processed_envelope_count = None
        self._processing_status = None
        self._results_uri = None
        self._submission_date = None
        self._submitted_by_user_info = None
        self._submitted_for_publishing_envelope_count = None
        self.discriminator = None

        setattr(self, "_{}".format('apply_connect_settings'), kwargs.get('apply_connect_settings', None))
        setattr(self, "_{}".format('envelope_count'), kwargs.get('envelope_count', None))
        setattr(self, "_{}".format('envelope_level_error_rollups'), kwargs.get('envelope_level_error_rollups', None))
        setattr(self, "_{}".format('envelope_publish_transaction_id'), kwargs.get('envelope_publish_transaction_id', None))
        setattr(self, "_{}".format('error_count'), kwargs.get('error_count', None))
        setattr(self, "_{}".format('file_level_errors'), kwargs.get('file_level_errors', None))
        setattr(self, "_{}".format('no_action_required_envelope_count'), kwargs.get('no_action_required_envelope_count', None))
        setattr(self, "_{}".format('processed_envelope_count'), kwargs.get('processed_envelope_count', None))
        setattr(self, "_{}".format('processing_status'), kwargs.get('processing_status', None))
        setattr(self, "_{}".format('results_uri'), kwargs.get('results_uri', None))
        setattr(self, "_{}".format('submission_date'), kwargs.get('submission_date', None))
        setattr(self, "_{}".format('submitted_by_user_info'), kwargs.get('submitted_by_user_info', None))
        setattr(self, "_{}".format('submitted_for_publishing_envelope_count'), kwargs.get('submitted_for_publishing_envelope_count', None))

    @property
    def apply_connect_settings(self):
        """Gets the apply_connect_settings of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The apply_connect_settings of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._apply_connect_settings

    @apply_connect_settings.setter
    def apply_connect_settings(self, apply_connect_settings):
        """Sets the apply_connect_settings of this EnvelopePublishTransaction.

          # noqa: E501

        :param apply_connect_settings: The apply_connect_settings of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._apply_connect_settings = apply_connect_settings

    @property
    def envelope_count(self):
        """Gets the envelope_count of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The envelope_count of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._envelope_count

    @envelope_count.setter
    def envelope_count(self, envelope_count):
        """Sets the envelope_count of this EnvelopePublishTransaction.

          # noqa: E501

        :param envelope_count: The envelope_count of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._envelope_count = envelope_count

    @property
    def envelope_level_error_rollups(self):
        """Gets the envelope_level_error_rollups of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The envelope_level_error_rollups of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: list[EnvelopePublishTransactionErrorRollup]
        """
        return self._envelope_level_error_rollups

    @envelope_level_error_rollups.setter
    def envelope_level_error_rollups(self, envelope_level_error_rollups):
        """Sets the envelope_level_error_rollups of this EnvelopePublishTransaction.

          # noqa: E501

        :param envelope_level_error_rollups: The envelope_level_error_rollups of this EnvelopePublishTransaction.  # noqa: E501
        :type: list[EnvelopePublishTransactionErrorRollup]
        """

        self._envelope_level_error_rollups = envelope_level_error_rollups

    @property
    def envelope_publish_transaction_id(self):
        """Gets the envelope_publish_transaction_id of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The envelope_publish_transaction_id of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._envelope_publish_transaction_id

    @envelope_publish_transaction_id.setter
    def envelope_publish_transaction_id(self, envelope_publish_transaction_id):
        """Sets the envelope_publish_transaction_id of this EnvelopePublishTransaction.

          # noqa: E501

        :param envelope_publish_transaction_id: The envelope_publish_transaction_id of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._envelope_publish_transaction_id = envelope_publish_transaction_id

    @property
    def error_count(self):
        """Gets the error_count of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The error_count of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """Sets the error_count of this EnvelopePublishTransaction.

          # noqa: E501

        :param error_count: The error_count of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._error_count = error_count

    @property
    def file_level_errors(self):
        """Gets the file_level_errors of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The file_level_errors of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_level_errors

    @file_level_errors.setter
    def file_level_errors(self, file_level_errors):
        """Sets the file_level_errors of this EnvelopePublishTransaction.

          # noqa: E501

        :param file_level_errors: The file_level_errors of this EnvelopePublishTransaction.  # noqa: E501
        :type: list[str]
        """

        self._file_level_errors = file_level_errors

    @property
    def no_action_required_envelope_count(self):
        """Gets the no_action_required_envelope_count of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The no_action_required_envelope_count of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._no_action_required_envelope_count

    @no_action_required_envelope_count.setter
    def no_action_required_envelope_count(self, no_action_required_envelope_count):
        """Sets the no_action_required_envelope_count of this EnvelopePublishTransaction.

          # noqa: E501

        :param no_action_required_envelope_count: The no_action_required_envelope_count of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._no_action_required_envelope_count = no_action_required_envelope_count

    @property
    def processed_envelope_count(self):
        """Gets the processed_envelope_count of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The processed_envelope_count of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._processed_envelope_count

    @processed_envelope_count.setter
    def processed_envelope_count(self, processed_envelope_count):
        """Sets the processed_envelope_count of this EnvelopePublishTransaction.

          # noqa: E501

        :param processed_envelope_count: The processed_envelope_count of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._processed_envelope_count = processed_envelope_count

    @property
    def processing_status(self):
        """Gets the processing_status of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The processing_status of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._processing_status

    @processing_status.setter
    def processing_status(self, processing_status):
        """Sets the processing_status of this EnvelopePublishTransaction.

          # noqa: E501

        :param processing_status: The processing_status of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._processing_status = processing_status

    @property
    def results_uri(self):
        """Gets the results_uri of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The results_uri of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._results_uri

    @results_uri.setter
    def results_uri(self, results_uri):
        """Sets the results_uri of this EnvelopePublishTransaction.

          # noqa: E501

        :param results_uri: The results_uri of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._results_uri = results_uri

    @property
    def submission_date(self):
        """Gets the submission_date of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The submission_date of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date):
        """Sets the submission_date of this EnvelopePublishTransaction.

          # noqa: E501

        :param submission_date: The submission_date of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._submission_date = submission_date

    @property
    def submitted_by_user_info(self):
        """Gets the submitted_by_user_info of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The submitted_by_user_info of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: UserInfo
        """
        return self._submitted_by_user_info

    @submitted_by_user_info.setter
    def submitted_by_user_info(self, submitted_by_user_info):
        """Sets the submitted_by_user_info of this EnvelopePublishTransaction.

          # noqa: E501

        :param submitted_by_user_info: The submitted_by_user_info of this EnvelopePublishTransaction.  # noqa: E501
        :type: UserInfo
        """

        self._submitted_by_user_info = submitted_by_user_info

    @property
    def submitted_for_publishing_envelope_count(self):
        """Gets the submitted_for_publishing_envelope_count of this EnvelopePublishTransaction.  # noqa: E501

          # noqa: E501

        :return: The submitted_for_publishing_envelope_count of this EnvelopePublishTransaction.  # noqa: E501
        :rtype: str
        """
        return self._submitted_for_publishing_envelope_count

    @submitted_for_publishing_envelope_count.setter
    def submitted_for_publishing_envelope_count(self, submitted_for_publishing_envelope_count):
        """Sets the submitted_for_publishing_envelope_count of this EnvelopePublishTransaction.

          # noqa: E501

        :param submitted_for_publishing_envelope_count: The submitted_for_publishing_envelope_count of this EnvelopePublishTransaction.  # noqa: E501
        :type: str
        """

        self._submitted_for_publishing_envelope_count = submitted_for_publishing_envelope_count

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
        if issubclass(EnvelopePublishTransaction, dict):
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
        if not isinstance(other, EnvelopePublishTransaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvelopePublishTransaction):
            return True

        return self.to_dict() != other.to_dict()
