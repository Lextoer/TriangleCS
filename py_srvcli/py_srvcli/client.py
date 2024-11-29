#!/usr/bin/env python3

from py_srvcli.srv import Triangle  # Servis mesajı dosyanızın modül adı
from py_srvcli.msg import Dimensions
import rclpy
from rclpy.node import Node
import math


class TriangleAreaClient(Node):
    def __init__(self):
        super().__init__('triangle_area_client')  # Node adı
        self.cli = self.create_client(
            Triangle, 'calculate_area'
        )  # Servis adı
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')
        self.req = Triangle.Request()

    def send_area_request(self, base, height):
        self.req.dimensions = Dimensions(base=base, height=height)
        future = self.cli.call_async(self.req)
        rclpy.spin_until_future_complete(self, future)
        return future.result()

    def calculate_perimeter(self, a, b, c):
        # Üçgen eşitsizliği kontrolü
        if not (a + b > c and a + c > b and b + c > a):
            self.get_logger().info('Invalid triangle sides. The triangle inequality is not satisfied.')
            return None
        return a + b + c


def main(args=None):
    rclpy.init(args=args)
    node = TriangleAreaClient()

    while True:
        print("\nSelect option:")
        print("A - Area calculation")
        print("P - Perimeter calculation")
        print("0 - Exit")
        
        user_input = input("Enter your choice (A/P/0): ").upper()

        if user_input == "0":
            node.get_logger().info('Exiting client.')
            break
        elif user_input == "A":
            # Alan hesaplama işlemi
            base = float(input('Enter the base of the triangle: '))
            height = float(input('Enter the height of the triangle: '))
            response = node.send_area_request(base, height)
            node.get_logger().info(f'Triangle area: {response.area}')
        elif user_input == "P":
            # Çevre hesaplama işlemi
            a = float(input('Enter the first side length of the triangle: '))
            b = float(input('Enter the second side length of the triangle: '))
            c = float(input('Enter the third side length of the triangle: '))
            perimeter = node.calculate_perimeter(a, b, c)
            if perimeter is not None:
                node.get_logger().info(f'Triangle perimeter: {perimeter}')
        else:
            node.get_logger().info('Invalid choice. Please enter A, P, or 0.')

    rclpy.shutdown()

if __name__ == '__main__':
    main()
