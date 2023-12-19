def validate_solution(instance_file, solution_file):
    # Wczytanie danych wejściowych
    with open(instance_file, "r") as instance:
        n = int(instance.readline().strip())
        jobs = [list(map(int, line.split())) for line in instance]

    # Wczytanie danych wyjściowych
    with open(solution_file, "r") as solution:
        expected_ewdw = int(solution.readline().strip())
        job_sequence = list(map(int, solution.readline().split()))

    if len(job_sequence) != n:
        print("Błędna liczba zadań w sekwencji!")
        return False

    completion_times = [0] * 4
    total_ewdw = 0
    ew, dw = 0, 0

    for job_index in job_sequence:
        job_data = jobs[job_index - 1]

        completion_times[0]+= job_data[0]
        for machine in range(1, 4):
            completion_times[machine] = max(completion_times[machine], completion_times[machine-1]) + job_data[machine]
            timer = job_data[4] - completion_times[3] 
        if (timer > 0):
            ew += (timer * job_data[5])
        else:
            dw += (-timer) * job_data[6]
    total_ewdw += ew + dw

    print("Oczekiwana suma ważonego wyprzedzenia i opóźnienia:", expected_ewdw)

    if total_ewdw != expected_ewdw:
        print("Błędna suma ważonego wyprzedzenia i opóźnienia! total:", total_ewdw, 'expected:', expected_ewdw)
        return False

    return True

# Przykład użycia
instance_file = "in_5.txt"
solution_file = "out_5.txt"
result = validate_solution(instance_file, solution_file)
if result:
    print("Rozwiązanie jest poprawne.")
