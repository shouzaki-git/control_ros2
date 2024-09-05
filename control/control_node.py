import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class JoyControl(Node):
    def __init__(self):
        super().__init__('joy_control')
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.joy_sub = self.create_subscription(Joy, 'joy', self.joy_callback, 10)

    def joy_callback(self, joy_msg):
        twist = Twist()

        # 左スティックで前進/後進
        twist.linear.x = joy_msg.axes[1]  # 前進/後進の速度
        # 右スティックで旋回
        twist.angular.z = joy_msg.axes[0]  # 左右旋回の速度


        self.cmd_vel_pub.publish(twist)
        self.get_logger().info(f"Published Twist: linear.x={twist.linear.x}, angular.z={twist.angular.z}")

def main(args=None):
    rclpy.init(args=args)
    node = JoyControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
