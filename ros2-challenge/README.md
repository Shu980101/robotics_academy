# ROS2-challenge
In this part, the example will show how to launch a robot and navigate in gazebo environment.//
[Example_video](https://youtu.be/2Wvg0Y5iKvc)
### Environment

ROS2: Humble
Ubuntu: 22.04

### Installation

Ros2 installation refers to this [LINK](https://docs.ros.org/en/humble/Installation.html)

### Part 1 - a

#### Step 1 - Setup workspace

Build up the workspace with the following commands:

````
mkdir ros2_ws
cd ros2_ws
mkdir src
colcon build
````

#### Step 2 - Create a package 
Inside the ros2_ws:
````
cd src/
ros2 pkg create publisher_subscriber_nodes --build-type ament_python --dependencies rclpy
````

#### Step 3 - Create nodes:

1. In the /ros2_ws/src/publisher_subscriber_nodes/publisher_subscriber_nodes folder, you can create your publisher and subscriber nodes.

2. Add the following to the setup.py:

````
"publisher = publisher_subscriber_nodes.publisher:main",
"subscriber = publisher_subscriber_nodes.subscribers:main"
````

3. build the workspace and source it with the following command.
````
cd ~/ros2_ws
colcon build
source install/setup.bash
````

4. Run the nodes in different terminals:

````
ros2 run publisher_subscriber_nodes publisher
````
````
ros2 run publisher_subscriber_nodes subscriber
````

### Part 1 - b

#### Step 1 -  Install TurtleBot 4 Simulator

Ubuntu 22.04 with ROS 2 Humble

````
sudo apt install ros-humble-turtlebot4-simulator ros-humble-irobot-create-nodes
````

#### Step 2 - Install Dev Tools

````
sudo apt install ros-dev-tools
````


#### Step 3 - Ignition Fortress must be installed:

````
sudo apt-get update && sudo apt-get install wget
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update && sudo apt-get install ignition-fortress
````


#### Step 4 - Running synchronous SLAM with Nav2:

````
ros2 launch turtlebot4_ignition_bringup turtlebot4_ignition.launch.py slam:=true nav2:=true rviz:=true
````

### Part 2 - a

#### Step 1 -  Run the turtlebot4 launch file:

````
ros2 launch turtlebot4_ignition_bringup turtlebot4_ignition.launch.py slam:=true nav2:=true rviz:=true
````

#### Step 2 -  Define the waypoints in Rvizs:

1. Click play bottom at the bottom left, and undock the turtlebot4 at the right panel.

2. In Rviz, click waypoint/Nav Through Poses Mode at bottom left, and use Nav2 Goal on the top to define where you want the turtlebot4 to go.

3. Click Start Nav Through Poses at the bottom left to start.

## Reference

[ROS2 Installation](https://docs.ros.org/en/humble/Installation.html)
[Nav2 Installation](https://docs.nav2.org/getting_started/index.html#installation)
[Turtlebot4 Installation](https://turtlebot.github.io/turtlebot4-user-manual/software/turtlebot4_simulator.html)






