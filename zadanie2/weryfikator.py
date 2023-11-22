def read_instance(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        machine_speeds = list(map(float, lines[0].split()))
        tasks = [tuple(map(int, line.split())) for line in lines[1:]]
    return machine_speeds, tasks

def read_solution(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        total_late_tasks = int(lines[0])
        schedules = [list(map(int, line.split()[1:])) for line in lines[1:]]
    return total_late_tasks, schedules

def verify_solution(instance_filename, solution_filename):
    machine_speeds, tasks = read_instance(instance_filename)
    total_late_tasks, schedules = read_solution(solution_filename)

    # Verify schedules
    for schedule in schedules:
        time = 0
        for task_id in schedule:
            processing_time, release_time, due_date = tasks[task_id - 1]
            completion_time = time + processing_time / machine_speeds[schedule.index(task_id)]
            if completion_time > due_date:
                total_late_tasks += 1
            time = completion_time

    print(f"Total late tasks: {total_late_tasks}")

# Test the verification for one instance and solution file
instance_filename = 'instance_n_50.txt'
solution_filename = 'solution_n_50.txt'
verify_solution(instance_filename, solution_filename)
