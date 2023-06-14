import subprocess

# Executar comandos no Git
comandos = [
    'git commit -m "first commit"',
    'git add .',
    'git commit -m "first commit"',
    'git branch -M main',
    'git push'
]

for comando in comandos:
    subprocess.run(comando, shell=True)