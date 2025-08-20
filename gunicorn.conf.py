import multiprocessing

# Socket a que o Gunicorn vai se vincular
bind = "unix:/app/run/gunicorn.sock"

# Número de workers (processos) do Gunicorn
# Um bom ponto de partida é (2 x número de cores da CPU) + 1
workers = multiprocessing.cpu_count() * 2 + 1

# Usuário e grupo que executarão o processo
# user = "www-data"
# group = "www-data"

# Arquivos de log
accesslog = '-' # Envia o log de acesso para a saída padrão
errorlog = '-'  # Envia o log de erro para a saída padrão

# Nível de log
loglevel = "info"
