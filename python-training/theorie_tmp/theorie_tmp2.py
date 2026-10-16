# récurcivité

# 1 2 6 24 120 720 5040 40320 362880 3628800 

import cProfile

def fact (n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

# compléxité → n

# raise → continuer si erreur


#fibonatchi
# n = (n - 1) + (n - 2)

def fibo(n): # vraiment pas opti, n factoriel → le n le plus complexe
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else: return fibo(n-1) + fibo(n-2)

print(fibo(5))
cProfile.run('fibo(5)')


# memorisation → utlise pour simplifier fibo, par contre risque de memory limit (au lieu de time)


def memo_fibo(n, memo={}): # vraiment pas opti, n factoriel → le n le plus complexe
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    #else: else vraiment pas opti ici et dans la plupart des cas,
    # éviter le else, si on passe dans tout les cas dans le if/elif
    memo[n] = memo_fibo(n - 1,memo) + memo_fibo(n - 2, memo)
    return memo[n]

print(fibo(5))
cProfile.run('memo_fibo(5)')


# calcul de complexité = pire complexité
# o(1) + o(n) + o(n²) + o(n³) = o(n³)

# o(n) + o(m) = o(n+m) → faire n * m, meme si carré comme sudoku (9*9 → ligne*colonne)

#complexité global =/= complexité propre

# if  o(1)
# if expression bool: instruction   o(1) + o(1)
# fonction    o(f)
# for ... instruction     o(1) + n*o(1) = max(o(n),...)
# when expression bool: instruction      n*(o(i)+o(i))

# set meilleur que list, n vs n+1, pour recherche dee valeur →
# si une seule recherche alors liste sinon set