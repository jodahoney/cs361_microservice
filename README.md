# Welcome to my number squaring microservice!

## This is a rest-api that acts as a number squaring microservice!

If you want to try it out locally, simply clone and to start up api, run `python api.py` and send a complying get request to the local url provided.

## HOW TO REQUEST DATA

As this is a rest-api, all communication is done through http requests. In order to request data, you send an http GET request to the url (currently not hosted in a central location, will need to clone and start local version of api).

GET Request format: `*url-address*/square-result/<*num to be squared*`

### Example GET request:
`http://127.0.0.1:5000/square-results/2`

## HOW TO RECEIVE DATA

When a GET request is sent, continuing on the example above, a JSON response is given.

Example JSON ouput:

```
{
  "squared_value": 4
}
```