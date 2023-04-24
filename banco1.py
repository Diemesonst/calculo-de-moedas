

import sqlite3
conexao=sqlite3.connect('banco')
cursor=conexao.cursor()
cursor.execute('create table cliente(id int,nome varchar(100))')
#cursor.execute('insert into clientes(id,nome)values(1,"sofia")')
#cursor.execute('update clientes set nome="levi" where id=1')
#cursor.execute('delete from clientes where id=1')
conexao.commit()
conexao.close