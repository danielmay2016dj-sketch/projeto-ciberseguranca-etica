# Laboratório de Teste de Intrusão: estudo de brute force com Medusa e Kali Linux

Este repositório reúne material de estudo sobre reconhecimento de rede, segurança de autenticação e defesa contra tentativas repetidas de login. Foi preparado como apoio a uma atividade prática de Segurança da Informação.

> **Situação desta entrega:** não foi possível executar a parte prática porque não há uma máquina virtual disponível. Portanto, não há resultados reais de Nmap ou Medusa nem capturas de execução. O repositório inclui uma simulação defensiva offline e documentação para organizar o estudo. Não declare como realizado o que não foi executado.

## Objetivos

- Entender, em nível conceitual, o reconhecimento autorizado de serviços.
- Diferenciar força bruta, password spraying e credential stuffing.
- Conhecer o papel de Kali Linux, Nmap, Medusa e DVWA em cursos de segurança.
- Demonstrar um controle defensivo de tentativas por meio de uma simulação local, sem senhas ou conexões de rede.
- Identificar medidas para reduzir o risco de abuso de autenticação.

## Ferramentas e ambiente de referência

- **[Kali Linux](https://www.kali.org/):** distribuição usada em cursos e auditorias de segurança. O uso depende de autorização e escopo.
- **[Nmap](https://nmap.org/):** ferramenta de descoberta e auditoria de redes. Não foi executada nesta entrega.
- **[Medusa](https://github.com/jmk-foofus/medusa):** ferramenta de auditoria de autenticação para ambientes controlados. Não foi executada nesta entrega.
- **[DVWA](https://github.com/digininja/DVWA):** aplicação web intencionalmente vulnerável para treinamento em laboratório isolado. Não foi instalada nesta entrega.
- **Python 3:** usado para executar o quiz e a simulação defensiva offline incluídos neste repositório.

## Situação e método da atividade

A prática proposta pela aula pode ser organizada em três etapas conceituais:

### 1. Planejamento e autorização

Antes de qualquer atividade técnica, o instrutor e o estudante devem definir por escrito o ambiente, o escopo, o período, os serviços permitidos e os critérios para interromper o exercício. Um endereço acessível não é, por si só, um alvo autorizado.

### 2. Ambiente de laboratório

Uma atividade operacional exigiria uma VM vulnerável de treinamento, como DVWA, e uma rede virtual isolada preparada pelo instrutor. Esta etapa **não foi realizada** nesta entrega, pois não há uma VM disponível. Não conecte uma aplicação vulnerável a redes públicas, domésticas ou corporativas.

### 3. Análise e defesa

Em vez de enviar tentativas de login a um sistema, este repositório fornece `simulacao_controle.py`. O programa gera eventos fictícios em memória e mostra como um limite defensivo pode bloquear novas falhas. Não testa senhas, não abre conexões e não usa Medusa.

## Executar os materiais locais

Requisito: Python 3; nenhuma dependência externa.

Quiz de revisão:

```bash
python3 quiz.py
```

Simulação defensiva offline:

```bash
python3 simulacao_controle.py
```

Testes automáticos:

```bash
python3 -m unittest discover -s tests -v
```

## Estrutura do repositório

```text
.
├── .github/workflows/test.yml    # testes automáticos no GitHub Actions
├── config/laboratorio.json       # escopo fictício da simulação offline
├── docs/                         # guia, glossário, casos e modelo de relatório
├── images/                       # pasta reservada a capturas reais e sanitizadas
├── tests/                        # testes automatizados
├── quiz.py                       # quiz conceitual
├── simulacao_controle.py         # simulação local de defesa
└── README.md                     # documentação da entrega
```

Não há wordlist de senhas no repositório. Ela não é necessária para a simulação e poderia expor ou facilitar o uso indevido de credenciais. Também não há capturas de ferramentas: nenhuma execução prática foi feita.

## Medidas de mitigação e defesa

- **Senhas únicas e longas:** reduzem o impacto da reutilização de credenciais; um gerenciador pode ajudar.
- **MFA:** adiciona uma etapa de verificação além da senha. Métodos resistentes a phishing são preferíveis quando disponíveis.
- **Limitação de tentativas:** pode reduzir abuso, mas deve ser configurada com cuidado para não bloquear usuários legítimos.
- **Monitoramento:** alertas sobre padrões incomuns e revisão responsável dos registros ajudam a detectar incidentes.
- **Proteção contra phishing:** treinamento e canais oficiais de recuperação reduzem risco de roubo de credenciais.
- **Armazenamento seguro:** aplicações não devem guardar senhas em texto simples; devem usar algoritmos próprios para hashing de senhas e salt individual.
- **Isolamento do laboratório:** máquinas vulneráveis devem ficar em rede virtual isolada, com dados fictícios e snapshot para restauração.

## Evidências e capturas de tela

A pasta `images/` contém registros visuais gerados a partir da saída real dos dois programas locais:

- [Quiz executado](images/quiz-executado.png)
- [Simulação defensiva offline](images/simulacao-offline.png)
- [Nota sobre as capturas](images/REGISTRO.md)

Essas imagens mostram apenas o quiz e a simulação offline; não são capturas de Nmap ou Medusa. Se a prática for realizada posteriormente em ambiente autorizado, novas capturas reais podem ser adicionadas. Antes de enviar imagens, remova senhas, tokens, dados pessoais e informações de rede que não devam ser públicas.

## Recursos de estudo

- [Kali Linux — site oficial](https://www.kali.org/)
- [DVWA — projeto oficial](https://github.com/digininja/DVWA)
- [Medusa — projeto/documentação](https://github.com/jmk-foofus/medusa)
- [Nmap — manual oficial](https://nmap.org/book/man.html)
- [GitHub Quickstart](https://docs.github.com/en/get-started/start-your-journey/hello-world)
- [GitHub Docs](https://docs.github.com/en/get-started/writing-on-github)
- [GitHub Flavored Markdown](https://github.github.com/gfm/)

## Autor e reflexão

**Autor:** Daniel Junior (conforme informado para esta atividade).

Complete esta parte com sua própria reflexão: o que você aprendeu sobre força bruta e defesa? Por que autorização e isolamento são necessários? O que ainda gostaria de praticar quando houver um laboratório disponível?

## Descrição breve para entregar

Projeto de estudo sobre segurança de autenticação com quiz e simulação offline de bloqueio defensivo. Inclui documentação sobre Kali Linux, Nmap, Medusa, DVWA e medidas de mitigação. A prática com VM e ferramentas de rede não foi executada porque não havia máquina virtual disponível.

## Aviso de uso

Material educacional. Não use ferramentas para testar contas, redes, formulários ou serviços sem autorização explícita e escopo escrito. Esta entrega não realiza ataques nem valida credenciais.

## Licença

O código está sob a licença MIT. Consulte `LICENSE`.
