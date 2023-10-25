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


class Document(object):
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
        'apply_anchor_tabs': 'str',
        'assign_tabs_to_recipient_id': 'str',
        'authoritative_copy': 'bool',
        'display': 'str',
        'doc_gen_form_fields': 'list[DocGenFormField]',
        'document_base64': 'str',
        'document_fields': 'list[NameValue]',
        'document_id': 'str',
        'encrypted_with_key_manager': 'str',
        'file_extension': 'str',
        'file_format_hint': 'str',
        'html_definition': 'DocumentHtmlDefinition',
        'include_in_download': 'str',
        'is_doc_gen_document': 'str',
        'match_boxes': 'list[MatchBox]',
        'name': 'str',
        'order': 'str',
        'pages': 'str',
        'password': 'str',
        'pdf_form_field_option': 'str',
        'remote_url': 'str',
        'signer_must_acknowledge': 'str',
        'signer_must_acknowledge_use_account_default': 'bool',
        'tabs': 'Tabs',
        'template_locked': 'str',
        'template_required': 'str',
        'transform_pdf_fields': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'apply_anchor_tabs': 'applyAnchorTabs',
        'assign_tabs_to_recipient_id': 'assignTabsToRecipientId',
        'authoritative_copy': 'authoritativeCopy',
        'display': 'display',
        'doc_gen_form_fields': 'docGenFormFields',
        'document_base64': 'documentBase64',
        'document_fields': 'documentFields',
        'document_id': 'documentId',
        'encrypted_with_key_manager': 'encryptedWithKeyManager',
        'file_extension': 'fileExtension',
        'file_format_hint': 'fileFormatHint',
        'html_definition': 'htmlDefinition',
        'include_in_download': 'includeInDownload',
        'is_doc_gen_document': 'isDocGenDocument',
        'match_boxes': 'matchBoxes',
        'name': 'name',
        'order': 'order',
        'pages': 'pages',
        'password': 'password',
        'pdf_form_field_option': 'pdfFormFieldOption',
        'remote_url': 'remoteUrl',
        'signer_must_acknowledge': 'signerMustAcknowledge',
        'signer_must_acknowledge_use_account_default': 'signerMustAcknowledgeUseAccountDefault',
        'tabs': 'tabs',
        'template_locked': 'templateLocked',
        'template_required': 'templateRequired',
        'transform_pdf_fields': 'transformPdfFields',
        'uri': 'uri'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """Document - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._apply_anchor_tabs = None
        self._assign_tabs_to_recipient_id = None
        self._authoritative_copy = None
        self._display = None
        self._doc_gen_form_fields = None
        self._document_base64 = None
        self._document_fields = None
        self._document_id = None
        self._encrypted_with_key_manager = None
        self._file_extension = None
        self._file_format_hint = None
        self._html_definition = None
        self._include_in_download = None
        self._is_doc_gen_document = None
        self._match_boxes = None
        self._name = None
        self._order = None
        self._pages = None
        self._password = None
        self._pdf_form_field_option = None
        self._remote_url = None
        self._signer_must_acknowledge = None
        self._signer_must_acknowledge_use_account_default = None
        self._tabs = None
        self._template_locked = None
        self._template_required = None
        self._transform_pdf_fields = None
        self._uri = None
        self.discriminator = None

        setattr(self, "_{}".format('apply_anchor_tabs'), kwargs.get('apply_anchor_tabs', None))
        setattr(self, "_{}".format('assign_tabs_to_recipient_id'), kwargs.get('assign_tabs_to_recipient_id', None))
        setattr(self, "_{}".format('authoritative_copy'), kwargs.get('authoritative_copy', None))
        setattr(self, "_{}".format('display'), kwargs.get('display', None))
        setattr(self, "_{}".format('doc_gen_form_fields'), kwargs.get('doc_gen_form_fields', None))
        setattr(self, "_{}".format('document_base64'), kwargs.get('document_base64', None))
        setattr(self, "_{}".format('document_fields'), kwargs.get('document_fields', None))
        setattr(self, "_{}".format('document_id'), kwargs.get('document_id', None))
        setattr(self, "_{}".format('encrypted_with_key_manager'), kwargs.get('encrypted_with_key_manager', None))
        setattr(self, "_{}".format('file_extension'), kwargs.get('file_extension', None))
        setattr(self, "_{}".format('file_format_hint'), kwargs.get('file_format_hint', None))
        setattr(self, "_{}".format('html_definition'), kwargs.get('html_definition', None))
        setattr(self, "_{}".format('include_in_download'), kwargs.get('include_in_download', None))
        setattr(self, "_{}".format('is_doc_gen_document'), kwargs.get('is_doc_gen_document', None))
        setattr(self, "_{}".format('match_boxes'), kwargs.get('match_boxes', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))
        setattr(self, "_{}".format('order'), kwargs.get('order', None))
        setattr(self, "_{}".format('pages'), kwargs.get('pages', None))
        setattr(self, "_{}".format('password'), kwargs.get('password', None))
        setattr(self, "_{}".format('pdf_form_field_option'), kwargs.get('pdf_form_field_option', None))
        setattr(self, "_{}".format('remote_url'), kwargs.get('remote_url', None))
        setattr(self, "_{}".format('signer_must_acknowledge'), kwargs.get('signer_must_acknowledge', None))
        setattr(self, "_{}".format('signer_must_acknowledge_use_account_default'), kwargs.get('signer_must_acknowledge_use_account_default', None))
        setattr(self, "_{}".format('tabs'), kwargs.get('tabs', None))
        setattr(self, "_{}".format('template_locked'), kwargs.get('template_locked', None))
        setattr(self, "_{}".format('template_required'), kwargs.get('template_required', None))
        setattr(self, "_{}".format('transform_pdf_fields'), kwargs.get('transform_pdf_fields', None))
        setattr(self, "_{}".format('uri'), kwargs.get('uri', None))

    @property
    def apply_anchor_tabs(self):
        """Gets the apply_anchor_tabs of this Document.  # noqa: E501

        Reserved: TBD  # noqa: E501

        :return: The apply_anchor_tabs of this Document.  # noqa: E501
        :rtype: str
        """
        return self._apply_anchor_tabs

    @apply_anchor_tabs.setter
    def apply_anchor_tabs(self, apply_anchor_tabs):
        """Sets the apply_anchor_tabs of this Document.

        Reserved: TBD  # noqa: E501

        :param apply_anchor_tabs: The apply_anchor_tabs of this Document.  # noqa: E501
        :type: str
        """

        self._apply_anchor_tabs = apply_anchor_tabs

    @property
    def assign_tabs_to_recipient_id(self):
        """Gets the assign_tabs_to_recipient_id of this Document.  # noqa: E501

          # noqa: E501

        :return: The assign_tabs_to_recipient_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._assign_tabs_to_recipient_id

    @assign_tabs_to_recipient_id.setter
    def assign_tabs_to_recipient_id(self, assign_tabs_to_recipient_id):
        """Sets the assign_tabs_to_recipient_id of this Document.

          # noqa: E501

        :param assign_tabs_to_recipient_id: The assign_tabs_to_recipient_id of this Document.  # noqa: E501
        :type: str
        """

        self._assign_tabs_to_recipient_id = assign_tabs_to_recipient_id

    @property
    def authoritative_copy(self):
        """Gets the authoritative_copy of this Document.  # noqa: E501

        Specifies the Authoritative copy feature. If set to true the Authoritative copy feature is enabled.  # noqa: E501

        :return: The authoritative_copy of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._authoritative_copy

    @authoritative_copy.setter
    def authoritative_copy(self, authoritative_copy):
        """Sets the authoritative_copy of this Document.

        Specifies the Authoritative copy feature. If set to true the Authoritative copy feature is enabled.  # noqa: E501

        :param authoritative_copy: The authoritative_copy of this Document.  # noqa: E501
        :type: bool
        """

        self._authoritative_copy = authoritative_copy

    @property
    def display(self):
        """Gets the display of this Document.  # noqa: E501

          # noqa: E501

        :return: The display of this Document.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this Document.

          # noqa: E501

        :param display: The display of this Document.  # noqa: E501
        :type: str
        """

        self._display = display

    @property
    def doc_gen_form_fields(self):
        """Gets the doc_gen_form_fields of this Document.  # noqa: E501

          # noqa: E501

        :return: The doc_gen_form_fields of this Document.  # noqa: E501
        :rtype: list[DocGenFormField]
        """
        return self._doc_gen_form_fields

    @doc_gen_form_fields.setter
    def doc_gen_form_fields(self, doc_gen_form_fields):
        """Sets the doc_gen_form_fields of this Document.

          # noqa: E501

        :param doc_gen_form_fields: The doc_gen_form_fields of this Document.  # noqa: E501
        :type: list[DocGenFormField]
        """

        self._doc_gen_form_fields = doc_gen_form_fields

    @property
    def document_base64(self):
        """Gets the document_base64 of this Document.  # noqa: E501

        The document's bytes. This field can be used to include a base64 version of the document bytes within an envelope definition instead of sending the document using a multi-part HTTP request. The maximum document size is smaller if this field is used due to the overhead of the base64 encoding.  # noqa: E501

        :return: The document_base64 of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document_base64

    @document_base64.setter
    def document_base64(self, document_base64):
        """Sets the document_base64 of this Document.

        The document's bytes. This field can be used to include a base64 version of the document bytes within an envelope definition instead of sending the document using a multi-part HTTP request. The maximum document size is smaller if this field is used due to the overhead of the base64 encoding.  # noqa: E501

        :param document_base64: The document_base64 of this Document.  # noqa: E501
        :type: str
        """

        self._document_base64 = document_base64

    @property
    def document_fields(self):
        """Gets the document_fields of this Document.  # noqa: E501

          # noqa: E501

        :return: The document_fields of this Document.  # noqa: E501
        :rtype: list[NameValue]
        """
        return self._document_fields

    @document_fields.setter
    def document_fields(self, document_fields):
        """Sets the document_fields of this Document.

          # noqa: E501

        :param document_fields: The document_fields of this Document.  # noqa: E501
        :type: list[NameValue]
        """

        self._document_fields = document_fields

    @property
    def document_id(self):
        """Gets the document_id of this Document.  # noqa: E501

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :return: The document_id of this Document.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Document.

        Specifies the document ID number that the tab is placed on. This must refer to an existing Document's ID attribute.  # noqa: E501

        :param document_id: The document_id of this Document.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def encrypted_with_key_manager(self):
        """Gets the encrypted_with_key_manager of this Document.  # noqa: E501

        When set to **true**, the document is been already encrypted by the sender for use with the DocuSign Key Manager Security Appliance.    # noqa: E501

        :return: The encrypted_with_key_manager of this Document.  # noqa: E501
        :rtype: str
        """
        return self._encrypted_with_key_manager

    @encrypted_with_key_manager.setter
    def encrypted_with_key_manager(self, encrypted_with_key_manager):
        """Sets the encrypted_with_key_manager of this Document.

        When set to **true**, the document is been already encrypted by the sender for use with the DocuSign Key Manager Security Appliance.    # noqa: E501

        :param encrypted_with_key_manager: The encrypted_with_key_manager of this Document.  # noqa: E501
        :type: str
        """

        self._encrypted_with_key_manager = encrypted_with_key_manager

    @property
    def file_extension(self):
        """Gets the file_extension of this Document.  # noqa: E501

        The file extension type of the document. If the document is not a PDF it is converted to a PDF.    # noqa: E501

        :return: The file_extension of this Document.  # noqa: E501
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Sets the file_extension of this Document.

        The file extension type of the document. If the document is not a PDF it is converted to a PDF.    # noqa: E501

        :param file_extension: The file_extension of this Document.  # noqa: E501
        :type: str
        """

        self._file_extension = file_extension

    @property
    def file_format_hint(self):
        """Gets the file_format_hint of this Document.  # noqa: E501

          # noqa: E501

        :return: The file_format_hint of this Document.  # noqa: E501
        :rtype: str
        """
        return self._file_format_hint

    @file_format_hint.setter
    def file_format_hint(self, file_format_hint):
        """Sets the file_format_hint of this Document.

          # noqa: E501

        :param file_format_hint: The file_format_hint of this Document.  # noqa: E501
        :type: str
        """

        self._file_format_hint = file_format_hint

    @property
    def html_definition(self):
        """Gets the html_definition of this Document.  # noqa: E501

        Defines how to generate the responsive-formatted HTML for the document. See [Responsive signing](/docs/esign-rest-api/esign101/concepts/responsive/) in the [eSignature concepts guide](/docs/esign-rest-api/esign101/concepts/).  # noqa: E501

        :return: The html_definition of this Document.  # noqa: E501
        :rtype: DocumentHtmlDefinition
        """
        return self._html_definition

    @html_definition.setter
    def html_definition(self, html_definition):
        """Sets the html_definition of this Document.

        Defines how to generate the responsive-formatted HTML for the document. See [Responsive signing](/docs/esign-rest-api/esign101/concepts/responsive/) in the [eSignature concepts guide](/docs/esign-rest-api/esign101/concepts/).  # noqa: E501

        :param html_definition: The html_definition of this Document.  # noqa: E501
        :type: DocumentHtmlDefinition
        """

        self._html_definition = html_definition

    @property
    def include_in_download(self):
        """Gets the include_in_download of this Document.  # noqa: E501

          # noqa: E501

        :return: The include_in_download of this Document.  # noqa: E501
        :rtype: str
        """
        return self._include_in_download

    @include_in_download.setter
    def include_in_download(self, include_in_download):
        """Sets the include_in_download of this Document.

          # noqa: E501

        :param include_in_download: The include_in_download of this Document.  # noqa: E501
        :type: str
        """

        self._include_in_download = include_in_download

    @property
    def is_doc_gen_document(self):
        """Gets the is_doc_gen_document of this Document.  # noqa: E501

          # noqa: E501

        :return: The is_doc_gen_document of this Document.  # noqa: E501
        :rtype: str
        """
        return self._is_doc_gen_document

    @is_doc_gen_document.setter
    def is_doc_gen_document(self, is_doc_gen_document):
        """Sets the is_doc_gen_document of this Document.

          # noqa: E501

        :param is_doc_gen_document: The is_doc_gen_document of this Document.  # noqa: E501
        :type: str
        """

        self._is_doc_gen_document = is_doc_gen_document

    @property
    def match_boxes(self):
        """Gets the match_boxes of this Document.  # noqa: E501

        Matchboxes define areas in a document for document matching when you are creating envelopes. They are only used when you upload and edit a template.   A matchbox consists of 5 elements:  * pageNumber - The document page number  on which the matchbox will appear.  * xPosition - The x position of the matchbox on a page.  * yPosition - The y position of the matchbox on a page. * width - The width of the matchbox.  * height - The height of the matchbox.    # noqa: E501

        :return: The match_boxes of this Document.  # noqa: E501
        :rtype: list[MatchBox]
        """
        return self._match_boxes

    @match_boxes.setter
    def match_boxes(self, match_boxes):
        """Sets the match_boxes of this Document.

        Matchboxes define areas in a document for document matching when you are creating envelopes. They are only used when you upload and edit a template.   A matchbox consists of 5 elements:  * pageNumber - The document page number  on which the matchbox will appear.  * xPosition - The x position of the matchbox on a page.  * yPosition - The y position of the matchbox on a page. * width - The width of the matchbox.  * height - The height of the matchbox.    # noqa: E501

        :param match_boxes: The match_boxes of this Document.  # noqa: E501
        :type: list[MatchBox]
        """

        self._match_boxes = match_boxes

    @property
    def name(self):
        """Gets the name of this Document.  # noqa: E501

          # noqa: E501

        :return: The name of this Document.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Document.

          # noqa: E501

        :param name: The name of this Document.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order(self):
        """Gets the order of this Document.  # noqa: E501

          # noqa: E501

        :return: The order of this Document.  # noqa: E501
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Document.

          # noqa: E501

        :param order: The order of this Document.  # noqa: E501
        :type: str
        """

        self._order = order

    @property
    def pages(self):
        """Gets the pages of this Document.  # noqa: E501

          # noqa: E501

        :return: The pages of this Document.  # noqa: E501
        :rtype: str
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this Document.

          # noqa: E501

        :param pages: The pages of this Document.  # noqa: E501
        :type: str
        """

        self._pages = pages

    @property
    def password(self):
        """Gets the password of this Document.  # noqa: E501

          # noqa: E501

        :return: The password of this Document.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Document.

          # noqa: E501

        :param password: The password of this Document.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def pdf_form_field_option(self):
        """Gets the pdf_form_field_option of this Document.  # noqa: E501

          # noqa: E501

        :return: The pdf_form_field_option of this Document.  # noqa: E501
        :rtype: str
        """
        return self._pdf_form_field_option

    @pdf_form_field_option.setter
    def pdf_form_field_option(self, pdf_form_field_option):
        """Sets the pdf_form_field_option of this Document.

          # noqa: E501

        :param pdf_form_field_option: The pdf_form_field_option of this Document.  # noqa: E501
        :type: str
        """

        self._pdf_form_field_option = pdf_form_field_option

    @property
    def remote_url(self):
        """Gets the remote_url of this Document.  # noqa: E501

        The file id from the cloud storage service where the document is located. This information is returned using [ML:GET /folders] or [ML:/folders/{folderid}].   # noqa: E501

        :return: The remote_url of this Document.  # noqa: E501
        :rtype: str
        """
        return self._remote_url

    @remote_url.setter
    def remote_url(self, remote_url):
        """Sets the remote_url of this Document.

        The file id from the cloud storage service where the document is located. This information is returned using [ML:GET /folders] or [ML:/folders/{folderid}].   # noqa: E501

        :param remote_url: The remote_url of this Document.  # noqa: E501
        :type: str
        """

        self._remote_url = remote_url

    @property
    def signer_must_acknowledge(self):
        """Gets the signer_must_acknowledge of this Document.  # noqa: E501

          # noqa: E501

        :return: The signer_must_acknowledge of this Document.  # noqa: E501
        :rtype: str
        """
        return self._signer_must_acknowledge

    @signer_must_acknowledge.setter
    def signer_must_acknowledge(self, signer_must_acknowledge):
        """Sets the signer_must_acknowledge of this Document.

          # noqa: E501

        :param signer_must_acknowledge: The signer_must_acknowledge of this Document.  # noqa: E501
        :type: str
        """

        self._signer_must_acknowledge = signer_must_acknowledge

    @property
    def signer_must_acknowledge_use_account_default(self):
        """Gets the signer_must_acknowledge_use_account_default of this Document.  # noqa: E501

          # noqa: E501

        :return: The signer_must_acknowledge_use_account_default of this Document.  # noqa: E501
        :rtype: bool
        """
        return self._signer_must_acknowledge_use_account_default

    @signer_must_acknowledge_use_account_default.setter
    def signer_must_acknowledge_use_account_default(self, signer_must_acknowledge_use_account_default):
        """Sets the signer_must_acknowledge_use_account_default of this Document.

          # noqa: E501

        :param signer_must_acknowledge_use_account_default: The signer_must_acknowledge_use_account_default of this Document.  # noqa: E501
        :type: bool
        """

        self._signer_must_acknowledge_use_account_default = signer_must_acknowledge_use_account_default

    @property
    def tabs(self):
        """Gets the tabs of this Document.  # noqa: E501

        A list of tabs, which are represented graphically as symbols on documents at the time of signing. Tabs show recipients where to sign, initial, or enter data. They may also display data to the recipients.  # noqa: E501

        :return: The tabs of this Document.  # noqa: E501
        :rtype: Tabs
        """
        return self._tabs

    @tabs.setter
    def tabs(self, tabs):
        """Sets the tabs of this Document.

        A list of tabs, which are represented graphically as symbols on documents at the time of signing. Tabs show recipients where to sign, initial, or enter data. They may also display data to the recipients.  # noqa: E501

        :param tabs: The tabs of this Document.  # noqa: E501
        :type: Tabs
        """

        self._tabs = tabs

    @property
    def template_locked(self):
        """Gets the template_locked of this Document.  # noqa: E501

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :return: The template_locked of this Document.  # noqa: E501
        :rtype: str
        """
        return self._template_locked

    @template_locked.setter
    def template_locked(self, template_locked):
        """Sets the template_locked of this Document.

        When set to **true**, the sender cannot change any attributes of the recipient. Used only when working with template recipients.   # noqa: E501

        :param template_locked: The template_locked of this Document.  # noqa: E501
        :type: str
        """

        self._template_locked = template_locked

    @property
    def template_required(self):
        """Gets the template_required of this Document.  # noqa: E501

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :return: The template_required of this Document.  # noqa: E501
        :rtype: str
        """
        return self._template_required

    @template_required.setter
    def template_required(self, template_required):
        """Sets the template_required of this Document.

        When set to **true**, the sender may not remove the recipient. Used only when working with template recipients.  # noqa: E501

        :param template_required: The template_required of this Document.  # noqa: E501
        :type: str
        """

        self._template_required = template_required

    @property
    def transform_pdf_fields(self):
        """Gets the transform_pdf_fields of this Document.  # noqa: E501

        When set to **true**, PDF form field data is transformed into document tab values when the PDF form field name matches the DocuSign custom tab tabLabel. The resulting PDF form data is also returned in the PDF meta data when requesting the document PDF. See the [ML:Transform PDF Fields] section for more information about how fields are transformed into DocuSign tabs.   # noqa: E501

        :return: The transform_pdf_fields of this Document.  # noqa: E501
        :rtype: str
        """
        return self._transform_pdf_fields

    @transform_pdf_fields.setter
    def transform_pdf_fields(self, transform_pdf_fields):
        """Sets the transform_pdf_fields of this Document.

        When set to **true**, PDF form field data is transformed into document tab values when the PDF form field name matches the DocuSign custom tab tabLabel. The resulting PDF form data is also returned in the PDF meta data when requesting the document PDF. See the [ML:Transform PDF Fields] section for more information about how fields are transformed into DocuSign tabs.   # noqa: E501

        :param transform_pdf_fields: The transform_pdf_fields of this Document.  # noqa: E501
        :type: str
        """

        self._transform_pdf_fields = transform_pdf_fields

    @property
    def uri(self):
        """Gets the uri of this Document.  # noqa: E501

          # noqa: E501

        :return: The uri of this Document.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Document.

          # noqa: E501

        :param uri: The uri of this Document.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if issubclass(Document, dict):
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
        if not isinstance(other, Document):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Document):
            return True

        return self.to_dict() != other.to_dict()
