def show_graph(graph):
    print("\n=== Grafo com Pesos ===")
    for v, edges in graph.items():
        linhas = ", ".join([f"{dest} ({peso})" for dest, peso in edges])
        print(f"{v} -> {linhas}")
    print("========================\n")
