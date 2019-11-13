import json
from pprint import pprint

NODE__ = 'v_1'

if __name__ == '__main__':

    temp = dict()
    temp['query'] = "住在西善桥北路89号的18526439876的在华为上班的同学是谁"

    va = {'v_%d' % x: dict() for x in range(8)}

    temp['variables'] = va

    node__ = 'v_0'
    s = 'v_2'
    node__1 = 'v_3'
    node__2 = 'v_4'

    types = [
        [('%s' % node__), 'type', 'ADDR'],
        [('%s' % NODE__), 'type', 'PERSON'],
        [('%s' % s), 'type', 'PHONE'],
        [('%s' % node__1), 'type', 'COMPANY'],
        [('%s' % node__2), 'type', 'PERSON'],
        ['v_5', '_', 'STRING'],
        ['v_6', '_', 'STRING'],
        ['v_7', '_', 'STRING']
    ]

    for t in types:
        va[t[0]]['type'] = t[2]
    va['v_5']['value'] = '西善桥北路89号'
    va['v_6']['value'] = '18526439876'
    va['v_7']['value'] = '华为'

    triples = [
        [node__, 'ADDR_NAME', 'v_5'],
        [NODE__, 'live_in', node__],
        [NODE__, 'p_has_phone', s],
        [s, 'phone_num', 'v_6'],
        [node__1, 'company_name', 'v_7'],
        [node__2, 'work_for', node__1],
        [NODE__, 'schoolmate', NODE__],
    ]

    temp['triples'] = triples
    temp['targets'] = ['v_5']
    with open('demo_1.json', 'w') as fw:
        json.dump(temp, fw)
    pprint(temp)

data = \
    {
        "query": "住在西善桥北路89号的18526439876的在华为上班的同学是谁",
        "nodes": [
            {
                "node_id": 0,
                "type": "PERSON",
                "property": null
            },
            {
                "node_id": 1,
                "type": "ADDR",
                "property": {
                    "ADDR_NAME": {
                        "type": "string",
                        "value": "西善桥北路89号"
                    }
                }
            },
            {
                "node_id": 2,
                "type": "TELEPHONE",
                "property": {
                    "TELEPHONE_NUM": {
                        "type": "string",
                        "value": "18526439876"
                    }
                }
            },
            {
                "node_id": 3,
                "type": "COMPANY",
                "property": {
                    "COMPANY_NAME": {
                        "type": "string",
                        "value": "华为"
                    }
                }
            },
            {
                "node_id": 4,
                "type": "PERSON",
                "property": null
            }
        ],
        "links": [
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
            }
        ],
        "targets": {
            "target_type": "node",
            "target_id": 4
        }
    }


