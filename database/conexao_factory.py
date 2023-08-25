import psycopg2

class ConexaoFactory:

    def get_conexao(self):

        return psycopg2.connect(host='silly.db.elephantsql.com',
                               database='imssujmh',
                               user='imssujmh',
                               password= 'FvgYQRLfqQU5hOKnxbnfg7rWDgtP1wh3' )
