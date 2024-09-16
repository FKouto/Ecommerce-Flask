# E-commerce Flask App
Este projeto é uma aplicação de e-commerce desenvolvida com Flask, fornecida como parte do Mini Curso de Python oferecido pela Rockeseat. O objetivo do projeto é criar um backend básico para uma loja online, com funcionalidades para gerenciamento de produtos e carrinho de compras, bem como autenticação de usuários.

## Funcionalidades

- **Autenticação de Usuário**: Permite login e logout de usuários com proteção de rotas.
- **Gerenciamento de Produtos**: Adiciona, exclui, atualiza e obtém detalhes dos produtos.
- **Carrinho de Compras**: Adiciona e remove itens do carrinho, visualiza itens do carrinho e realiza o checkout.

## Tecnologias Utilizadas

- **Flask**: Framework web para criação da aplicação.
- **Flask-SQLAlchemy**: ORM para gerenciamento do banco de dados.
- **Flask-CORS**: Permite o acesso a recursos de diferentes hosts.
- **Flask-Login**: Gerencia a autenticação e sessões de usuários.

## Configuração do Ambiente

1. **Clone o repositório**

   ```bash
   git clone https://github.com/FKouto/Ecommerce-Flask.git
   cd Ecommerce-Flask
   ```

2. **Instale as dependências**

   É recomendável usar um ambiente virtual. Primeiro, crie e ative um ambiente virtual:

   ```bash
   python -m venv ecomapienv
   source ecomapienv/bin/activate  # No Windows use: ecomapienv\Scripts\activate
   ```

   Em seguida, instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuração do Banco de Dados**

   O projeto utiliza SQLite para armazenamento de dados. O banco de dados será criado automaticamente ao iniciar a aplicação pela primeira vez.

   * Para visualizar o Banco de Dados instale a extensão SQLite Viewer

4. **Executar a Aplicação**

   Para iniciar a aplicação, use o seguinte comando:

   ```bash
   python app.py
   ```

   A aplicação será executada no modo de desenvolvimento (`debug=True`), e você pode acessá-la em `http://127.0.0.1:5000` utlizando o swagger no postman.

## Endpoints

- **Autenticação**
  - `POST /login`: Faz login de um usuário.
  - `POST /logout`: Faz logout do usuário atual.

- **Gerenciamento de Produtos** (Protegido)
  - `POST /api/products/add`: Adiciona um novo produto.
  - `DELETE /api/products/delete/<int:product_id>`: Remove um produto existente.
  - `GET /api/products/<int:product_id>`: Obtém detalhes de um produto pelo ID.
  - `PUT /api/products/update/<int:product_id>`: Atualiza um produto existente.
  - `GET /api/products`: Lista todos os produtos.

- **Carrinho de Compras** (Protegido)
  - `POST /api/cart/add/<int:product_id>`: Adiciona um item ao carrinho.
  - `DELETE /api/cart/remove/<int:product_id>`: Remove um item do carrinho.
  - `GET /api/cart`: Lista todos os itens no carrinho.
  - `POST /api/cart/checkout`: Realiza o checkout e limpa o carrinho.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.