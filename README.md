# Gerador-de-Senha
Gerador de senhas configuravel atraves de arquivo .ini

Para gerar o executavel é necessario possuir o pyinstaller instalado:
</br>
<strong>-- pip install pyinstaller </strong>


Para gerar o executavel
</br>
<strong>-- pyinstaller -F GeraSenha.py </strong>


o arquivo.exe será gerado na pasta dist
Não esqueça de copiar o arquivo .ini para a mesma pasta do seu .exe

Para gerar a senha, adicione o campo e seus valores a serem randomizados no arquivo .ini, adicione quantos campos quiser e quantas vezes quiser no campo ordem, sempre dentro de '[ ]', Voce pode adicionar valores constantes na senha, basta que eles estejam fora dos '[ ]'
