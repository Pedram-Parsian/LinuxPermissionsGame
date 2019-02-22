# Linux Permissions Game
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GPL Licence](https://badges.frapsoft.com/os/gpl/gpl.svg?v=103)](https://opensource.org/licenses/GPL-3.0/)

Have you ever get confused with Linux permissions?  Then this game will definitely help you!

Try playing it again and again and see how you can easily learn the rules for converting permissions from 'number' notation to 'string' notation, and vice versa.



## Installation

Simply clone the whole project:
```bash
#HTTPS
git clone https://github.com/Pedram-Parsian/LinuxPermissionsGame.git

#SSH
git clone git@github.com:Pedram-Parsian/LinuxPermissionsGame.git
```

## Usage
Use your terminal to run the `main.py` file. Please make sure that you have already installed [python 3.6+](https://www.python.org/downloads/). As you continue playing, it will keep the history of previous asked questions and also your high-score in a `data.log` file.
```bash
python3 main.py
```

## Clear Game Data
If you wish to remove game data, which includes both your high-score and previous asked questions, just remove the `data.log` file:
```bash
rm data.log
```
:warning: Please do not change `data.log` file.


## Requirements
Requirements are listed inside the [`REQUIREMENTS`](https://github.com/Pedram-Parsian/LinuxPermissionsGame/blob/master/REQUIREMENTS) file. install them using [pip](https://pypi.org/):
```bash
pip3 install -r ./REQUIREMENTS
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[GNU GPLv3](https://opensource.org/licenses/GPL-3.0)
