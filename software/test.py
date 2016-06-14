import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# adding parent directory to path, so we can access the utils easily
import sys
sys.path.append(HERE_PATH)

import logging
logging.basicConfig(level=logging.INFO)

import time

#
from manager import manager

XP_dict = {
    'surfactant_volume': 3.5,
    'formulation': {
        'octanol': 30,
        'octanoic': 50,
        'pentanol': 20,
        'dep': 0
    },
    'video_info': {
        'path': os.path.join(HERE_PATH, 'video.avi'),
        'duration': 100
    },
    'droplets': [
        {
            'volume': 4,
            'position': [5, 0]
        },
        {
            'volume': 4,
            'position': [-5, 0]
        },
        {
            'volume': 4,
            'position': [0, 5]
        },
        {
            'volume': 4,
            'position': [0, -5]
        }
    ]
}

start_time = time.time()

for _ in range(1):
    manager.add_XP(XP_dict)

manager.wait_until_XP_finished()

elapsed = time.time() - start_time

print 'Purge took {} seconds'.format(elapsed)
