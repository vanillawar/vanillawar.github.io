import templater

INDEX_HTML = '''<!DOCTYPE html>
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

<div class="row">
  <div class="col-sm-12">
    <h1>VANILLA WARRIOR</h1>

    <p>Why play?</p>
    <ul>
      <li>Key class, valid for any PvP objective, highest DPS, only real tank in Vanilla WoW</li>
      <li>Nice gear progression</li>
      <li>Mortal Strike</li>
    </ul>
  </div>
</div>

<div class="row">
  <div class="col-sm-12">
    <h2>Starting a warrior...</h2>
  </div>
</div>

<div class="row">
  <div class="col-sm-12">
    <h2>TL;DR:</h2>
    <h3>Alliance: Human (PvE) or Gnome/Dwarf (PvP)</h3>
    <h3>Horde: Orc (female) or Orc (male)</h3>
  </div>
</div>

<div class="row">
  <div class="col-sm-6">
    <h3>Alliance</h3>
    <div class="card">Human
      <ul>
        <li>Best DPS/TPS due sword/mace skill</li>
        <li>Diplomacy yields a gear advantage in early game</li>
      </ul>
    </div>
    <div class="card">Dwarf
      <ul>
        <li>Stoneform enables you to prey on rogues, trivializes WSG flag extraction against rogue defense</li>
        <li>Stoneform is another defensive CD for progression tanking, helps in various instances, raids and while leveling</li>
      </ul>
    </div>
    <div class="card">Gnome
      <ul>
        <li>Escape Artist covers a warrior's greatest weakness (competent frost mages will still destroy you)</li>
      </ul>
    </div>
    <div class="card">Nightelf
      <ul>
        <li>Shadowmeld allows for unique PvP tactics, spell dodging, getting more Charge openers</li>
        <li>Shadowmeld can also be used as "poor man's" stealth in combination with invisibility potions</li>
        <li>Whisp form grants an advantage in world PvP draws, despite being mocked a lot</li>
      </ul>
    </div>
  </div>
  <div class="col-sm-6">
    <h3>Horde</h3>
    <div class="card">Orc
      <ul>
        <li>Bloodfury and axe skill </li>
        <li>Stun resistance passive is the best Horde PvP racial</li>
      </ul>
    </div>
    <div class="card">Tauren
      <ul>
        <li>AoE stun as additional interrupt, shutting down enemy avoidance</li>
        <li>Bigger melee range and hitbox</li>
        <li>Additional health helps for progression, but Vanilla is figured out</li>
      </ul>
    </div>
    <div class="card">Troll
      <ul>
        <li>Best for TPS tanking</li>
        <li>Otherwise outshadowed by other Horde races</li>
      </ul>
    </div>
    <div class="card">Undead
      <ul>
        <li>WotF helps with fear-heavy bosses, reduces damage taken in PvP because you can fight in Battle Stance more</li>
        <li>WotF allows escaping Succubus/Magic Dust</li>
        <li>Cannibalize as another bandage</li>
      </ul>
    </div>
  </div>
  Keep in mind that you need to be comfortable with the animation/looks of your character! My picks: Dwarf for Alliance, Orc
  for Horde!
</div>

  <footer class="row">
    <div class="col-sm-12">
      <p>© 2018-2019 Warlord Drak | <a href="https://discord.gg/W55S8MB">discord.gg/W55S8MB</a> | <a href="about.html" class="col-sm-1">About</a></p>
    </div>
  </footer>
</body>

</html>
'''

INDEX_HTML_SNIPPET = templater.read_file('snippet.index.html')

ABOUT_HTML = '''<!DOCTYPE html>
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

<div class="row">
  <h2>Hey, I'm Drak</h2>
  <p>
    I played Vanilla WoW since the closed US beta and quit retail before the first WotLK content patch. During retail Vanilla
    I achieved r12 on Alliance and cleared all content till 4HM (4HM, Sapph, KT one week after TBC release). After some WoW
    break, I picked up Vanilla WoW again via the emulation scene. There I achieved 2 r13 warriors (Orc/NE) with all content
    cleared. I also played warriors of all races but UD/Gnome, some of which I ranked to r10.
  </p>
  <p>
    On this website I want to share my in-depth knowledge of the warrior class and Vanilla WoW in general.
  </p>
</div>

<div class="row" style="text-align:center;">
  <i class="col-sm-12">
    Endless strife,<br> till our last breath,<br> protecting life,<br> and marking death<br>
    <br> WARRIORS!
    <br> EVER!
    <br> CHARGE!
    <br> FORWARD!
  </i>
</div>

  <footer class="row">
    <div class="col-sm-12">
      <p>© 2018-2019 Warlord Drak | <a href="https://discord.gg/W55S8MB">discord.gg/W55S8MB</a> | <a href="about.html" class="col-sm-1">About</a></p>
    </div>
  </footer>
</body>

</html>
'''

ABOUT_HTML_SNIPPET = templater.read_file('snippet.about.html')


def test_index_regression():
    assert templater.generate(INDEX_HTML_SNIPPET) == INDEX_HTML

def test_about_regression():
    assert templater.generate(ABOUT_HTML_SNIPPET) == ABOUT_HTML
