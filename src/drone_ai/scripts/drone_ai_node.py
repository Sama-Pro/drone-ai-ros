#!/usr/bin/env python3
import rospy

def main():
    rospy.init_node('drone_ai_node')  # Register the node with ROS
    rospy.loginfo("🚁 Drone AI Activated 🚁")
    rospy.spin()  # Keep the node alive

if __name__ == '__main__':
    main()
