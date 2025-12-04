# 📘 Projeto 2: Grafo com Algoritmo de Dijkstra**

# Grafo com Dijkstra – Estrutura de Dados

## 📌 Nome do Projeto
Implementação do Algoritmo de Dijkstra para Menor Caminho

## 🧩 Descrição do Problema / Solução
Este projeto implementa o algoritmo de **Dijkstra**, utilizado para calcular as menores distâncias  
de um vértice inicial até todos os outros em um grafo orientado com pesos positivos.

A estrutura utilizada é o modelo de lista de adjacência com pesos, e o algoritmo é implementado  
com fila de prioridade (heap), garantindo eficiência.

---

## 🧪 Funcionalidades Implementadas
### ✔ Requisitos mínimos:
- Representação de grafo com pesos (lista de adjacência)
- Exibição textual do grafo
- Execução completa do algoritmo

### ✔ Funcionalidades avançadas (nota 9–10):
- Algoritmo clássico: **Dijkstra**  
  - Calcula distância mínima  
  - Apresenta resultado final em formato textual

---

## 🛠️ Linguagem e Versão
- Python **3.11+**
- Biblioteca usada: `heapq` (fila de prioridade nativa)

---

## ▶️ Instruções de Execução
Execute na pasta raiz:

```bash
python src/main.py
```
### 📥 Exemplo de Entrada
graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("E", 3)],
    "D": [],
    "E": [("D", 4)]
}
### 📤 Exemplo de Saída
 Grafo com Pesos 
A -> B (4), C (2)
B -> C (5), D (10)
C -> E (3)
D ->
E -> D (4)

{'A': 0, 'C': 2, 'B': 4, 'E': 5, 'D': 9}

## Link do Vídeo
(https://youtu.be/XZB94kWNOTc?si=MICkh11C2QctF8Ys)

## Autor
Marcelo Sampaio
