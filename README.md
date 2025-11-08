# 🩺 Plataforma Médica - Sistema de Agendamento Digital
Projeto desenvolvido pela **KaaioH Soluções Digitais** para gestão de pacientes e agendamento online de consultas.

---

## 🎯 Status do Projeto
| Módulo | Status | Descrição |
| :--- | :--- | :--- |
| **Desenvolvimento (Fase 2)** | ✅ FINALIZADO | Escopo completo entregue (Cadastro, Agendamento, Painel Admin). |
| **Tecnologia** | 🐍 Python/Django | Plataforma robusta, segura e pronta para escalabilidade. |

---

## ✨ Funcionalidades Entregues

A plataforma oferece uma experiência otimizada tanto para o paciente quanto para a equipe administrativa (médico/secretária).

### 1. Agendamento Inteligente para o Paciente

Fim da navegação lenta! O sistema prioriza a usabilidade:
* **Próximo Dia Livre:** A tela de agendamento abre automaticamente no **primeiro dia útil** com horários disponíveis.
* **UX Otimizada:** Navegação rápida por Dia e Semana, com exclusão automática de Sábados e Domingos.
* **Validação em Tempo Real:** Garante que o horário não está ocupado.

**[Captura de Tela: Agendamento e Seleção de Horário (Ex: image_465399.png)]**

> *Instrução: Coloque aqui o link da imagem da tela de agendamento com os slots coloridos e a navegação semanal (Ex: image_465399.png).*

### 2. Cadastro Otimizado
O processo de cadastro é rápido e adaptado para o formato brasileiro.
* **Data Flexível:** Aceita o formato de data brasileiro (DDMMAAAA ou DD/MM/AAAA) sem exigir a formatação com barras.
* **Jornada Direta:** Após o cadastro, o paciente é redirecionado imediatamente para a página de agendamento.

**[Captura de Tela: Formulário de Cadastro (Ex: image_46c3f9.png)]**

> *Instrução: Coloque aqui o link da imagem da tela de cadastro (Ex: image_46c3f9.png).*

### 3. Painel Administrativo Profissional (UX para o Médico)

A gestão da clínica é feita em um painel com design moderno, eliminando a tela administrativa padrão e pouco intuitiva.
* **Interface Jazzmin:** Layout profissional, limpo e com menu lateral de fácil acesso.
* **Gestão de Consultas:** A secretária pode alterar o status da consulta (Pendente -> Confirmada) após o contato de validação com o paciente.
* **Filtros Rápidos:** Pesquisa e filtragem de pacientes e agendamentos por status, data e médico.

**[Captura de Tela: Painel Admin (Ex: image_457ceb.png)]**

> *Instrução: Coloque aqui o link da imagem do painel admin com o tema escuro/azul (Ex: image_457ceb.png).*

---

## 🛠️ Configuração e Instalação (Ambiente de Desenvolvimento)

Para configurar e rodar o projeto localmente:

### Pré-requisitos
* Python 3.9+
* Pip (gerenciador de pacotes Python)

### 1. Clone o Repositório
```bash
git clone [https://docs.github.com/pt/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github](https://docs.github.com/pt/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
cd plataforma_medica
``` 
2. Configurar Ambiente Virtual
```bash
python -m venv venv
.\venv\Scripts\activate  # No Windows
# source venv/bin/activate  # No Linux/macOS
```
3. Instalar Dependências
```bash
pip install -r requirements.txt 
# Observação: Você deve criar o arquivo requirements.txt primeiro: pip freeze > requirements.txt    
```
4. Configurar o Banco de Dados
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Criar Superusuário (Admin)
```bash
python manage.py createsuperuser
# Use o login do médico/secretária (Ex: KaaioH)
```
6. Coletar Arquivos Estáticos (CSS/JS do Jazzmin)
```bash
python manage.py collectstatic --noinput
```
7. Iniciar o Servidor
```bash
python manage.py runserver
```
O sistema estará acessível em: http://127.0.0.1:8000/

Desenvolvido por KaaioH Soluções Digitais © 2025