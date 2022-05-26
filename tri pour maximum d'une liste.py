def tri(liste):
    max=0
    for i in range(len(liste)):
        if liste[i] > max:
            max=liste[i]
    min = max
    for y in range(len(liste)):
        if liste[y] < min:
            min = liste[y]
    print("Le maximum de la liste est ",max," et le minimum est ",min,".")
    return

tri([])