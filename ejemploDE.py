import numpy as np
import matplotlib.pyplot as plt

nombre_funcion = "x"
limite_inferior = 0
limite_superior = 2


def fitness(x):
    # print(x)
    # print(type(x))
    z = 0
    for alelo in x:
        if alelo:
            z += 1
    if z < 2:
        return 1000
    else:
        return z


def de(fobj, bounds, mut=1, crossp=0.7, popsize=20, its=1000):
    dimensions = len(bounds)
    # generar poblacion
    # pop = np.random.rand(popsize, dimensions)
    pop = np.random.randint(limite_inferior, limite_superior, (popsize, dimensions))
    min_b, max_b = np.asarray([(0,1)] * 8).T
    print(f"min_b : {min_b}    max_b : {max_b}")
    diff = np.fabs(min_b - max_b)
    print(diff)
    pop_denorm = min_b + pop * diff
    print(pop_denorm)
    fitness = np.asarray([fobj(ind) for ind in pop_denorm])
    best_idx = np.argmin(fitness)
    best = pop_denorm[best_idx]
    
    
    for i in range(its):
        for j in range(popsize):
            idxs = [idx for idx in range(popsize) if idx != j]
            a, b, c = pop[np.random.choice(idxs, 3, replace = False)]
            # print(f"a {a}  b {b}  c {c}")
            mutant = np.clip(a + mut * (b - c), 0, 1)
            # print(mutant)
            cross_points = np.random.rand(dimensions) < crossp
            # print(cross_points)
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
        if i % 100 == 0:
            print("El MEjor De La GEneracion  :  ", end="")
            print(best)
            print(str(f"genracion : {i} dimension : {dimensions} performance : {fobj(best)}"))

        yield best, fitness[best_idx]


# for d in [2, 4, 8, 16]:
for d in [8]:
    for i in range(1):
        it = list(de(fitness, [(limite_inferior, limite_superior)] * d, its=1000))
        x, f = zip(*it)

    plt.plot(f, label='d={}'.format(d))
plt.legend()
plt.show()
