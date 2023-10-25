import random
import os

def generate_instance(n):
    # Zakres wartości zadań i czasów trwania
    min_task_value = 1
    max_task_value = 100
    min_task_duration = 1
    max_task_duration = 50

    # Generowanie instancji problemu
    instance = []
    for _ in range(n):
        task_value = random.randint(min_task_value, max_task_value)
        max_duration = min(task_value * 2, max_task_duration)  # Czas trwania nie więcej niż 100% od wartości
        task_duration = random.randint(min_task_duration, max_duration)
        instance.append((task_value, task_duration))

    # Generowanie czasu przezbrojenia maszyny; Sii = 0
    setup_times = [[0 if i == j else random.randint(1, 20) for j in range(n)] for i in range(n)]

    return instance, setup_times

def save_instance_to_file(instance, setup_times, folder, filename):
    with open(os.path.join(folder, filename), 'w') as file:
        # Zapisz długość instancji
        file.write(f"{len(instance)}\n")
        # Zapisz wartości zadań i czasy trwania
        for task in instance:
            file.write(f"{task[0]} {task[1]}\n")
        
        # Zapisz czasy przezbrojenia maszyny
        for row in setup_times:
            file.write(" ".join(map(str, row)) + "\n")

def main():
    sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

    for n in sizes:
        instance, setup_times = generate_instance(n)
        folder = "instances"
        filename = f'in_147567_{n}.txt'
        save_instance_to_file(instance, setup_times, folder, filename)
        print(f'Generated instance with n={n} and saved to {folder}/{filename}')

if __name__ == "__main__":
    main()
