# IGVC Competition code

This is the code for the Rutgers IGVC robotics club, a member of Rutgers IEEE. We make an autonomously driven vehicle designed to navigate a track of various obstacles and constraints, among other things. Our task is the make a robot that will navigate this track efficiently and without human aid. 

## Installation

The Ubuntu version is 20.04, and the ROS version is noetic. To run the code, put the package into the src directory. Then, run:

```bash
catkin_make
```
(it may be necessary to create an extra "temporary" package then run catkin_make because catkin doesn't recognize the package you put in directly)

Finally, run:

```bash
source devel/setup.bash
```

## Running the Simulation

Go to the user's directory and put the necessary models in the .gazebo/models folder.

To run the simulation, use the command

```bash
roslaunch igvc display.launch
```

This will initialize your robot in rviz as well as set up all the necessary nodes and topics for the robot to function. It also generates a world in gazebo with accordance with the testWorld.world file in the /igvc/worlds directory.

The nodes responsible for movement of the robot are initialized separately as so:

```bash
python3 src/igvc/scripts/houghLines.py
python3 src/igvc/scripts/movement.py
```

We make use of various OpenCV libraries to process the image, then we send that data to a movement node that controls the robot. 

## Competition

![image](https://github.com/user-attachments/assets/6281bd20-9f6c-4c79-a98e-cac00979c380)
![image](https://github.com/user-attachments/assets/012ade39-81c1-4ca6-ad4e-872e6dca8f61)
![image](https://github.com/user-attachments/assets/740c576d-eab8-43c6-88ce-4f2fb41184a0)



## OpenCV Library

This program makes extensive use of the OpenCV library. OpenCV is an open source computer vision library that aids in the creation of real-time computer vision projects. 

## The Robot

## Results

## Go Rutgers!

