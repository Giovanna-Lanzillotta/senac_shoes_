# PASSO A PASSO PARA A UTILIZAÇÃO BÁSICA DO GIT/GITHUB

1. Ir no github e criar o repositório do projeto;
2. Abrir o diretório do projeto no VScode.
3. Abrir a tela do terminal do VScode (CTRL + J).
4. git init -> Cria o repositório local do projeto na pasta aonde ele está armazenado.
5. Informar as credencias do git, isso é realizado uma unica vez no computador.
- git config --global user.name "Giovanna Lanzillotta"
- git config --global user.email "lanzillottagigi@gmail.com"
6. git status -> Verifica quais arquivos/pastas foram enviadas para o repositório local.
7. git add . -> Inclui todos os arquivos/pastas no repositório local.
8. git branch -M main->Altera o nome da branch atual para main.
9. git commit -m "A informação fica aqui" -> Realiza um novo commit no repositório local.
10. git remote add origin endereço_do_repositorio_remoto -> Comando para realizar a sincronização do repositório local com o remoto.
11. git push -u origin main -> Envia o repositório local para o remoto.