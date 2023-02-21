from setuptools import setup
import os
from glob import glob

package_name = 'chess_manipulator'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #Add all xacro and URDF files that descripe the robot to the share directory
        (os.path.join('share',package_name,'description'),glob('description/*.xacro')),
        #Adding visual and collision mehses to the share directory
        (os.path.join('share',package_name,'meshes','visual'),glob('meshes/visual/*.dae')),
        (os.path.join('share',package_name,'meshes','collision'),glob('meshes/collision/*.stl')),
        #Adding Rviz2 configuration files
        (os.path.join('share',package_name,'rviz'),glob('rviz/*.rviz')),
        #Adding launch files
        (os.path.join('share',package_name,'launch'),glob('launch/*.launch.*')),
       
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Zein Alabedeen Barhoum and Rahaf Alshaowa',
    maintainer_email='zein.barhoum799@gmail.com',
    description='Franka Emika Panda manipulator playing chess',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)