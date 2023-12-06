import subprocess
import time
import sys


def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        data = [list(map(int, line.split())) for line in lines[1:n+1]]
        S = [list(map(int, line.split())) for line in lines[n+1:]]
    return n, data, S


def calculate_Lmax(order, data, S):
    n = len(order)
    C = [0] * n
    L = [0] * n
    for i in range(n):
        j = order[i]
        if i > 0:
            C[i] = C[i - 1] + data[j][0] + S[order[i - 1]][j]
        else:
            C[i] = data[j][0]
        L[i] = max(float('-inf'), C[i] - data[j][1])
    return max(L)


def verify_solution(input_file, output_file):
    n, data, S = read_input(input_file)

    with open(output_file, 'r') as file:
        lines = file.read().splitlines()
        reported_Lmax = int(lines[0])
        order = [int(j) - 1 for j in lines[1].split()]  # Assuming tasks are numbered from 1

    if len(set(order)) != n:
        return False, "Each task must occur exactly once."

    calculated_Lmax = calculate_Lmax(order, data, S)

    if calculated_Lmax != reported_Lmax:
        return False, f"Incorrect Lmax. Expected: {reported_Lmax}, obtained: {calculated_Lmax}."

    return True, f"Correct Lmax. Value: {calculated_Lmax}."


def convert_time_limit(time_limit_str):
    try:
        return float(time_limit_str)
    except ValueError:
        print("The time limit must be a number.")
        sys.exit(1)


if len(sys.argv) != 5:
    print("Usage: python run_executable.py executable_path input_filename output_filename time_limit")
    sys.exit(1)

_, executable_path, input_filename, output_filename, time_limit_str = sys.argv

try:
    time_limit = float(time_limit_str)
except ValueError:
    print("The time limit must be a number.")
    sys.exit(1)

start_time = time.time()

try:
    process = subprocess.run([executable_path, input_filename, output_filename, time_limit_str],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             timeout=time_limit,
                             text=True)
except subprocess.TimeoutExpired:
    print(f"Process exceeded the time limit of {time_limit_str} seconds and was terminated.")
    sys.exit(1)

end_time = time.time()

elapsed_time = end_time - start_time

# Verify the correctness of the solution
is_correct, message = verify_solution(input_filename, output_filename)
print(f"{message} Time: {elapsed_time:.4f} seconds")

if process.returncode == 0 and is_correct:
    print("Execution and verification successful.")
    print(process.stdout)
else:
    print("Execution failed or solution is incorrect.")
    if process.stderr:
        print(process.stderr)