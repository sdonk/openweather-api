import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='openweather-api-client',
    version='0.0.1',
    author='Alessandro De Noia',
    author_email='alessandro.denoia@gmail.com',
    description='OpenWeather API client',
    license='Apache2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sdonk/openweather-api-client',
    packages=setuptools.find_packages(exclude=['tests*']),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.6',
)
