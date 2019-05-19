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
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css" />
  <link rel="stylesheet" href="static/blitz.css" />
  <link rel="shortcut icon" type="image/png" href="static/logo.png" />
  <title>Vanilla Warrior</title>
</head>

<body>
 <div class="container">
  <div class="banner">
    <img src="static/vanillawar_banner_logo_96px.png" alt="Vanilla Warrior Text Logo">
  </div>

  <nav class="row">
    <a href="index.html" class="col-sm-1"><div class="vw-logo"></div></a>
    <a href="level.html" class="col-sm-1">Level</a>
    <a href="talents.html" class="col-sm-1">Talents</a>
    <a href="gear.html" class="col-sm-1">Gear</a>
    <a href="pvp.html" class="col-sm-1">PvP</a>
    <a href="economy.html" class="col-sm-1">Economy</a>
    <a href="ui-and-macros.html" class="col-sm-1">UI and Macros</a>
  </nav>

<h1>Hy!</h1>

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
