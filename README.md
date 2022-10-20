"# jupyter-rest-consumer"

## Install jupyter
pip install jupyterlab

## Run jupyter in local browser
jupyter-lab

## Q: Explain the rationale behind your choice of API and its intended usage
________

**_```1. Climatic Forecast 30 days:```_** To forecast weather data for 30 days. Climate Forecast 30 Days allows you to request daily weather data for the next 30 days. Data is available in JSON and XML formats.

**_```2. Hourly Forecast 4 days:```_** Hourly forecast is available for 4 days. Hourly forecast for 4 days (96 timestamps). Weather data is available in JSON and XML formats. You can search weather forecast for 4 days with data every hour by geographic coordinates.

**_```3. CoinCap API:```_** */rates* API is used to know the rate of a specific coin. For example: *bitcoin*. Through this API, it is possible to know the *bitcoin* *symbol*, *currencySymbol*, *type* and *rateUsd*.

## Q: Explain the steps (process) followed and the terminology used
_________
* __Steps:__ 
    
    1. First consume the CoinCap */rates* API, get the result and save it as it is to the filesystem as a flat format.
    2. Then consume *Climatic Forecast 30 days* API and finally *Hourly Forecast 4 days* API and save the response as they are respectively.

* __Terminology__

        Python http client is used to consume the APIs. 
        The app can be run as a Jupyter notebook.

## Q. Please explain your strategy to manage the version controlling of files from each day
___
As it is specified that the API will be consumed once a day, so whenever the API will be consumed, the response file will be saved appending the datetime with the file name. Thus the version of each day can be managed.

## Q. Please explain theoretically what is version controlling and its benefits and how you will manage version controlling of the data retrieved

Version controlling is the measure of keeping each version of a data uniquely. 


The benefint of version controlling is, it helps to identify the difference of each version of data and helps to manage the data of different versions.

Each time the API will be called, the response will be saved in file system. The file name will contain the API calling timestamp. Each timestamp is unique and thus the version of each API calling response data can be managed.