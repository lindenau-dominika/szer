import sys

def schedule_jobs(instance_file, result_file):
    with open(instance_file, 'r') as instance:
        n = int(instance.readline().strip())
        machine_speeds = list(map(float, instance.readline().split()))
        tasks = [tuple(map(int, line.split())) for line in instance]

    sorted_tasks = sorted(range(n), key=lambda x: (tasks[x][1] + tasks[x][0]) - tasks[x][2])

    # Przydzielanie zadań do maszyn
    schedules = [[] for _ in range(5)]
    machine_completion_times = [0] * 5
    total_tardiness = 0

    for task_idx in sorted_tasks:
        processing_time, release_time, due_date = tasks[task_idx]

        # Wybieranie maszyny o najwcześniejszym zakończeniu
        selected_machine = min(range(5), key=lambda x: machine_speeds[x])

        # Przydzielanie zadania do maszyny
        schedules[selected_machine].append(task_idx + 1)

        # Aktualizacja czasu zakończenia maszyny z uwzględnieniem czasu opóźnienia
        completion_time = max(machine_completion_times[selected_machine], release_time) + processing_time * machine_speeds[selected_machine]
        machine_completion_times[selected_machine] = completion_time

        # Zliczanie spóźnionych zadań
        if completion_time > due_date:
            total_tardiness += 1

    # Zapis wyniku do pliku
    with open(result_file, 'w') as result:
        # Zapis łącznej liczby spóźnionych zadań jako pierwszej linii pliku wynikowego
        result.write(str(total_tardiness) + "\n")

        # Zapis sekwencji zadań na maszynach
        for schedule in schedules:
            result.write(" ".join(map(str, schedule)) + "\n")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Error: python script.py <instance_file_path> <solution_file_path> <time>")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        time_limit = sys.argv[3]
        schedule_jobs(input_file_path, output_file_path)