import numpy as np

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    n = int(lines[0])
    data = [list(map(int, line.split())) for line in lines[1:]]
    
    return n, np.array(data)

def calculate_criterion(sequence, processing_times, deadlines, weights):
    n = len(sequence)
    completion_times = np.zeros((4,))
    weighted_earliness = 0
    weighted_tardiness = 0

    for i in range(n):
        job_index = sequence[i] - 1
        machine_times = np.zeros((4,))

        for j in range(4):  # Teraz iterujemy po wszystkich 4 maszynach
            machine_times[j] = max(completion_times[j], machine_times[j]) + processing_times[job_index, j]
            completion_times[j] = machine_times[j]

        tardiness = max(0, completion_times[3] - deadlines[job_index])
        earliness = max(0, deadlines[job_index] - completion_times[3])

        weighted_earliness += weights[job_index, -2] * earliness
        weighted_tardiness += weights[job_index, -1] * tardiness

    return weighted_earliness + weighted_tardiness, sequence

def solve_flow_shop(input_data):
    n, processing_times = input_data

    sorted_jobs = sorted(range(1, n + 1), key=lambda x: sum(processing_times[x - 1]))

    sequence = [sorted_jobs[0]]
    for i in range(1, n):
        if sum(processing_times[sequence[-1] - 1]) <= sum(processing_times[sorted_jobs[i] - 1]):
            sequence.append(sorted_jobs[i])
        else:
            sequence.insert(0, sorted_jobs[i])

    criterion, _ = calculate_criterion(sequence, processing_times, processing_times[:, -3], processing_times[:, -2:])

    return criterion, sequence

def validate_solution_verbose(instance_file, solution_file):
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
        print(f"Job {job_index}:")
        print(f"Processing times: {job_data[:4]}")
        for machine in range(1, 4):
            completion_times[machine] = max(completion_times[machine], completion_times[machine-1]) + job_data[machine]
            timer = job_data[4] - completion_times[3]
            print(f"Machine {machine}: Completion Time = {completion_times[machine]}")
        if timer > 0:
            ew += (timer * job_data[5])
            print(f"Earliness = {ew}")
        else:
            dw += (-timer) * job_data[6]
            print(f"Tardiness = {dw}")
    total_ewdw += ew + dw

    print(f"Oczekiwana suma ważonego wyprzedzenia i opóźnienia dla n={n}: {expected_ewdw}")
    print(f"Obliczona suma ważonego wyprzedzenia i opóźnienia dla n={n}: {total_ewdw}")

    if total_ewdw != expected_ewdw:
        print(f"Błędna suma ważonego wyprzedzenia i opóźnienia dla n={n}! total:{total_ewdw}, expected:{expected_ewdw}")
        return False

    return True

file_path_input = 'in_147567_50.txt'
file_path_output = 'out_50.txt'

input_data = read_input(file_path_input)

result_criterion, result_sequence = solve_flow_shop(input_data)

print(result_criterion)
print(result_sequence)

validate_solution_verbose(file_path_input, file_path_output)

def write_output(file_path, criterion, sequence):
    with open(file_path, 'w') as file:
        file.write(f"{int(criterion)}\n")
        file.write(" ".join([f"{i}" for i in sequence]) + "\n")

write_output(file_path_output, result_criterion, result_sequence)
