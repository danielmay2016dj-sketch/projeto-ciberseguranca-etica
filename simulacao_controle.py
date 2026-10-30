#!/usr/bin/env python3
"""Simulação offline de bloqueio defensivo; não verifica senhas nem acessa redes."""


def simulate_lockout(attempts: int = 6, threshold: int = 3) -> dict:
    """Simula eventos de falha de login e bloqueio, sem credenciais reais."""
    if attempts < 0:
        raise ValueError("attempts não pode ser negativo")
    if threshold < 1:
        raise ValueError("threshold deve ser pelo menos 1")

    failures = 0
    events = []
    locked = False
    for attempt in range(1, attempts + 1):
        if failures >= threshold:
            locked = True
            events.append(f"Tentativa simulada {attempt}: bloqueada pelo controle defensivo")
            continue
        failures += 1
        events.append(f"Tentativa simulada {attempt}: falha registrada ({failures}/{threshold})")
    return {"events": events, "failures": failures, "locked": locked}


def main() -> None:
    result = simulate_lockout()
    print("SIMULAÇÃO OFFLINE — controle de tentativas de login")
    print("Nenhuma senha é testada. Nenhuma rede ou conta real é acessada.\n")
    for event in result["events"]:
        print(event)
    print("\nConclusão: limites de tentativas podem reduzir abuso, mas devem ser combinados")
    print("com MFA, monitoramento e recuperação segura para evitar bloquear usuários legítimos.")


if __name__ == "__main__":
    main()
