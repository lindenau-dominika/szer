def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.read().splitlines()

    num_tasks = int(lines[0])
    tasks_data = [list(map(int, line.split())) for line in lines[1:]]

    return num_tasks, tasks_data


def schedule_jobs(input_file):
    n, jobs = read_input(input_file)

    job_sequence = sorted(range(n), key=lambda job_index: (
        jobs[job_index][4] - sum(jobs[job_index][:4])*jobs[job_index][6],
        jobs[job_index][4] - sum(jobs[job_index][:4])*jobs[job_index][5], 
    ))


    assert len(set(job_sequence)) == n, "Błąd: Zadania nie są unikalne."

    completion_times = [0] * 4
    total_ewdw = 0
    ew, dw = 0, 0

    for job_index in job_sequence:
        job_data = jobs[job_index]

        completion_times[0] += job_data[0]
        for machine in range(1, 4):
            completion_times[machine] = max(completion_times[machine], completion_times[machine-1]) + job_data[machine]

        timer = job_data[4] - completion_times[3]
        if timer > 0:
            ew += (timer * job_data[5])
        else:
            dw += (-timer) * job_data[6]

    total_ewdw += ew + dw

    output_file = 'out_50.txt'
    with open(output_file, 'w') as file:
        file.write(f"{total_ewdw}\n")
        file.write(" ".join(map(lambda x: str(x + 1), job_sequence)))

    print(f"Oczekiwana suma ważonego wyprzedzenia i opóźnienia dla n={n}: {total_ewdw}")
    print(" ".join(map(lambda x: str(x + 1), job_sequence)), total_ewdw)

schedule_jobs('in_148178_50.txt')
