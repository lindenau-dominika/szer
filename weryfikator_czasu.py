import subprocess
import time
import os

def run_scheduler(program_path, input_file, output_file, time_limit):
    try:
        # Uruchom program zadanym plikiem wejściowym i limitem czasu
        start_time = time.time()
        command = [program_path, input_file, output_file, str(time_limit)]
        subprocess.run(command, timeout=time_limit)
        end_time = time.time()

        # Oblicz czas wykonania programu
        execution_time = end_time - start_time

        # Sprawdź, czy czas wykonania przekroczył limit
        time_exceeded = execution_time > time_limit

        return execution_time, time_exceeded

    except subprocess.TimeoutExpired:
        # Program przekroczył limit czasu
        return time_limit, True
    except Exception as e:
        # Inny błąd lub wyjątek
        return None, False

def main():
    program_path = "generator.exe"
    instances_folder = "instances"  
    time_limit = 60

    sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    
    for n in sizes:
        input_file = os.path.join(instances_folder, f'instance_n{n}.txt')
        output_file = "output.txt"  # Plik wynikowy, w którym program zapisuje rozwiązanie
        execution_time, time_exceeded = run_scheduler(program_path, input_file, output_file, time_limit)

        if time_exceeded:
            print(f"Czas wykonania programu dla instancji n={n} przekroczony.")
        elif execution_time is not None:
            print(f"Czas wykonania programu dla instancji n={n}: {execution_time} sekund.")
        else:
            print(f"Wystąpił błąd podczas wykonywania programu dla instancji n={n}.")

if __name__ == "__main__":
    main()
