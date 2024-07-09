import requests

cookies = {
    '_aimtellSubscriberID': 'ad14902a-ae24-6de0-abf8-9efd80a269cd',
    'cookieId': '43317A8E_4FDD_2C14_6116_B6C98F2081A9',
    'sessionID_shein': 's%3A6P6vv_Q6q3EBX4_b4O060g306z-Td4MI.25NWn%2FcMqdIWdj2UtRsg0Ibn9fn5z4IBkvo9V1nnleY',
    'RESOURCE_ADAPT_WEBP': '1',
    'smidV2': '20240410172451969ea831424ae3108d9e50734c4b1db2007de1b717184f6d0',
    'armorUuid': '2024041017245169eedd9d7246c8d64eecda35311ed0890072f62cc823ad6100',
    'lastRskxRun': '1720553760535',
    'rskxRunCookie': '0',
    'rCookie': '2k2id25rpzfskltxooponlyetaa6x',
    '_gcl_gs': '2.1.k1$i1720553751',
    '_gcl_au': '1.1.1765087197.1720553762',
    '_fbp': 'fb.1.1720553761892.871249053297134877',
    '_uetsid': '797a9e003e2a11ef87a6ef4b1fd91709',
    '_uetvid': '65677080f77811ee87d261f5b9440e93',
    '_pin_unauth': 'dWlkPVkyUTNZamczWTJJdFpXUTJNaTAwTURCaExUazJZMlV0TWpKbVpqQm1aVFF3WlRsag',
    '_csrf': 'If72IqYsKDy6AViF_dHRHXkA',
    '_gcl_aw': 'GCL.1720553764.EAIaIQobChMI6rrnl9qahwMVVhetBh2NzwEREAAYASAAEgLJXPD_BwE',
    'forterToken': '075427677168401380fd2d9b70aeb598_1720553764976__UDF43-m4_17ck_',
}

headers = {
    'accept': '*/*',
    'accept-language': 'pt-PT,pt;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_aimtellSubscriberID=ad14902a-ae24-6de0-abf8-9efd80a269cd; cookieId=43317A8E_4FDD_2C14_6116_B6C98F2081A9; sessionID_shein=s%3A6P6vv_Q6q3EBX4_b4O060g306z-Td4MI.25NWn%2FcMqdIWdj2UtRsg0Ibn9fn5z4IBkvo9V1nnleY; RESOURCE_ADAPT_WEBP=1; smidV2=20240410172451969ea831424ae3108d9e50734c4b1db2007de1b717184f6d0; armorUuid=2024041017245169eedd9d7246c8d64eecda35311ed0890072f62cc823ad6100; lastRskxRun=1720553760535; rskxRunCookie=0; rCookie=2k2id25rpzfskltxooponlyetaa6x; _gcl_gs=2.1.k1$i1720553751; _gcl_au=1.1.1765087197.1720553762; _fbp=fb.1.1720553761892.871249053297134877; _uetsid=797a9e003e2a11ef87a6ef4b1fd91709; _uetvid=65677080f77811ee87d261f5b9440e93; _pin_unauth=dWlkPVkyUTNZamczWTJJdFpXUTJNaTAwTURCaExUazJZMlV0TWpKbVpqQm1aVFF3WlRsag; _csrf=If72IqYsKDy6AViF_dHRHXkA; _gcl_aw=GCL.1720553764.EAIaIQobChMI6rrnl9qahwMVVhetBh2NzwEREAAYASAAEgLJXPD_BwE; forterToken=075427677168401380fd2d9b70aeb598_1720553764976__UDF43-m4_17ck_',
    'pragma': 'no-cache',
    'prefetch': '1',
    'priority': 'u=1, i',
    'referer': 'https://br.shein.com/?url_from=brgooglebrandshein_sheinshein02_srsa_20210130&cid=1453018537&setid=58136794738&adid=495662299646&kwd=kwd-1667706624&pf=GOOGLE&gad_source=1&gclid=EAIaIQobChMI6rrnl9qahwMVVhetBh2NzwEREAAYASAAEgLJXPD_BwE',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response = requests.get('https://br.shein.com/cart', cookies=cookies, headers=headers)

print(response.text)