# roscore_move

Please note: there is a delay between publishing and the servo moving.
Kind of a major delay.

# Dependencies
1. rpi sensors and its dependencies: https://github.com/bivab/smbus-cffi/blob/master/README.rst
2. servo_control: https://github.com/NoelleTemple/servo_control

Use
```
sudo pip install -e .
```
inside the folder with the setup.py file to properly install python packages

# Pinouts
Raspberry Pi Pinout:

***INSERT RASPBERRY PI PINOUT PIC

The servo I use: Tower Pro Micro Servo 9g SG90
Note that this servo takes duty cycle inputs between 2 and 13 with a frequency of 50 Hz.  

***INSERT SERVO PINOUT PIC

Pinout:
Vin -> pin 2
Ground -> pin 39
Control -> pin 33

Sensor used: VL6180X

***INSERT SENSOR PINOUT PIC

Pinout:
Vin -> pin 1
Ground -> pin 9
SDA -> pin 3
SCL -> pin 5

# Setup Roscore

```
sudo apt install ros-desktop-full ros-desktop-full-dev
sudo apt install build-essential dpkg-dev git 
sudo apt install libopencv-dev liborocos-kdl-dev libompl-dev
```

```
mkdir ~/ros-underlay
cd ~/ros-underlay
rosinstall_generator ros_comm --rosdistro kinetic --exclude RPP --exclude-path /usr/share --deps --wet-only > kinetic_debian_ros_comm.rosinstall
wstool init -j8 src kinetic_debian_ros_comm.rosinstall
cd ~/ros-underlay
catkin_make
```

# Create Workspace

```
cd ~/
source ros-underlay/devel/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
```

# Create Package

```
cd ~/catkin_ws/src
catkin_create_pkg <name of package> std_msgs rospy 
cd <name of package>/src
```
# Create Subscriber and Listener
``` 
cd ~/
git clone https://github.com/NoelleTemple/roscore_move.git
cd roscore_move
cp talker.py ~/catkin_ws/src/<name of package>/src/
cp listener.py ~/catkin_ws/src/<name of package</src/
cd ~/catkin_ws/src/<name of package>/src/
chmod +x listener.py
chmod +x talker.py
```

Each of these commands will need to be run in 3 different windows:
```
roscore
```

```
python listener.py
```

```
python talker.py
```

The servo has a delay, but will move based on the distance an object is from the sensor.  

