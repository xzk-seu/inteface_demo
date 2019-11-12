"""
已知时间点查车次
转为查边上属性
"""

data = \
    {
        'query': '昨天凌晨张熠坐的哪一辆火车去的虹桥站？',
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
                                    "name": "虹桥站",
                                    "granularity": "车站",
                                    "attribution": "终点站",
                                    "fuzzy": None
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
                                    "time_start": "2019-10-30-00-00",
                                    "time_end": "2019-10-30-24-00",
                                    "granularity": "天",
                                    "fuzzy": None
                                }
                        }
                }
            ],
        'targets':
            {
                'target_type': 'link_property',
                'link_id': 0,
                'property': 'train_number'
            }
    }
