import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from std_msgs.msg import String

class DirectionPublisher(Node):
    def __init__(self):
        super().__init__('direction_publisher')
        self.publisher_ = self.create_publisher(String, 'direction', 10)
        self.subscription = self.create_subscription(
            Joy,
            'joy',
            self.joy_callback,
            10)
        self.subscription  # prevent unused variable warning

    def joy_callback(self, msg):
        if msg.buttons[0]:  # 例えば、Aボタンで前進
            direction = 'w'
        elif msg.buttons[1]:  # Bボタンで後退
            direction = 's'
        elif msg.buttons[2]:  # Xボタンで左
            direction = 'a'
        elif msg.buttons[3]:  # Yボタンで右
            direction = 'd'
        else:
            direction = ''

        if direction:
            string_msg = String()
            string_msg.data = direction
            self.publisher_.publish(string_msg)
            self.get_logger().info(f'Sent: {direction}')

def main(args=None):
    rclpy.init(args=args)
    node = DirectionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
