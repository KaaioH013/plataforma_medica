# 🩺 Plataforma Médica - Sistema de Agendamento Digital
Projeto desenvolvido pela **KaaioH Digitais** para gestão de pacientes e agendamento online de consultas, focado em alta usabilidade (UX) e segurança.

---

## 🎯 Status do Projeto
| Módulo | Status | Descrição |
| :--- | :--- | :--- |
| **Desenvolvimento (Fase 2)** | ✅ FINALIZADO | Escopo completo entregue (Cadastro, Agendamento Inteligente, Painel Admin Estilizado). |
| **Tecnologia** | 🐍 Python/Django | Plataforma robusta, segura e pronta para escalabilidade. |

---

## ✨ Funcionalidades Entregues e UX Aprimorada

A plataforma oferece uma experiência otimizada e inteligente para todos os usuários.

### 1. Agendamento Inteligente para o Paciente

O sistema elimina o problema do usuário ter que "chutar" horários e garante que a agenda da clínica seja respeitada.

* **Próximo Dia Livre Automático:** A tela de agendamento abre no **primeiro dia útil** (pulando fins de semana) com horários disponíveis, eliminando a navegação clique a clique.
* **Navegação Rápida:** O paciente navega por Dias e **Semanas**.
* **Validação de Conflito:** Garante que dois pacientes não agendem o mesmo slot.

![Agendamento Inteligente e Slots Clicáveis](https://raw.githubusercontent.com/KaaioH013/plataforma_medica/main/docs/agendamento_ux.png)

### 2. Cadastro de Pacientes Otimizado

A jornada do novo paciente é direta e adaptada ao Brasil.

* **UX Brasileira na Data:** O campo de data aceita o formato **DDMMAAAA** (ex: 26101996), corrigindo um erro comum de sistemas estrangeiros.
* **Jornada Direta:** Após o cadastro, o paciente é redirecionado imediatamente para a página de **Agendamento** (Fluxo: Cadastrou -> Agenda).

![Formulário de Cadastro com UX Melhorada](https://raw.githubusercontent.com/KaaioH013/plataforma_medica/main/docs/cadastro_ux.png)

### 3. Painel Administrativo Profissional (UX para o Médico/Secretária)

A gestão interna é feita em uma interface moderna e intuitiva, que o cliente espera de um produto final.

* **Design Profissional:** O Painel Admin (acessível via /admin) foi estilizado com o tema Jazzmin, proporcionando um layout limpo, moderno e com menu lateral.
* **Gestão Visual:** Facilita a alteração do status da consulta (PENDENTE -> CONFIRMADA), essencial para a redução de faltas (*No-Show*).
* **Filtros Inteligentes:** Consultas podem ser filtradas por Status, Médico e Data.

![Painel Admin com Tema Profissional (Jazzmin)](https://raw.githubusercontent.com/KaaioH013/plataforma_medica/main/docs/admin_jazzmin.png)

---

## 🛠️ Configuração e Instalação

### Pré-requisitos
* Python 3.12+
* Pip (gerenciador de pacotes Python)
* Ambiente Virtual Ativo (`.\venv\Scripts\activate`)

### Passos
1.  **Clonar:** Clone o repositório.
2.  **Dependências:** Instale os requisitos: `pip install -r requirements.txt`
3.  **Setup:** Configure o banco de dados e o superusuário:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```
4.  **Estáticos:** Colete arquivos de estilos (Jazzmin/Bootstrap): `python manage.py collectstatic --noinput`
5.  **Rodar:** Inicie o servidor: `python manage.py runserver`

---
*Desenvolvido por **KaaioH Soluções Digitais** © 2025. Todos os direitos reservados.*