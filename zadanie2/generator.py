import random

def generate_instance(n):
    # Generate random coefficients for machine speeds
    machine_speeds = [round(random.uniform(1, 2), 2) for _ in range(5)]

    # Set at least one machine speed to 1
    machine_speeds[random.randint(0, 4)] = 1.0

    # Generate random task parameters for n tasks
    tasks = []
    for _ in range(n):
        processing_time = random.randint(1, 20)
        release_time = random.randint(0, 10)
        due_date = release_time + processing_time + random.randint(1, 10)
        tasks.append((processing_time, release_time, due_date))

    # Write the instance to a text file
    with open(f'in_147567_{n}.txt', 'w') as file:
        # Write the number of instances as the first line
        file.write(str(n) + "\n")

        # Write machine speeds
        file.write(" ".join(map(str, machine_speeds)) + "\n")
        
        # Write task parameters
        for task in tasks:
            file.write(" ".join(map(str, task)) + "\n")

# Generate instances for n = 50, 100, 150, ..., 500
for n in range(50, 501, 50):
    generate_instance(n)
