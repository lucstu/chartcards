import requests

def recurseResult(cursor):
  data = {
    "operationName": "SearchMomentListings",
    "variables": {
      "byPlayers": [],
      "byTagNames": [],
      "byTeams": [],
      "bySets": [],
      "bySeries": [],
      "bySetVisuals": [],
      "byGameDate": {
        "start": None,
        "end": None
      },
      "byCreatedAt": {
        "start": None,
        "end": None
      },
      "byPower": {
        "min": None,
        "max": None
      },
      "byPrice": {
        "min": None,
        "max": None
      },
      "byListingType": [
        "BY_USERS"
      ],
      "byPlayStyle": [],
      "bySkill": [],
      "byPrimaryPlayerPosition": [],
      "bySerialNumber": {
        "min": None,
        "max": None
      },
      "searchInput": {
        "pagination": {
          "cursor": cursor,
          "direction": "RIGHT",
          "limit": 50
        }
      },
      "orderBy": "UPDATED_AT_DESC"
    },
    "query": "query SearchMomentListings($byPlayers: [ID], $byTagNames: [String!], $byTeams: [ID], $byPrice: PriceRangeFilterInput, $orderBy: MomentListingSortType, $byGameDate: DateRangeFilterInput, $byCreatedAt: DateRangeFilterInput, $byListingType: [MomentListingType], $bySets: [ID], $bySeries: [ID], $bySetVisuals: [VisualIdType], $byPrimaryPlayerPosition: [PlayerPosition], $bySerialNumber: IntegerRangeFilterInput, $searchInput: BaseSearchInput!) {\n  searchMomentListings(input: {filters: {byPlayers: $byPlayers, byTagNames: $byTagNames, byGameDate: $byGameDate, byCreatedAt: $byCreatedAt, byTeams: $byTeams, byPrice: $byPrice, byListingType: $byListingType, byPrimaryPlayerPosition: $byPrimaryPlayerPosition, bySets: $bySets, bySeries: $bySeries, bySetVisuals: $bySetVisuals, bySerialNumber: $bySerialNumber}, sortBy: $orderBy, searchInput: $searchInput}) {\n    data {\n      filters {\n        byPlayers\n        byTagNames\n        byTeams\n        byPrimaryPlayerPosition\n        byGameDate {\n          start\n          end\n          __typename\n        }\n        byCreatedAt {\n          start\n          end\n          __typename\n        }\n        byPrice {\n          min\n          max\n          __typename\n        }\n        bySerialNumber {\n          min\n          max\n          __typename\n        }\n        bySets\n        bySeries\n        bySetVisuals\n        __typename\n      }\n      searchSummary {\n        count {\n          count\n          __typename\n        }\n        pagination {\n          leftCursor\n          rightCursor\n          __typename\n        }\n        data {\n          ... on MomentListings {\n            size\n            data {\n              ... on MomentListing {\n                id\n                version\n                circulationCount\n                flowRetired\n                set {\n                  id\n                  flowName\n                  setVisualId\n                  flowSeriesNumber\n                  __typename\n                }\n                play {\n                  description\n                  id\n                  stats {\n                    playerName\n                    dateOfMoment\n                    playCategory\n                    teamAtMomentNbaId\n                    teamAtMoment\n                    __typename\n                  }\n                  __typename\n                }\n                assetPathPrefix\n                priceRange {\n                  min\n                  max\n                  __typename\n                }\n                momentListings {\n                  id\n                  moment {\n                    id\n                    owner {\n                      dapperID\n                      username\n                      __typename\n                    }\n                    __typename\n                  }\n                  __typename\n                }\n                listingType\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
  }

  r = requests.post('https://api.nba.dapperlabs.com/marketplace/graphql?SearchMomentListings', json=data)

  j = r.json()

  rightCursor = j['data']['searchMomentListings']['data']['searchSummary']['pagination']['rightCursor']
  moments = j['data']['searchMomentListings']['data']['searchSummary']['data']['data']

  with open("moments.csv", "a") as myfile:
    for moment in moments:
      player_name = moment['play']['stats']['playerName']
      circulation = str(moment['circulationCount'])
      moment_set = moment['set']['flowName']
      set_id = moment['set']['id']
      moment_id = set_id + '+' + moment['play']['id']
      moment_date = moment['play']['stats']['dateOfMoment']
      asset_link = moment['assetPathPrefix']

      myfile.write('\n' + moment_id + ',' + player_name + ',' + moment_set + ',' + set_id + ',' + moment_date + ',' + circulation)

  return rightCursor
    
curr = recurseResult("")
last_res = False

while last_res == False:
  curr = recurseResult(curr)
  if curr == "":
    last_res = True
