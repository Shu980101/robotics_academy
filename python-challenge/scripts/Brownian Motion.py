import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arena_size = 10
robot_position = np.array([arena_size / 2, arena_size / 2])
robot_direction = np.random.uniform(0, 2 * np.pi)
step_size = 0.5

def move_robot():
    global robot_position, robot_direction
    new_position = robot_position + step_size * np.array([np.cos(robot_direction), np.sin(robot_direction)])
    
    if new_position[0] <= 0 or new_position[0] >= arena_size or new_position[1] <= 0 or new_position[1] >= arena_size:
        robot_direction = np.random.uniform(0, 2 * np.pi)
    else:
        robot_position[:] = new_position  

fig, ax = plt.subplots()
ax.set_xlim(0, arena_size)
ax.set_ylim(0, arena_size)
robot_dot, = ax.plot([], [], 'bo', markersize=10)

def init():
    robot_dot.set_data([], [])
    return robot_dot,

def update(frame):
    move_robot()
    robot_dot.set_data(robot_position[0], robot_position[1])
    return robot_dot,

ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True)
plt.show()
