import datetime
import os
import json


def generate():
    yesterday = datetime.datetime.utcnow() - datetime.timedelta(days=1)
    month_folder = yesterday.strftime('%Y-%m')
    month_folder_fp = os.path.join('build/output', month_folder)
    yesterday = yesterday.strftime('%Y-%m-%d')
    os.makedirs(month_folder_fp, exist_ok=True)

    content = ''
    for filename in os.listdir('build/cache'):
        if not filename.startswith(yesterday):
            continue
        stream = open(os.path.join('build/cache', filename))
        tweet = json.load(stream)
        stream.close()
        created_at = tweet['created_at'].replace('+0000 ', '')
        created_at = datetime.datetime.strptime(created_at, '%a %b %d %H:%M:%S %Y')
        created_at = created_at.strftime('%H:%M:%S')
        content += '## {}\n{}\n'.format(created_at, tweet['full_text'])

    with open(os.path.join(month_folder_fp, yesterday) + '.md', 'w+') as f:
        f.write(content)

    with open(os.path.join(month_folder_fp, 'index.md'), 'a') as f:
        line = '[{}]({})'.format(yesterday, yesterday)
        f.write(line + '\n')

    with open('build/index.md', 'w+') as f:
        for filename in os.listdir('build/output'):
            line = '[{}](output/{})'.format(filename, filename)
            f.write(line + '\n')
