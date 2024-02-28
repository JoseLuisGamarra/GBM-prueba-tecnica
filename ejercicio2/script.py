def calcular_puntos(resultado, sistema_puntuacion):
    puntos = [0 for _ in range(len(resultado))]
    for i in range(min(len(sistema_puntuacion), len(resultado))):
        puntos[resultado[i] - 1] = sistema_puntuacion[i]
    return sum(puntos)


def encontrar_campeones(resultados, sistemas_puntuacion):
    campeones = {}
    for sistema in sistemas_puntuacion:
        puntos_campeon = 0
        id_campeon = None
        for resultado in resultados:
            puntos = calcular_puntos(resultado, sistema)
            if puntos > puntos_campeon:
                puntos_campeon = puntos
                id_campeon = None
            if puntos == puntos_campeon:
                id_campeon = None if id_campeon else id_campeon
                id_campeon = min(id_campeon, resultado[0])
        if id_campeon:
            campeones.setdefault(id_campeon, set()).add(id_campeon)
    return " ".join(map(str, sorted(campeones))) or "No hay ganador"


while True:
    G, P = map(int, input().split())
    if G == 0 and P == 0:
        break

    resultados = []
    for _ in range(G):
        resultados.append(list(map(int, input().split())))

    S = int(input())
    sistemas_puntuacion = []
    for _ in range(S):
        K = int(input())
        sistemas_puntuacion.append(list(map(int, input().split())))

    campeones = encontrar_campeones(resultados, sistemas_puntuacion)
    print(campeones)
