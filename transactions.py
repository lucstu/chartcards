import requests
import json

def recurseResult(cursor):
    data = {
    "operationName": "SearchMarketplaceTransactions",
    "variables": {
        "input": {
        "sortBy": "UPDATED_AT_DESC",
        "searchInput": {
            "pagination": {
            "cursor": cursor,
            "direction": "RIGHT",
            "limit": 0
            }
        }
        }
    },
    "query": "query SearchMarketplaceTransactions($input: SearchMarketplaceTransactionsInput!) {\n  searchMarketplaceTransactions(input: $input) {\n    data {\n      searchSummary {\n        pagination {\n          rightCursor\n          __typename\n        }\n        data {\n          ... on MarketplaceTransactions {\n            size\n            data {\n              ... on MarketplaceTransaction {\n                id\n                sortID\n                seller {\n                  ...UserFragment\n                  __typename\n                }\n                buyer {\n                  ...UserFragment\n                  __typename\n                }\n                price\n                moment {\n                  assetPathPrefix\n                  flowSerialNumber\n                  id\n                  play {\n                    id\n                    stats {\n                      playerName\n                      dateOfMoment\n                      playCategory\n                      teamAtMomentNbaId\n                      teamAtMoment\n                      jerseyNumber\n                      __typename\n                    }\n                    __typename\n                  }\n                  set {\n                    id\n                    flowName\n                    flowSeriesNumber\n                    setVisualId\n                    __typename\n                  }\n                  setPlay {\n                    ID\n                    circulationCount\n                    flowRetired\n                    __typename\n                  }\n                  __typename\n                }\n                txHash\n                updatedAt\n                __typename\n              }\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment UserFragment on UserPublicInfo {\n  dapperID\n  flowAddress\n  username\n  profileImageUrl\n  __typename\n}\n"
    }

    r = requests.post('https://api.nba.dapperlabs.com/marketplace/graphql?SearchMomentListings', json=data)

    j = r.json()

    rightCursor = j['data']['searchMarketplaceTransactions']['data']['searchSummary']['pagination']['rightCursor']
    txs = j['data']['searchMarketplaceTransactions']['data']['searchSummary']['data']['data']

    for tx in txs:
        tx_id = tx['id']
        seller_id = tx['seller']['username']
        buyer_id = tx['buyer']['username']
        price = tx['price']
        moment_id = tx['moment']['set']['id'] + '+' + tx['moment']['play']['id']
        time = tx['updatedAt']
        tx_hash = tx['txHash']

        with open("transactions.csv", "a") as myfile:
            myfile.write('\n' + tx_id + ',' + seller_id + ',' + buyer_id + ',' + price + ',' + moment_id + ',' +  time + ',' + tx_hash)
    
    return rightCursor

curr = recurseResult("")
last_res = False

while last_res == False:
    curr = recurseResult(curr)
    if curr == "":
        last_res = True



    