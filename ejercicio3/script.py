def min_saltos(x, k):
  # Caso base: 1 salto para llegar al punto 1.
  if x == 1:
    return 1

  # Inicializa la matriz DP con el máximo número posible de saltos necesarios.
  dp = [float('inf')] * (x + 1)

  # 0 saltos necesarios para llegar al punto 0.
  dp[0] = 0

  # Itera a través de las posiciones posibles.
  for i in range(1, x + 1):
    # Prueba ambas opciones de salto y actualiza dp en función del mínimo.
    dp[i] = min(dp[i], dp[i - 1] + 1, *(dp[max(0, i - j)] + 1 for j in range(1, min(k, i) + 1)))

  # Devuelve el número mínimo de saltos para llegar a x.
  return dp[x]

# Obtén el número de casos de prueba.
t = int(input())

# Recorre cada caso de prueba.
for _ in range(t):
  # Obtén el punto de destino y el máximo número de saltos por movimiento.
  x, k = map(int, input().split())
  # Llama a la función para encontrar los saltos mínimos e imprime el resultado.
  print(min_saltos(x, k))
