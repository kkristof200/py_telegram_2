import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'ktg2'

setuptools.setup(
    name='ktg2',
    version='0.0.3',
    author='Kristóf-Attila Kovács',
    description='ktg2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kkristof200/py_telegram_2',
    packages=setuptools.find_packages(),
    install_requires=[
        'jsoncodable>=0.1.7',
        'kcu>=0.0.73',
        'noraise>=0.0.16',
        'setuptools>=59.3.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)