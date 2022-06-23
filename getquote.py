import requests


# function that gets the random quote
def get_random_quote(source):
    url = {
        "zen": "https://zenquotes.io/api/random",
        "quotegarden": "https://quote-garden.herokuapp.com/api/v3/quotes/random",
    }

    try:
        # making the get request
        response = requests.get(url[source])
        if response.status_code == 200:
            # extracting the core data
            json_data = response.json()
            data = json_data[0]

            # getting the quote from the data
            return f"{data['q']} \n\n{data['a']}"
        else:
            return "Error while getting quote"
    except:
        raise Exception("Something went wrong! Try Again!")


get_random_quote("zen")
