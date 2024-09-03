import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DirectionPublisher(Node):
    def __init__(self):
        super().__init__('direction_publisher')
        self.publisher_ = self.create_publisher(String, 'direction', 10)
        self.get_logger().info('Press w/a/s/d to send direction commands.')
        self.timer = self.create_timer(0.1, self.get_keyboard_input)

    def get_keyboard_input(self):
        direction = input()  # ユーザーからの入力を取得
        if direction in ['w', 'a', 's', 'd']:
            msg = String()
            msg.data = direction
            self.publisher_.publish(msg)
            self.get_logger().info(f'Sent: {direction}')
        else:
            self.get_logger().info('Invalid input, use w/a/s/d')

def main(args=None):
    rclpy.init(args=args)
    node = DirectionPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()