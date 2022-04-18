from flask import Blueprint

from api.client import CensysClient
from api.utils import get_credentials, jsonify_data

health_api = Blueprint('health', __name__)


@health_api.route('/health', methods=['POST'])
def health():
    credentials = get_credentials()

    client = CensysClient(credentials)
    client.health()

    return jsonify_data({'status': 'ok'})
