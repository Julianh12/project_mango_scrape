from bs4 import BeautifulSoup
import requests
import json
url = "https://shop.mango.com/services/garments/1704202008"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'stock-id': '006.IN.0.false.false.v0',
  'Connection': 'keep-alive',
  'Referer': 'https://shop.mango.com/gb/women/skirts-midi/midi-satin-skirt_17042020.html?c=08',
  'Cookie': 'oam.Flash.RENDERMAP.TOKEN=4fwdoh2i; MNGSESSIONID=206F155E0821BCF01463B207F63C968B; mangoShopCookie=IN_006____006_001_she___8ZLL7SQTTJRSORJGIDIHGC4H; mangoShopCookie_Version=v4; BolsaCookie=01170420202108-Mango; googleexperiments=t8C28DR0Sb2tRepMbNXt4A%3A1%2CKgtNo3S3SWCTsPzuWFIT-Q%3A1%2Cb7AXQ_k3OolrT4dy9Jo-mT%3A2%2C; browserId=3001189598191730624087073519753447458780; AWSELB=BFC5C7171EE3DEE8EF093B004B4B9C189E4132CE52E3CFD7F1E8BF88BEC1B83C88F12E356B06366930B57CA5788D6E7FAB3D788E3BDE5A9441478424AF0CFC20F248DD295D4D083367D62BCC0E50F51BBDF2C71A88; _abck=C1142244A908CF3C71CF8462162F56B8~-1~YAAQTYYUArG1aHp8AQAAL9oeewbmWdht+mGFBGkaMc81MDqqIHpzlHAKqMtBwEn5VY6dTglJnaMLLQipcd76U6OlGoAfuRn2wm8TBmqAEO1iyIFw8yp8ZPVv5LrL/7xD+hAfy1s4nHGKM0zrT2xgQCFI3N8IndVZJ/G8avKHcgjL2ovkjD8t+RHjhTdKLm0OhHLnCkXqBSFeAtcsgS6Rq+Q8ZhOWjVub+NV3VrW7veIba9Hph8YyjawH0g3JY0mSZFHYq/i8jfWZH2yXK2FJMjWFqk/N1Sn1ZpBDqnnPgj9Kpi3UO5szpXS3vw45NsvbqECvwc028YFgho3ARNgeWssYv67Zme/aH4MhXBDn8Xy7MPVUdup0GWRBxekhOueK3wL4FxkDIV73fVkoATa294meMMrY~-1~-1~-1; ak_bmsc=B2A605B96788CF6EAD4574CC4298F174~000000000000000000000000000000~YAAQTYYUAiataHp8AQAAHQgdew1x2UB9JS2IL1mzQ2KljE3nne/FV7UO+GKpEreDM5O+xcsV3aa6loyUrnxpvfEPEY6fXM6n3hzodWSakwziav4uUwLosvUNxy0dworanOc2LUZve4kkHQkWH8ytXgC98AaliYg0CIj1fqKfZ4yhZhPF9tKsfAGJ8zBSjjg/iNUwTfsWoq3z2tWl3VFrgLhVa5dWTV1d4YONShCh/qvbPhibhXTfwThl+b7R6GCk7qyCj1hsQbW9HXegmWM5hG+8p6knzeI9qPbtqx+dg+/SavbOpRcqoZeKSz1dtfv7cTQBd24hhKA+l+mFIz6gJRzVCnvBFxVymYhsETGNeyWj8+8ezAs5cBxyRmM0X1jfeDlY1PsTGWX5tBB0/PfmC8ux1jtq+UE6pxmb0E93nMB02ukwhdD+fgW8bCiREpbEvIuKuBsC6xXNSJz0V6Bd3F9fLkp+wesIxG1Gg/BQbLOJlH1Dh/+seP4t6/9RF5IzDP4T0iZY4WP64TfR7a4ByHms6c5R6Qd6DXM+MVw=; bm_sz=B8CEF70402E495E0DE263E372804D9D1~YAAQTYYUAuSsaHp8AQAAg/0cew22z/4HovE1Qt1fSprWDJ+tGagIgZ0YqK1FhzUyllNe3O7AJTfIyrFqtCCLCdg1yTS8wSwg/7CRcfaKwwZmK22QXcooQv67m75CSLTfwyhrYgkstPfhrRyC3RVXXXPerMwveuoydvDJCCsH6ujnARCD2wbDDUtGrpGsct+ZuP53t1FD0/ajHgxEJB+tfJNRAoRfzJ5hnKwyRhoaGw4viKfKOlVrQhekZpTtjtjdmKOFwL6k1u7NpOCExko+LS8I/gdccM5kGreHUQIZeuuQkQ==~3158320~4601652; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Oct+13+2021+22%3A24%3A32+GMT%2B0300+(Moscow+Standard+Time)&version=6.20.0&isIABGlobal=false&hosts=&consentId=9e1336db-d312-47b3-8322-19fc7f49a1e4&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1%2CC0005%3A1; bm_sv=6572BE74D2ED78BE6822AB9C2D4B1EB4~wZE6uOmD8u+Xf27ZtwQjOEHfWuCVrCpq5WVUin75EVjtx1oTzkWdlaG2YZ+wUgp6sZPzDbU34jWGhz23zCQDKen0a1Ox21wD08ueMYh9jupXJH8u0pWzpTrOx3Ur+5ari3FJEMX4xdkZq88KuK7KOb1Cq3wRuXktAaHAondYPf0=; bm_mi=4A4B7E5C794C6DC62D7F41BEF9BA5B48~ph4GpAA5xViZkKzgbiGGcOjpWfJzfTxq3csCRRTKzV10YBe4/O6mk3fm3zw7GThckcMWKN9Xc5LuZjUd7kuAhyrYBCSwse+ST5Qm/5B+WjqMQJN4toKDuLDzAYT1+Pq/rrav/nzLb/pmoxfOWt3VS1xBF29IjVuH2wmwtY7RDbDMxGmTx+7AgvBy4ud+yEkx5+Mz6oGXYrFyj+hGduQzEtgu8Z475qSiTwED/9mWzCH4+Vgg9RcQB6jbb0QNroQH; RT=z=1&dm=shop.mango.com&si=522ff859-da83-42f8-900f-f73748310a46&ss=kupwjm2a&sl=1&tt=1ms&bcn=%2F%2F684dd308.akstat.io%2F; OptanonAlertBoxClosed=2021-10-13T19:24:32.694Z; _gaexp=GAX1.2.VzvKIlPhRsuyxTLbZD4GJw.19006.1; _gcl_au=1.1.464941951.1634153073; _scid=3df0b82e-bfa2-4bd5-a679-06deb9706a45; _ga_FGHFN35PBM=GS1.1.1634153072.1.1.1634153191.60; _ga=GA1.2.1858471610.1634153073; fita.sid.mango=XdVTqlBYuEoO6Odvsq3ASpkIQO6vk17g; rmStore=atm:pixel; _pin_unauth=dWlkPVpESmxZVEZoTWpBdE1XWmxNaTAwWlRGbUxXRTNPVEV0TjJFNVpqSTVOVEV6T0RKaw; _gid=GA1.2.442310991.1634153075; _hjid=a2384024-65ed-4e21-b2a8-b3ec187dd974; _hjFirstSeen=1; _fbp=fb.1.1634153074817.126575509; _hjIncludedInSessionSample=1; _hjAbsoluteSessionInProgress=1; FPID=FPID1.2.vEuHB%2BqTb4HoLiQz96rbWx0fZlYlf7QGEcmH1wNk1GA%3D.1634153073; stc117613=tsa:1634153074981.173415293.827662.5188867088317841.52:20211013195434|env:1%7C20211113192434%7C20211013195434%7C1%7C1071125:20221013192434|uid:1634153074981.1682016218.5764177.117613.1950118280:20221013192434|srchist:1071125%3A1%3A20211113192434:20221013192434; cto_bundle=xUAXrl9TRW5EUVA0OVpHaG9Ja1QzMGFsJTJCYXQlMkJqUTg5SWs2VUtDUHlDYkZvN21lWWlsUUFCTFI4MVM0ZTBaeHJJVnU3cmpLU2lVOXR6Vk9hanJrbGE4dGF0SmVLekQyVllQM1BHbHBJT0hFRU5EVGlMdXNicjNqbUlxZldaRVhHdHVyZll2a1BmNGl2cHBzQmElMkJXajVhV2cwa0ElM0QlM0Q; _uetsid=320323c02c5b11ec9cebe1b6fef821c9; _uetvid=320347302c5b11ecb14a6b59f30b6439; _dc_gtm_UA-855910-26=1',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'Cache-Control': 'max-age=0',
  'TE': 'trailers'
}

r = requests.get(url, headers=headers)

product=r.json()

name=product["name"]

print(name)
price=float(product["colors"]["colors"][0]["price"]["price"])
print(price)
color=product["colors"]["colors"][0]["label"]
print(color)
size=product["colors"]["colors"][0]["sizes"][1]["value"]
print(size)



# some JSON:
x =  { "name":name, "price":price, "color":color,"size":size}

# parse x:
y = json.dumps(x)

# the result is a Python dictionary:
print(y)