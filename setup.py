from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name = 'FileCrypter',
    version = '0.0.1',
    author = 'Krzysztof Murawski',
    author_email = 'murek.krzys@gmail.com',
    license = 'MIT',
    description = 'Simple file encryption and decryption CLI tool',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/KrzysMur/FileCrypter.git',
    py_modules = ['cli_tool', 'encrypt_decrypt'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.10',
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: Microsoft :: Windows",
    ],
    entry_points = '''
        [console_scripts]
        filecrypter=cli_tool:main
    '''
)