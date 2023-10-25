import random
import os

def generate_solution(n):
    # Generowanie sekwencji zadań
    order = list(range(1, n + 1))
    random.shuffle(order)
    
    # Obliczenie wartości Lmax (sztuczna wartość)
    lmax = random.randint(1, 1000)

    return lmax, order

def save_solution_to_file(lmax, order, folder, filename):
    with open(os.path.join(folder, filename), 'w') as file:
        file.write(f"{lmax}\n")
        file.write(" ".join(map(str, order)))

def main():
    sizes = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    
    for n in sizes:
        lmax, order = generate_solution(n)
        folder = "solutions"  # Folder, do którego chcemy zapisać pliki
        filename = f'solution_{n}.txt'
        save_solution_to_file(lmax, order, folder, filename)
        print(f'Generated solution for n={n} and saved to {folder}/{filename}')

if __name__ == "__main__":
    main()
