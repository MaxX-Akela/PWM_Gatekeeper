import rospy
import time
import threading
import pigpio
import collections
import numpy
import rospy
from clover.srv import SetLEDEffect 
from sensor_msgs.msg import Range 
from aruco_pose.msg import MarkerArray

rospy.init_node('my_node')

set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect) 

TRIG = 23  # Trig 
ECHO = 24  # Echo 

pi = pigpio.pi()
done = threading.Event()

def rise(gpio, level, tick):
    global high
    high = tick

def fall(gpio, level, tick):
    global low
    low = tick - high
    done.set()

def read_distance():
    global low
    done.clear()
    pi.gpio_trigger(TRIG, 50, 1)
    if done.wait(timeout=5):
        return low / 58.0 / 100.0

pi.set_mode(TRIG, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)
pi.callback(ECHO, pigpio.RISING_EDGE, rise)
pi.callback(ECHO, pigpio.FALLING_EDGE, fall)

history = collections.deque(maxlen=20)  
def read_distance_filtered():
    if (read_distance < 0.5):
        set_effect(r=255, g=0, b=0)    
    if (read_distance >= 0.5 and read_distance <1):
        set_effect(r=255, g=255, b=0)     
    if (read_distance> 1):
        set_effect(r=0, g=255, b=0)

def range_callback(msg):    
    if (msg.range < 0.5):
        set_effect(r=255, g=0, b=0)     
    if (msg.range >= 0.5 and msg.range<1):
        set_effect(r=255, g=255, b=0) 
    if (msg.range > 1):
        set_effect(r=0, g=255, b=0)

rospy.Subscriber('rangefinder/range', Range, range_callback)

def markers_callback(msg):
    for marker in msg.markers:
        if marker.id == 1:
            print('Дрон среднего размера')
        if marker.id == 2:
            print('Дрон большого размера')
        else:
            print('Дрон малого размера')


rospy.Subscriber('aruco_detect/markers', MarkerArray, markers_callback)


rospy.spin()
