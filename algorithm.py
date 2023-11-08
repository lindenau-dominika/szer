# Funkcja do wczytywania danych z pliku wejściowego
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()
    num_tasks = int(lines[0])
    tasks_data = [list(map(int, line.split())) for line in lines[1:num_tasks + 1]]
    setup_times = [list(map(int, line.split())) for line in lines[num_tasks + 1:]]
    return num_tasks, tasks_data, setup_times


# Funkcja do obliczania Lmax na podstawie ustalonej kolejności zadań
def calculate_Lmax(order, tasks_data, setup_times):
    n = len(order)
    C = [0] * n  # Czas zakończenia dla każdego zadania
    L = [0] * n  # Spóźnienie dla każdego zadania

    for i in range(n):
        task_index = order[i]
        processing_time = tasks_data[task_index][0]
        due_date = tasks_data[task_index][1]
        setup_time = setup_times[order[i - 1]][task_index] if i > 0 else 0
        C[i] = (C[i - 1] if i > 0 else 0) + processing_time + setup_time
        L[i] = max(0, C[i] - due_date)

    return max(L)


# Funkcja heurystyczna do ustalania kolejności zadań
def heuristic_schedule_weighted(tasks_data, alpha=0.2):
    n = len(tasks_data)
    jobs = list(range(n))
    weighted_scores = []

    for job in jobs:
        processing_time = tasks_data[job][0]
        due_date = tasks_data[job][1]
        weighted_due_date = (1 - alpha) * due_date
        weighted_processing_time = alpha * processing_time
        score = weighted_due_date + weighted_processing_time
        weighted_scores.append((score, job))

    # Sortowanie zadań na podstawie ich wyników ważonych
    weighted_scores.sort()
    ordered_jobs = [job for score, job in weighted_scores]

    return ordered_jobs


# Główna funkcja rozwiązująca problem
def solve(index, n):
    input_file = f'instancje/in_{index}_{n}.txt'
    num_tasks, tasks_data, setup_times = read_input(input_file)
    ordered_jobs = heuristic_schedule_weighted(tasks_data)
    Lmax = calculate_Lmax(ordered_jobs, tasks_data, setup_times)

    result_file = f'wyniki/out_{index}_{n}.txt'
    with open(result_file, 'w') as file:
        file.write(str(Lmax) + '\n')
        file.write(' '.join(str(job + 1) for job in ordered_jobs))


# Uruchomienie programu dla przykładowego pliku wejściowego
indices = [148163, 148066, 145442, 144441, 148144, 148160, 147567, 148178, 148239, 148410, 147414]
sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

for index in indices:
    for n in sizes:
        solve(index, n)



# def solve(input_file):
#     num_tasks, tasks_data, setup_times = read_input(input_file)
#     ordered_jobs = heuristic_schedule_weighted(tasks_data)
#     Lmax = calculate_Lmax(ordered_jobs, tasks_data, setup_times)

#     result_file = 'output.txt'
#     with open(result_file, 'w') as file:
#         file.write(str(Lmax) + '\n')
#         file.write(' '.join(str(job + 1) for job in ordered_jobs))


# # Uruchomienie programu dla przykładowego pliku wejściowego
# solve('instances/in_147567_500.txt')