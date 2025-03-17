import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shu/robotics_academy/ros2_ws/install/publisher_subscriber_nodes'
