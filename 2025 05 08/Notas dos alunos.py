from statistics import median
import sys 

# Informando a nota da etapa 1
etapa1 = int(input('Informe a nota da Etapa 1: '))
if etapa1 < 0 or etapa1 > 100:
    sys.exit('ERRO: Nota Etapa 1 Inválida. Informe a nota entre 0 e 100.')

# Informando a nota da etapa 2
etapa2 = int(input('Informe a nota da Etapa 2: '))
if etapa1 < 0 or etapa1 > 100:
    sys.exit('ERRO: Nota Etapa 2 Inválida. Informe a nota entre 0 e 100.')

# Calculando a média
média = (etapa1 * 2 + etapa2 * 3) / 5
print(f'Média do aluno {média:.0f}')

# Verificando a situação do aluno
if média >= 60:
    print('Aluno Aprovado.')
elif média >= 20:
    print('Aluno em prova Final.')
else:
    print('Aluno Reprovado')