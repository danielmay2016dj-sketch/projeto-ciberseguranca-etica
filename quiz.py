#!/usr/bin/env python3
"""Quiz offline de fundamentos de cibersegurança ética e defesa."""

QUESTIONS = [
    {
        "question": "Qual é a prática correta antes de testar a segurança de um sistema?",
        "options": [
            "A) Obter autorização explícita e definir o escopo",
            "B) Testar qualquer sistema acessível pela internet",
            "C) Usar credenciais encontradas em fóruns",
            "D) Desativar os registros para não gerar alertas",
        ],
        "answer": "A",
        "explanation": "Testes devem ocorrer apenas com autorização e escopo claramente definidos.",
    },
    {
        "question": "O que melhor descreve password spraying?",
        "options": [
            "A) Tentar uma senha comum contra várias contas, com cuidado para evitar bloqueios",
            "B) Tentar muitas senhas em uma única conta",
            "C) Reutilizar uma senha vazada em vários serviços automaticamente",
            "D) Armazenar senhas usando um hash forte",
        ],
        "answer": "A",
        "explanation": "A defesa inclui MFA, senhas únicas, detecção de padrões e políticas de autenticação seguras.",
    },
    {
        "question": "Credential stuffing costuma explorar qual problema?",
        "options": [
            "A) Reutilização de credenciais vazadas em outros serviços",
            "B) Certificados TLS atualizados",
            "C) Backups criptografados",
            "D) Atualizações automáticas do sistema",
        ],
        "answer": "A",
        "explanation": "Senhas únicas por serviço e MFA reduzem o risco de reutilização de credenciais.",
    },
    {
        "question": "Qual medida é mais apropriada para armazenar senhas de usuários?",
        "options": [
            "A) Texto simples em uma planilha",
            "B) Hash adaptativo com salt individual, como Argon2id ou bcrypt",
            "C) Uma cifra reversível sem controle de chave",
            "D) A mesma senha para todos os usuários",
        ],
        "answer": "B",
        "explanation": "Um algoritmo de hash de senhas com salt individual dificulta ataques offline após vazamentos.",
    },
    {
        "question": "Em que contexto ferramentas como Nmap ou WPScan devem ser usadas?",
        "options": [
            "A) Em qualquer endereço encontrado online",
            "B) Somente em alvos próprios ou expressamente autorizados e dentro do escopo",
            "C) Para contornar controles de acesso de terceiros",
            "D) Para testar contas reais sem avisar o responsável",
        ],
        "answer": "B",
        "explanation": "Ferramentas legítimas ainda podem causar impacto; autorização e escopo são essenciais.",
    },
    {
        "question": "Qual configuração reduz o risco ao estudar Metasploitable 2?",
        "options": [
            "A) Expor a VM vulnerável diretamente à internet",
            "B) Usar rede isolada de laboratório, snapshots e dados fictícios",
            "C) Conectar a VM à rede corporativa",
            "D) Usar credenciais pessoais reais",
        ],
        "answer": "B",
        "explanation": "Isolamento e snapshots limitam o impacto e permitem restaurar o ambiente com segurança.",
    },
    {
        "question": "Por que MFA é útil contra comprometimento de senhas?",
        "options": [
            "A) Elimina a necessidade de atualizar sistemas",
            "B) Adiciona uma etapa de verificação além da senha",
            "C) Torna seguro compartilhar senhas",
            "D) Impede qualquer tipo de phishing",
        ],
        "answer": "B",
        "explanation": "MFA reduz a dependência de um único segredo, embora não elimine todos os riscos de phishing.",
    },
    {
        "question": "Qual ação é uma resposta defensiva adequada após detectar tentativas suspeitas de login?",
        "options": [
            "A) Ignorar os alertas",
            "B) Preservar registros, investigar o escopo e aplicar controles de contenção",
            "C) Publicar os dados dos usuários",
            "D) Desligar toda a auditoria permanentemente",
        ],
        "answer": "B",
        "explanation": "Uma resposta estruturada preserva evidências e ajuda a conter e corrigir o incidente.",
    },
]


def main():
    print("\nCIBERSEGURANÇA ÉTICA — QUIZ DE FUNDAMENTOS E DEFESA")
    print("Responda A, B, C ou D. Este quiz é apenas conceitual e offline.\n")
    score = 0
    for number, item in enumerate(QUESTIONS, start=1):
        print(f"{number}. {item['question']}")
        for option in item["options"]:
            print(f"   {option}")
        while True:
            response = input("Sua resposta: ").strip().upper()
            if response in {"A", "B", "C", "D"}:
                break
            print("Digite apenas A, B, C ou D.")
        if response == item["answer"]:
            score += 1
            print("Correto! " + item["explanation"] + "\n")
        else:
            print(f"Não foi dessa vez. Resposta: {item['answer']}. {item['explanation']}\n")
    percent = round(score / len(QUESTIONS) * 100)
    print(f"Resultado: {score}/{len(QUESTIONS)} ({percent}%).")
    if percent >= 80:
        print("Ótimo trabalho — continue praticando com autorização e foco defensivo.")
    elif percent >= 50:
        print("Bom começo — revise os conceitos e tente novamente.")
    else:
        print("Vale revisar o README e repetir o quiz.")


if __name__ == "__main__":
    main()
