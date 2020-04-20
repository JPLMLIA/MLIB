from setuptools import find_packages, setup
with open('requirements.txt') as f:
    requirements = f.read().splitlines()
if __name__ == '__main__':
    setup(
        name='mliamlib',
        version='1.0.0',
        license='CalTech',
        author='Lukas Mandrake',
        author_email='lukas.mandrake@jpl.caltech.edu',
        url='https://github.com/JPLMLIA/MLIB',
        download_url='https://github.com/JPLMLIA/MLIB/archive/1.0.0.tar.gz',
        packages=find_packages(),
        include_package_data=True,
        package_data={},
        install_requires=requirements,
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Education',
            'License :: CalTech License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.6 :: Only',
            'Topic :: Utilities'
        ])
