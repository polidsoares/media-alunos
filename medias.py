import argparse

# Lê os argumentos
parser = argparse.ArgumentParser()
parser.add_argument('--entrada', help='nome do arquivo de notas')
parser.add_argument('--saida', help='nome do arquivo de médias')
args = parser.parse_args()

# Carrega as notas
with open(args.entrada, 'r') as arquivo:
    linhas = arquivo.read().splitlines()

# Calcula média para cada aluno
dados = []
for linha in linhas:
    linha = linha.split('\t')
    if len(linha) == 4:
        nome = linha[0]
        media = sum([float(nota) for nota in linha[1:]])/3
        dados.append(f'{nome}\t{media:.3f}')
dados = '\n'.join(dados)

# Escreve o resultado no arquivo
with open(args.saida, 'w') as arquivo:
    arquivo.write(dados)

print(f'Arquivo {args.saida} gerado!')