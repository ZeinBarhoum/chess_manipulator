To complete this project, I did the following:
1. Prepare the manipulator's description:
      - Main URDF for the manipulator's arm
      - Custom End Effictor URDF
      - Manipulator's URDF that includes the former two
      - Added plugins for Gazebo and ros-control to be able to simulate and control the manipulator

2. Prepare the controllers config file:
    -  JointStateBroadcaster
    -  JointTrajectoryController with `position` command interface
3. Create the launch files:
      - Launch Gazebo with the custom world I created that includes a chessboard
      - spawn the manipulator
      - spwn the controller and broadcaster
4. Some utils:
      - Create a class for the manipulator
      - Define a class's method to convert a path (end effector) to joint angles
      - Define a class's method to exectute to plan a path from one position to another and execute it (publish to the control topics)
5. Control the manipulator to play chess !!
      - Create a python file and define some movements like go to the first peace and move it and so on.
      - TODO: integrate stockfish to let it decide what to play
