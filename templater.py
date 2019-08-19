'''
Author: Warlord Drak
'''

import glob
import json
import os
import time

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
  <meta name="description" content="World of Warcraft: Classic (Vanilla) Warrior guides and resources!" />
  <meta name="robots" content="index, follow" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="World of Warcraft: Classic (Vanilla) Warrior guides and resources!" />
  <meta property="og:image" content="https://www.vanillawar.com/static/logo.png" />
  <meta property="twitter:title" content="{title}" />
  <meta property="twitter:description" content="World of Warcraft: Classic (Vanilla) Warrior guides and resources!" />
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
    <span class="col-sm"><a href="{rel}level.html">Level</a></span>
    <span class="col-sm"><a href="{rel}talents.html">Talents</a></span>
    <span class="col-sm"><a href="{rel}pve-gear.html">PvE/Gear</a></span>
    <span class="col-sm"><a href="{rel}pvp.html">PvP</a></span>
    <span class="col-sm"><a href="{rel}gold.html">Gold</a></span>
    <span class="col-sm"><a href="{rel}ui-macros.html">UI/Macros</a></span>
    <span class="col-sm"><a href="{rel}tools.html">Tools</a></span>
    <span class="col-sm"><a href="{rel}glossary.html">Glossary</a></span>
  </nav>''' if show_header else '') + f'''

{snippet.content}

''' + (f'''  <footer class="row">
    <div class="col-sm">
      <p>
        <small>
          © 2018-2019 by <a href="{rel}about.html">Drak</a> | <a href="{rel}about.html#legal">About</a>
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
        print(time.ctime(os.path.getmtime(snippet_file)) + " " + snippet_file + " " + html_file)
        rendered = template(snippet)
        write_file(html_file, rendered)

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

if __name__ == "__main__":
    main()
