def validate_solution(instance_file, solution_file):
    # Wczytanie danych wejściowych
    with open(instance_file, "r") as instance:
        n = int(instance.readline().strip())
        jobs = [list(map(int, line.split())) for line in instance]

    # Wczytanie danych wyjściowych
    with open(solution_file, "r") as solution:
        expected_ewdw = int(solution.readline().strip())
        job_sequence = list(map(int, solution.readline().split()))

    if len(job_sequence) != n:
        print("Błędna liczba zadań w sekwencji!")
        return False

    completion_times = [0] * 4
    total_ewdw = 0

    for job_index in job_sequence:
        job_data = jobs[job_index - 1]  # Indeksacja w pliku zaczyna się od 1

        for machine, time in enumerate(job_data[:4]):  # Zmiana zakresu na pierwsze cztery kolumny
            completion_times[machine] += time
            dw = max(0, completion_times[machine] - job_data[-3])
            ew = max(0, job_data[-3] - completion_times[machine])  # Poprawa indeksacji
        total_ewdw += job_data[-2] * ew + job_data[-1] * dw

    # Pokazanie oczekiwanej wartości wynikowej
    print("Oczekiwana suma ważonego wyprzedzenia i opóźnienia:", expected_ewdw)

    # Sprawdzenie, czy obliczona suma ważonego wyprzedzenia i opóźnienia zgadza się z wartością z pliku wyjściowego
    if total_ewdw != expected_ewdw:
        print("Błędna suma ważonego wyprzedzenia i opóźnienia! total:", total_ewdw, 'expected:', expected_ewdw)
        return False

    # Jeżeli dotarliśmy do tego punktu, rozwiązanie jest poprawne
    return True

# Przykład użycia
instance_file = "input_100.txt"
solution_file = "output_100.txt"
result = validate_solution(instance_file, solution_file)
if result:
    print("Rozwiązanie jest poprawne.")
