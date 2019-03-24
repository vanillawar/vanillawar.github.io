import templater

def test_is_snippet():
    assert templater.is_snippet('snippet.index.html')

def test_is_no_snippet():
    assert not templater.is_snippet('index.html')

TEMPLATE = '''
'''

def test_generate():
    assert templater.generate('<h1>Hy!</h1>') == '''<!DOCTYPE html>
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

<h1>Hy!</h1>

  <footer class="row">
    <div class="col-sm-12">
      <p>© 2018-2019 Warlord Drak | <a href="https://discord.gg/W55S8MB">discord.gg/W55S8MB</a> | <a href="about.html" class="col-sm-1">About</a></p>
    </div>
  </footer>
</body>

</html>
'''
