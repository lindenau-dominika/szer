def validate_schedule(instance_file, result_file):
    with open(instance_file, 'r') as instance:
        n = int(instance.readline().strip())
        machine_speeds = list(map(float, instance.readline().split()))
        tasks = [tuple(map(int, line.split())) for line in instance]

    with open(result_file, 'r') as result:
        total_tardiness = int(result.readline().strip())
        schedules = [list(map(int, line.split())) for line in result]

    if len(schedules) != 5:
        print("Błędna liczba sekwencji zadań w pliku wynikowym.")
        return False

    # unikatowość zadania
    task_count = {i + 1: 0 for i in range(n)}
    for schedule in schedules:
        for task in schedule:
            task_count[task] += 1

    for count in task_count.values():
        if count != 1:
            print("Błąd: Każde zadanie powinno wystąpić dokładnie raz w sekwencjach.")
            return False

    # Obliczenie łącznej liczby spóźnionych zadań
    total_tardiness_calculated = 0
    for i, schedule in enumerate(schedules):
        machine_speed = machine_speeds[i]
        current_time = 0

        for task in schedule:
            processing_time, release_time, due_date = tasks[task - 1]
            current_time = max(current_time, release_time)
            completion_time = current_time + processing_time * machine_speed
            current_time = completion_time
            delay = max(completion_time - due_date, 0)
            total_tardiness_calculated += 1 if delay > 0 else 0

    # Sprawdzenie kryterium oceny
    if total_tardiness_calculated != total_tardiness:
        print("Błąd: Niezgodność kryterium oceny.")
        print(f"Oczekiwana liczba zadań spóźnionych: {total_tardiness}, Otrzymana liczba zadań spóźnionych: {total_tardiness_calculated}")
        return False

    print("Wyniki są poprawne.")
    print("Łączna liczba zadań spóźnionych:", total_tardiness_calculated)
    return True

# Przykład użycia
instance_file = "in_148178_500.txt"
result_file = "out_500"
validate_schedule(instance_file, result_file)

