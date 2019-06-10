import os
import sys
import glob
import setuptools 

with open("README.md") as f:
    readme = f.read()

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNUv3 License',
    'Programming Language :: Python :: 3.5',
    ]

#  wavFiles = glob.glob( 'MyPiano/data/*/*/*.wav' )
#  print( f"[INFO ] Total {len(wavFiles)} wav files." )

setuptools.setup(
    name = "MyPiano",
    version = "0.0.1",
    description = "Play simple notes or MIDI files",
    long_description = readme,
    packages = [ 'MyPiano' ],
    package_dir = { 'MyPiano' : 'MyPiano' },
    package_data = { 'MyPiano' : 'data/*/*/*.wav' },
    include_package_data = True,
    install_requires = [ 'mido', 'soundfile', 'sounddevice' ],
    zip_safe = False,
    author = "Dilawar Singh",
    author_email = "dilawars@ncbs.res.in",
    url = "http://github.com/dilawar/MyPiano",
    license='GPLv3',
    classifiers=classifiers,
    entry_points={
        'console_scripts' : [ 'mypiano = MyPiano.main' ]
        },
)
