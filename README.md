# IGVC Competition code

This is the code for the Rutgers IGVC robotics club, a child club of IEEE. We make an autonomously driven vehicle designed to navigate a track of various obstacles and constraints, among other things. Our task is the make a robot that will navigate this track efficiently and without human aid. 

## Installation

The Ubuntu version is 20.04, and the ROS version is noetic. To run the code, just put the package in the src directory of your chosen workspace and run the command

'''bash
catkin_make
'''

Also, every time you open a new terminal run

'''bash
source devel/setup.bash
'''

to source the directory

## Running the Simulation

_Warning: Display.launch will not properly launch the gazebo world without the necessary my_ground_plane gazebo model placed in the /.gazebo/models folder. This is a separate folder not part of this repository._

To run the simulation, use the command

'''bash
roslaunch igvc display.launch
'''

This will initialize your robot in rviz as well as set up all the necessary nodes and processes for the robot to function. It also generates a world in gazebo with accordance with the testWorld.world file in the /igvc/worlds directory

The nodes responsible for movement of the robot are initialized separately as so:

'''bash
python3 src/igvc/scripts/houghLines.py
python3 src/igvc/scripts/movement.py
'''

We make use of various OpenCV libraries to process the image, then we send that data to a movement node that controls the robot. 
