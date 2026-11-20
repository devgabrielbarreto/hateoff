'use strict';

// Endpoint da API local e seletor do elemento que contém o texto do tweet
const API_URL = 'http://localhost:8989/analise';
const TWEET_SELECTOR = 'div > article > div > div > div:nth-child(3) > div:nth-child(1)';

// Verifica periodicamente até o conteúdo do tweet carregar na página
const interval = setInterval(async () => {
    // Seleciona o container e extrai o texto substituindo quebras de linha por espaço
    const container = document.querySelector(TWEET_SELECTOR);
    const texto = container?.innerText.replace(/\n/g, ' ').trim();

    // Se o tweet ainda não carregou, aguarda a próxima verificação
    if (!texto) return;

    // Para o loop assim que encontra o texto do tweet
    clearInterval(interval);

    try {
        // Monta a URL codificando o texto para evitar quebras com caracteres especiais
        const url = `${API_URL}?texto=${encodeURIComponent(texto)}`;
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Erro na API: ${response.status}`);
        }

        // Lê a classificação retornada pela API (0 = não racista, 1 = racista)
        const dados = await response.json();
        const ehRacista = String(dados.racista) === '1';
        const mensagem = ehRacista
            ? 'Este tweet provavelmente seja racista'
            : 'Este tweet provavelmente não seja racista';

        // Insere o bloco de alerta visual logo acima do tweet
        container.insertAdjacentHTML(
            'beforebegin',
            `
            <ul class="mlext-container">
                <li class="a">${mensagem}</li>
            </ul>
            `
        );
    } catch (erro) {
        // Registra no console caso a API local esteja offline ou falhe
        console.error('[Hateoff] Não foi possível analisar o tweet:', erro);
    }
}, 1000);