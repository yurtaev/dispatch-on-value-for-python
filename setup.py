from distutils.core import setup

setup(
    name='dispatchonvalue',
    version='0.9.2',
    author='Ian Macinnes',
    author_email='ian.macinnes@gmail.com',
    packages=['dispatchonvalue', 'dispatchonvalue.test'],
    url='https://github.com/minimind/dispatch-on-value-for-python',
    license='MIT',
    description='Provides the ability to dispatch on values using pattern'
                'matching for various builtin types such as nested '
                'lists and dictionaries.',
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2 :: Only'
    ],
    keywords=['dispatch on value', 'multiple dispatch', 'dynamic dispatch',
              'pattern matching', 'value patterns', 'patterns'],
    include_package_data=True
)
