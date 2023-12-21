from setuptools import setup, find_packages

setup(name='body_visualizer',
      version='1.1.0',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,

      #data_files=[()],
      
      author=['Nima Ghorbani',],
      author_email=['nghorbani@tuebingen.mpg.de'],
      maintainer='Nima Ghorbani',
      maintainer_email='nghorbani@tuebingen.mpg.de',
      url='https://github.com/nghorbani/body_visualizer',
      description='Visualizer for SMPL body model family.',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      install_requires=[],
      dependency_links=[],
      classifiers=[
          "Intended Audience :: Developers",
          "Intended Audience :: Researchers",
          "Natural Language :: English",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: POSIX",
          "Operating System :: POSIX :: BSD",
          "Operating System :: POSIX :: Linux",
          "Operating System :: Microsoft :: Windows",
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7", ],
      )
