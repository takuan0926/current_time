import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime

class TimePublisher(Node):
    def __init__(self):
        super().__init__('time_publisher')
        self.publisher_ = self.create_publisher(String, 'current_time', 10)
        self.timer = self.create_timer(1.0, self.publish_current_time)  # 1秒ごとに時刻を配信
        self.get_logger().info('Time Publisher Node has started.')

    def publish_current_time(self):
        msg = String()
        msg.data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 現在時刻をフォーマットしてメッセージにセット
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    time_publisher = TimePublisher()
    rclpy.spin(time_publisher)
    time_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

