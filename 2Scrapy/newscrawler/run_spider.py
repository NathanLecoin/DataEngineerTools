import os
import subprocess

json_file = 'articles.json'

if os.path.exists(json_file):
    os.remove(json_file)
    print(f"{json_file} supprimé avec succès.")

subprocess.run(['scrapy', 'crawl', 'lemondev4', '-o', json_file])
