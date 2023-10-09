import os
from ttgo_t8 import TTGO_T8


t8 = TTGO_T8()
try:
    t8.sdcard_mount()
except Exception as e:
    raise e
else:
    if 'main.py' in os.listdir('/sd'):
        exec(open('/sd/main.py', 'r').read())

