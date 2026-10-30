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

    {
        "question": "Qual é a finalidade geral de uma distribuição como Kali Linux em um curso de segurança?",
        "options": [
            "A) Oferecer ferramentas para auditoria e estudo em ambientes autorizados",
            "B) Garantir acesso a qualquer sistema conectado à internet",
            "C) Substituir a autorização do responsável pelo sistema",
            "D) Tornar inofensiva qualquer ferramenta executada",
        ],
        "answer": "A",
        "explanation": "A distribuição reúne ferramentas; o uso continua sujeito a autorização, escopo e medidas de segurança.",
    },
    {
        "question": "Por que uma wordlist usada em um exercício deve ser fictícia e restrita ao laboratório?",
        "options": [
            "A) Para evitar expor dados pessoais e limitar o exercício ao escopo autorizado",
            "B) Para facilitar o uso de senhas reais de colegas",
            "C) Porque listas de palavras substituem a autorização",
            "D) Para compartilhar credenciais publicamente",
        ],
        "answer": "A",
        "explanation": "Dados fictícios e escopo controlado reduzem riscos de privacidade e uso indevido.",
    },
    {
        "question": "Qual medida ajuda a reduzir o risco de abuso de formulários de login?",
        "options": [
            "A) Monitorar padrões, limitar tentativas com cuidado e oferecer MFA",
            "B) Armazenar senhas em texto simples para facilitar a auditoria",
            "C) Desativar registros de autenticação",
            "D) Usar a mesma senha para todos os usuários",
        ],
        "answer": "A",
        "explanation": "Controles de autenticação, monitoramento e MFA ajudam a detectar e reduzir tentativas abusivas.",
    },
    {
        "question": "Qual é um risco de depender apenas de códigos enviados por SMS para MFA?",
        "options": [
            "A) SMS pode estar sujeito a fraude, interceptação ou redirecionamento do número",
            "B) SMS impede toda forma de phishing",
            "C) SMS elimina a necessidade de proteger a conta telefônica",
            "D) SMS torna segura a reutilização de senhas",
        ],
        "answer": "A",
        "explanation": "MFA é útil, mas os métodos variam em resistência. Proteja também a conta telefônica e prefira métodos mais resistentes a phishing quando disponíveis.",
    },
    {
        "question": "Qual descrição de Metasploitable 2 é adequada em uma aula?",
        "options": [
            "A) Uma máquina vulnerável intencionalmente criada para treinamento controlado",
            "B) Um serviço público que pode ser testado sem autorização",
            "C) Um substituto para backups e snapshots",
            "D) Um sistema que deve ser exposto para receber tráfego externo",
        ],
        "answer": "A",
        "explanation": "Ela deve ser usada em ambiente isolado, com autorização e sem exposição à internet.",
    },
]


def main():
    print("\nQuiz de cibersegurança ética: fundamentos e defesa")
    print("Vamos revisar os conceitos. Responda A, B, C ou D. O quiz é offline e conceitual.\n")
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
            print("Isso mesmo! " + item["explanation"] + "\n")
        else:
            print(f"Quase! A resposta correta é: {item['answer']}. {item['explanation']}\n")
    percent = round(score / len(QUESTIONS) * 100)
    print(f"Resultado: {score}/{len(QUESTIONS)} ({percent}%).")
    if percent >= 80:
        print("Muito bem! Continue estudando com responsabilidade e foco na defesa.")
    elif percent >= 50:
        print("Bom começo! Revise os conceitos e tente mais uma vez.")
    else:
        print("Sem problema: leia o README, revise o conteúdo e tente novamente.")


if __name__ == "__main__":
    main()
