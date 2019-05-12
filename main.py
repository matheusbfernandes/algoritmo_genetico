from algoritmo_genetico import AG


def main():
    algoritmo_genetico = AG([-10, 10], 30, 20, 0.01, 0.7, 7)
    algoritmo_genetico.selecionar()


if __name__ == "__main__":
    main()
