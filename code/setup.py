import setuptools

setuptools.setup(
    name = 'einet',
    packages = setuptools.find_packages(),
    install_requires=[
        'networkx',
        'numpy',
        'scipy',
        'scikit-learn'
    ]
)
