# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 15:45:25 2018

@author: Jens
"""
import logging
logging.basicConfig(level=logging.INFO)

from qdev_wrappers.station_configurator import StationConfigurator
import time

import numpy as np
import matplotlib.pyplot as plt

import qcodes as qc
from qdev_wrappers.alazar_controllers.ATSChannelController import ATSChannelController
from qdev_wrappers.alazar_controllers.alazar_channel import AlazarChannel
from qcodes.station import Station

import logging
logging.basicConfig(level=logging.INFO)

    
start = time.time()
scfg = StationConfigurator('testSetupConfig.yaml')

alazar = scfg.load_instrument('Alazar')
alazar.sync_settings_to_card()

myctrl = scfg.load_instrument('AlazarController')
done = time.time()

print("Init took {:0.3} s".format(done-start))





# Print all information about this Alazar card
alazar.get_idn()



# Create the acquisition controller which will take care of the data handling and tell it which 
# alazar instrument to talk to. Explicitly pass the default options to the Alazar.
# Dont integrate over samples but avarage over records
#myctrl = ATSChannelController(name='my_controller', alazar_name='Alazar')
#
#station = qc.Station(alazar, myctrl)

myctrl.int_delay(2e-7)
myctrl.int_time(2e-6)
print(myctrl.samples_per_record())
#
chan1 = AlazarChannel(myctrl, 'mychan', demod=False, integrate_samples=False)
myctrl.channels.append(chan1)
#
chan1.num_averages(1000)
#
chan1.alazar_channel('A')
chan1.prepare_channel()
#
## Measure this 
#data1 = qc.Measure(chan1.data).run()
#qc.MatPlot(data1.AlazarController_mychan_data)
