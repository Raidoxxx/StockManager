import sqlite3
from manager.stock import stock_class

def database():
    # Create a sqlite database
    conn = sqlite3.connect('stock.db')

    sqls = [
        '''CREATE TABLE IF NOT EXIST produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            codigo_barras VARCHAR(100) UNIQUE,
            custo DECIMAL(10,2) NOT NULL,
            preco DECIMAL(10,2) NOT NULL,
            quantidade INT NOT NULL,
            unidade VARCHAR(50) NOT NULL,
            categoria VARCHAR(100),
            validade DATE,
            fornecedor_id INT,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id)
        )''',

        '''CREATE TABLE IF NOT EXIST fornecedores (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            contato VARCHAR(255),
            email VARCHAR(255),
            telefone VARCHAR(20),
            endereco TEXT,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )''',

        '''CREATE TABLE IF NOT EXIST usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            senha VARCHAR(255) NOT NULL,
            cargo ENUM('admin', 'atendente') NOT NULL,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )'''

        '''CREATE TABLE IF NOT EXIST historico_estoque (
            id INT AUTO_INCREMENT PRIMARY KEY,
            produto_id INT NOT NULL,
            tipo ENUM('entrada', 'saida', 'ajuste') NOT NULL,
            quantidade INT NOT NULL,
            custo DECIMAL(10,2),
            preco DECIMAL(10,2),
            fornecedor_id INT,
            atendente_id INT,
            motivo TEXT,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (produto_id) REFERENCES produtos(id),
            FOREIGN KEY (fornecedor_id) REFERENCES fornecedores(id),
            FOREIGN KEY (atendente_id) REFERENCES usuarios(id)
        )'''

        '''CREATE TABLE IF NOT EXIST alertas (
            id INT AUTO_INCREMENT PRIMARY KEY,
            produto_id INT NOT NULL,
            tipo ENUM('estoque_baixo', 'vencimento_proximo', 'movimentacao_anormal') NOT NULL,
            mensagem TEXT NOT NULL,
            status ENUM('pendente', 'resolvido') DEFAULT 'pendente',
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )'''
    ]

    for sql in sqls:
        conn.cursor().execute(sql)
        conn.commit()
    
    conn.close()
    loadData()
            
def main():
    database()

def loadData():
    stock_data = sqlite3.connect('stock.db').cursor().execute('SELECT * FROM stock')
    supplier_data = sqlite3.connect('stock.db').cursor().execute('SELECT * FROM supplier')
    item_data = sqlite3.connect('stock.db').cursor().execute('SELECT * FROM item')
    
if __name__ == "__main__":
    main()