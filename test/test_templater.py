import templater

def test_is_snippet():
    assert templater.is_snippet('snippet.index.html')

def test_is_no_snippet():
    assert not templater.is_snippet('index.html')

TEMPLATE = '''
'''

def test_generate():
    generated = templater.template(templater.Snippet({'title': 'title'}, '<h1>Hy!</h1>'))


    assert generated.startswith('''<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Security-Policy" content="default-src 'self' 'unsafe-inline' 'unsafe-eval' *;">
  <link rel="stylesheet" href="https://cdn.rawgit.com/Chalarangelo/mini.css/v3.0.1/dist/mini-default.min.css" />
  <link rel="stylesheet" href="static/vanillawar.css" />
  <link rel="shortcut icon" type="image/png" href="static/logo.png" />
  <title>title | Vanilla Warrior</title>
  <meta name="description" content="VanillaWar.com provides guides and resources focussed on the Warrior class in World of Warcraft Classic!" />
  <meta name="robots" content="index, follow" />

  <meta property="og:type" content="article" />
  <meta property="og:title" content="title | Vanilla Warrior" />
  <meta property="og:description" content="VanillaWar.com provides guides and resources focussed on the Warrior class in World of Warcraft Classic!" />
  <meta property="og:image" content="https://www.vanillawar.com/static/logo.png" />
  <meta property="twitter:title" content="title | Vanilla Warrior" />
  <meta property="twitter:description" content="VanillaWar.com provides guides and resources focussed on the Warrior class in World of Warcraft Classic!" />
  <meta property="twitter:creator" content="@WarlordDrak" />
  <meta property="twitter:site" content="@WarlordDrak" />
  <meta property="twitter:image" content="https://www.vanillawar.com/static/logo.png" />

  <script src="static/js/timer.js"></script>

  <script>var whTooltips = {colorLinks: true, iconizeLinks: true, renameLinks: true, hide: {ilvl: true}};</script>
  <script src="https://wow.zamimg.com/widgets/power.js"></script>
</head>

<body>
 <div class="container">
  <a href="https://www.vanillawar.com">
    <div class="banner">
      <img src="static/vanillawar_banner_logo_w_icon_96px.png" alt="Vanilla Warrior Text Logo">
    </div>
  </a>

  <nav class="row">
''')
    assert generated.endswith('''  </nav>

<h1>Hy!</h1>

  <footer class="row">
    <div class="col-sm">
      <p>
        <small>
          <a href="about.html#legal">About</a><br>
          <a href="https://discord.gg/EQERaDj" target="_blank">discord.gg/EQERaDj</a><br>
          © 2018-2020 by <a href="about.html">Warlord Drak</a>
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
''')
