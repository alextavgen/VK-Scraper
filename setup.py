##
## Copyright (c) 2017 Ivan Semkin.
## 
## This file is part of VK-Scraper 
## (see https://github.com/vanyasem/VK-Scraper).
## 
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.
##

from setuptools import setup, find_packages

setup(
    name='VK-Scraper',
    version='1.0.0.dev1',
    description='',
    url='https://github.com/vanyasem/VK-Scraper',
    author='Ivan Semkin',
    author_email='ivan@semkin.ru',
    license='GPL-2.0',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent'
        'Programming Language :: Python'
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    install_requires=['vk_api', 'tqdm>=3.8.0'],
    entry_points={
        'console_scripts': [
            'vk-scraper=vk_scraper.app:main',
        ],
    },
    keywords=['vk', 'vkontakte', 'scraper', 'download', 'media', 'photos', 'videos', 'stories']
)
