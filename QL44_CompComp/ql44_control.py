# coding: utf-8
#
# QL44 籾播きホバークラフト用コンパニオンコンピュータ
#　　・RaspberryPi上のdronekit-pythonで動作
#　　・コンパニオンコンピュータはNAVIO2
#　　・
#
# Import DroneKit-Python
from dronekit import connect, VehicleMode
import time
#import math
#from pymavlink import mavutil








#
print "QL44 Momimaki Hovercraft companion computer on dronekit-python"
#
connection_string = "127.0.0.1:14552"       #udp
#
# Connect to the Vehicle.
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)


# 設定を読み出す。
# もしくはフライトコントローラー側に保存している設定を読み出す。


def set_momiokuri_






while True:
    #
    # Get some vehicle attributes (state)
    print "groundspeed : %s" % vehicle.groundspeed
    '''
    print "Get some vehicle attribute values:"
    print " GPS: %s" % vehicle.gps_0
    print " Battery: %s" % vehicle.battery
    print " Last Heartbeat: %s" % vehicle.last_heartbeat
    print " Is Armable?: %s" % vehicle.is_armable
    print " System status: %s" % vehicle.system_status.state
    print " Mode: %s" % vehicle.mode.name # settable
    '''
    time.sleep(0.1)


# Close vehicle object before exiting script
vehicle.close()
print("Completed")