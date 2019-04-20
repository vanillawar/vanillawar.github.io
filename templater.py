'''
Author: Warlord Drak
'''

import os

TEMPLATE = '''<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.0/dist/mini-default.min.css" />
  <link rel="stylesheet" href="static/blitz.css" />
  <link rel="shortcut icon" type="image/png" href="static/drak.png" />
  <title>Vanilla War</title>
</head>

<body class="container">
  <nav class="row">
    <a href="index.html" class="col-sm-1">Vanilla War</a>
    <a href="level.html" class="col-sm-1">Level</a>
    <a href="talents.html" class="col-sm-1">Talents</a>
    <a href="gear.html" class="col-sm-1">Gear</a>
    <a href="pvp.html" class="col-sm-1">PvP</a>
    <a href="economy.html" class="col-sm-1">Economy</a>
    <a href="ui-and-macros.html" class="col-sm-1">UI and Macros</a>
  </nav>

%s

  <footer class="row">
    <div class="col-sm-12">
      <p>© 2018-2019 Warlord Drak | <a href="https://discord.gg/W55S8MB">discord.gg/W55S8MB</a> | <a href="about.html" class="col-sm-1">About</a></p>
    </div>
  </footer>
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