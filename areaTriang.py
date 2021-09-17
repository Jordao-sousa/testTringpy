import math

# Armazena os valores de input na lista.
medidasTriangulo = list(map(float, input('Digite as medidas do triangulo: ').split()))
# Faz a soma dos valores em um Arrey.
somaDosLadosMenores = sum(medidasTriangulo) - max(medidasTriangulo)

# Funçao que retorna a área do Triangulo
def areaTriangulo(medidas):
    semiPerimetro = sum(medidas) / 2
    area = ((semiPerimetro) * (semiPerimetro - medidas[0]) * (semiPerimetro - medidas[1]) * (semiPerimetro - medidas[2]))
    areaTriang = math.sqrt(area)
    return areaTriang

if max(medidasTriangulo) < somaDosLadosMenores:
    print(f'Área do Triângulo corresponde a -> {areaTriangulo(medidasTriangulo):.2f} M2')
else:
    print('Os valores informados nao Formam um Triângulo!!!')
