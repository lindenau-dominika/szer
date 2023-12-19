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
        job_index = sequence[i]
        machine_times = np.zeros((4,))

        for j in range(4):
            machine_times[j] = max(completion_times[j], machine_times[j]) + processing_times[job_index, j]
            completion_times[j] = machine_times[j]

        tardiness = max(0, completion_times[3] - deadlines[job_index])
        earliness = max(0, deadlines[job_index] - completion_times[3])

        weighted_earliness += weights[job_index, -2] * earliness
        weighted_tardiness += weights[job_index, -1] * tardiness

    return weighted_earliness + weighted_tardiness, sequence

def solve_flow_shop(input_data):
    n, processing_times = input_data

    sorted_jobs = sorted(range(n), key=lambda x: sum(processing_times[x]))

    sequence = [sorted_jobs[0]]
    for i in range(1, n):
        if sum(processing_times[sequence[-1]]) <= sum(processing_times[sorted_jobs[i]]):
            sequence.append(sorted_jobs[i])
        else:
            sequence.insert(0, sorted_jobs[i])

    criterion, _ = calculate_criterion(sequence, processing_times, processing_times[:, -3], processing_times[:, -2:])

    return criterion, sequence

def write_output(file_path, criterion, sequence):
    with open(file_path, 'w') as file:
        file.write(f"{int(criterion)}\n")
        file.write(" ".join([f"{i+1}" for i in sequence]) + "\n")

file_path_input = 'input_100.txt'
file_path_output = 'output_100.txt'

input_data = read_input(file_path_input)

result_criterion, result_sequence = solve_flow_shop(input_data)

print(result_criterion)
print(result_sequence)

write_output(file_path_output, result_criterion, result_sequence)
