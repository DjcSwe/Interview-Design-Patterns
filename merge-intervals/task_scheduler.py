def least_time(tasks, n):
    frequencies = {}

    for t in tasks:
        frequencies[t] = frequencies.get(t,0) + 1

    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    max_freq = frequencies.popitem()[1]
    idle_time = (max_freq - 1) * n

    while frequencies and idle_time > 0:
        idle_time -= min(max_freq - 1, frequencies.popitem()[1])
    idle_time = max(0, idle_time)

    return len(tasks) + idle_time

# Driver code
def least_time_test():
    all_tasks = [['A', 'A', 'B', 'B'],
                 ['A', 'A', 'A', 'B', 'B', 'C', 'C'],
                 ['S', 'I', 'V', 'U', 'W', 'D', 'U', 'X'],
                 ['M', 'A', 'B', 'M', 'A', 'A', 'Y', 'B', 'M'],
                 ['A', 'K', 'X', 'M', 'W', 'D', 'X', 'B', 'D', 'C', 'O', 'Z', 'D', 'E', 'Q']]
    all_ns = [2, 1, 0, 3, 3]

    for i in range(len(all_tasks)):
        print(i+1, '.', '\tTasks: ', all_tasks[i], sep='')
        print('\tn: ', all_ns[i], sep='')
        min_time = least_time(all_tasks[i], all_ns[i])
        print('\tMinimum time required to execute the tasks: ', min_time)
        print('-' * 100)