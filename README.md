# fitbit-sleep-study
Download Fitbit data and analyze it with pySpark

## Installation & Usage

1. `pip install CherryPy fitbit`
2. `./gather_keys_oauth2.py` 
3. Copy the API keys/tokens into the `start.py` file as labeled
4. Change `start.py` to gather the type of data you want
5. Run `python start.py > your-fitbit-data.json`
6. Upload your Fitbit JSON data to Amazon S3 or otherwise ingest it with pySpark
7. See the `fitbit-sleep-study.ipynb` iPython notebook for example analysis of Fitbit sleep data
8. Make it your own and have fun!
