
ids = [
    [11, 81, 32, 52, 13],
    [31, 71, 42, 62, 23],
    [21, 61, 12, 72, 33],
    [44, 51, 22, 82, 43]
]

cellDatabase = [
    # cell_1
    {
        'code': 1,
        'motors': [
            {'pins': {'digital': (53, 52), 'pwm': 11}},
            {'pins': {'digital': (51, 50), 'pwm': 12}},
            {'pins': {'digital': (49, 48), 'pwm': 13}},
        ]
    },
    # cell_8
    {
        'code': 4,
        'motors': [
            {'pins': {'digital': (29, 28), 'pwm': 5}},
            {'pins': {'digital': (31, 30), 'pwm': 6}},
            {'pins': {'digital': (33, 32), 'pwm': 7}},
        ]
    },
    # cell_3
    {
        'code': 2,
        'motors': [
            {'pins': {'digital': (33, 32), 'pwm': 2}},
            {'pins': {'digital': (31, 30), 'pwm': 3}},
            {'pins': {'digital': (29, 28), 'pwm': 4}},
        ]
    },
    # cell_5
    {
        'code': 3,
        'motors': [
            {'pins': {'digital': (53, 52), 'pwm': 8}},
            {'pins': {'digital': (51, 50), 'pwm': 9}},
            {'pins': {'digital': (49, 48), 'pwm': 10}},
        ]
    },
    # cell_1
    {
        'code': 1,
        'motors': [
            {'pins': {'digital': (53, 52), 'pwm': 11}},
            {'pins': {'digital': (51, 50), 'pwm': 12}},
            {'pins': {'digital': (49, 48), 'pwm': 13}},
        ]
    },
    # cell_3
    {
        'code': 2,
        'motors': [
            {'pins': {'digital': (33, 32), 'pwm': 2}},
            {'pins': {'digital': (31, 30), 'pwm': 3}},
            {'pins': {'digital': (29, 28), 'pwm': 4}},
        ]
    },
    # cell_7
    {
        'code': 4,
        'motors': [
            {'pins': {'digital': (23, 22), 'pwm': 4}},
            {'pins': {'digital': (25, 24), 'pwm': 3}},
            {'pins': {'digital': (27, 26), 'pwm': 2}},
        ]
    },
    # cell_4
    {
        'code': 2,
        'motors': [
            {'pins': {'digital': (27, 26), 'pwm': 5}},
            {'pins': {'digital': (25, 24), 'pwm': 6}},
            {'pins': {'digital': (23, 22), 'pwm': 7}},
        ]
    },
    # cell_6
    {
        'code': 3,
        'motors': [
            {'pins': {'digital': (47, 38), 'pwm': 11}},
            {'pins': {'digital': (37, 36), 'pwm': 12}},
            {'pins': {'digital': (35, 34), 'pwm': 13}},
        ]
    },
    # cell_2
    {
        'code': 1,
        'motors': [
            {'pins': {'digital': (47, 38), 'pwm': 10}},
            {'pins': {'digital': (37, 36), 'pwm': 9}},
            {'pins': {'digital': (35, 34), 'pwm': 8}},

        ]
    },
    # cell_2
    {
        'code': 1,
        'motors': [
            {'pins': {'digital': (47, 38), 'pwm': 10}},
            {'pins': {'digital': (37, 36), 'pwm': 9}},
            {'pins': {'digital': (35, 34), 'pwm': 8}},

        ]
    },
    # cell_6
    {
        'code': 3,
        'motors': [
            {'pins': {'digital': (47, 38), 'pwm': 11}},
            {'pins': {'digital': (37, 36), 'pwm': 12}},
            {'pins': {'digital': (35, 34), 'pwm': 13}},
        ]
    },
    # cell_1
    {
        'code': 1,
        'motors': [
            {'pins': {'digital': (53, 52), 'pwm': 11}},
            {'pins': {'digital': (51, 50), 'pwm': 12}},
            {'pins': {'digital': (49, 48), 'pwm': 13}},
        ]
    },
    # cell_7
    {
        'code': 4,
        'motors': [
            {'pins': {'digital': (23, 22), 'pwm': 4}},
            {'pins': {'digital': (25, 24), 'pwm': 3}},
            {'pins': {'digital': (27, 26), 'pwm': 2}},
        ]
    },
    # cell_3
    {
        'code': 2,
        'motors': [
            {'pins': {'digital': (33, 32), 'pwm': 2}},
            {'pins': {'digital': (31, 30), 'pwm': 3}},
            {'pins': {'digital': (29, 28), 'pwm': 4}},
        ]
    },
    # cell_4
    {
        'code': 2,
        'motors': [
            {'pins': {'digital': (27, 26), 'pwm': 5}},
            {'pins': {'digital': (25, 24), 'pwm': 6}},
            {'pins': {'digital': (23, 22), 'pwm': 7}},
        ]
    },
    # cell_5
    {
        'code': 3,
        'motors': [
            {'pins': {'digital': (53, 52), 'pwm': 8}},
            {'pins': {'digital': (51, 50), 'pwm': 9}},
            {'pins': {'digital': (49, 48), 'pwm': 10}},
        ]
    },
    # cell_2
    {
        'code': 1,
        'motors': [
            {'pins': {'digital': (47, 38), 'pwm': 10}},
            {'pins': {'digital': (37, 36), 'pwm': 9}},
            {'pins': {'digital': (35, 34), 'pwm': 8}},

        ]
    },
    # cell_8
    {
        'code': 4,
        'motors': [
            {'pins': {'digital': (29, 28), 'pwm': 5}},
            {'pins': {'digital': (31, 30), 'pwm': 6}},
            {'pins': {'digital': (33, 32), 'pwm': 7}},
        ]
    },
    # cell_4
    {
        'code': 2,
        'motors': [
            {'pins': {'digital': (27, 26), 'pwm': 5}},
            {'pins': {'digital': (25, 24), 'pwm': 6}},
            {'pins': {'digital': (23, 22), 'pwm': 7}},
        ]
    },
]
k = 0
for i in range(4):
    for j in range(5):
        j1 = j*2
        if i%2 == 1:
            j1 = j1 + 1
        cellDatabase[k]['id'] = ids[i][j]
        cellDatabase[k]['location'] = [i, j1]
        k += 1

y0 = 163.75
x0 = 165.8
dy = 157.5
dx = 90.93 * 2
r=0
for i in range(4):
    x0 = 165.8
    if i == 1 or i == 3:
        x0 = x0+dx/2
    for j in range(5):
        location = [x0, y0]
        cellDatabase[r]['coordinates'] = location
        # print(cellDatabase[r]['coordinates'])
        x0 = x0+dx
        r+= 1
    y0=y0+dy

