def schedule_tasks(instance_file, result_file):
    with open(instance_file, 'r') as instance:
        n = int(instance.readline().strip())
        machine_speeds = list(map(float, instance.readline().split()))
        tasks = [tuple(map(int, line.split())) for line in instance]

    # Check if the number of machines matches the expected value (5)
    if len(machine_speeds) != 5:
        print("Error: Incorrect number of machines in the instance file.")
        return

    # Sort tasks by release time and processing time
    sorted_tasks = sorted(enumerate(tasks, 1), key=lambda x: (x[1][1], x[1][0]))

    # Initialize schedules for each machine
    schedules = [[] for _ in range(5)]

    # Schedule tasks using the modified Johnson's algorithm
    for idx, (processing_time, release_time, due_date) in sorted_tasks:
        min_machine_idx = machine_speeds.index(min(machine_speeds))
        max_machine_idx = machine_speeds.index(max(machine_speeds))

        # Assign task to the machine with the minimum completion time
        if machine_speeds[min_machine_idx] * (sum(tasks[j][0] / machine_speeds[j] for j in schedules[min_machine_idx]) + processing_time / machine_speeds[min_machine_idx]) <= machine_speeds[max_machine_idx] * (sum(tasks[j][0] / machine_speeds[j] for j in schedules[max_machine_idx]) + processing_time / machine_speeds[max_machine_idx]):
            schedules[min_machine_idx].append(idx)
        else:
            schedules[max_machine_idx].append(idx)

    # Calculate total tardiness
    total_tardiness = sum(max(sum(tasks[j][0] / machine_speeds[j] for j in schedules[i]) - tasks[idx - 1][2], 0) for i, idx in enumerate([task for sublist in schedules for task in sublist], 1))

    # Write the result to a text file
    with open(result_file, 'w') as result:
        result.write(str(total_tardiness) + "\n")
        for schedule in schedules:
            result.write(" ".join(map(str, schedule)) + "\n")

# Przykład użycia
instance_file = "in_147567_50.txt"
result_file = "out_50.txt"
schedule_tasks(instance_file, result_file)
validate_schedule(instance_file, result_file)
