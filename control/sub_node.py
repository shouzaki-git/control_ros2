import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial

class DirectionSubscriber(Node):
    def __init__(self):
        super().__init__('direction_subscriber')
        self.subscription = self.create_subscription(
            String,
            'direction',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.ser = serial.Serial('/dev/ttyACM0', 9600)  # Arduinoと通信するシリアルポート

    def listener_callback(self, msg):
        direction = msg.data
        self.ser.write(direction.encode())  # 受信したデータをArduinoに送信
        self.get_logger().info(f'Received: {direction}')

def main(args=None):
    rclpy.init(args=args)
    node = DirectionSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
