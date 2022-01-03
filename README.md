# Multi-agent system that deals with voting problem

## About The Project
The project was developed to address the problem of voting in a multi-agent systems.
The system was developed to work with the Python SPADE (Smart Python multi-Agent Development Environment) library and its main purpose is to vote in a meeting.

### Built With
* [Python](https://www.python.org/)
* [SPADE](https://spade-mas.readthedocs.io/en/latest/index.html)

### Prerequisites

You will ned spade library to run the Python program.
  ```sh
  pip install spade
  ```
  
### Installation

The following are the installation steps:

Clone the repo
   ```sh
   git clone https://github.com/bzitkovic/multiagent-system-voting-problem.git
   ```
Install SPADE library
   ```sh
   pip install spade
   ```
## Usage
You can run the program in two ways (depending on the voting method used and the number of agents you want to have).

First:
   ```sh
   python3 main.py plurality 10
   ```
Second:
   ```sh
   python3 main.py runoff 10
   ```
## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.
