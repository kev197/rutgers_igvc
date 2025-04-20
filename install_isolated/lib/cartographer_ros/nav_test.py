#!/usr/bin/env python

import rospy
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped, Point
from std_msgs.msg import Header
import numpy as np
import heapq

class PathPlanner:
    def __init__(self):
        # Initialize the node
        rospy.init_node("path_planner_node")

        # Parameters for start and goal positions
        self.start = (78, 420)  # Set your starting point
        self.goal = (145, 230)  # Set your goal point

        # Subscriber to /map topic
        rospy.Subscriber("/map", OccupancyGrid, self.map_callback)

        # Publisher for the planned path
        self.path_pub = rospy.Publisher("/planned_path", PoseStamped, queue_size=10)

        # Variable to hold the map data
        self.map_data = None

    def map_callback(self, msg):
        rospy.loginfo("Received map data")
        self.map_data = msg
        self.plan_path()

    def plan_path(self):
        if self.map_data is None:
            rospy.logwarn("No map data available yet.")
            return

        # Get map dimensions and resolution
        width = self.map_data.info.width
        height = self.map_data.info.height
        print(width)
        print(height)
        resolution = self.map_data.info.resolution
        origin = (self.map_data.info.origin.position.x, self.map_data.info.origin.position.y)

        # Convert map data to a numpy array
        grid = np.array(self.map_data.data, dtype=np.int8).reshape(height, width)

        # A* Algorithm to find a path
        path = self.a_star(grid, self.start, self.goal)

        rospy.loginfo(f"Start Cell Value: {grid[self.start[1], self.start[0]]}")
        rospy.loginfo(f"Goal Cell Value: {grid[self.goal[1], self.goal[0]]}")

        # Publish path
        if path:
            rospy.loginfo("Path found, publishing...")
            self.publish_path(path, resolution, origin)
        else:
            rospy.logwarn("No path found!")

    def a_star(self, grid, start, goal):
        # A* algorithm implementation
        def heuristic(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        open_set = []
        heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))

        came_from = {}
        g_score = {start: 0}

        while open_set:
            _, current_cost, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                return path[::-1]

            neighbors = self.get_neighbors(current, grid)
            for neighbor in neighbors:
                tentative_g_score = g_score[current] + 1  # Assume cost=1 for each step
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_set, (tentative_g_score + heuristic(neighbor, goal), tentative_g_score, neighbor))

        return None

    def get_neighbors(self, current, grid):
        neighbors = []
        x, y = current
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] == 0:
                neighbors.append((nx, ny))
        return neighbors

    def publish_path(self, path, resolution, origin):
        for point in path:
            x = origin[0] + point[0] * resolution
            y = origin[1] + point[1] * resolution
            pose = PoseStamped()
            pose.header = Header(stamp=rospy.Time.now(), frame_id="map")
            pose.pose.position.x = x
            pose.pose.position.y = y
            self.path_pub.publish(pose)

            # Sleep to allow the robot to process each waypoint
            rospy.sleep(1.0)  # Adjust as needed for robot movement

if __name__ == "__main__":
    try:
        planner = PathPlanner()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
