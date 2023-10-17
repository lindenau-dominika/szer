import os

def load_instance(filename):
    # Wczytaj instancję z pliku
    instance = []
    with open(filename, 'r') as file:
        next(file)  # Pomijamy pierwszą linię z nagłówkiem
        for line in file:
            values = line.split()
            if len(values) == 2:
                task_value = int(values[0])
                task_duration = int(values[1])
                instance.append((task_value, task_duration))
    return instance

def load_solution(filename):
    # Wczytaj rozwiązanie z pliku
    solution = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.split()
            if len(values) == 2:
                task_index = int(values[0])
                task_start_time = int(values[1])
                solution.append((task_index, task_start_time))
    return solution

def verify_solution(instance, solution):
    # Weryfikacja poprawności rozwiązania
    total_value = 0
    max_end_time = 0
    for task_index, task_start_time in solution:
        if task_index < 0 or task_index >= len(instance):
            return f"Niepoprawny numer zadania: {task_index}"

        task_value, task_duration = instance[task_index]
        task_end_time = task_start_time + task_duration

        if task_start_time < 0 or task_end_time > max_end_time:
            return f"Zadanie {task_index} jest niepoprawnie zaplanowane"

        total_value += task_value
        max_end_time = max(max_end_time, task_end_time)

    return f"Wartość rozwiązania: {total_value}"

def main():
    instance_folder = "instances"
    solution_folder = "solutions"
    
    sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

    for n in sizes:
        instance_filename = os.path.join(instance_folder, f'instance_n{n}.txt')
        solution_filename = os.path.join(solution_folder, f'solution_n{n}.txt')

        instance = load_instance(instance_filename)
        solution = load_solution(solution_filename)

        verification_result = verify_solution(instance, solution)
        print(f"Verification for n={n}: {verification_result}")

if __name__ == "__main__":
    main()
