'''
Author: Warlord Drak
'''

import os

TEMPLATE = '''<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' ; script-src 'self' 'unsafe-inline' wow.zamimg.com; style-src 'self' 'unsafe-inline' wow.zamimg.com; img-src 'self' *; media-src 'self' ; frame-src wow.zamimg.com;">
  <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css" />
  <link rel="stylesheet" href="static/vanillawar.css" />
  <link rel="shortcut icon" type="image/png" href="static/logo.png" />
  <title>Vanilla Warrior</title>
  <script>var whTooltips = ''' + '{colorLinks: true, iconizeLinks: true, renameLinks: true}' + ''';</script>
  <script src="https://wow.zamimg.com/widgets/power.js"></script>
</head>

<body>
 <div class="container">
  <a href="https://www.vanillawar.com/">
    <div class="banner">
      <img src="static/vanillawar_banner_logo_96px.png" alt="Vanilla Warrior Text Logo">
    </div>
  </a>

  <nav class="row">
    <a href="index.html" class="col-sm-1"><div class="vw-logo"></div></a>
    <a href="level.html" class="col-sm-1">Level</a>
    <a href="talents.html" class="col-sm-1">Talents</a>
    <a href="gear.html" class="col-sm-1">Gear</a>
    <a href="pvp.html" class="col-sm-1">PvP</a>
    <a href="economy.html" class="col-sm-1">Economy</a>
    <a href="ui-and-macros.html" class="col-sm-1">UI and Macros</a>
    <a href="glossary.html" class="col-sm-1">Glossary</a>
  </nav>

%s

  <footer class="row">
    <div class="col-sm">
      <p>
        <small>
          © 2018-2019 by <a href="about.html">Warlord Drak</a><br>
          <a href="https://discord.gg/W55S8MB">discord.gg/W55S8MB</a>
        </small>
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
        rendered = generate(content)
        html_file = target_filename(snippet_file)
        write_file(html_file, rendered)

def is_snippet(filename):
    return filename.startswith('snippet.')

def generate(html_body):
    return TEMPLATE % html_body

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
