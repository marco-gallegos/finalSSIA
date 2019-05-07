# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from ORM import Optimizacion

nombre_funcion = "sphere"
limite_inferior = 0
limite_superior = 2


def fitness(x,d=1):
    # print(x);
    z = 0
    for alelo in x:
        z += alelo ** 2
    return z


def de(fobj, bounds, mut=0.8, crossp=0.7, popsize=20, its=1000):
    dimensions = len(bounds)
    pop = np.random.randint(limite_inferior, limite_superior, (popsize, dimensions))
    min_b, max_b = np.asarray(bounds).T
    diff = np.fabs(min_b - max_b)
    pop_denorm = min_b + pop * diff
    fitness = np.asarray([fobj(ind) for ind in pop_denorm])
    best_idx = np.argmin(fitness)
    best = pop_denorm[best_idx]
    for i in range(its):
        for j in range(popsize):
            idxs = [idx for idx in range(popsize) if idx != j]
            a, b, c = pop[np.random.choice(idxs, 3, replace = False)]
            mutant = np.clip(a + mut * (b - c), 0, 1)
            cross_points = np.random.rand(dimensions) < crossp
            if not np.any(cross_points):
                cross_points[np.random.randint(0, dimensions)] = True
            trial = np.where(cross_points, mutant, pop[j])
            trial_denorm = min_b + trial * diff
            f = fobj(trial_denorm)
            if f < fitness[j]:
                fitness[j] = f
                pop[j] = trial
                if f < fitness[best_idx]:
                    best_idx = j
                    best = trial_denorm
        # print(str(f"genracion : {i} dimension : {dimensions} performance : {fobj(best)}"))
        yield best, fitness[best_idx]


# for d in [2, 4, 8, 16]:
for d in [4]:
    it = list(de(fitness, [(limite_inferior, limite_superior)] * d, its=4000))
    x, f = zip(*it)

    # plt.plot(f, label='d={}'.format(d))
# plt.legend()
# plt.show()