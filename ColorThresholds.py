import numpy as np

ColorThresholds = {
    'red': {
        'lower': (0, 0, 0),
        'upper': (12, 255, 255),
    },
    'orange': {
        'lower': (12, 0, 0),
        'upper': (20, 255, 255),
    },
    'blue': {
        'lower': (80, 0, 0),
        'upper': (130, 255, 255),
    },
    'yellow': {
        'lower': (20, 0, 0),
        'upper': (40, 255, 255),
    },
    'green': {
        'lower': (45, 0, 0),
        'upper': (70, 255, 255),
    },
    'purple': {
        'lower': (130, 0, 0),
        'upper': (255, 255, 255),
    },
    "white": {
        'lower': (0, 0, 0),
        'upper': (255, 5, 5),
    }
}