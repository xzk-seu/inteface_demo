"""
值属性的查询
"""

"""
{
“query”: “住在西善桥北路89号的18526439876的在华为上班的同学是谁”,
 “targets”: [“v_5”],
“triples”: [[“v_0”, “ADDR_NAME”, “v_5”],
             [“v_1”, “live_in”, “v_0”],
             [“v_1”, “p_has_phone”, “v_2”],
             [“v_2”, “phone_num”, “v_6”],
             [“v_3”, “company_name”, “v_7”],
             [“v_4”, “work_for”, “v_3”],
             [“v_1”, “schoolmate”, “v_1”]],
 “variables”: {“v_0”: {“type”: “ADDR”},
               “v_1”: {“type”: “PERSON”},
               “v_2”: {“type”: “PHONE”},
               “v_3”: {“type”: “COMPANY”},
               “v_4”: {“type”: “PERSON”},
               “v_5”: {“type”: “STRING”, “value”: “西善桥北路89号”},
               “v_6”: {“type”: “STRING”, “value”: “18526439876”},
               “v_7”: {“type”: “STRING”, “value”: “华为”}}}

"""

data = \
    {
        'query': '住在西善桥北路89号的18526439876的在华为上班的同学是谁',
        'nodes':
            [
                {
                    'node_id': 0,
                    'type': 'PERSON',
                    'property': None
                },
                {
                    'node_id': 1,
                    'type': 'ADDR',
                    'property':
                        {
                            'ADDR_NAME':
                                {
                                    'type': 'string',
                                    'value': '西善桥北路89号'
                                }
                        }
                },
                {
                    'node_id': 2,
                    'type': 'TELEPHONE',
                    'property':
                        {
                            'TELEPHONE_NUM':
                                {
                                    'type': 'string',
                                    'value': '18526439876'
                                }
                        }
                },
                {
                    'node_id': 3,
                    'type': 'COMPANY',
                    'property':
                        {
                            'COMPANY_NAME':
                                {
                                    'type': 'string',
                                    'value': '华为'
                                }
                        }
                },
                {
                    'node_id': 4,
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
                    "key": "reside"
                },
                {
                    "link_id": 1,
                    "source": 0,
                    "target": 2,
                    "key": "p_has_telephone"
                },
                {
                    "link_id": 3,
                    "source": 0,
                    "target": 4,
                    "key": "schoolmate"
                },
                {
                    "link_id": 4,
                    "source": 4,
                    "target": 3,
                    "key": "work_for"
                },
            ],
        'targets':
            [
                {
                    'target_type': 'node',
                    'node_id': 4
                }
            ],
        'steps':
            [
                {'current_target_node_id': 1,
                 'related_links_id': None},
                {'current_target_node_id': 2,
                 'related_links_id': None},
                {'current_target_node_id': 0,
                 'related_links_id': [0, 1]},
                {'current_target_node_id': 3,
                 'related_links_id': None},  # 0->1  0->2
                {'current_target_node_id': 4,
                 'related_links_id': [3, 4]}  # 0->4  4->3
            ]
    }

# pprint(data)
# t = json.dumps(data, indent=4)
# print(t)
