from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Twitter Sentiment Analysis',
    version='1.3.0'


    classifiers=[

        'Development Status :: 4 - Beta',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],


    keywords='python twitter sentiment-analysis textblob nlp tweepy nltk',


    install_requires=['tweepy','textblob','matplotlib'],

   
)
