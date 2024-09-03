from setuptools import find_packages, setup

package_name = 'control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='shouzaki',
    maintainer_email='sho.uzaki@icloud.com',
    description='A package for controlling',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_node = control.pub_node:main',
            'sub_node = control.sub_node:main',
            'control_node = control.control_node:main'
        ],
    },
)
