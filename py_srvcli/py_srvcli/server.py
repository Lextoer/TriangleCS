#!/usr/bin/env python3

from py_srvcli.srv import Triangle
from py_srvcli.msg import Dimensions
import rclpy
from rclpy.node import Node


class TriangleAreaService(Node):
    def __init__(self):
        super().__init__('triangle_area_service')
        self.srv = self.create_service(
            Triangle, 'calculate_area', self.calculate_area_callback
        )
        self.get_logger().info('Triangle Area Service is ready.')

    def calculate_area_callback(self, request, response):
        dimensions = request.dimensions
        response.area = 0.5 * dimensions.base * dimensions.height
        self.get_logger().info(
            f'Received dimensions - base: {dimensions.base}, height: {dimensions.height}, area: {response.area}'
        )
        return response


def main():
    rclpy.init()
    node = TriangleAreaService()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()