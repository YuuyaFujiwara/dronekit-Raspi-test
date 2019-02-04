# coding: utf-8
#
# QL44 籾播きホバークラフト用コンパニオンコンピュータ
#　　・RaspberryPi上のdronekit-pythonで動作
#　　・コンパニオンコンピュータはNAVIO2
#　　・
#
# Import DroneKit-Python
from dronekit import connect, VehicleMode
from pymavlink import mavutil
from ql44_my_vehicle import MyVehicle #Our custom vehicle class
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
vehicle = connect(connection_string, wait_ready=True, vehicle_class=MyVehicle)


# 設定を読み出す。
# もしくはフライトコントローラー側に保存している設定を読み出す。


# SERVO_CHに値を設定する。
def set_servo_ch( servo_ch, servo_val ):
    #MAVLinkコマンドメッセージを生成する
    msg = vehicle.message_factory.command_long_encode(
        0, 0,   #ターゲットシステム、コンポーネント
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO, #コマンド
        0,  #confirmation 
        servo_ch,   # param1 servo_number
        servo_val,  # param2 PWM (microseconds, 1000 to 2000 typical)
        0, 0, 0, 0, 0)  # param 3 ~ 7 not used

    # MAVLinkメッセージ送信
    vehicle.send_mavlink(msg)


# 速度に応じて籾送りCHのPWM値を制御する。
def set_momiokuri_PWM():
    # 籾送り制御CH
    momiokuri_ch = 8

    # 速度
    ship_spd = vehicle.groundspeed

    # pwm値作る
    # 速度 0～10m/sより pwm 1000～2000を生成する。
    if( ship_spd > 10.0 ): 
        ship_spd = 10.0
    momiokuri_pwm =  ship_spd * 100.0 + 1000

    # サーボCH設定
    set_servo_ch( momiokuri_ch, momiokuri_pwm )


# groundspeed変化時のコールバック
# デコレーターなので登録せずにコールバックされる
@vehicle.on_attribute('groundspeed')  
def decorated_groundspeed_callback(self, attr_name, value):
    print(" PARAMETER CALLBACK: %s changed to: %s" % (attr_name, value))
    # 速度に応じて籾送りCHのPWM値を制御する。
    # set_momiokuri_PWM()


# サーボ出力変更時のコールバック
# デバッグ用に表示する。
@vehicle.on_attribute('servo_output_raw')  
def servo_output_raw_callback( self, attr_name, value ):
    # attr_name == 'servo_output_raw'
    # value == vehicle.servo_output_raw
    print(value)

#vehicle.add_attribute_listener('servo_output_raw', servo_output_raw_callback)


while True:
    #
    # Get some vehicle attributes (state)
    #print "groundspeed : %s" % vehicle.groundspeed
    '''
    print "Get some vehicle attribute values:"
    print " GPS: %s" % vehicle.gps_0
    print " Battery: %s" % vehicle.battery
    print " Last Heartbeat: %s" % vehicle.last_heartbeat
    print " Is Armable?: %s" % vehicle.is_armable
    print " System status: %s" % vehicle.system_status.state
    print " Mode: %s" % vehicle.mode.name # settable
    '''

    '''
    # 速度に応じて籾送りCHのPWM値を制御する。
    set_momiokuri_PWM()
    '''
'''
    set_servo_ch( 7, 1000 )
    time.sleep(1)

    set_servo_ch( 6, 1500 )
    time.sleep(1)

    set_servo_ch( 5, 2000 )
    '''
    time.sleep(1)


# Close vehicle object before exiting script
vehicle.close()
print("Completed")