# Guia de estudos: fundamentos de cibersegurança

Este guia resume os principais conceitos da lição e ajuda a organizar uma prática autorizada. O repositório contém material de estudo e uma simulação defensiva.

## 1. Objetivos de aprendizagem

Ao terminar esta revisão, a pessoa estudante deverá conseguir:

- explicar por que autorização, escopo e registro são necessários em um teste de segurança;
- diferenciar tentativas comuns de comprometimento de credenciais;
- indicar medidas básicas para proteger contas e senhas;
- reconhecer que ferramentas de segurança podem causar impacto e exigem controle;
- descrever como manter um laboratório vulnerável isolado;
- registrar observações e recomendações de forma clara.

## 2. Princípios básicos

A segurança da informação é frequentemente explicada pelos princípios de confidencialidade, integridade e disponibilidade. Confidencialidade significa que a informação só deve ser acessada por quem tem permissão. Integridade trata de manter os dados corretos e detectar alterações indevidas. Disponibilidade significa que sistemas e dados estejam acessíveis quando necessários.

Autorização vem antes da atividade técnica. Um teste responsável define quem autorizou, quais sistemas estão incluídos, quais atividades são permitidas e quando o trabalho deve parar. Um endereço acessível pela internet não é automaticamente um alvo permitido.

## 3. Tentativas contra credenciais

- **Força bruta:** muitas combinações são tentadas contra uma conta ou serviço. Limites de tentativas e monitoramento ajudam a reduzir o risco.
- **Password spraying:** uma ou poucas senhas comuns são usadas contra várias contas. Alertas por padrão de tentativas, MFA e políticas de senha ajudam na defesa.
- **Credential stuffing:** pares de usuário e senha expostos em um serviço são reutilizados em outros. Senhas únicas e MFA são importantes para reduzir o impacto.

Esses termos descrevem riscos para fins de reconhecimento e prevenção; este projeto não automatiza tentativas de login.

## 4. Proteção de contas e senhas

Use senhas longas e únicas, preferencialmente gerenciadas por um gerenciador confiável. Ative autenticação multifator sempre que possível e prefira métodos resistentes a phishing quando disponíveis. Sistemas que armazenam senhas devem usar funções próprias para hashing de senhas, com salt individual e parâmetros adequados; não devem guardar senhas em texto simples.

MFA reduz o risco, mas não elimina todos os ataques. Treinamento contra phishing, atualização de sistemas, controle de acesso, limitação de tentativas e monitoramento continuam importantes.

## 5. Ferramentas citadas na lição

Ferramentas como Nmap, Hydra, John the Ripper, WPScan e Patator aparecem em cursos de segurança para auditoria e laboratório. A ferramenta, por si só, não torna uma atividade autorizada. Seu uso deve estar limitado a máquinas próprias ou a um escopo formalmente autorizado. Este projeto apenas apresenta o contexto defensivo e não contém comandos para executá-las contra alvos.

## 6. Preparação de um laboratório seguro

1. Confirme a autorização e escreva o objetivo do exercício.
2. Use máquinas virtuais descartáveis e uma rede virtual isolada, sem encaminhamento para a internet ou para redes de terceiros.
3. Não use dados pessoais, contas reais ou senhas reutilizadas.
4. Crie um snapshot antes do exercício e defina como restaurar o ambiente.
5. Registre horário, observações e mudanças feitas.
6. Pare se o teste sair do escopo ou afetar um sistema que não faz parte do laboratório.
7. Ao terminar, desligue as máquinas vulneráveis e restaure o snapshot.

## 7. Perguntas para revisão

1. Por que a autorização precisa definir também o escopo e o período do teste?
2. Qual é a diferença entre password spraying e credential stuffing?
3. Como MFA e senhas únicas reduzem riscos diferentes?
4. Por que uma máquina vulnerável deve ficar isolada?
5. Que informações devem aparecer em um relatório de atividade?

## 8. Reflexão individual

Escreva com suas próprias palavras qual conceito foi mais importante para você, o que ainda precisa revisar e como aplicaria as práticas defensivas em um ambiente autorizado. Não apresente como experiência pessoal algo que você não realizou.

