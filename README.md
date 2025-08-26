# Sistema de Gerenciamento de Materiais de Construção

Este é um sistema bem simples em Python para cadastro, listagem e venda de materiais de construção.  
O programa roda no terminal e permite gerenciar produtos da loja, assim como realizar as vendas.

---

# Funcionalidades
- Cadasto de múltiplos produtos (nome, unidade, preço, estoque).  
- Listagem detalhada dos produtos cadastrados.  
- Realização de vendas, com:
  - Escolha do produto pelo índice.
  - Validação de estoque disponível.
  - Aplicação de desconto automático se o valor bruto for maior que R$100,00.
- Atualização automática do estoque após cada venda.
- Relatório de venda exibindo:
  - Produto
  - Quantidade
  - Valor bruto
  - Desconto aplicado (quando houver)
  - Valor final
  - Estoque atualizado

---

# Pré-requisitos
- Python 3.8 ou superior instalado na máquina.  
Pode verificar com o comando:
```bash
python --version
