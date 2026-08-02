import copy
from dados import produtos
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p : p['preco']
)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep= '\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')