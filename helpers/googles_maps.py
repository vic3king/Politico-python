from graphql import GraphQLError


def verify_address(api_key, address):
    """
    Returns the formated address for any given address.
    API: https://developers.google.com/maps/documentation/geocoding/start

    # INPUT -------------------------------------------------------------------
    api_key                  [str]
    address                 [str]

    # RETURN ------------------------------------------------------------------
    formated_address                     [str]

    """
    import requests
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ', '+'), api_key))

    response = requests.get(url)
    resp_json_payload = response.json()

    if len(resp_json_payload['results']) > 0:
        return resp_json_payload['results'][0]['formatted_address']
    else:
        raise GraphQLError(f'{address} not found, enter a valid address')
