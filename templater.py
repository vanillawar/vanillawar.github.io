'''
Author: Warlord Drak
'''

import glob
from html import escape
import json
import os
import time

DESCRIPTION = 'VanillaWar.com provides guides and resources focussed on the Warrior class in World of Warcraft Classic!'

def template(snippet):
    title = snippet.meta.get('title', '')
    if len(title):
        title += " | Vanilla Warrior"
    else:
        title = "Vanilla Warrior"
    rel = snippet.meta.get('rel', '')
    show_header = snippet.meta.get('header', True)
    show_footer = snippet.meta.get('footer', True)
    footer_link = '#' if show_header else 'https://www.vanillawar.com'
    return f'''<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' 'unsafe-inline' 'unsafe-eval' *;">
  <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css" />
  <link rel="stylesheet" href="{rel}static/vanillawar.css" />
  <link rel="shortcut icon" type="image/png" href="{rel}static/logo.png" />
  <title>{title}</title>
  <meta name="description" content="{DESCRIPTION}" />
  <meta name="robots" content="index, follow" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{DESCRIPTION}" />
  <meta property="og:image" content="https://www.vanillawar.com/static/logo.png" />
  <meta property="twitter:title" content="{title}" />
  <meta property="twitter:description" content="{DESCRIPTION}" />
  <meta property="twitter:creator" content="@WarlordDrak" />
  <meta property="twitter:site" content="@WarlordDrak" />
  <meta property="twitter:image" content="https://www.vanillawar.com/static/logo.png" />

  <script src="{rel}static/js/timer.js"></script>

  <script>var whTooltips = ''' + '{colorLinks: true, iconizeLinks: true, renameLinks: true, hide: {ilvl: true}}' + f''';</script>
  <script src="https://wow.zamimg.com/widgets/power.js"></script>
</head>

<body>
 <div class="container">''' + \
  (f'''\n  <a href="https://www.vanillawar.com">
    <div class="banner">
      <img src="{rel}static/vanillawar_banner_logo_w_icon_96px.png" alt="Vanilla Warrior Text Logo">
    </div>
  </a>

  <nav class="row">
    <span class="col-sm"><a href="{rel}pug/ony/">Onyxia PuG</a></span>
    <span class="col-sm"><a href="{rel}tools/honor/">Honor Calculator</a></span>
  <!--
    <span class="col-sm"><a href="{rel}pug/mc/">MC PuG</a></span>
    <span class="col-sm"><a href="{rel}talents.html">Talents</a></span>
    <span class="col-sm"><a href="{rel}pve-gear.html">PvE/Gear</a></span>
    <span class="col-sm"><a href="{rel}pvp.html">PvP</a></span>
    <span class="col-sm"><a href="{rel}gold.html">Gold</a></span>
    <span class="col-sm"><a href="{rel}ui-macros.html">UI/Macros</a></span>
    <span class="col-sm"><a href="{rel}tools.html">Tools</a></span>
    <span class="col-sm"><a href="{rel}glossary.html">Glossary</a></span>
    -->
  </nav>''' if show_header else '') + f'''

{snippet.content}

''' + (f'''  <footer class="row">
    <div class="col-sm">
      <p>
        <small>
          © 2018-2020 by <a href="{rel}about.html">Drak</a> | <a href="{rel}about.html#legal">About</a><br>
          <a href="https://discord.gg/EQERaDj" target="_blank">discord.gg/EQERaDj</a>
        </small>
      </p>
      <p>
      <a href="{footer_link}"><img src="{rel}static/logo.png" src="VanillaWar.com icon" /></a>
      </p>
    </div>
  </footer>''' if show_footer else '') + f'''
 </div>
</body>

</html>
'''

class Snippet(object):
    def __init__(self, meta, content):
        self.meta = meta
        self.content = content

def main():
    snippet_files = [path for path in glob.glob('**/*.html', recursive=True) if is_snippet(path)]
    for snippet_file in snippet_files:
        snippet = read_file(snippet_file)
        html_file = target_filename(snippet_file)
        rendered = template(snippet)
        write_file(html_file, rendered)

    write_sitemap(snippet_files)

def is_snippet(path):
    return path.split('/')[-1].startswith('snippet.')

def target_filename(snippet_filename):
    return snippet_filename.replace('snippet.', '')

def read_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()
        meta = {}
        if len(lines) and lines[0].startswith('<!--') and lines[0].endswith('-->\n'):
            meta = json.loads(lines[0].replace('<!--', '').replace('-->', '').strip())
            lines = lines[1:]
        return Snippet(meta, ''.join(lines))

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

BASE_URI = 'https://www.vanillawar.com/'
def write_sitemap(pages):
    sitemap_xml = []
    sitemap_xml.append('<?xml version="1.0" encoding="utf-8" standalone="yes" ?>')
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    pages = sorted([page for page in pages if page != 'snippet.404.html'])
    for page in pages:
        html_file = target_filename(page).replace('index.html', '')
        last_modified = time.strftime('%Y-%m-%d', time.gmtime(os.path.getmtime(page)))
        sitemap_xml.append(f'  <url>')
        sitemap_xml.append(f'    <loc>{escape(BASE_URI + html_file)}</loc>')
        sitemap_xml.append(f'    <lastmod>{last_modified}</lastmod>')
        sitemap_xml.append(f'  </url>')
    sitemap_xml.append('</urlset>\n')

    write_file('sitemap.xml', '\n'.join(sitemap_xml))

if __name__ == "__main__":
    main()
