"""
已知时间和人物，查目的地

"""

data = \
    {
        'query': '1179923375@qq.com在8月份给哪些人订过火车票？',
        'nodes':
            [
                {
                    'node_id': 0,
                    'type': 'EMAIL',
                    'property':
                        {
                            'email_address':
                                {
                                    'type': 'string',
                                    'value': '1179923375@qq.com'
                                }
                        }
                },
                {
                    'node_id': 1,
                    'type': 'TRAIN_TICKETS',
                    'property': None
                },
                {
                    'node_id': 2,
                    'type': 'PERSON',
                    'property': None
                }
            ],
        'links':
            [
                {
                    "link_id": 0,
                    "source": 0,
                    "target": 1,
                    "key": "Booking_train_tickets",
                    'property':
                        {
                            "time":
                                {
                                    "time_start": "2019-08-01-00-00",
                                    "time_end": "2019-08-01-00-00",
                                    "granularity": "月",
                                    "fuzzy": None
                                }
                        }
                },
                {
                    "link_id": 1,
                    "source": 2,
                    "target": 1,
                    "key": "OWN_TICKET",
                    'property': None
                }
            ],
        'targets':
            [
                {
                    'target_type': 'node',
                    'node_id': 2
                }
            ],
        'steps':  # 对待查边两边的节点进行广度优先遍历
            [
                {'current_target_node_id': 0,
                 'related_links_id': None},
                {'current_target_node_id': 1,
                 'related_links_id': [0]},
                {'current_target_node_id': 2,
                 'related_links_id': [1]}
            ]

    }
