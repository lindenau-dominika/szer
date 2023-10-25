def read_instance_from_file(filename):
    with open(filename, 'r') as file:
        n = int(file.readline().strip())
        instance = [tuple(map(int, file.readline().split())) for _ in range(n)]
        setup_times = [list(map(int, file.readline().split())) for _ in range(n)]

    return n, instance, setup_times

def read_solution_file(filename):
    with open(filename, 'r') as file:
        lmax = int(file.readline().strip())
        schedule = list(map(int, file.readline().split()))
        return lmax, schedule

def compute_lmax(instance, setup_times, schedule):
    lmax = 0
    time = 0

    for i in range(len(schedule)):
        if i == 0:
            setup_time = 0
        else:
            setup_time = setup_times[schedule[i-1]-1][schedule[i]-1]
        time += setup_time + instance[schedule[i]-1][0]
        delay = time - instance[schedule[i]-1][1]
        lmax = max(lmax, delay)

    return lmax

def main():
    sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

    for n in sizes:
        # Wczytaj instancję
        instance_file = f'instances/in_147567_{n}.txt'
        n, instance, setup_times = read_instance_from_file(instance_file)

        # Wczytaj rozwiązanie
        solution_file = f'solutions/out_50'
        expected_lmax, schedule = read_solution_file(solution_file)

        lmax_computed = compute_lmax(instance, setup_times, schedule)

        # Porównaj wynik obliczony z oczekiwanym wynikiem
        if lmax_computed == expected_lmax:
            print(f'Instance with n={n} is correctly solved. lmax={lmax_computed}')
        else:
            print(f'Instance with n={n} is not correctly solved. Expected lmax={expected_lmax}, computed lmax={lmax_computed}')

if __name__ == "__main__":
    main()
