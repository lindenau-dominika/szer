def get_data_from_file(path):
    with open(path, "r") as file:
        lines = file.read()
    lines = lines.split("\n")
    n = int(lines[0])
    temp = lines[1]
    temp = lines[1].split()
    machines = []
    for machine in temp:
        machines.append(float(machine))
    tasks = []
    for i in range(n):
        task = lines[i+2].split(" ")
        task[0] = int(task[0])
        task[1] = int(task[1])
        task[2] = int(task[2])
        tasks.append(task)
    return tasks, machines

def get_answer_from_file(path):
    with open(path, "r") as file:
        lines = file.read()
    lines = lines.split("\n")
    Lmax = lines[0]
    machine1 = []
    machine2 = []
    machine3 = []
    machine4 = []
    machine5 = []
    for x in lines[1].split(" "):
        if x.isdigit():
            machine1.append(int(x))
    for x in lines[2].split(" "):
        if x.isdigit():
            machine2.append(int(x))
    for x in lines[3].split(" "):
        if x.isdigit():
            machine3.append(int(x))
    for x in lines[4].split(" "):
        if x.isdigit():
            machine4.append(int(x))
    for x in lines[5].split(" "):
        if x.isdigit():
            machine5.append(int(x))
    return Lmax, [machine1, machine2, machine3, machine4, machine5]


def calculate_lmax(sequences, tasks, machines):
    t = [0] * len(sequences)
    lMaxs = [float("-inf")] * len(sequences)
    machine_num = 0
    for sequence in sequences:
        task_num = 0
        for task_index in sequence:
            processing_time, ready_time, deadline = tasks[task_index-1]
            if task_num == 0:
                t[machine_num] += ready_time
            if ready_time > t[machine_num]:
                t[machine_num] = ready_time
            t[machine_num] += processing_time * machines[machine_num]
            lMaxs[machine_num] = max(lMaxs[machine_num], t[machine_num] - deadline)
            task_num += 1
        machine_num += 1
    return max(lMaxs)



tasks, machines = get_data_from_file("in_147567_50.txt")
Lmax, sequences = get_answer_from_file("out_50")
print(tasks)
print(machines)
print(Lmax)
print(calculate_lmax(sequences, tasks, machines))