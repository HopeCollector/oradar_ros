#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

'''
parameters=[
        {'device_model': 'MS200'},
        {'frame_id': 'laser_frame'},
        {'scan_topic': 'MS200/scan'},
        {'port_name': '/dev/oradar'},
        {'baudrate': 230400},
        {'angle_min': 0.0},
        {'angle_max': 360.0},
        {'range_min': 0.05},
        {'range_max': 20.0},
        {'clockwise': False},
        {'motor_speed': 10}
      ]
'''

def generate_launch_description():
  # LiDAR publisher node
  ordlidar_node = Node(
      package='oradar_lidar',
      executable='oradar_scan',
      name='MS200',
      output='screen',
      parameters=[
        PathJoinSubstitution([
            FindPackageShare("oradar_lidar"),
            "launch/ms200.yaml"])
      ],
      # prefix=["gdbserver localhost:3000"]
  )

  # base_link to laser_frame tf node
  base_link_to_laser_tf_node = Node(
    package='tf2_ros',
    executable='static_transform_publisher',
    name='base_link_to_base_laser',
    arguments=['0','0','0.18','0','0','0','base_link','laser_frame']
  )


  # Define LaunchDescription variable
  ord = LaunchDescription()

  ord.add_action(ordlidar_node)
  ord.add_action(base_link_to_laser_tf_node)

  return ord
