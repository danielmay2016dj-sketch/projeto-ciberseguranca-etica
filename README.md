# Cibersegurança: simulação defensiva de tentativas de login

Projeto educacional para acompanhar uma lição introdutória sobre força bruta, Medusa e Kali Linux. O objetivo é explicar o risco de tentativas repetidas de autenticação e mostrar, de forma segura, como um controle defensivo de limite/bloqueio pode responder.

> **Importante:** esta entrega não executa brute force e não usa Medusa contra nenhum serviço. A demonstração é uma simulação local em memória: não testa senhas, não abre conexões e não acessa contas, sites ou redes.

## Objetivos

- Diferenciar força bruta, password spraying e credential stuffing em nível conceitual.
- Reconhecer que ferramentas como Medusa só podem ser usadas em um laboratório autorizado e com escopo explícito.
- Demonstrar uma resposta defensiva simples a falhas repetidas de autenticação.
- Revisar o valor de MFA, monitoramento, senhas únicas e recuperação segura de contas.
- Praticar documentação e organização de um repositório GitHub.

## Como executar

Requisito: Python 3. Não há dependências externas.

Execute o quiz:

```bash
python3 quiz.py
```

Execute a simulação defensiva offline:

```bash
python3 simulacao_controle.py
```

A simulação usa valores fictícios em memória. Por padrão, mostra falhas simuladas até o limite de três e, em seguida, eventos bloqueados. Ela não recebe nem verifica senhas. Para executar os testes:

```bash
python3 -m unittest discover -s tests -v
```

## Como funciona a simulação

A função `simulate_lockout()` recebe apenas uma quantidade de eventos e um limite numérico. Ela registra falhas fictícias e indica quando o controle bloquearia novas tentativas. Não há usuário/senha, formulário, endereço de rede, chamada HTTP ou integração com Medusa. O propósito é visualizar uma medida defensiva e discutir seus limites: bloqueios precisam ser configurados para reduzir abuso sem impedir indevidamente o acesso de usuários legítimos.

## Estrutura do repositório

- `quiz.py` — quiz conceitual sobre segurança e defesa.
- `simulacao_controle.py` — simulação local de limite/bloqueio, sem teste de senha.
- `config/laboratorio.json` — declaração do escopo didático fictício e offline.
- `docs/guia-de-estudos.md` — conceitos, ferramentas em alto nível, proteção de contas e segurança de laboratório.
- `docs/glossario.md` — glossário da lição.
- `docs/casos-para-discussao.md` — cenários fictícios para análise defensiva.
- `docs/modelo-de-relatorio.md` — roteiro para documentar atividade autorizada.
- `tests/` — testes automáticos do quiz e da simulação.
- `.github/workflows/test.yml` — execução automática dos testes no GitHub Actions.
- `images/` — pasta opcional para capturas reais e sanitizadas; não contém imagens inventadas.

## Conceitos importantes

**Força bruta** é a tentativa repetida de combinações contra um mecanismo de autenticação. **Password spraying** usa uma ou poucas senhas comuns contra várias contas. **Credential stuffing** reutiliza pares de credenciais expostos em outros serviços. São riscos diferentes, mas medidas como MFA, senhas únicas, limitação cuidadosa de tentativas, alertas e resposta a incidentes ajudam a reduzir impactos.

Medusa é uma ferramenta mencionada em cursos de auditoria de autenticação. Seu uso operacional pode afetar contas e serviços; por isso, este repositório não fornece comandos de ataque, listas de senhas ou instruções para executá-la. Em qualquer exercício prático, siga o material do instrutor, use apenas sistemas explicitamente autorizados e mantenha o laboratório isolado.

## Proteções que podem ser discutidas

- MFA, preferindo métodos resistentes a phishing quando disponíveis.
- Senhas longas, únicas e armazenadas em um gerenciador confiável.
- Armazenamento de senhas com algoritmo apropriado de hashing e salt individual.
- Alertas para padrões incomuns e revisão de logs com respeito à privacidade.
- Limites de tentativas configurados com cuidado e recuperação segura de conta.
- Treinamento contra phishing e proteção da conta telefônica quando SMS é usado.

## Escopo e segurança

A configuração em `config/laboratorio.json` declara que o exercício é offline, sem alvo, credenciais reais ou wordlist. Não foram incluídos arquivos de senhas: uma lista pode ser reutilizada para tentar autenticar em sistemas, e não é necessária para esta demonstração segura.

Não teste contas, formulários, redes, endereços IP ou serviços de terceiros. Não publique credenciais, tokens, dados pessoais ou informações do laboratório. Se o curso exigir uma prática com ferramenta real, peça ao instrutor o ambiente, autorização e limites por escrito; não adapte esta simulação para outro alvo.

## Capturas de tela opcionais

A pasta `images/` contém instruções. Se quiser incluir evidência, capture a execução local do quiz ou da simulação, revise a imagem para remover informações pessoais e salve-a nessa pasta. Não use capturas fabricadas nem mostre credenciais.

## Entrega

**Link do repositório:** https://github.com/danielmay2016dj-sketch/projeto-ciberseguranca-etica

**Descrição breve para o campo de entrega:** Projeto educativo sobre segurança de autenticação, com quiz e simulação offline de bloqueio defensivo. Inclui guia de estudos, configuração fictícia de laboratório e testes automatizados; não testa senhas nem acessa serviços reais.

## Licença

O código é distribuído sob a licença MIT. Consulte `LICENSE`.

## Recursos oficiais indicados na atividade

- [Kali Linux — site oficial](https://www.kali.org/)
- [DVWA — repositório oficial do projeto](https://github.com/digininja/DVWA)
- [Medusa — repositório/documentação do projeto](https://github.com/jmk-foofus/medusa)
- [Nmap — manual oficial](https://nmap.org/book/man.html)
- [GitHub Quickstart — Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)
- [GitHub Docs — escrita e formatação no GitHub](https://docs.github.com/en/get-started/writing-on-github)
- [GitHub Flavored Markdown — especificação](https://github.github.com/gfm/)

Use a documentação oficial para leitura e contexto. As referências a ferramentas não significam autorização para executar testes em sistemas reais. Para qualquer prática operacional, siga as instruções e o ambiente definido pelo instrutor.
