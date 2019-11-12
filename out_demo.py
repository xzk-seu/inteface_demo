import json
from demo1 import data as d1
from demo2 import data as d2
from demo3 import data as d3
from demo4 import data as d4
from demo5 import data as d5
from demo6 import data as d6
from demo7 import data as d7


if __name__ == '__main__':
    t = [d1, d2, d3, d4, d5, d6, d7]
    for i in range(1, 8):
        # t.append('d%d' % i)
        # print(t)
        # print('from demo%d import data as d%d' % (i, i))
        with open('demo_%d.json' % i, 'w') as fw:
            json.dump(t[i-1], fw)
