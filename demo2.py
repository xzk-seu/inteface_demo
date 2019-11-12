"""
值属性的查询
"""
import json

data = {
    'query': '张三小于35岁的同学的生日',
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
                                'type': 'int',
                                'constrain': {'op': '<', 'para': 35}
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
            'target_type': 'node_property',
            'node': 1,
            'property': 'birthday'
        }

}

# pprint(data)
t = json.dumps(data, indent=4)
print(t)
