import sys

from setuptools import setup

setup(
    name='aztarna',
    version='2.0',
    packages=[
                'aztarna',
                'aztarna.ros',
                'aztarna.ros.ros',
                'aztarna.ros.sros',
                'aztarna.ros.industrial',
                'aztarna.ros.ros2',
                'aztarna.industrialrouters',
              ],
    url='https://www.d2e.top',
    project_urls={
        'Source Code': 'https://github.com/YYX1000/aztarna'
    },
    license='GPLv3',
    author='Alias Robotics',
    author_email='2671713870@qq.com',
    description='一款ROS类型(包括ROS,ROS2,SROS,SROS2)的机器人操作系统足迹探测工具',
    long_description='''Aztarna,一个用于机器人脚印分析的工具。
        为研究人员提供研究联网ROS、SROS机器人以及工业路由器的方法。
        Alias Robotics支持原始机器人制造商评估其安全性并提升软件质量。
        我们绝不会鼓励或推广对正在运行的机器人系统的未经授权篡改行为。
        这可能导致严重的人身伤害和物质损失。
    ''',
    keywords=['network', 'footprinting', 'ros', 'sros', 'ics', 'industrialrouters'],
    entry_points = {
        'console_scripts': ['aztarna=aztarna.cmd:main'],
    },
    install_requires=[
        'aiohttp==3.5.4',
        'aiohttp-xmlrpc==0.7.4',
        'alabaster==0.7.12',
        'argcomplete==1.9.5',
        'asn1crypto==0.24.0',
        'async-timeout==3.0.1',
        'attrs==19.1.0',
        'Babel==2.6.0',
        'certifi==2019.3.9',
        'cffi==1.12.2',
        'chardet==3.0.4',
        'Click==7.0',
        'click-plugins==1.1.1',
        'colorama==0.4.1',
        'cryptography==2.6.1',
        'dnspython==1.16.0',
        'docutils==0.14',
        'idna==2.8',
        'idna-ssl==1.1.0',
        'imagesize==1.1.0',
        'ipwhois==1.1.0',
        'Jinja2==2.10.1',
        'lxml==4.3.3',
        'MarkupSafe==1.1.1',
        'multidict==4.5.2',
        'packaging==19.0',
        'property==2.2',
        'pycparser==2.19',
        'Pygments==2.3.1',
        'pyparsing==2.4.0',
        'pytz==2019.1',
        'requests==2.22.0',
        'scapy==2.4.2',
        'shodan==1.12.1',
        'six==1.12.0',
        'snowballstemmer==1.2.1',
        'Sphinx==2.0.1',
        'sphinxcontrib-applehelp==1.0.1',
        'sphinxcontrib-devhelp==1.0.1',
        'sphinxcontrib-htmlhelp==1.0.2',
        'sphinxcontrib-jsmath==1.0.1',
        'sphinxcontrib-qthelp==1.0.2',
        'sphinxcontrib-serializinghtml==1.1.3',
        'sphinxcontrib-websupport==1.1.0',
        'urllib3==1.25.11',
        'uvloop==0.12.2',
        'XlsxWriter==1.1.6',
        'yarl==1.3.0',
        'pyshark==0.4.2.9',
    ],
    include_package_data=True
)
