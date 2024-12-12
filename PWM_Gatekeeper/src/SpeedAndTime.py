import time
import threading
import pigpio
import collections
import numpy
import rospy
from clover.srv import SetLEDEffect
from sensor_msgs.msg import Range

rospy.init_node('test')

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
    else:
        return None # Handle timeout

pi.set_mode(TRIG, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)
pi.callback(ECHO, pigpio.RISING_EDGE, rise)
pi.callback(ECHO, pigpio.FALLING_EDGE, fall)

history = collections.deque(maxlen=20)  # Keep track of recent measurements

start_time = time.time()
previous_distance = None
previous_time = None

def range_callback(msg):
    global previous_distance, previous_time, start_time
    distance = msg.range

    current_time = time.time()

    if previous_distance is not None and previous_time is not None:
        time_diff = current_time - previous_time
        distance_diff = distance - previous_distance
        if time_diff > 0:
            speed = distance_diff / time_diff
            print(f"Speed: {speed:.2f} m/s")

    previous_distance = distance
    previous_time = current_time

    if (distance < 0.5):
        set_effect(r=255, g=0, b=0)  # Red
    elif (distance >= 0.5 and distance < 1):
        set_effect(r=255, g=255, b=0)  # Yellow
    else:
        set_effect(r=0, g=255, b=0)  # Green


rospy.Subscriber('rangefinder/range', Range, range_callback)

rate = rospy.Rate(10) 

while not rospy.is_shutdown():
    distance = read_distance()
    if distance is not None:
        history.append(distance)
    rate.sleep()