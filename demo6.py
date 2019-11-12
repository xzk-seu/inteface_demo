"""
已知时间和人物，查目的地

"""

data = \
    {
        'query': '前年到去年之间，张熠经常坐火车去哪些地方？',
        'nodes':
            [
                {
                    'node_id': 0,
                    'type': 'PERSON',
                    'property':
                        {
                            'FIRSTNAME':
                                {
                                    'type': 'string',
                                    'value': '张'
                                },
                            'LASTNAME':
                                {
                                    'type': 'string',
                                    'value': '熠'
                                }
                        }
                },
                {
                    'node_id': 1,
                    'type': 'ADDR',
                    'property':
                        {
                            'location':
                                {
                                    "name": "unknown",
                                    "granularity": None,
                                    "attribution": "目的地"
                                }
                        }
                }
            ],
        'links':
            [
                {
                    "link_id": 0,
                    "source": 0,
                    "target": 1,
                    "key": "ARRIVED_AT",
                    'property':
                        {
                            "time":
                                {
                                    "time_start": "2018-01-01-00-00",
                                    "time_end": "2019-01-01-00-00",
                                    "granularity": "年",
                                    "fuzzy": None

                                }
                        }
                }
            ],
        'targets':
            {
                'target_type': 'node',
                'node_id': 1,
                'limit':'often'
            }
    }
