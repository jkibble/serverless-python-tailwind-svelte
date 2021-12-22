from jinja2 import Environment, select_autoescape, FileSystemLoader
from babel.support import Translations
import json
import pprint
import mimetypes

pp = pprint.PrettyPrinter(indent=4)

env = Environment(
    loader=FileSystemLoader('pages/'),
    autoescape=select_autoescape(),
    extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape', 'jinja2.ext.with_']
)

translations = Translations.load(
    'services/index/i18n', ['en'])
env.install_gettext_translations(translations)


def asset_for(path):
    with open('public/manifest.json') as json_file:
        data = json.load(json_file)
    
    file, ext = path.split('.')

    for k, v in data.items():
        if k.endswith(file):
            if ext in v:
                return f'/static/{v[ext][0]}'
            elif ext == 'js':
                return f'/static/{v["file"]}'
    return ''

def render(template, **kwargs):
    template = env.get_template(template)
    template.globals.update({'asset_for': asset_for})

    return template.render(kwargs)


def response(content, statusCode=200, contentType='text/html', data={}):
    if isinstance(content, str):
        if content.endswith('.html'):
            body = render(content, **data)
        else:
            body = content
    elif isinstance(content, dict):
        body = json.dumps(content)
        contentType = 'application/json'

    return {
        'statusCode': statusCode,
        'body': body,
        'headers': {'content-type': contentType}
    }


def api(event, context):
    if event['pathParameters']['path']:
        page = event['pathParameters']['path']
    else:
        page = 'index'
    return response('layout.html', data={'page':page})


def static(event, context):
    file = event['pathParameters']['path']
    type = mimetypes.guess_type(file)[0]

    pointer = open(f'public/{file}', 'r')
    body = pointer.read()
    pointer.close()

    return response(body, 200, type)
