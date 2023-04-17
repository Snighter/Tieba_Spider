import subprocess

# 运行Scrapy爬虫
subprocess.run(['scrapy', 'crawl', 'tieba_spider', '-o', 'output/output.json'])
subprocess.run(['python', 'GV/run_gv.py'])