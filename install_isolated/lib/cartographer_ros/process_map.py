#!/usr/bin/env python3

import rospy
from nav_msgs.msg import OccupancyGrid

def process_map(data):
    # Convert the immutable tuple to a mutable list
    grid_data = list(data.data)

    # Process the grid data
    for i in range(len(grid_data)):
        if grid_data[i] > 40:  # Threshold for occupied space
            grid_data[i] = 100  # Fully occupied
        elif grid_data[i] >= 0:  # Threshold for free space
            grid_data[i] = 0  # Free space

    # Update the OccupancyGrid data with modified values
    data.data = tuple(grid_data)  # Convert back to tuple (if needed)

    # Publish the modified map
    pub.publish(data)

# Initialize the ROS node
rospy.init_node('map_processor')

# Create the publisher for the modified map
pub = rospy.Publisher('/processed_map', OccupancyGrid, queue_size=1)

# Subscribe to the original map topic
sub = rospy.Subscriber('/map', OccupancyGrid, process_map)

# Keep the node alive
rospy.spin()
