cmake_minimum_required(VERSION 3.0.2)
project(igvc)

find_package(catkin REQUIRED)
find_package(message_generation)
find_package(std_msgs)

add_message_files(
  FILES
  pair.msg
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/houghLines.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
