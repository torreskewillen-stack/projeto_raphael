function adicionarCarrinho(nome, preco) {
    let carrinho = JSON.parse(localStorage.getItem('carrinho')) || [];

    const quantidade = parseInt(
        document.getElementById('quantidade')?.value || 1
    );

    const produtoExistente = carrinho.find(
        produto => produto.nome === nome
    );

    if (produtoExistente) {
        produtoExistente.quantidade += quantidade;
    } else {
        carrinho.push({
            nome: nome,
            preco: preco,
            quantidade: quantidade
        });
    }

    localStorage.setItem('carrinho', JSON.stringify(carrinho));

    alert('Produto adicionado à sacola!');
}