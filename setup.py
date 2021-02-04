import setuptools


with open('README.md', 'r') as file:
    long_description = file.read()


setuptools.setup(
    name='dev_achievements',
    version='1.0.0',
    author='Ravi Patel',
    author_email='ravi.patel1245@gmail.com',
    description='Earn Achievements while learning how to code',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/raviolliii/dev-achievements',
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
