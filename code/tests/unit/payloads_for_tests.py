EXPECTED_PAYLOAD_OF_CENSYS = [
    {
        "timestamp": "2022-04-14T07:32:19.409Z",
        "service_observed": {
            "id": {
                "port": 53,
                "transport_protocol": "UDP",
                "service_name": "DNS"
            },
            "observed_at": "2022-04-14T07:32:19.382893452Z",
            "perspective_id": "PERSPECTIVE_NTT",
            "changed_fields": [
                {
                    "field_name": "dns.answers"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:32:30.369Z",
        "service_observed": {
            "id": {
                "port": 53,
                "transport_protocol": "UDP",
                "service_name": "DNS"
            },
            "observed_at": "2022-04-14T07:32:29.719301999Z",
            "perspective_id": "PERSPECTIVE_TATA",
            "changed_fields": [
                {
                    "field_name": "dns.answers"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:33:20.100Z",
        "service_observed": {
            "id": {
                "port": 53,
                "transport_protocol": "UDP",
                "service_name": "DNS"
            },
            "observed_at": "2022-04-14T07:33:20.042583206Z",
            "perspective_id": "PERSPECTIVE_HE",
            "changed_fields": [
                {
                    "field_name": "dns.answers"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:34:18.017Z",
        "service_observed": {
            "id": {
                "port": 53,
                "transport_protocol": "UDP",
                "service_name": "DNS"
            },
            "observed_at": "2022-04-14T07:34:17.958692540Z",
            "perspective_id": "PERSPECTIVE_NTT",
            "changed_fields": [
                {
                    "field_name": "dns.answers"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:34:26.128Z",
        "service_observed": {
            "id": {
                "port": 80,
                "service_name": "HTTP",
                "transport_protocol": "TCP"
            },
            "observed_at": "2022-04-14T07:34:26.070569439Z",
            "perspective_id": "PERSPECTIVE_HE",
            "changed_fields": [
                {
                    "field_name": "http.response.headers.Cf-Ray.headers"
                },
                {
                    "field_name": "banner"
                }
            ]
        },
        "_event": "service_observed"
    },
    {
        "timestamp": "2022-04-14T07:34:26.183Z",
        "service_observed": {
            "id": {
                "port": 443,
                "service_name": "HTTP",
                "transport_protocol": "TCP"
            },
            "observed_at": "2022-04-14T07:34:26.075740583Z",
            "perspective_id": "PERSPECTIVE_HE",
            "changed_fields": [
                {
                    "field_name":
                        "http.response.headers.X-Amz-Request-Id.headers"
                },
                {
                    "field_name": "http.response.status_reason"
                },
                {
                    "field_name": "http.response.headers.Location.headers"
                },
                {
                    "field_name": "http.response.body_size"
                },
                {
                    "field_name":
                        "http.response.headers.X-Rgw-Object-Type.headers"
                },
                {
                    "field_name":
                        "http.response.headers.Served-In-Seconds.headers"
                },
                {
                    "field_name": "http.response.html_tags"
                },
                {
                    "field_name": "http.request.uri"
                },
                {
                    "field_name": "banner"
                },
                {
                    "field_name": "http.response.headers.Expires.headers"
                },
                {
                    "field_name": "http.response.headers.Cf-Ray.headers"
                },
                {
                    "field_name": "http.response.headers.Report-To.headers"
                },
                {
                    "field_name": "http.response.headers.Age.headers"
                },
                {
                    "field_name": "http.response.status_code"
                },
                {
                    "field_name": "http.response.headers.Set-Cookie.headers"
                },
                {
                    "field_name": "http.response.headers.Last-Modified.headers"
                },
                {
                    "field_name": "http.body_hash"
                },
                {
                    "field_name": "http.response.body"
                }
            ]
        },
        "_event": "service_observed"
    }
]


def base_payload():
    return {
        'data':
            {
                'sightings': {
                    'count': 6,
                    'docs': [
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [
                                    {'name': 'timestamp', 'type': 'string'},
                                    {'name': 'service_observed',
                                     'type': 'string'},
                                    {'name': '_event', 'type': 'string'}],
                                'rows': [['2022-04-14T07:32:19.409Z',
                                          "{'id': {'port': 53, 'transport_pro"
                                          "tocol': 'UDP', 'service_name': 'DN"
                                          "S'}, 'observed_at': '2022-04-14T07"
                                          ":32:19.382893452Z', 'perspective_i"
                                          "d': 'PERSPECTIVE_NTT', 'changed_fi"
                                          "elds': [{'field_name': 'dns.answer"
                                          "s'}]}",
                                          'service_observed']
                                         ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-73978e74-3497-4523-b6cf'
                                  '-45c778df6999',
                            'internal': True,
                            'observables': [{'type': 'ip',
                                             'value': '1.1.1.1'}],
                            'observed_time': {
                                'start_time':
                                    '2022-04-14T07:32:19.382893452Z'},
                            'schema_version': '1.1.11',
                            'short_description': 'Event service_observed obse'
                                                 'rved at Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'source': 'Censys', 'type': 'sighting'},
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [{'name': 'timestamp',
                                             'type': 'string'},
                                            {'name': 'service_observed',
                                             'type': 'string'},
                                            {'name': '_event',
                                             'type': 'string'}],
                                'rows': [
                                    ['2022-04-14T07:32:30.369Z',
                                     "{'id': {'port': 53, 'transport_protocol"
                                     "': 'UDP', 'service_name': 'DNS'}, 'obse"
                                     "rved_at': '2022-04-14T07:32:29.71930199"
                                     "9Z', 'perspective_id': 'PERSPECTIVE_TAT"
                                     "A', 'changed_fields': [{'field_name': '"
                                     "dns.answers'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-61d25337-da63-47ca-97d5'
                                  '-b8e6e4630249',
                            'internal': True,
                            'observables': [{'type': 'ip',
                                             'value': '1.1.1.1'}],
                            'observed_time': {
                                'start_time':
                                    '2022-04-14T07:32:29.719301999Z'},
                            'schema_version': '1.1.11',
                            'short_description': 'Event service_observed obse'
                                                 'rved at Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'source': 'Censys', 'type': 'sighting'},
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [{'name': 'timestamp',
                                             'type': 'string'},
                                            {'name': 'service_observed',
                                             'type': 'string'},
                                            {'name': '_event',
                                             'type': 'string'}],
                                'rows': [
                                    ['2022-04-14T07:33:20.100Z',
                                     "{'id': {'port': 53, 'transport_protocol"
                                     "': 'UDP', 'service_name': 'DNS'}, 'obse"
                                     "rved_at': '2022-04-14T07:33:20.04258320"
                                     "6Z', 'perspective_id': 'PERSPECTIVE_HE'"
                                     ", 'changed_fields': [{'field_name': 'dn"
                                     "s.answers'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-792646ce-67c1-443c-b647'
                                  '-e148295aa5a3',
                            'internal': True,
                            'observables': [{'type': 'ip',
                                             'value': '1.1.1.1'}],
                            'observed_time': {
                                'start_time': '2022-04-14T07:33:20.042583206Z'
                            },
                            'schema_version': '1.1.11',
                            'short_description':
                                'Event service_observed observed at Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'source': 'Censys', 'type': 'sighting'
                        },
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [
                                    {'name': 'timestamp', 'type': 'string'},
                                    {'name': 'service_observed',
                                     'type': 'string'},
                                    {'name': '_event', 'type': 'string'}],
                                'rows': [
                                    ['2022-04-14T07:34:18.017Z',
                                     "{'id': {'port': 53, 'transport_protocol"
                                     "': 'UDP', 'service_name': 'DNS'}, 'obse"
                                     "rved_at': '2022-04-14T07:34:17.95869254"
                                     "0Z', 'perspective_id': 'PERSPECTIVE_NTT"
                                     "', 'changed_fields': [{'field_name': 'd"
                                     "ns.answers'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-d6b1e628-c24c-4302-8aec'
                                  '-1737ef6adba7',
                            'internal': True,
                            'observables': [
                                {'type': 'ip', 'value': '1.1.1.1'}
                            ],
                            'observed_time': {
                                'start_time': '2022-04-14T07:34:17.958692540Z'
                            },
                            'schema_version': '1.1.11',
                            'short_description':
                                'Event service_observed observed at Censys',
                            'source': 'Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'type': 'sighting'
                        },
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [
                                    {'name': 'timestamp', 'type': 'string'},
                                    {'name': 'service_observed',
                                     'type': 'string'},
                                    {'name': '_event', 'type': 'string'}],
                                'rows': [
                                    ['2022-04-14T07:34:26.128Z',
                                     "{'id': {'port': 80, 'service_name': 'HT"
                                     "TP', 'transport_protocol': 'TCP'}, 'obs"
                                     "erved_at': '2022-04-14T07:34:26.0705694"
                                     "39Z', 'perspective_id': 'PERSPECTIVE_HE"
                                     "', 'changed_fields': [{'field_name': 'h"
                                     "ttp.response.headers.Cf-Ray.headers'}, "
                                     "{'field_name': 'banner'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-c1901f65-5f1f-477a-af30'
                                  '-ec6d9f5cfa4e',
                            'internal': True,
                            'observables': [
                                {'type': 'ip', 'value': '1.1.1.1'}
                            ],
                            'observed_time': {
                                'start_time':
                                    '2022-04-14T07:34:26.070569439Z'
                            },
                            'schema_version': '1.1.11',
                            'short_description':
                                'Event service_observed observed at Censys',
                            'source': 'Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'type': 'sighting'
                        },
                        {
                            'confidence': 'High',
                            'count': 1,
                            'data': {
                                'columns': [
                                    {'name': 'timestamp', 'type': 'string'},
                                    {'name': 'service_observed',
                                     'type': 'string'},
                                    {'name': '_event', 'type': 'string'}
                                ],
                                'rows': [
                                    ['2022-04-14T07:34:26.183Z',
                                     "{'id': {'port': 443, 'service_name': 'H"
                                     "TTP', 'transport_protocol': 'TCP'}, 'ob"
                                     "served_at': '2022-04-14T07:34:26.075740"
                                     "583Z', 'perspective_id': 'PERSPECTIVE_H"
                                     "E', 'changed_fields': [{'field_name': '"
                                     "http.response.headers.X-Amz-Request-Id."
                                     "headers'}, {'field_name': 'http.respons"
                                     "e.status_reason'}, {'field_name': 'http"
                                     ".response.headers.Location.headers'}, {"
                                     "'field_name': 'http.response.body_size'"
                                     "}, {'field_name': 'http.response.header"
                                     "s.X-Rgw-Object-Type.headers'}, {'field_"
                                     "name': 'http.response.headers.Served-In"
                                     "-Seconds.headers'}, {'field_name': 'htt"
                                     "p.response.html_tags'}, {'field_name': "
                                     "'http.request.uri'}, {'field_name': 'ba"
                                     "nner'}, {'field_name': 'http.response.h"
                                     "eaders.Expires.headers'}, {'field_name'"
                                     ": 'http.response.headers.Cf-Ray.headers"
                                     "'}, {'field_name': 'http.response.heade"
                                     "rs.Report-To.headers'}, {'field_name': "
                                     "'http.response.headers.Age.headers'}, {"
                                     "'field_name': 'http.response.status_cod"
                                     "e'}, {'field_name': 'http.response.head"
                                     "ers.Set-Cookie.headers'}, {'field_name'"
                                     ": 'http.response.headers.Last-Modified."
                                     "headers'}, {'field_name': 'http.body_ha"
                                     "sh'}, {'field_name': 'http.response.bod"
                                     "y'}]}",
                                     'service_observed']
                                ]
                            },
                            'description': 'Event service_observed for 1.1.1.'
                                           '1 observed at Censys',
                            'id': 'transient:sighting-7b7a9f34-2bf8-4339-8f54'
                                  '-cf972ae5ba3e',
                            'internal': True,
                            'observables': [
                                {'type': 'ip', 'value': '1.1.1.1'}
                            ],
                            'observed_time': {
                                'start_time': '2022-04-14T07:34:26.075740583Z'
                            },
                            'schema_version': '1.1.11',
                            'short_description': 'Event service_observed obse'
                                                 'rved at Censys',
                            'title': 'Event for 1.1.1.1 observed by Censys',
                            'source': 'Censys', 'type': 'sighting'}
                    ]
                }
            }
    }


def refer_payload():
    return {
        'data':
            [
                {
                    "categories": [
                        "Censys",
                        "Search",
                        "Events"
                    ],
                    "description": "Events for this ip in the Censys",
                    "id": "ref-censys-search-ip-1.1.1.1",
                    "title": "Events for this IP",
                    "url": "https://search.censys.io/hosts/1.1.1.1/events"
                }
            ]
    }
