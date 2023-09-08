import csv
from model.editora import Editora


def ler_csv() -> None:
    with open('editoras.csv') as arquivo_csv:
        list_csv = list()
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        for linha in csv_reader:
            list_csv.append(linha)
        return list_csv


def ler_csv_e_cria_lista_de_editoras() -> None:
    with open('editoras.csv') as arquivo_csv:
        list_csv = list()
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        lista_editoras = list()
        for linha in csv_reader:
            list_csv.append(linha)
        for item in list_csv:
            editora = Editora(item[0], item[1], item[2])
            lista_editoras.append(editora)
    return lista_editoras


def ler_csv_e_cria_dicionario_de_editoras() -> None:
    with open('editoras.csv') as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        lista_editoras = list()
        for dic in csv_reader:
            editora = Editora(dic['nome'], dic['endereco'], dic['telefone'])
            lista_editoras.append(editora)
    return lista_editoras


def criando_csv_usando_lista_de_editoras(lista_editoras: list[Editora], nome_arquivo_csv: str) -> None:
    with open(nome_arquivo_csv, 'w', newline='') as novo_arquivo:
        escritor = csv.writer(novo_arquivo)
        escritor.writerow(['nome', 'endereco', 'telefone'])
        for editora in lista_editoras:
            escritor.writerow(
                [editora.nome, editora.endereco, editora.telefone])

    print('Os dados foram carregados com sucesso!')


if __name__ == '__main__':
    # print(ler_csv())

    # lista_edt = ler_csv_e_cria_lista_de_editoras()
    # for edt in lista_edt:
    #    print(f'{edt.nome} | {edt.endereco} | {edt.telefone}')

    # lista_edt = ler_csv_e_cria_dicionario_de_editoras()
    # for edt in lista_edt:
    #    print(f'{edt.nome} | {edt.endereco} | {edt.telefone}')

    criando_csv_usando_lista_de_editoras(
        ler_csv_e_cria_dicionario_de_editoras(), "teste.csv")
