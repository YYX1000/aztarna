# aztarna
<a href="https://www.d2e.top"><img src="https://www.d2e.top/upload/system/logo_e9b236c9-c62b-4747-8d3a-44c476ce1018.jpg" align="left" hspace="8" vspace="2" width="200"></a>

此仓库包含Alias Robotics的aztarna，这是一种用于机器人足迹分析的工具。

**Alias Robotics致力于协助原始机器人制造商评估其安全性并提升软件质量。我们绝无意鼓励或推广对运行中的机器人系统进行未经授权的篡改。此类行为可能给人类造成严重的伤害并导致物质损失**

[![PyPI version](https://badge.fury.io/py/aztarna.svg)](https://badge.fury.io/py/aztarna)   [![Documentation Status](https://readthedocs.org/projects/aztarna/badge/?version=latest)](https://aztarna.readthedocs.io/en/latest/?badge=latest)    [![Article](https://img.shields.io/badge/article-arxiv%3A1812.09490-red.svg)](https://arxiv.org/pdf/1812.09490.pdf)



### For ROS
* 系统中存在ROS节点的列表(发布者和订阅者)
* 对于每个节点，列出已发布和订阅的主题(包括主题类型)
* 对于每个节点，该节点提供的ROS服务
* 参数服务器中所有ROS参数的列表。
* 系统中正在运行的活动通信列表。单个通信包括
涉及的发布者/订阅者节点和主题

### SROS
* 正在确定系统是否为SROS主控。
* 正在检测演示配置是否正在使用。
* 系统中发现的节点列表。(扩展模式)
* 每个节点的允许/拒绝策略列表。
  * 可发布主题。
  * 可订阅的主题。
  * 可执行服务。
  * 可读参数。
  
### For ROS2 **(Funded under the [ROSIN project](http://rosin-project.eu/))**
* 每个通信域中存在ROS2节点的列表。
* 每个通信域上发现的主题列表。
* 每个通信域上发现的服务列表。
* 对于每个节点，发布和订阅主题的关系。
* 对于每个节点，该节点提供的服务。
### For Industrial routers
* 检测eWON、Moxa、Sierra Wireless和Westermo工业路由器。
* 对发现的路由器进行默认凭据检查。

### For ROS Industrial packages **(Funded under the [ROSIN project](http://rosin-project.eu/))**
* Detection of ROS Industrial Hosts.
* Manufacturers:
    * ABB
    * Fanuc
    * Kuka
        

### 项目维护中,暂时只支持下面的运行方式
**运行环境**
```
python3.12
PRETTY_NAME="Ubuntu 24.04.3 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.3 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ros2 = jazzy
```
**注意**
python版本与jazzyros2运行时的版本需一致
### Code usage:

```bash
usage: python3 -m aztarna [-h] -t TYPE [-a ADDRESS] [-p PORTS] [-i INPUT_FILE]
               [-o OUT_FILE] [-e] [-r RATE] [-d DOMAIN] [--daemon] [--hidden]
               [--shodan] [--api-key API_KEY] [--passive PASSIVE]

Aztarna

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  <ROS/ros/SROS/sros/ROS2/ros2/IROUTERS/irouters> Scan
                        ROS, SROS, ROS2 hosts or Industrial routers
  -a ADDRESS, --address ADDRESS
                        Single address or network range to scan.
  -p PORTS, --ports PORTS
                        Ports to scan (format: 13311 or 11111-11155 or
                        1,2,3,4)
  -i INPUT_FILE, --input_file INPUT_FILE
                        Input file of addresses to use for scanning
  -o OUT_FILE, --out_file OUT_FILE
                        Output file for the results
  -e, --extended        Extended scan of the hosts
  -r RATE, --rate RATE  Maximum simultaneous network connections
  -d DOMAIN, --domain DOMAIN
                        ROS 2 DOMAIN ID (ROS_DOMAIN_ID environmental
                        variable). Only applies to ROS 2.
  --daemon              Use rclpy daemon (coming from ros2cli).
  --hidden              Show hidden ROS 2 nodes. By default filtering
                        _ros2cli*
  --shodan              Use shodan for the scan types that support it.
  --api-key API_KEY     Shodan API Key
  --passive PASSIVE     Passive search for ROS2
```

### Run the code (example input file):

```bash
python3 -m aztarna -t ROS -p 11311 -i ros_scan_s20.csv
```


### Run the code (example single ip address):

```bash
python3 -m aztarna -t ROS -p 11311 -a 115.129.241.241
```

### Run the code (example subnet):

```bash
python3 -m aztarna -t ROS -p 11311 -a 115.129.241.0/24
```

### Run the code (example single ip address, port range):

```bash
python3 -m aztarna -t ROS -p 11311-11500 -a 115.129.241.241
```

### Run the code (example single ip address, port list):

```bash
python3 -m aztarna -t ROS -p 11311,11312,11313 -a 115.129.241.241
```

### Run the code with ROS 2 (example exploring all ranges, 0-231)

```bash
python3 -m aztarna -t ROS2
```

### Run the code with ROS 2 with `ROS_DOMAIN_ID=15`

```bash
python3 -m aztarna -t ROS2 -d 15
```

### Run the code with ROS 2 using rclpy ros2cli daemon and with `ROS_DOMAIN_ID=0` while showing hidden nodes

```bash
python3 -m aztarna -t ros2 -d 0 --daemon --hidden
```

### Run de code with ROS 2 using passive mode to search the hosts. if you set 'any' as argument, is going to search on all interfaces in your system:

```bash
python3 -m aztarna -t ros2 --passive any
```

### Run the code (example piping directly from zmap):

```bash
python3 -m azmap -p 11311 0.0.0.0/0 -q | aztarna -t SROS -p 11311
```

### Run the code (example search for industrial routers in shodan)
```bash
python3 -m aztarna -t IROUTERS --shodan --api-key <yourshodanapikey>
```

### Run the code (example search for industrial routers in shodan, piping to file)
```bash
python3 -m aztarna -t IROUTERS --shodan --api-key <yourshodanapikey> -o routers.csv
```
## Cite our work
If you're using our work for your research, please cite us as:
```
@ARTICLE{2018arXiv181209490V,
  author = {{Vilches}, V{\'\i}ctor Mayoral and {Mendia}, Gorka Olalde and
  {Baskaran}, Xabier Perez and {Cordero}, Alejandro Hern{\'a}ndez
  and {Juan}, Lander Usategui San and {Gil-Uriarte}, Endika and
  {de Urabain}, Odei Olalde Saez and {Kirschgens}, Laura Alzola},
  title = "{Aztarna, a footprinting tool for robots}",
  journal = {arXiv e-prints},
  keywords = {Computer Science - Cryptography and Security, Computer Science - Robotics},
  year = 2018,
  month = Dec,
  eid = {arXiv:1812.09490},
  pages = {arXiv:1812.09490},
  archivePrefix = {arXiv},
  eprint = {1812.09490},
  primaryClass = {cs.CR},
  adsurl = {https://ui.adsabs.harvard.edu/\#abs/2018arXiv181209490V},
  adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

***
<!--
    ROSIN acknowledgement from the ROSIN press kit
    @ https://github.com/rosin-project/press_kit
-->

<a href="http://rosin-project.eu">
  <img src="http://rosin-project.eu/wp-content/uploads/rosin_ack_logo_wide.png"
       alt="rosin_logo" height="60" >
</a></br>

Supported by ROSIN - ROS-Industrial Quality-Assured Robot Software Components.
More information: <a href="http://rosin-project.eu">rosin-project.eu</a>

<img src="http://rosin-project.eu/wp-content/uploads/rosin_eu_flag.jpg"
     alt="eu_flag" height="45" align="left" >

This repository was partly funded by ROSIN RedROS2-I FTP which received funding from the European Union’s Horizon 2020
research and innovation programme under the project ROSIN with the grant agreement No 732287.

