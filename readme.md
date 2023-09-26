# Projeto BotDiscord com ScrapingMedium

## Objetivo

O objetivo deste projeto é criar um bot do Discord que tem a capacidade de carregar comandos (cogs) dinamicamente e executar scraping em páginas do Medium para capturar screenshots e enviá-las de volta para o canal do Discord de onde o comando foi originado. 

## Funcionalidades

### ScrapingMedium
- Este cog é responsável pela funcionalidade de scraping.
- Captura screenshots de uma URL do Medium fornecida.
- Possui capacidade de login através do Twitter (outras opções de login podem ser adicionadas no futuro).
- Envia a screenshot capturada de volta para o canal do Discord.

## Próximas Atualizações

1. **Melhorias no Cog de Scraping**
   - Adição de suporte para mais tipos de credenciais para login.
   - Melhoria na estabilidade e manipulação de exceções durante o processo de scraping.

2. **Novos Cogs**
   - Desenvolvimento e adição de novos cogs com diferentes funcionalidades, tornando o bot mais versátil.

3. **Otimização de Código**
   - Refatoração e otimização do código existente para melhor desempenho e manutenibilidade.

4. **Integração com Outras Plataformas**
   - Explorar a possibilidade de integrar o bot com outras plataformas e serviços online.

5. **Configurações Dinâmicas**
   - Implementação de um sistema para alterar configurações do bot dinamicamente, sem a necessidade de reiniciar.

## Como Usar

- Clone o repositório e instale as dependências necessárias.
- Crie um arquivo de configuração com as credenciais necessárias e o token do bot do Discord.
- Execute o bot e use o comando `!medium <URL>` em um canal do Discord para capturar uma screenshot de uma página do Medium.

Este projeto está em desenvolvimento ativo, e mais funcionalidades serão adicionadas no futuro. Contribuições e sugestões são sempre bem-vindas!
