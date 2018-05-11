from setuptools import setup, Extension, Command


config = {
    'name': 'roguelike',
    'description': 'roguelike',
    'author': 'Josh Gwaltney',
    'author_email': 'xproj2501x@gmail.com',
    'url': 'http://github.com/xproj2501x/roguelike',
    'download_url': 'https://github.com/xproj2501x/roguelike/releases',
    'version': '1.0.0',
    'package_dir': {
          '': 'src'
    },
    'packages': ['roguelike', 'roguelike.engine', 'roguelike.common', 'roguelike.game'],
    'entry_points': {
        'console_scripts': ['roguelike=roguelike.main:main'],
    },
    'license': 'MIT License'
}

setup(**config)
