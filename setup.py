import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="filecrypter",
    version="0.0.1",
    author="Krzysztof Murawski",
    author_email="mure.krzys@gmail.com",
    packages=["filecrypter"],
    description="Simple file encryption tool",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/KrzysMur/FileCrypter.git",
    license='MIT',
    python_requires='>=3.10',
    install_requires=[]
)