<h1 align="center">
Python/Bash logging&weather CLI app

## Dependencies:

- [Python](https://www.python.org)
- Linux

## Usage:
    
To see all available CLI commands, run `python3 main.py --help` in shell.

Run `typer --install-completion` for auto-completion.

### ram-usage-warning:
    
Usage: `python3 main.py ram-usage-warning [VALUE]`    

Example:
    `python3 main.py ram-usage-warning 10`

If RAM usage doesn't exceed your limit, app outputs an info log into `./app.log`:

`INFO:2022-05-27 20:35:24,081:RAM usage: 2%, using 125MB out of 12726MB.`

If RAM usage exceeds 10%, app outputs a critical log in `./app.log`.
    
Critical output:
    `CRITICAL:2022-05-27 20:22:36,127: More than 10% of ram is used!`
     
### storage-used-warning:

Usage: `python3 main.py storage-used-warning [VALUE]`    

Example:
    `python3 main.py storage-used-warning 35`

If haven't used more than 35% of your storage, app outputs an info log into `./app.log`:

`INFO:2022-05-27 20:37:39,297:Storage used: 0.8%, using 2GB out of 250GB.`

If you've used more than 35% of your storage, app outputs a critical log in `./app.log`.
    
Example output:
    `CRITICAL:2022-05-27 20:25:04,709: More than 35% of storage is used!`

## weather:

Usage: `python3 main.py weather [COUNTRY/CITY]`  

App requests and logs the current weather into `./weather.txt`.

- [Weather API](https://github.com/robertoduessmann/weather-api)

Example(s):
    `python3 main.py weather Denmark`
    `python3 main.py weather Stockholm`