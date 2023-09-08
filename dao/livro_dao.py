from model.livro import Livro
from database.conexao_factory import ConexaoFactory
from dao.categoria_dao import CategoriaDAO
from dao.editora_dao import EditoraDAO
from dao.autor_dao import AutorDAO


class LivroDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Livro]:
        livros = list()
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, titulo, isbn, paginas, ano, resumo, categoria_id, editora_id, autor_id FROM livros")
        resultados = cursor.fetchall()
        for resultado in resultados:
            categoria = CategoriaDAO().buscar_por_id(resultado[6])
            editora = EditoraDAO().buscar_por_id(resultado[7])
            autor = AutorDAO().buscar_por_id(resultado[8])
            liv = Livro(resultado[1], resultado[2], resultado[3], resultado[4],
                        resultado[5], categoria, editora, autor)
            liv.id = resultado[0]
            livros.append(liv)
        cursor.close()
        conexao.close()
        return livros

    def adicionar(self, livro: Livro) -> None:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO livros (titulo, isbn, paginas, ano, resumo, categoria_id, editora_id, autor_id) VALUES \
                       ('{livro.titulo}', '{livro.isbn}', '{livro.paginas}', '{livro.ano}', '{livro.resumo}', '{livro.categoria.id}', '{livro.editora.id}', '{livro.autor.id}')")
        conexao.commit()
        cursor.close()
        conexao.close()

    def remover(self, livro_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM livros WHERE id = %s", (livro_id,))
        livros_removidos = cursor.rowcount
        conexao.commit()
        cursor.close()
        conexao.close()

        if (livros_removidos == 0):
            return False

        return True

    def buscar_por_id(self, livro_id) -> Livro:
        liv = None
        conexao = self.__conexao_factory.get_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "SELECT id, titulo, isbn, paginas, ano, resumo, categoria_id, editora_id, autor_id FROM livros WHERE id = %s", (livro_id,))
        resultado = cursor.fetchone()
        cursor.close()
        conexao.close()
        if (resultado):
            categoria = CategoriaDAO().buscar_por_id(resultado[6])
            editora = EditoraDAO().buscar_por_id(resultado[7])
            autor = AutorDAO().buscar_por_id(resultado[8])
            liv = Livro(resultado[1], resultado[2], resultado[3], resultado[4],
                        resultado[5], categoria, editora, autor)
            liv.id = resultado[0]
        return liv
