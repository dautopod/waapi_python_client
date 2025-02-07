# coding: utf-8

"""
    WAHA - WhatsApp HTTP API

    <b>WhatsApp HTTP API</b> that you can run in a click!<br/><a href=\"/dashboard\"><b>📊 Dashboard</b></a><br/><br/>Learn more:<ul><li><a href=\"https://waha.devlike.pro/\" target=\"_blank\">Documentation</a></li><li><a href=\"https://waha.devlike.pro/docs/how-to/engines/#features\" target=\"_blank\">Supported features in engines</a></li><li><a href=\"https://github.com/devlikeapro/waha\" target=\"_blank\">GitHub - WAHA Core</a></li><li><a href=\"https://github.com/devlikeapro/waha-plus\" target=\"_blank\">GitHub - WAHA Plus</a></li></ul><p>Support the project and get WAHA Plus version!</p><ul><li><a href=\"https://waha.devlike.pro/docs/how-to/plus-version/\" target=\"_blank\">WAHA Plus</a></li><li><a href=\"https://patreon.com/wa_http_api/\" target=\"_blank\">Patreon</a></li><li><a href=\"https://boosty.to/wa-http-api/\" target=\"_blank\">Boosty</a></li><li><a href=\"https://portal.devlike.pro/\" target=\"_blank\">Patron Portal</a></li></ul>  # noqa: E501

    OpenAPI spec version: 2024.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class WAHAWebhookMessageAck(object):
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
        'id': 'object',
        'session': 'object',
        'metadata': 'object',
        'engine': 'object',
        'event': 'object',
        'payload': 'WAMessageAckBody',
        'me': 'MeInfo',
        'environment': 'WAHAEnvironment'
    }

    attribute_map = {
        'id': 'id',
        'session': 'session',
        'metadata': 'metadata',
        'engine': 'engine',
        'event': 'event',
        'payload': 'payload',
        'me': 'me',
        'environment': 'environment'
    }

    def __init__(self, id=None, session=None, metadata=None, engine=None, event=None, payload=None, me=None, environment=None):  # noqa: E501
        """WAHAWebhookMessageAck - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._session = None
        self._metadata = None
        self._engine = None
        self._event = None
        self._payload = None
        self._me = None
        self._environment = None
        self.discriminator = None
        self.id = id
        self.session = session
        if metadata is not None:
            self.metadata = metadata
        self.engine = engine
        self.event = event
        self.payload = payload
        if me is not None:
            self.me = me
        self.environment = environment

    @property
    def id(self):
        """Gets the id of this WAHAWebhookMessageAck.  # noqa: E501


        :return: The id of this WAHAWebhookMessageAck.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WAHAWebhookMessageAck.


        :param id: The id of this WAHAWebhookMessageAck.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def session(self):
        """Gets the session of this WAHAWebhookMessageAck.  # noqa: E501


        :return: The session of this WAHAWebhookMessageAck.  # noqa: E501
        :rtype: object
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this WAHAWebhookMessageAck.


        :param session: The session of this WAHAWebhookMessageAck.  # noqa: E501
        :type: object
        """
        if session is None:
            raise ValueError("Invalid value for `session`, must not be `None`")  # noqa: E501

        self._session = session

    @property
    def metadata(self):
        """Gets the metadata of this WAHAWebhookMessageAck.  # noqa: E501

        Metadata for the session.  # noqa: E501

        :return: The metadata of this WAHAWebhookMessageAck.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this WAHAWebhookMessageAck.

        Metadata for the session.  # noqa: E501

        :param metadata: The metadata of this WAHAWebhookMessageAck.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def engine(self):
        """Gets the engine of this WAHAWebhookMessageAck.  # noqa: E501


        :return: The engine of this WAHAWebhookMessageAck.  # noqa: E501
        :rtype: object
        """
        return self._engine

    @engine.setter
    def engine(self, engine):
        """Sets the engine of this WAHAWebhookMessageAck.


        :param engine: The engine of this WAHAWebhookMessageAck.  # noqa: E501
        :type: object
        """
        if engine is None:
            raise ValueError("Invalid value for `engine`, must not be `None`")  # noqa: E501

        self._engine = engine

    @property
    def event(self):
        """Gets the event of this WAHAWebhookMessageAck.  # noqa: E501

        Receive events when server or recipient gets the message, read or played it.  # noqa: E501

        :return: The event of this WAHAWebhookMessageAck.  # noqa: E501
        :rtype: object
        """
        return self._event

    @event.setter
    def event(self, event):
        """Sets the event of this WAHAWebhookMessageAck.

        Receive events when server or recipient gets the message, read or played it.  # noqa: E501

        :param event: The event of this WAHAWebhookMessageAck.  # noqa: E501
        :type: object
        """
        if event is None:
            raise ValueError("Invalid value for `event`, must not be `None`")  # noqa: E501

        self._event = event

    @property
    def payload(self):
        """Gets the payload of this WAHAWebhookMessageAck.  # noqa: E501


        :return: The payload of this WAHAWebhookMessageAck.  # noqa: E501
        :rtype: WAMessageAckBody
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this WAHAWebhookMessageAck.


        :param payload: The payload of this WAHAWebhookMessageAck.  # noqa: E501
        :type: WAMessageAckBody
        """
        if payload is None:
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def me(self):
        """Gets the me of this WAHAWebhookMessageAck.  # noqa: E501


        :return: The me of this WAHAWebhookMessageAck.  # noqa: E501
        :rtype: MeInfo
        """
        return self._me

    @me.setter
    def me(self, me):
        """Sets the me of this WAHAWebhookMessageAck.


        :param me: The me of this WAHAWebhookMessageAck.  # noqa: E501
        :type: MeInfo
        """

        self._me = me

    @property
    def environment(self):
        """Gets the environment of this WAHAWebhookMessageAck.  # noqa: E501


        :return: The environment of this WAHAWebhookMessageAck.  # noqa: E501
        :rtype: WAHAEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this WAHAWebhookMessageAck.


        :param environment: The environment of this WAHAWebhookMessageAck.  # noqa: E501
        :type: WAHAEnvironment
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

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
        if issubclass(WAHAWebhookMessageAck, dict):
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
        if not isinstance(other, WAHAWebhookMessageAck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
