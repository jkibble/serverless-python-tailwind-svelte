from jinja2 import Environment, select_autoescape, FileSystemLoader
from babel.support import Translations
from urllib.parse import parse_qs
import json
import pprint
import mimetypes
import jwt
from faker import Faker

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
        if k.endswith(path) and 'css' in v:
            for c in v['css']:
                imports += f'<link rel="stylesheet" href="/static/{c}">'
        if k.endswith(path) and 'file' in v:
            imports += f'<script type="module" src="/static/{v["file"]}"></script>'

    return imports


def post(event, context):
    pp.pprint(parse_qs(event['body']))

    return response('layout.html')


def language(event, context):
    return response({'title': 'title loaded from server', 'subtitle': 'subtitle loaded from server'})


def render(template, **kwargs):
    template = env.get_template(template)
    template.globals.update({'assets_for': assets_for})

    return template.render(kwargs)


def response(body, statusCode=200, contentType='text/html', data={}):
    if isinstance(body, str):
        if body.endswith('.html'):
            body = render(body, **data)
        else:
            body = body
    elif isinstance(body, dict) or isinstance(body, list):
        body = json.dumps(body)
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

    if page == 'login' or page == 'forgot':
        loggedIn = False

    lang = {
        'en': {
            'title': 'here is the title in english',
            'subtitle': 'here is the subtitle in english'
        },
        'es': {
            'title': 'here is the title in spanish'
        }
    }

    return response('layout.html', data={'page': page, 'loggedIn': loggedIn, 'flash': '', 'language': 'es', 'lang': lang})


def login(event, context):
    form = parse_qs(event['body'])

    encoded = jwt.encode(
        {'language': 'en', 'email': form['email'][0], 'flash': 'Login Successful'}, key='start', algorithm='HS256')

    return {
        'statusCode': 307,
        'body': '',
        'headers': {'Set-Cookie': f'token={encoded}; samesite=lax; path=/', 'location': '/'}
    }


def table(event, context):
    fake = Faker()
    result = {'header': [], 'body': []}

    for i in range(0, 8):
        result['header'].append(fake.company())
        result['body'].append([])
        for x in range(0, 8):
            result['body'][i].append(fake.name())

    return response(result)


def static(event, context):
    file = event['pathParameters']['path']
    type = mimetypes.guess_type(file)[0]

    pointer = open(f'public/{file}', 'r')
    body = pointer.read()
    pointer.close()

    return response(body, 200, type)
