# Mis asi on anagramm?

def leidub_anagramm(matrix):
    def on_anagramm(s1, s2):
        return sorted(s1) == sorted(s2)
    
    for rida in matrix:
        for i in range(len(rida)):
            vasak = rida[i - 1] if i > 0 else ""
            parem = rida[i + 1] if i < len(rida) - 1 else ""
            sone = rida[i]
            if on_anagramm(vasak + parem, sone):
                return True
            else: return False
    
