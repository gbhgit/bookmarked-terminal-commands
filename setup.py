from distutils.core import setup

with open("README.desc") as file:
    long_description = file.read()

setup(
  name = 'btcmd', # How you named your package folder (MyLib)
  long_description=long_description,
  packages = ['btcmd'], # Chose the same as "name"
  version = '0.3', # Start with a small number and increase it with every change you make
  license='MIT', # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Bookmark Terminal Commands', # Give a short description about your library
  author = 'Gabriel Bandeira and Wellington Mendes', # Type in your name
  author_email = 'wellmend0@gmail.com', # Type in your E-Mail
  url = 'https://github.com/gbhgit/bookmarked-terminal-commands', # Provide either the link to your github or to your website
  download_url = 'https://github.com/gbhgit/bookmarked-terminal-commands/archive/refs/tags/v.0.3.tar.gz', # I explain this later on
  keywords = ['terminal', 'bookmark', 'commands'],   # Keywords that define your package best
#   install_requires=[  # I get to this in a second
#           'validators',
#       ],
  classifiers=[
    'Development Status :: 4 - Beta', # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities',
    'Natural Language :: English',
  ],
  scripts=['bin/btcmd'],
)