"""
关系查询
"""

data = \
    {
        'query': '张三和李四是什么关系',
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
                                    'value': '三'
                                }
                        }
                },
                {
                    'node_id': 1,
                    'type': 'PERSON',
                    'property':
                        {
                            'FIRSTNAME':
                                {
                                    'type': 'string',
                                    'value': '李'
                                },
                            'LASTNAME':
                                {
                                    'type': 'string',
                                    'value': '四'
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
                    "key": "unknown"
                }
            ],
        'targets':
            {
                'target_type': 'link',
                'link_id': 0,
            }
    }
