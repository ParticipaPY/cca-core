from setuptools import setup

setup(
  name = 'cca-core',
  packages = ['cca-core'], # this must be the same as the name above
  version = '0.1',
  description = 'NLP and ML modules for processing civic input',
  author = 'Marcelo Alcaraz',
  author_email = 'marce.mmad@gmail.com',
  url = 'https://github.com/ParticipaPY/cca-core', # use the URL to the github repo
  keywords = ['Natural Language Processing', 'Machine Learnign', 'Civic input'], # arbitrary keywords
  classifiers = [],
  install_requires=['nltk>=3.2.4', 'sklearn', 'beautifulsoup4>=4.6.0', 'googletrans>=2.2.0', 'pandas>=0.20.3'],
  python_requires='>=3',
  package_data={
    'cca-core': ['lexicon_lib/*'],
  },
)