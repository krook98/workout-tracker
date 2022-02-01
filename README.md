# General info
Enter your workout to Google Sheets. Find out how much calories you've burned and keep track on your consistency.

### API Used
I use Sheety API to save data to Google Sheets document (https://sheety.co/)  
Natural language and calories counter are done with Nutritionix API (https://developer.nutritionix.com/)  


### Technology
Python 3.9.10  
Google Sheets

### Setup
To run this project you might need your own API keys. Nutritionix and Google accounts are neccessary.    
requests, datetime and os Python libraries are required

### Launch
Firstly, you need to add your own API keys. You can set environment variables in terminal with:  <br/><br/>
`export 'YOUR_ENV_VAR_NAME'=value`  <br/><br/>
Then you can access it in code with:  <br/><br/>
`os.environ.get('YOU_ENV_VAR_NAME')`  <br/><br/>
Run app with:  <br/><br/>
`python3 main.py` 
