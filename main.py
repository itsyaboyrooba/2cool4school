import os
import typer
import logging
import requests
import module.ram as ram
import module.storage as storage
from datetime import datetime
app = typer.Typer()

@app.command()
def ram_usage_warning(ram_warning_pct: float):
    logging.info("RAM usage: {}%, using {}MB out of {}MB.".format(ram.usage_pct(), ram.usage(), ram.total()))
    if (ram.usage_pct() > ram_warning_pct):
        logging.critical(" More than {}% of ram is used!".format(ram_warning_pct))
    
@app.command()
def storage_used_warning(storage_warning_pct: float):
    logging.info("Storage used: {}%, using {}GB out of {}GB.".format(storage.used_pct(), storage.used(), storage.total()))
    if (storage.used_pct() > storage_warning_pct):
        logging.critical(" More than {}% of storage is used!".format(storage_warning_pct))
    
@app.command()
def weather(city: str):
    URL = ("https://goweather.herokuapp.com/weather/" + str(city))
    now = datetime.now()
    response = requests.get(URL).json()
    temperature = str(response["temperature"])
    wind = str(response["wind"])
    description = str(response["description"])
    with open('weather.txt', 'a') as f:
        f.write("{}: {}: {}, {}, {}. \n".format(now, city, temperature, wind, description))

def main():
    logging.basicConfig( 
        filename = 'app.log', 
        level = logging.INFO, 
        format = '%(levelname)s:%(asctime)s:%(message)s')
    app()

if __name__ == '__main__':
    main()
    