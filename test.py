def print_comb() -> None: #None considéré comme null en python.
    for i in range(8): 
        for j in range(i + 1, 9):
            for k in range(j + 1, 10):
                print(f"{i}{j}{k}")

print_comb()