import time  # Dodaj import modułu time

indices = [148163, 148066, 145442, 144441, 148144, 148160, 147567, 148178, 148239, 148410, 147414]
sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

# Funkcja do wczytywania danych z pliku wejściowego
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        data = [list(map(int, line.split())) for line in lines[1:n+1]]
        S = [list(map(int, line.split())) for line in lines[n+1:]]
    return n, data, S

# Funkcja do obliczania Lmax na podstawie ustalonej kolejności zadań
def calculate_Lmax(order, data, S):
    n = len(order)
    C = [0] * n
    L = [0] * n
    for i in range(n):
        j = order[i]
        if i > 0:
            C[i] = C[i - 1] + data[j][0] + S[order[i - 1]][j]
        else:
            C[i] = data[j][0]
        L[i] = max(0, C[i] - data[j][1])
    return max(L)

# Funkcja weryfikująca poprawność pliku wynikowego
def verify_solution(index, size):
    start_time = time.time()  # Zarejestruj czas rozpoczęcia weryfikacji
    input_instance_path = f'instancje/in_{index}_{size}.txt'
    output_result_path = f'wyniki/out_{index}_{size}.txt'

    n, data, S = read_input(input_instance_path)


    # Wczytanie wyniku
    with open(output_result_path, 'r') as file:
        lines = file.read().splitlines()
        reported_Lmax = int(lines[0])
        order = [int(j) - 1 for j in lines[1].split()]  # Asumujemy, że zadania są numerowane od 1

    if len(set(order)) != n:
        return False, "Każde zadanie musi wystąpić dokładnie jeden raz."

    # Obliczenie Lmax na podstawie kolejności z pliku wynikowego
    calculated_Lmax = calculate_Lmax(order, data, S)

    end_time = time.time()  # Zarejestruj czas zakończenia weryfikacji
    elapsed_time = end_time - start_time  # Oblicz czas trwania weryfikacji

    # Porównanie obliczonego Lmax z podanym w pliku wynikowym
    if calculated_Lmax != reported_Lmax:
        return False, f"Niepoprawny Lmax. Oczekiwano: {reported_Lmax}, otrzymano: {calculated_Lmax}. Czas weryfikacji: {elapsed_time} sekund."

    return True, f"Poprawny Lmax. Wartość: {calculated_Lmax}. Czas weryfikacji: {elapsed_time} sekund."

# Uruchomienie funkcji weryfikującej dla wszystkich kombinacji indices i sizes
for index in indices:
    for size in sizes:
        is_correct, message = verify_solution(index, size)
        print(f"{message} Dla pliku in_{index}_{size}.txt")
