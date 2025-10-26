
import requests
import json

SEMKG_IMAGES_HOST = "https://files.semkg.org"

def query_corrected(query_string):
    # The 'params' parameter correctly sends data as URL parameters for a GET request
    params = {
        'query': query_string
    }
    response = requests.get('https://vision.semkg.org/sparql', params=params)
    
    # It's also good practice to check if the request was successful
    response.raise_for_status()  # This will raise an error for bad responses (e.g., 404, 500)
    
    return response.json()
          

#def query(query_string, token=""):
      #response = requests.get('https://vision.semkg.org/sparql',
     #                        json={"query": query_string, token: token})
     # _data=response.json()
      # print(_data)
      # data=[]
      # # pprint(_data)
      # for result in _data['results']['bindings']:
      #       tmp={}
      #       for key in result.keys():
      #             tmp[key]=result[key]['value']
      #       data.append(tmp)
      # return _data