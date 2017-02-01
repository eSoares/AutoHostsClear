# AutoHostsClear

The idea of this script is cleaning automatically all local network devices ssh keys.
This is usable for people who ssh for local machines that get IP via DHCP.

## How to use

Simply run:
```
python src/main.py
```

To auto clean any local IP address at the end of an SSH connection create the following alias in your bash profile:
```
alias ssh="f(){/usr/bin/ssh $1; python /path/to/project};f"
```

Note: replace ```/usr/bin/ssh``` to the output of ```which ssh``` and ```/path/to/project``` to where you checkout the project.


## License

This project is BSD-3 licensed, you can file the full license in [this](LICENSE) file.