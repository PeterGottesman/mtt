#!/usr/bin/env python
#
# Copyright (c) 2015-2018  Intel, Inc. All rights reserved.
# $COPYRIGHT$
#
# Additional copyrights may follow
#
# $HEADER$
#

from __future__ import print_function
from yapsy.IPlugin import IPlugin

## @addtogroup Stages
# @{
# @addtogroup Firmware
# ordering 100
# @}
class FirmwareMTTStage(IPlugin):
    def __init__(self):
        # initialise parent class
        IPlugin.__init__(self)
    def print_name(self):
        print("Firmware flash and query stage")

    def ordering(self):
        return 100
