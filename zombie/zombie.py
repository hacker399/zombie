## Zombi3_404 17-01-2025 (00:24)
# -*- coding: utf-8 -*-
# yt channel: Dragon Xploiters 
##
import time
from core.misc import *
from core.onlen import *

clearscreen()
logo()
print """
Select an Attack:
  01) Create a Netcat Payload and Listener
  02) Facebook Group Hijack Attack
  03) SMS Bomber Attack Vectors
  04) SMS Spoof Attack Vectors
  05) Wifi jamming (DDOS)
  
  00) Exit 
"""
claymore = raw_input("zombie > ")

if claymore == "01" or claymore == "1":
	netcat_rat()
elif claymore == "02" or claymore == "2":
	facebookgroup_hijack()
elif claymore == "03" or claymore == "3":
	sms_bomber_jdid()
elif claymore == "04" or claymore == "4":
	sms_spoof_elk()
elif claymore == "05" or claymore == "5":
	denialofservice_attack()
else:
	print "\nERROR: Wrong Input..."
	time.sleep(2)
	restart_program()