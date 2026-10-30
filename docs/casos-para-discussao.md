# Casos para discussão em aula

Os cenários abaixo são fictícios. Não exigem acesso a sistemas nem execução de ferramentas; o objetivo é propor respostas defensivas.

## Caso 1 — Alertas de login em várias contas

Uma equipe recebe alertas de falhas de autenticação em várias contas em um curto período. Não há autorização para fazer testes ativos.

**Converse sobre:** que evidências devem ser preservadas? Quem deve ser avisado? Que controles preventivos podem ser revistos? Como evitar bloquear usuários legítimos durante a investigação?

**Pontos para considerar:** preservar registros de forma controlada, seguir o processo de resposta a incidentes, verificar se há logins bem-sucedidos, avaliar MFA e limites de autenticação e documentar as decisões. Não tente reproduzir o evento em contas reais.

## Caso 2 — Senha reutilizada

Uma pessoa descobre que usou a mesma senha em vários serviços e recebe um aviso de que um dos serviços foi afetado por um vazamento.

**Converse sobre:** qual deve ser a ordem de ações? Como reduzir a chance de o mesmo problema ocorrer novamente?

**Pontos para considerar:** alterar a senha nos serviços afetados por canais oficiais, criar senhas únicas, ativar MFA, encerrar sessões desconhecidas e usar um gerenciador de senhas. Nunca envie sua senha para quem oferece ajuda.

## Caso 3 — Laboratório vulnerável

Uma turma pretende estudar uma máquina virtual vulnerável usando uma distribuição de segurança. Um estudante sugere conectar a VM vulnerável à rede doméstica para facilitar o acesso.

**Converse sobre:** quais riscos existem? Que condições mínimas deveriam ser confirmadas antes de começar?

**Pontos para considerar:** rede virtual isolada, autorização do instrutor, dados fictícios, snapshot, escopo por escrito e procedimento de desligamento/restauração. Se o isolamento não puder ser confirmado, não inicie a prática.

## Caso 4 — Código por SMS inesperado

Uma pessoa recebe códigos de verificação por SMS sem ter tentado entrar na conta.

**Converse sobre:** o que fazer e o que não fazer?

**Pontos para considerar:** não compartilhar o código, acessar o serviço pelo aplicativo ou endereço oficial, revisar sessões e métodos de recuperação, trocar a senha se houver suspeita e contatar o suporte oficial. Não clicar em links recebidos junto à mensagem.

## Registro da discussão

Para cada caso, anote: risco identificado, evidências que seriam necessárias, responsável que deve ser comunicado, ação defensiva de baixo risco e informação que não deve ser compartilhada.
