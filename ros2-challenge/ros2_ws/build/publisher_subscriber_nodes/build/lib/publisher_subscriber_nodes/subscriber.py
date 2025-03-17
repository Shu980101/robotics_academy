#!usr/bin/env python3

from rclpy.node import Node
import rclpy
from std_msgs.msg import String


class MessageSubscriber(Node):
    def __init__(self):
        super().__init__("publisher_node")
        self.subscriber_ = self.create_subscription(String,"message_from_publisher",self.subscriber_callback,10)
        

    def subscriber_callback(self, msg):
        self.get_logger().info(f"Message received: {msg.data}")

def main(args=None):

    rclpy.init(args=args)
    node=MessageSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()

