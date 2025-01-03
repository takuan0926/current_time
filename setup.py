from setuptools import setup

package_name = 'current_time_publisher'

setup(
    name=package_name,
    version='0.0.1',
    packages=['current_time_publisher'],
    install_requires=['setuptools', 'rclpy', 'std_msgs'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your-email@example.com',
    description='A ROS2 node that publishes current time on a topic.',
    license='BSD',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'time_publisher = current_time_publisher.time_publisher:main',
        ],
    },
)
