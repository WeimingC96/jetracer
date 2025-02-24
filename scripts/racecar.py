#!/usr/bin/env python3

import rospy
from jetracer.nvidia_racecar import NvidiaRacecar
from std_msgs.msg import Float32

#Initialize car variable and tune settings
car = NvidiaRacecar()
car.steering_gain = 0.65
car.steering_offset = -0.16
car.throttle_gain = 1
car.steering = 0.0
car.throttle = 0.0

pub = rospy.Publisher('test_topic', Float32, queue_size=1)
test = 1

#Throttle
def callback_throttle(throt):
    car.throttle = throt.data
    rospy.loginfo("Throttle: %s", str(throt.data))

#Steering
def callback_steering(steer):
    car.steering = steer.data
    rospy.loginfo("Steering: %s", str(steer.data))

#Setup node and topics subscription
def racecar():
    rospy.init_node('racecar', anonymous=True)
    rospy.Subscriber("throttle", Float32, callback_throttle)
    rospy.Subscriber("steering", Float32, callback_steering)

    #rospy.spin()
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(test)
        r.sleep()

if __name__ == '__main__':
    print("Running racecar.py")
    racecar()
