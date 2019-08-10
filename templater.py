'''
Author: Warlord Drak
'''

import os

def template(title, content):
    return f'''<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' 'unsafe-inline' 'unsafe-eval' *;">
  <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css" />
  <link rel="stylesheet" href="static/vanillawar.css" />
  <link rel="shortcut icon" type="image/png" href="static/logo.png" />
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

  <script src="static/js/timer.js"></script>

  <script>var whTooltips = ''' + '{colorLinks: true, iconizeLinks: true, renameLinks: true, hide: {ilvl: true}}' + f''';</script>
  <script src="https://wow.zamimg.com/widgets/power.js"></script>
</head>

<body>
 <div class="container">
  <a href="https://www.vanillawar.com/">
    <div class="banner">
      <img src="static/vanillawar_banner_logo_w_icon_96px.png" alt="Vanilla Warrior Text Logo">
    </div>
  </a>

  <nav class="row">
    <span class="col-sm"><a href="level.html">Level</a></span>
    <span class="col-sm"><a href="talents.html">Talents</a></span>
    <span class="col-sm"><a href="pve-gear.html">PvE/Gear</a></span>
    <span class="col-sm"><a href="pvp.html">PvP</a></span>
    <span class="col-sm"><a href="gold.html">Gold</a></span>
    <span class="col-sm"><a href="ui-macros.html">UI/Macros</a></span>
    <span class="col-sm"><a href="glossary.html">Glossary</a></span>
  </nav>

{content}

  <footer class="row">
    <div class="col-sm">
      <p>
        <small>
          © 2018-2019 by <a href="about.html">Drak</a> | <a href="tools.html">Tools</a> | <a href="about.html#legal">About</a>
        </small>
      </p>
      <p>
      <a href="#"><img src="static/logo.png" src="VanillaWar.com icon" /></a>
      </p>
    </div>
  </footer>
 </div>
</body>

</html>
'''

def main():
    snippet_files = [filename for filename in os.listdir('.') if is_snippet(filename)]
    for snippet_file in snippet_files:
        content = read_file(snippet_file)
        html_file = target_filename(snippet_file)
        title = html_file.replace(".html", "")
        if len(title) == 0 or title == 'index':
            title = "Vanilla Warrior"
        else:
            title += " | Vanilla Warrior"
        rendered = template(title, content)
        write_file(html_file, rendered)

def is_snippet(filename):
    return filename.startswith('snippet.')

def target_filename(snippet_filename):
    return snippet_filename.replace('snippet.', '')

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    main()
