from jinja2 import Environment, select_autoescape, FileSystemLoader
from babel.support import Translations
from urllib.parse import parse_qs
import json
import pprint
import mimetypes
import jwt

pp = pprint.PrettyPrinter(indent=4)

env = Environment(
    loader=FileSystemLoader('pages/'),
    autoescape=select_autoescape(),
    extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape', 'jinja2.ext.with_']
)

translations = Translations.load(
    'services/index/i18n', ['en'])
env.install_gettext_translations(translations)

def assets_for(path):
    imports = ''
    with open('public/manifest.json') as json_file:
        data = json.load(json_file)
    
    for k, v in data.items():
        if k.endswith(path) and 'file' in v:
            imports += f'<script type="module" src="/static/{v["file"]}"></script>'
        if k.endswith(path) and 'css' in v:
            for c in v['css']:
                imports += f'<link rel="stylesheet" href="/static/{c}">'
    
    return imports


def render(template, **kwargs):
    template = env.get_template(template)
    template.globals.update({'assets_for': assets_for})

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

    loggedIn = True

    pp.pprint(parse_qs(event['cookies'][0]))

    if page == 'login' or page == 'forgot':
        loggedIn = False
    
    return response('layout.html', data={'page':page, 'loggedIn': loggedIn, 'flash': ''})

def login(event, context):
    form = parse_qs(event['body'])

    encoded = jwt.encode({'language': 'en', 'email': form['email'][0], 'flash': 'Login Successful'}, key='start', algorithm='HS256')

    return {
        'statusCode': 307,
        'body': '',
        'headers': {'Set-Cookie': f'token={encoded}; samesite=lax; path=/', 'location': '/'}
    }


def static(event, context):
    file = event['pathParameters']['path']
    type = mimetypes.guess_type(file)[0]

    pointer = open(f'public/{file}', 'r')
    body = pointer.read()
    pointer.close()

    return response(body, 200, type)
