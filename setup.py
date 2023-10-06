from setuptools import setup, find_packages

setup(
    name='python-toolkit',
    version='0.0.1',
    description='',
    python_requires='>=3.7',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"base": ["py.typed"]},
    install_requires=[
        'requests>=2.31.0',
        'types-requests==2.31.0.8',
        'pydantic>=2.3.0',
        'pydantic_core==2.6.3',
        'setuptools==68.2.2',
        'types-setuptools==68.2.0.0',
        'python-dotenv==1.0.0'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Typing :: Typed'
    ]
)