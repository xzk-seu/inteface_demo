"""
关系对应实体的查询
"""

data = {
    'query': '张三的同学，名字里有凯',
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
                        'age':
                            {
                                'type': 'string',
                                'constrain': {'op': 'regex', 'para': '*凯*'}
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
                "key": "schoolmate"
            }
        ],
    'targets':
        {
            'target_type': 'node',
            'node_id': 1
        }
}
