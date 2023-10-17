import random
import os

def generate_instance(input_size):
    # Zakres wartości zadań i czasów trwania
    min_task_value = 1
    max_task_value = 100
    min_task_duration = 1
    max_task_duration = 20

    # Generowanie instancji problemu
    instance = []
    for _ in range(input_size):
        task_value = random.randint(min_task_value, max_task_value)
        max_duration = min(task_value * 2, max_task_duration)  # Czas trwania nie więcej niż 100% od wartości
        task_duration = random.randint(min_task_duration, max_duration)
        instance.append((task_value, task_duration))

    return instance

def save_instance_to_file(instance, folder, filename):
    with open(os.path.join(folder, filename), 'w') as file:
        for task in instance:
            file.write(f"{task[0]} {task[1]}\n")

def main():
    sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    
    for n in sizes:
        instance = generate_instance(n)
        folder = "instances"  # Folder, do którego chcemy zapisać pliki
        filename = f'instance_n{n}.txt'
        save_instance_to_file(instance, folder, filename)
        print(f'Generated instance with n={n} and saved to {folder}/{filename}')

if __name__ == "__main__":
    main()
