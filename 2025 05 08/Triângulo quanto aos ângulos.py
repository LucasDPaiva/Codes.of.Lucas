'''
    Programa para classificar um triângulo quanto aos ângulos.
    
    - O programa deverá solicitar 3 ângulos inteiros positivos;
    - Para ser um triângulo, a soma dos ângulos deve ser igual a 180;

    - Retângulo: possui um ângulo interno reto (igual a 90).
    - Obtusângulo: Possui um ângulo interno obtuso (maior que 90).
    - Acutângulo: Possui todos os ângulos internos agudos (menores que 90).
'''  

import sys
angulo01 = int(input('Informe o PRIMEIRO ângulo positivo:'))
angulo02 = int(input('Informe o SEGUNDO ângulo positivo:'))
angulo03 = int(input('Informe o TERCEIRO ângulo positivo:'))

Soma = angulo01 + angulo02 + angulo03 

if Soma < 180 or Soma > 180:
    sys.exit('nao é triangulo')
 






   