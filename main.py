import gym

import numpy

if __name__ == '__main__':
    env = gym.make('CarRacing-v0')
    env.reset()
    for i in range(10000):
        env.render()
        env.step(env.action_space.sample())
    env.close()
