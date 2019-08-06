setup(
    name='minml-nlp',
    version='0.0.1',
    description="Barebones generalized NLP pipeline",
    author="Tim Hannifan",
    author_email='hannifan@gmail.com',
    url='https://github.com/timhannifan/minml-nlp',
    packages=find_packages('src', exclude=['examples']),
    package_dir={'': 'nlp'},
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)