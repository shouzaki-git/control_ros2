import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class DirectionSubscriber(Node):
    def __init__(self):
        super().__init__('direction_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        
        # Arduinoとのシリアル通信の設定 (ポートとボーレートを適切に設定)
        self.ser = serial.Serial('/dev/ttyACM0', 9600)# ポート名を適切に設定
        self.get_logger().info('Serial connection established.')

    def listener_callback(self, twist):
        # Twistメッセージから線形速度と角速度を取得
        linear_x = twist.linear.x
        angular_z = twist.angular.z


        # 速度データをArduinoに送信 (例: "L:0.5,A:0.2\n" のようなフォーマットで送信)
        command = f'L:{linear_x:.2f},A:{angular_z:.2f}\n '
        #self.ser.white(command.encode()) #シリアル通信で送信
        self.get_logger().info(f'Sent to Arduino: {command}')

def main(args=None):
    rclpy.init(args=args)
    node = DirectionSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
