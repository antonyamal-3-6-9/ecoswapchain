from django.dispatch import Signal, receiver
from requests.exceptions import RequestException
from rest_framework.exceptions import ValidationError
from decimal import Decimal
import requests
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .tasks import nftTransferTask, susScoreTask

channel_layer = get_channel_layer()

nft_transfer_signal = Signal()
sus_score_signal = Signal()

@receiver(nft_transfer_signal)
def transferNFT(sender, orderId, tx_hash, **kwargs):
    nftTransferTask.delay(orderId, tx_hash)


@receiver(sus_score_signal)
def susScore(sender, nftId, **kwargs):
    susScoreTask.delay(nftId)