# Cibersegurança Ética: fundamentos e defesa

Projeto de estudo em Python criado para revisar os temas de uma lição introdutória de cibersegurança. O programa principal é um quiz offline; a documentação complementar reúne conceitos, cuidados para laboratório e um modelo de relatório.

## Comece por aqui

1. Leia o [guia de estudos](docs/guia-de-estudos.md).
2. Confira os termos no [glossário](docs/glossario.md).
3. Leia os [casos para discussão](docs/casos-para-discussao.md).
4. Execute o quiz no seu computador.
5. Se realizar uma atividade autorizada, registre-a usando o [modelo de relatório](docs/modelo-de-relatorio.md).

## Executar o quiz

Requisito: Python 3. Não há bibliotecas externas para instalar.

```bash
python3 quiz.py
```

Responda com A, B, C ou D. O quiz informa a pontuação e explica cada resposta. Para rodar os testes do projeto:

```bash
python3 -m unittest discover -s tests -v
```

## O que faz parte do projeto

- `quiz.py` — quiz interativo com perguntas conceituais.
- `docs/guia-de-estudos.md` — revisão, ferramentas em alto nível, wordlists, SMS e segurança de laboratório.
- `docs/glossario.md` — termos importantes da lição.
- `docs/casos-para-discussao.md` — cenários fictícios para análise defensiva.
- `docs/modelo-de-relatorio.md` — estrutura para documentar uma prática autorizada.
- `tests/` — testes automáticos da estrutura das perguntas.
- `.github/workflows/test.yml` — execução automática dos testes quando há alterações no GitHub.

## Temas estudados

Princípios de segurança, autorização e escopo; força bruta, password spraying e credential stuffing; wordlists e proteção de dados; boas práticas de senhas, hashing e MFA; contexto responsável de ferramentas como Nmap, Hydra, John the Ripper, WPScan e Patator; e cuidados ao usar Kali Linux e Metasploitable 2 em um laboratório isolado.

## Regras de segurança

Este repositório não executa varreduras, tentativas de login, exploração de falhas nem envio de mensagens. Ferramentas citadas são apresentadas somente como contexto. Qualquer prática deve ocorrer em sistemas próprios ou com autorização explícita, dentro de um escopo definido, sem dados ou contas reais. Máquinas vulneráveis devem permanecer isoladas e ser restauradas ao final.

## Reflexão pessoal

Se este projeto for usado em uma entrega escolar, escreva sua reflexão com suas próprias palavras: o que aprendeu, qual tópico achou mais importante e o que ainda quer estudar. Não apresente como experiência pessoal algo que não realizou.

## Licença

O código é distribuído sob a licença MIT. Veja o arquivo `LICENSE`.
