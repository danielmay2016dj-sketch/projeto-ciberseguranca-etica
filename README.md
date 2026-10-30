# Cibersegurança Ética: Fundamentos e Defesa

Projeto educacional em português inspirado nos tópicos da lição: fundamentos de segurança, tipos de ataque, proteção de credenciais, ferramentas de Kali Linux e laboratório controlado com Metasploitable 2.

## Objetivo

Revisar os conceitos de forma segura por meio de um quiz offline. O projeto **não executa varreduras, tentativas de login, exploração de vulnerabilidades nem envia mensagens**. Todas as perguntas são conceituais e voltadas à defesa.

## Executar

Requisitos: Python 3.9 ou superior. Não há dependências externas.

```bash
python3 quiz.py
```

## Conteúdo abordado

- Princípios de segurança e autorização
- Tipos de ataques e redução de riscos
- Password spraying, credential stuffing e força bruta: diferenças e defesas
- Hashes, senhas e armazenamento responsável de credenciais
- Noções de Nmap, Hydra, John the Ripper, WPScan e Patator no contexto de laboratório autorizado
- Ambiente isolado com Kali Linux e Metasploitable 2
- Wordlists, MFA e riscos de phishing/SMS

## Regras do laboratório

1. Pratique somente em sistemas próprios ou com autorização explícita e por escrito.
2. Use máquinas virtuais isoladas, snapshots e dados fictícios.
3. Não exponha a máquina vulnerável à internet nem use contas ou credenciais reais.
4. Registre escopo, objetivo, evidências e medidas de correção.
5. Ao terminar, desligue o laboratório e reverta o snapshot.

## Estrutura

- `quiz.py` — quiz interativo executado localmente.
- `LICENSE` — licença MIT.

## Aviso

Este material tem finalidade educacional e defensiva. O autor não incentiva acesso não autorizado, coleta de credenciais ou interrupção de serviços. Siga as leis e políticas aplicáveis.
