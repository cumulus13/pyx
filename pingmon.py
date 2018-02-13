#!/usr/bin/env python
#coding:utf-8
"""
  Author:  LICFACE --<licface@yahoo.com>
  Purpose: Auto dial modem connect
  Created: 12/22/2017
"""

import vping
import huaweicontrol
hw = huaweicontrol.huaweicontrol('TSEL-TIMEBASED')
import time
from make_colors import make_colors
while 1:
    if vping.vping('8.8.8.8'):
        time.sleep(60)
    else:
        print make_colors('Re-Connecting ....', 'white', 'red', ['blink'])
        hw.navigator('TSEL-TIMEBASED')
        
