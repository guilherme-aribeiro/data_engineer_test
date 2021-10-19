import psycopg2


class Conexao(object): #classe para gerenciar conexao com o banco de dados
   _db = None

   def __init__(self, mhost, db, usr, pwd):
    self._db = psycopg2.connect(
        host=mhost, database=db, user=usr,  password=pwd)

   def manipular(self, sql):
        try:
           cur = self._db.cursor()
           cur.execute(sql)
           cur.close();
           self._db.commit()
        except:
            return False
        return True
   def consultar(self, sql):
     rs=None
     try:
         cur=self._db.cursor()
         cur.execute(sql)
         rs=cur.fetchall()
     except:
         return None
     return rs
def proximaPK(self, tabela, chave):
     sql='select max('+chave+') from '+tabela
     rs = self.consultar(sql)
     pk = rs[0][0]
     return pk+1
def fechar(self):
     self._db.close()


def manipula_sql(sql):
    #print("SQL ===  " +sql)
    conn.manipular(sql)

def consulta_sql(sql):
    #print(sql)
    ret = conn.consultar(sql)
    return ret

#CRIA NOVA CONEXÃO

conn = Conexao('localhost','data','postgres','123456')


