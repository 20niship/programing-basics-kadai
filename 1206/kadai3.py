import statistics
import random

class RandomWalk:
    def __init__(self, p, x0):
        self.p = p
        self.x0 = x0

    def calc_stats(self, n, m):
        return mean, var



rw = RandomWalk(p = 0.6, x0 = 0)
traj = rw.gen_traj(1000)
(mean, var) = rw.calc_stats(100, 10000)