## 9. Kali Linux e ferramentas: visão geral

Kali Linux é uma distribuição voltada a testes de segurança e treinamento. Ela não concede permissão para testar sistemas de terceiros. O ambiente de trabalho precisa estar definido antes de abrir qualquer ferramenta.

| Ferramenta | Uso geral em segurança | Lembrete defensivo |
|---|---|---|
| Nmap | Inventário e avaliação de serviços de rede | Use somente no escopo autorizado; confirme horário e limites com o responsável. |
| Hydra | Avaliação de controles de autenticação em laboratório | Não teste formulários ou contas reais sem autorização específica. |
| John the Ripper | Auditoria de qualidade de senhas em material autorizado | Trabalhe com hashes de demonstração, nunca com dados obtidos sem permissão. |
| WPScan | Avaliação de segurança de instalações WordPress autorizadas | Preserve o ambiente e siga o escopo e a política do responsável pelo site. |
| Patator | Estrutura de testes de autenticação em contexto controlado | Pode gerar tentativas numerosas; não use contra serviços públicos ou contas reais. |

A tabela serve para reconhecer o papel geral das ferramentas. Não é um roteiro de execução. A autorização, o escopo e a contenção continuam indispensáveis.

## 10. Wordlists e cuidado com dados

Uma wordlist é uma coleção de palavras que pode aparecer em contextos de auditoria e treinamento. Listas obtidas de vazamentos podem conter dados pessoais e credenciais reais. Em exercícios acadêmicos, prefira conjuntos sintéticos fornecidos pelo instrutor e nunca publique listas com senhas, nomes ou outros dados pessoais. Não compartilhe arquivos de credenciais em repositórios Git.

Antes de enviar qualquer arquivo ao GitHub, confira se ele não contém senhas, tokens, chaves privadas, endereços ou dados de pessoas. Se um segredo for publicado por engano, removê-lo do arquivo não basta: revogue ou troque a credencial imediatamente e avise o responsável.

## 11. Riscos de autenticação por SMS

Códigos por SMS podem ser mais vulneráveis a fraude envolvendo a linha telefônica, interceptação ou engenharia social do que métodos mais resistentes a phishing. Sempre que possível, utilize uma chave de segurança ou aplicativo autenticador aprovado pela organização. Proteja a conta da operadora com PIN e mecanismos de recuperação seguros. Nenhum método dispensa senhas únicas, atenção a mensagens suspeitas e canais oficiais de recuperação.

## 12. Análise de tentativas de acesso — abordagem defensiva

Ao revisar alertas de login, um analista autorizado pode observar horários, volume, origem aproximada, quantidade de contas afetadas e resultados de autenticação. A análise deve respeitar a privacidade, limitar o acesso aos registros e seguir o plano de resposta a incidentes. Medidas possíveis incluem alertar o responsável, revogar sessões suspeitas, exigir redefinição de credenciais quando justificado e reforçar MFA. Preserve evidências e documente cada ação.

## 13. Escopo para um exercício escolar

Um escopo escrito deve indicar: máquinas virtuais específicas, rede isolada utilizada, janela de tempo, atividades permitidas, atividades proibidas, pessoa responsável, contato de emergência, critérios para interromper a prática e procedimento de restauração. Se algum item não estiver claro, interrompa a atividade e peça orientação ao instrutor.

## 14. Demonstração segura de controles de autenticação

O arquivo `simulacao_controle.py` representa eventos de falha usando apenas números fictícios. A função não pede usuário ou senha e não envia tráfego. O limite é um exemplo didático, não uma recomendação universal de configuração: sistemas reais precisam equilibrar segurança, disponibilidade e risco de bloqueio indevido.

Na discussão, compare controles possíveis: MFA, alertas, limites graduais, detecção de padrões, recuperação de conta e suporte ao usuário. Considere também que mensagens de erro excessivamente detalhadas podem revelar informações sobre contas. Não use a simulação como base para automatizar tentativas contra um serviço real.
