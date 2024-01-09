def validate_solution(instance_file, solution_file):
    with open(instance_file, "r") as instance:
        n = int(instance.readline().strip())
        jobs = [list(map(int, line.split())) for line in instance]

    with open(solution_file, "r") as solution:
        expected_ewdw = int(solution.readline().strip())
        job_sequence = list(map(int, solution.readline().split()))

    if len(job_sequence) != n:
        print(f"Błędna liczba zadań w sekwencji dla n={n}!")
        return False

    if len(set(job_sequence)) != n or set(job_sequence) != set(range(1, n + 1)):
        print(f"Niewłaściwa sekwencja zadań dla n={n}! Każde zadanie musi wystąpić dokładnie raz.")
        return False

    completion_times = [0] * 4
    total_ewdw = 0
    ew, dw = 0, 0

    for job_index in job_sequence:
        job_data = jobs[job_index - 1]

        completion_times[0] += job_data[0]
        for machine in range(1, 4):
            completion_times[machine] = max(completion_times[machine], completion_times[machine-1]) + job_data[machine]
            timer = job_data[4] - completion_times[3]
        if timer > 0:
            ew += (timer * job_data[5])
        else:
            dw += (-timer) * job_data[6]
    total_ewdw += ew + dw

    print(f"Oczekiwana suma ważonego wyprzedzenia i opóźnienia dla n={n}: {expected_ewdw}")

    if total_ewdw != expected_ewdw:
        print(f"Błędna suma ważonego wyprzedzenia i opóźnienia dla n={n}! total:{total_ewdw}, expected:{expected_ewdw}")
        return False

    return True

for n in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]:
    instance_file = f"in_148178_{n}.txt"
    solution_file = f"out_{n}.txt"
    result = validate_solution(instance_file, solution_file)
    if result:
        print(f"Rozwiązanie dla n=50 jest poprawne.")
