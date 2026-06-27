def descendentes(arvore):
    return [descendente for subarvore in arvore[1] for descendente in [subarvore[0]] + descendentes(subarvore)]