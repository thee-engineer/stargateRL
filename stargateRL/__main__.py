"""Main method for stargateRL."""

import pyglet

from stargateRL.engine.screen import GameWindow
from stargateRL.engine.graphx import GxTileset
from stargateRL.engine import widgets

import json

# Load config file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)


# Load the tileset
gx_tileset = GxTileset(config['resources']['tileset'],
                       config['graphics']['size'])

# Create the game window
window_config = config['graphics']['window']

window = GameWindow(window_config['width'],
                    window_config['height'],
                    fullscreen=window_config['fullscreen'],
                    resizable=window_config['resizable'],
                    style=window_config['style'])
window.set_mouse_visible(window_config['mouse'])

screen_border = widgets.BorderWidget(gx_tileset, 0, 0,
                                     window.width/16,
                                     window.height/16,
                                     'border')
window.push_widget(screen_border)

pyglet.app.run()
