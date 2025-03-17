#!usr/bin/env python3

from rclpy.node import Node
import rclpy
from std_msgs.msg import String


class MessagePublisher(Node):
    def __init__(self):
        super().__init__("publisher_node")
        self.publisher_ = self.create_publisher(String,"message_from_publisher",10)
        self.counter = 0
        timmer = self.create_timer(1.0,self.publisher_message)

    def publisher_message(self):
        msg=String()
        msg.data=f"Hello! ROS2 is fun. {self.counter}"
        self.publisher_.publish(msg)
        self.counter +=1
        self.get_logger().info(f"Message has been sent: {msg.data}")

def main(args=None):

    rclpy.init(args=args)
    node=MessagePublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()























