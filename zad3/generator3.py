import random

def generate_instance(n):
    input_data = f"{n}\n"
    for i in range(1, n + 1):
        pi = [random.randint(1, 100) for _ in range(4)]
        min_di = sum(pi)
        di = random.randint(min_di, min_di + int(round(min_di*0.2)))
        ai = random.randint(1, 10)
        bi = random.randint(1, 10)

        input_data += " ".join(map(str, pi + [di, ai, bi])) + '\n'

        with open(f"input_{n}.txt", "w") as input_file:
            input_file.write(input_data)
    

for n in range(50, 501, 50):
    generate_instance(n)

# segregowanie po długosci ostatniego (4) zadania i najkrótsze na początek. Wymiennie