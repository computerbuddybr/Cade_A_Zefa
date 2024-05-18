# Cadê a Zefa Gente!
## Tutorial de Jogo educacional em Tkinter para Desktop e Raspberry Pi

### Informações
- **Autora:** Adriana Laura Cerdeira
- **Projeto Final de Conclusão de Curso em Enegenharia de Computação - Universidade Anhembi Morumbi**
- **Outros integrantes do grupo de projeto final:** Diego Luiz Godoy Portalupi, Leonardo Bueno Santos, Hudson Gustavo Ferreira, Mikaelle Cristina Iosi
- **Outros integrantes do grupo de pré-projeto final:** Andre de Almeida Alves Batista, Gabriel Campos de Paula, Janderson Barbosa Braz, Thiago Henrique da Cruz
 **Nota Final**: 10




### Bem vindos, bem vindas ao nosso Projeto de Conclusão de Curso em Engenharia de Computação!

Este projeto foi desenvolvido como o nosso TCC e tem como premissa a disponibilização de um tutorial com código fonte aberto para que qualquer pessoa possa desenvolver um jogo de detetive digital com Raspberry Pi. O nosso público alvo principal são professores de escolas de ensino fundamental e médio que queiram ensinar programação e eletrônica de uma forma divertida e interativa, mas qualquer um que tenha interesse em praticar programação em Python e o GPIO de Raspberry Pi com entradas de botões vai encontrar um material interessante e gratuito aqui.

Este projeto não tem fins lucrativos, é feito com a intenção de fornecer um material de ensino modular para professores que queiram utilizá-lo. Ele é muito adaptável, o professor pode escolher adotá-lo na integra ou em partes. E o jogo escolhido também é educacional, para que depois possa ser usado para jogar e aprender.

Recomendo assistir ao vídeo introdutório:
[Aula 01 - Apresentação](https://youtu.be/LeJLGBOfmYs)

[Os vídeos tutoriais estão disponíveis no YouTube e podem ser acessados aqui.](https://www.youtube.com/playlist?list=PLhx-V5qg9T6RO1tbo4svEUJkJL4f0R207)

O código do jogo está neste mesmo repositório, na pasta [Jogo](Jogo/).

Os recursos para o tutorial se encontram na pasta [Recursos](Recursos/), onde você encontra detalhes de diagramas, bibliotecas usadas, links para cursos de base, além de outras informações.

Além disso, para quem quer adaptar a base de dados para si, na pasta [BaseVazia](Recursos/BaseVazia/), você encontra uma base que contém somente as tabelas, mas sem a informação, para adicionar a informação que quiser.

A pasta [DBModelagem](Recursos/DBModelagem/) possui o modelo da base de dados em formato .mwb, além de arquivo com o DDL da base para quem quiser montar a base do zero e dois arquivos de ajuda para popular os continentes e países com sua configuração em Outubro de 2023.

E tem um executável para Windows em [ZipComExecutavelDoJogo](Recursos/ZipComExecutavelDoJogo/).

### O Projeto

Neste projeto, criaremos um jogo de detetive chamado "Cadê a Zefa, gente!" onde o jogador deve perseguir a Zefa, notória ladra internacional de origem brasileira que atua mundo afora desde que ela roubou a taça Jules Rimet com seu pai (um quinto integrante do grupo que a PF nunca divulgou e que escapou), em 1983 na tenra idade de 10 anos. Desde então ela tem aplicado roubos cada vez mais ousados pelo Brasil e o mundo e a nossa dedicada PF nunca deixou de persegui-la décadas afora. Será o nosso detetive intrépido a pessoa que finalmente irá apreender está elusiva ladra?

Este jogo será criado em 3 versões diferentes. Uma para se jogar na Linha de Comando de qualquer computador. Uma para se jogar em qualquer computador com uma interface gráfica. E uma para se jogar em um Raspberry Pi com uma interface gráfica e botões físicos e um display de 7".

Você educador pode escolher qualquer um destes projetos, ou todos. Ou pode até escolher que seus alunos simplesmente joguem o jogo. Nos tutoriais vou mostrar como alterar a base de dados para poder colocar informação relevante aos seus estudos.

Há já uma base de dados pronta com 35 cidades, seus casos e pistas. Porém esta base foi criada por alunos de Engenharia de Computação, não História ou Geografia, com informações tiradas da Wikipedia. Então, por favor levar isto em consideração ao usá-la.

Bons estudos!

### A escolha do nome
Este projeto é voltado para escolas brasileiras e queriamos um nome que fosse bem emblemático do Brasil. Que mostrasse nossa cultura de acolhimento. Nossa cultura de sempre sermos simpáticos e já acolher os outros de cara. Por isso mesmo é um apelido, e não o nome. Porque isso também é um traço nosso de sermos informais e de sempre termos um apelido para todo mundo. E também porque é um nome que é comum no Brasil, mas não em outros países. 

Eu gosto muito do nome justamente por isso. Por ele representar o que eu mais amo do nosso país que é essa simpatia do Brasileiro. Essa disponibilidade para ajudar. Tive oportunidade de morar fora várias vezes e sempre decidi voltar para o Brasil. Apesar de ter morado nos Estados Unidos e a Europa eu ainda considero o Brasil, com todos seus problemas, o melhor lugar para morar. E é por causa do Brasileiro. Problemas você encontra em todo lugar. Mas esse jeito, de ajudar um ao outro não. E eu acho que isso é o que faz o Brasil ser um lugar tão especial. E é por isso que eu quis colocar esse nome no jogo. Porque eu acho que ele representa o que eu mais amo do Brasil.

A Zefa é uma ladra internacional. Ela é perigosa. Mas ela não deixa de ser brasileira. Portanto mesmo perigosa, ela é simpática. Muitas pistas serão de como ela conversou com alguém que a estava atendendendo, sobre algum assunto. Batendo papo mesmo. Porque isso é muito nosso. De chegar em qualquer lugar, no bar, na fila do banco, da padaria, e começar a conversar com estranhos como se fossem amigos de longa data. E é claro, que nossa ladra não vai ser diferente. Ela vai chegar em qualquer lugar e vai começar a conversar com as pessoas. E é claro que ela vai deixar pistas. Porque ela é brasileira. E ela é simpática. E é por isso que o jogo se chama "Cadê a Zefa, gente!".

### A licença

O código e tutoriais está sendo fornecido de forma gratuita para ser usado baixo as regras da licença GNU GPL (Licença Geral Pública). Você pode usar e distribuir este material à vontade. Você não pode vendê-lo ou usá-lo para fins lucrativos. Não foi criado para fins lucrativos, mas para fins educacionais.

Você e qualquer pessoa à qual você venha a entregar este material isentam os autores deste projeto de responsabilidade sobre o uso deste jogo e tutorial, sendo você o único responsável por qualquer uso que você faça do material contido aqui neste repositório e nos links associados, e qualquer consequência deste uso.

### Isenção
Os autores deste trabalho e repositório não são responsáveis por qualquer dano causado ao baixar arquivos deste projeto.
