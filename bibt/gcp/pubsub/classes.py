import logging

from google.cloud import pubsub_v1

_LOGGER = logging.getLogger(__name__)


class Client:
    """ """

    def __init__(self, credentials=None):
        self._client = pubsub_v1.PublisherClient(credentials=credentials)
