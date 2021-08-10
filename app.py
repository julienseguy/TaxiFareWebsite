import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

# API - Provided by le Wagon
# url = 'https://taxifare.lewagon.ai/predict'

# My APY - CGP Cloud Run
url = 'https://taxi-fare-image-j7vxpv56fq-ew.a.run.app/predict'

# if url == 'https://taxifare.lewagon.ai/predict':

#     st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

# fill the parameters for the prediction
params = dict(
  pickup_datetime='2012-10-06 12:10:20',
  pickup_longitude=40.7614327,
  pickup_latitude=-73.9798156,
  dropoff_longitude=40.6413111,
  dropoff_latitude=-73.9797156,
  passenger_count=1
)

# retrieve the response
response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.status_code, "API call success")
else:
    print(response.status_code, "API call error")

response.status_code, response.json().get("prediction", "no prediction"), response.json()
