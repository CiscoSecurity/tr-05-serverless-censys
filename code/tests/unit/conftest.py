from http import HTTPStatus
from unittest.mock import MagicMock

import jwt
from pytest import fixture

from app import app
from api.errors import INVALID_ARGUMENT
from tests.unit.payloads_for_tests import PRIVATE_KEY


@fixture(scope='session')
def client():
    app.rsa_private_key = PRIVATE_KEY

    app.testing = True

    with app.test_client() as client:
        yield client


@fixture(scope='session')
def valid_jwt(client):
    def _make_jwt(
            api_id='api_id',
            api_secret='api_secret',
            jwks_host='visibility.amp.cisco.com',
            aud='http://localhost',
            kid='02B1174234C29F8EFB69911438F597FF3FFEE6B7',
            wrong_structure=False,
            wrong_jwks_host=False
    ):
        payload = {
            'api_id': api_id,
            'api_secret': api_secret,
            'jwks_host': jwks_host,
            'aud': aud,
        }

        if wrong_jwks_host:
            payload.pop('jwks_host')

        if wrong_structure:
            payload.pop('api_id')

        return jwt.encode(
            payload, client.application.rsa_private_key, algorithm='RS256',
            headers={
                'kid': kid
            }
        )

    return _make_jwt


@fixture(scope='module')
def invalid_json_expected_payload():
    def _make_message(message):
        return {
            'errors': [{
                'code': INVALID_ARGUMENT,
                'message': message,
                'type': 'fatal'
            }]
        }

    return _make_message


def mock_api_response(status_code=HTTPStatus.OK, payload=None):
    mock_response = MagicMock()

    mock_response.status_code = status_code
    mock_response.ok = status_code == HTTPStatus.OK

    mock_response.json = lambda: payload

    return mock_response


@fixture(scope='module')
def ssl_error_expected_relay_response():
    return {
        'errors':
            [
                {
                    'code': 'unknown',
                    'message':
                        'Unable to verify SSL certificate: '
                        'self signed certificate',
                    'type': 'fatal'
                }
            ]
    }


@fixture
def mock_exception_for_ssl_error():
    mock_response = MagicMock()
    mock_response.reason.args.__getitem__().verify_message = 'self signed' \
                                                             ' certificate'
    return mock_response


@fixture(scope='module')
def authorization_error_expected_relay_response():
    return {
        'errors':
            [
                {
                    'code': 'authorization error',
                    'message': 'Authorization failed: 403 (unauthorized): '
                               'Unauthorized. You must authenticate with a'
                               ' valid API ID and secret.',
                    'type': 'fatal'
                }
            ]
    }
