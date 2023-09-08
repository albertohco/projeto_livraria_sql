from model.editora import Editora
from database.conexao_factory import ConexaoFactory


class EditoraDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Editora]:
        editoras = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, endereco, telefone FROM editoras")
        resultados = cursor.fetchall()
        for resultado in resultados:
            edi = Editora(resultado[1], resultado[2], resultado[3])
            edi.id = resultado[0]
            editoras.append(edi)
        cursor.close()
        conexao.close()
        return editoras

    def adicionar(self, editora: Editora) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            f"INSERT INTO editoras (nome, endereco, telefone) VALUES ('{editora.nome}', '{editora.endereco}', '{editora.telefone}')")
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, editora_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM editoras WHERE id = %s", (editora_id,))
        editoras_removidas = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()
        if (editoras_removidas == 0):
            return False
        return True

    def buscar_por_id(self, editora_id) -> Editora:
        edi = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, nome, endereco, telefone FROM editoras WHERE id = %s", (editora_id,))
        resultado = cursor.fetchone()
        if (resultado):
            edi = Editora(resultado[1], resultado[2], resultado[3])
            edi.id = resultado[0]
        cursor.close()
        conexao.close()
        return edi

    def adicionar_muitos(self, lista_editoras):
        for editora in lista_editoras:
            self.adicionar(editora)
