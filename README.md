Agro
============

API Safra
-------
- Produtos:
	Paths:
		http://localhost:8000/safra/products/create # Cria novos produtos
		http://localhost:8000/safra/products/list # Lista todos produtos existentes e dá opção para remover ou editar.

- Safras:
	Paths:
		http://localhost:8000/safra/harvest/create # Cria nova safra
		http://localhost:8000/safra/harvest/list # Lista todas safras e dá opção para editar ou remover.


API Services
-------
- Services:
	Paths:
		http://localhost:8000/services/create # Cria novo serviço
		http://localhost:8000/services/list # Lista todos serviços
		http://localhost:8000/services/prices # Atualiza price dos produtos



	Como o tempo estava meio escasso, acabei não conseguindo colocar todas validações de campos necessárias, e nem trabalhar um pouco mais na aparência das telas e informações,
como por exemplo os campos de preço com a currency correta.
	Também não foi feita a parte de Editar e Excluir serviços, como é algo semelhante ao feito na API Safra, pela falta de tempo optei por não fazê-lo.
	O cálculo do produto fiz colocando peso no produtos, caso haja produtos diferentes, para não ficar o mesmo preço em todos.
	
	Na obs.1 criei um simples método que geral um json a partir do dicionário do product_id e preço médio, que pode ser usado para enviar a outro sistema.

	Infelizmente não tive muito tempo para fazer todas as melhorias possíveis, mas espero que esteja de acordo com o que foi pedido no desafio, 
qualquer dúvida só entrar em contato comigo, meu email está logo abaixo.


Gustavo Siqueira
gustavo.siqueira@outlook.com
