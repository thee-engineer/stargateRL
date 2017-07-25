"""Main method for stargateRL."""
import pdb
import pyglet

from stargateRL.engine.screen import GameWindow
from stargateRL.engine.graphx import TileColor
from stargateRL.engine.colors import DefaultColors
from stargateRL.objects import widgets
from stargateRL.launcher.utils import load_config


from stargateRL.world.genesis import WorldData
from stargateRL.world.exports import default_export_biomes, monochrome


# DEBUG
# TODO: Prepare settings for world generation
def test_exports(tt):
    """Test export methods."""
    print tt
    world_data = WorldData(seed=-1)
    monochrome(world_data.elevation(), 'elevation')
    monochrome(world_data.moisture(), 'moisture')
    default_export_biomes(world_data.biomes())


def main():
    """Create the game."""
    pyglet.options['debug_gl'] = False

    CONFIG = load_config()
    window_config = CONFIG['window']

    window = GameWindow(window_config['width'],
                        window_config['height'],
                        fullscreen=window_config['fullscreen'],
                        resizable=window_config['resizable'],
                        style=window_config['style'],
                        vsync=CONFIG['graphics']['vsync'])

    # Configurate window
    window.set_mouse_visible(window_config['mouse'])
    window.set_icon(pyglet.resource.image(CONFIG['resources']['icon']))

    # Render screen border
    screen_border = widgets.BorderWidget(0, 0, window.x_tiles, window.y_tiles,
                                         TileColor(DefaultColors.BORDER))

    selection_menu =\
        widgets.SelectionMenuWidget(window.x_tiles / 4, window.y_tiles / 2,
                                    window.x_tiles / 2, window.y_tiles / 4,
                                    TileColor(DefaultColors.GOLD),
                                    TileColor(DefaultColors.WHITE),
                                    TileColor(DefaultColors.RED,
                                              DefaultColors.GOLD),
                                    # Menu options
                                    ('Compile World', test_exports, [None]),
                                    ('Testing Area', pdb.set_trace, []),
                                    ('Saves/Worlds', None, []),
                                    ('Settings', None, []),
                                    ('Credits/About', []),
                                    ('Exit', pyglet.app.exit, []))

    window.push_widget(screen_border)
    window.push_widget(selection_menu)

    pyglet.app.run()


if __name__ == '__main__':
    main()
