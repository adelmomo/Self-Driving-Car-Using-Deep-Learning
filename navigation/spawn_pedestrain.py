import glob
import os
import sys
import cv2
import numpy as np
import random
try:
    sys.path.append(glob.glob('carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass
import carla
client = carla.Client('127.0.0.1',2000)
client.set_timeout(2.0)
world = client.get_world()
blueprintsWalkers = world.get_blueprint_library().filter("walker.*")
walker_bp = random.choice(blueprintsWalkers)
spawn_points = []
walkers_list=[]

spawn_points = world.get_map().get_spawn_points()
for i in range(len(spawn_points)):
    spawn_point = carla.Transform()
    spawn_point.location = spawn_points[i].location
    if (spawn_point.location != None):
        spawn_points.append(spawn_point)
batch = []
for spawn_point in spawn_points:
    walker_bp = random.choice(blueprintsWalkers)
    batch.append(carla.command.SpawnActor(walker_bp, spawn_point))

# apply the batch
results = client.apply_batch_sync(batch, True)
for i in range(len(results)):
    
        walkers_list.append({"id": results[i].actor_id})
batch = []
walker_controller_bp = world.get_blueprint_library().find('controller.ai.pedestrian')
for i in range(len(walkers_list)):
    batch.append(carla.command.SpawnActor(walker_controller_bp, carla.Transform(), walkers_list[i]["id"]))

# apply the batch
results = client.apply_batch_sync(batch, True)
for i in range(len(results)):
    if results[i].error:
        logging.error(results[i].error)
    else:
        walkers_list[i]["con"] = results[i].actor_id

