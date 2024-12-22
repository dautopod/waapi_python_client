# coding: utf-8

# flake8: noqa
"""
    WAHA - WhatsApp HTTP API

    <b>WhatsApp HTTP API</b> that you can run in a click!<br/><a href=\"/dashboard\"><b>📊 Dashboard</b></a><br/><br/>Learn more:<ul><li><a href=\"https://waha.devlike.pro/\" target=\"_blank\">Documentation</a></li><li><a href=\"https://waha.devlike.pro/docs/how-to/engines/#features\" target=\"_blank\">Supported features in engines</a></li><li><a href=\"https://github.com/devlikeapro/waha\" target=\"_blank\">GitHub - WAHA Core</a></li><li><a href=\"https://github.com/devlikeapro/waha-plus\" target=\"_blank\">GitHub - WAHA Plus</a></li></ul><p>Support the project and get WAHA Plus version!</p><ul><li><a href=\"https://waha.devlike.pro/docs/how-to/plus-version/\" target=\"_blank\">WAHA Plus</a></li><li><a href=\"https://patreon.com/wa_http_api/\" target=\"_blank\">Patreon</a></li><li><a href=\"https://boosty.to/wa-http-api/\" target=\"_blank\">Boosty</a></li><li><a href=\"https://portal.devlike.pro/\" target=\"_blank\">Patron Portal</a></li></ul>  # noqa: E501

    OpenAPI spec version: 2024.12.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from wa_agent.models.base64_file import Base64File
from wa_agent.models.binary_file import BinaryFile
from wa_agent.models.button import Button
from wa_agent.models.call_data import CallData
from wa_agent.models.captcha_body import CaptchaBody
from wa_agent.models.channel import Channel
from wa_agent.models.chat_archive_event import ChatArchiveEvent
from wa_agent.models.chat_request import ChatRequest
from wa_agent.models.contact import Contact
from wa_agent.models.contact_request import ContactRequest
from wa_agent.models.create_channel_request import CreateChannelRequest
from wa_agent.models.create_group_request import CreateGroupRequest
from wa_agent.models.custom_header import CustomHeader
from wa_agent.models.delete_status_request import DeleteStatusRequest
from wa_agent.models.description_request import DescriptionRequest
from wa_agent.models.edit_message_request import EditMessageRequest
from wa_agent.models.engine_payload import EnginePayload
from wa_agent.models.hmac_configuration import HmacConfiguration
from wa_agent.models.image_status import ImageStatus
from wa_agent.models.inline_response200 import InlineResponse200
from wa_agent.models.inline_response200_info import InlineResponse200Info
from wa_agent.models.inline_response503 import InlineResponse503
from wa_agent.models.join_group_request import JoinGroupRequest
from wa_agent.models.join_group_response import JoinGroupResponse
from wa_agent.models.label import Label
from wa_agent.models.label_body import LabelBody
from wa_agent.models.label_chat_association import LabelChatAssociation
from wa_agent.models.label_id import LabelID
from wa_agent.models.map import Map
from wa_agent.models.me_info import MeInfo
from wa_agent.models.message_contact_vcard_request import MessageContactVcardRequest
from wa_agent.models.message_destination import MessageDestination
from wa_agent.models.message_file_request import MessageFileRequest
from wa_agent.models.message_forward_request import MessageForwardRequest
from wa_agent.models.message_image_request import MessageImageRequest
from wa_agent.models.message_link_preview_request import MessageLinkPreviewRequest
from wa_agent.models.message_location_request import MessageLocationRequest
from wa_agent.models.message_poll import MessagePoll
from wa_agent.models.message_poll_request import MessagePollRequest
from wa_agent.models.message_reaction_request import MessageReactionRequest
from wa_agent.models.message_reply_request import MessageReplyRequest
from wa_agent.models.message_star_request import MessageStarRequest
from wa_agent.models.message_text_request import MessageTextRequest
from wa_agent.models.message_video_request import MessageVideoRequest
from wa_agent.models.message_voice_request import MessageVoiceRequest
from wa_agent.models.noweb_config import NowebConfig
from wa_agent.models.noweb_store_config import NowebStoreConfig
from wa_agent.models.otp_request import OTPRequest
from wa_agent.models.participant import Participant
from wa_agent.models.participants_request import ParticipantsRequest
from wa_agent.models.pin_message_request import PinMessageRequest
from wa_agent.models.ping_response import PingResponse
from wa_agent.models.poll_vote import PollVote
from wa_agent.models.poll_vote_payload import PollVotePayload
from wa_agent.models.proxy_config import ProxyConfig
from wa_agent.models.qr_code_value import QRCodeValue
from wa_agent.models.remote_file import RemoteFile
from wa_agent.models.reply_to_message import ReplyToMessage
from wa_agent.models.request_code_request import RequestCodeRequest
from wa_agent.models.retries_configuration import RetriesConfiguration
from wa_agent.models.s3_media_data import S3MediaData
from wa_agent.models.send_buttons_request import SendButtonsRequest
from wa_agent.models.send_seen_request import SendSeenRequest
from wa_agent.models.server_status_response import ServerStatusResponse
from wa_agent.models.session_config import SessionConfig
from wa_agent.models.session_create_request import SessionCreateRequest
from wa_agent.models.session_dto import SessionDTO
from wa_agent.models.session_info import SessionInfo
from wa_agent.models.session_logout_deprecated_request import SessionLogoutDeprecatedRequest
from wa_agent.models.session_start_deprecated_request import SessionStartDeprecatedRequest
from wa_agent.models.session_stop_deprecated_request import SessionStopDeprecatedRequest
from wa_agent.models.session_update_request import SessionUpdateRequest
from wa_agent.models.set_labels_request import SetLabelsRequest
from wa_agent.models.settings_security_change_info import SettingsSecurityChangeInfo
from wa_agent.models.stop_request import StopRequest
from wa_agent.models.stop_response import StopResponse
from wa_agent.models.subject_request import SubjectRequest
from wa_agent.models.text_status import TextStatus
from wa_agent.models.v_card_contact import VCardContact
from wa_agent.models.video_binary_file import VideoBinaryFile
from wa_agent.models.video_remote_file import VideoRemoteFile
from wa_agent.models.video_status import VideoStatus
from wa_agent.models.voice_binary_file import VoiceBinaryFile
from wa_agent.models.voice_remote_file import VoiceRemoteFile
from wa_agent.models.voice_status import VoiceStatus
from wa_agent.models.waha_chat_presences import WAHAChatPresences
from wa_agent.models.waha_environment import WAHAEnvironment
from wa_agent.models.waha_presence_data import WAHAPresenceData
from wa_agent.models.waha_session_presence import WAHASessionPresence
from wa_agent.models.waha_webhook_call_accepted import WAHAWebhookCallAccepted
from wa_agent.models.waha_webhook_call_received import WAHAWebhookCallReceived
from wa_agent.models.waha_webhook_call_rejected import WAHAWebhookCallRejected
from wa_agent.models.waha_webhook_chat_archive import WAHAWebhookChatArchive
from wa_agent.models.waha_webhook_engine_event import WAHAWebhookEngineEvent
from wa_agent.models.waha_webhook_group_join import WAHAWebhookGroupJoin
from wa_agent.models.waha_webhook_group_leave import WAHAWebhookGroupLeave
from wa_agent.models.waha_webhook_label_chat_added import WAHAWebhookLabelChatAdded
from wa_agent.models.waha_webhook_label_chat_deleted import WAHAWebhookLabelChatDeleted
from wa_agent.models.waha_webhook_label_deleted import WAHAWebhookLabelDeleted
from wa_agent.models.waha_webhook_label_upsert import WAHAWebhookLabelUpsert
from wa_agent.models.waha_webhook_message import WAHAWebhookMessage
from wa_agent.models.waha_webhook_message_ack import WAHAWebhookMessageAck
from wa_agent.models.waha_webhook_message_any import WAHAWebhookMessageAny
from wa_agent.models.waha_webhook_message_reaction import WAHAWebhookMessageReaction
from wa_agent.models.waha_webhook_message_revoked import WAHAWebhookMessageRevoked
from wa_agent.models.waha_webhook_poll_vote import WAHAWebhookPollVote
from wa_agent.models.waha_webhook_poll_vote_failed import WAHAWebhookPollVoteFailed
from wa_agent.models.waha_webhook_presence_update import WAHAWebhookPresenceUpdate
from wa_agent.models.waha_webhook_session_status import WAHAWebhookSessionStatus
from wa_agent.models.waha_webhook_state_change import WAHAWebhookStateChange
from wa_agent.models.wa_location import WALocation
from wa_agent.models.wa_media import WAMedia
from wa_agent.models.wa_message import WAMessage
from wa_agent.models.wa_message_ack_body import WAMessageAckBody
from wa_agent.models.wa_message_reaction import WAMessageReaction
from wa_agent.models.wa_message_revoked_body import WAMessageRevokedBody
from wa_agent.models.wa_number_exist_result import WANumberExistResult
from wa_agent.models.wa_reaction import WAReaction
from wa_agent.models.wa_session_status_body import WASessionStatusBody
from wa_agent.models.webhook_config import WebhookConfig
from wa_agent.models.worker_info import WorkerInfo
