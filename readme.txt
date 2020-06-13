To run this project follow the following instructions:
1) Download the carla simulator version 0.9.5 from https://github.com/carla-simulator/carla
2) copy the files in the navigation folder of the repository and paste them in the navigation folder of the carla simulator that is placed in CARLA_0.9.5\PythonAPI\carla\agents\navigation
3) download the deep neural network's weights in https://drive.google.com/drive/folders/1vcpQdDyVd3RHXu_z2uEThS_IJCxPpVCw?usp=sharing and move them to the navigation folder of the repository
3) open the command prompt and change the current directory to CARLA_0.9.5 through: cd CARLA_0.9.5
4) type in command prompt the following: carlaue4 -quality-level=Low
5) carla simulator is supposed to be open by step 4, now open the python IDE and open drive.py file that is placed in CARLA_0.9.5\PythonAPI\carla\agents\navigation to run the project.
6) carla simulator provides ai cars in the environment, if you want to generate the ai cars open the spawn_npc.py file that is placed in CARLA_0.9.5\PythonAPI\carla\agents\navigation