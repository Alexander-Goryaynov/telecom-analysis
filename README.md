# Сайт для анализа данных о поставщиках телекоммуникационных услуг

Приложение позволяет получить текстовый и графический отчёт о результатах анализа данных, загружаемых в виде CSV-файла

## Скриншоты

Пример CSV-файла

| id | company_name | company_code | market_cap | stock_price | daily_gain | country |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Comcast | CMCSA | 276.76 | 60.30 | -2.30 | USA | 
| 1 | Verizon | VZ | 226.96 | 54.82 | -1.10 | USA | 
| 2 | AT&T | T | 195.77 | 27.42 | -0.51 | USA | 
| 3 | T-Mobile US | TMUS | 167.81 | 134.47 | -1.12 | USA | 
| 4 | Charter Communications | CHTR | 147.21 | 800.83 | -1.29 | USA | 
| 5 | American Tower | AMT | 136.18 | 299.22 | -0.92 | USA | 
| 6 | China Mobile | 0941.HK | 128.13 | 6.26 | -1.62 | China | 
| 7 | Nippon Telegraph & Telephone | NPPXF | 107.08 | 29.61 | 3.89 | Japan | 
| 8 | SoftBank | SFTBF | 106.81 | 62.35 | 9.48 | Japan | 
| 9 | Deutsche Telekom | DTE.DE | 100.64 | 21.22 | -0.13 | Germany | 
| 10 | Crown Castle | CCI | 84.51 | 195.54 | -1.49 | USA | 

![](https://sun9-74.userapi.com/impg/UQOMKDQIhY2Q-AaEWrsBo7vNkPZSC_09fl9UFg/HA9ZMSRy_9E.jpg?size=1344x624&quality=96&sign=2368380b1df81912f2244363075087ef&type=album)

![](https://sun9-29.userapi.com/impg/rSPiiQEfPW9V1UJVGO3v4pIxO4LsAUOyXQ9N5Q/wPNu2oSrQ8I.jpg?size=1337x617&quality=96&sign=1b1cb72cce14f12350e47b8c1afb3e5a&type=album)

![](https://sun9-16.userapi.com/impg/TeLSgZjjG2QeyidRsHaAppYlej6Z0a_pCejXuw/RuyNrPcOE8s.jpg?size=1345x620&quality=96&sign=2d9692fdb45eb2ec38bdefbd8b0c7326&type=album)

![](https://sun9-18.userapi.com/impg/roJzbXh3mbaCu8WBpAUcdVyi7N-LIWh5dwGmDw/k1SRXVzwNSY.jpg?size=1345x618&quality=96&sign=33281b8e1e059f1d86eb9b065d7c9070&type=album)

![](https://sun9-8.userapi.com/impg/VyVfD-4-r8LGj4fwqlyqwsnSrKulkJ9yjV79Aw/e2yBl93C8sk.jpg?size=1339x615&quality=96&sign=309cfba9b39aaab7aa75881415fc75a2&type=album)

![](https://sun9-2.userapi.com/impg/0Sz6GYJPyxxEpHf5QHi4DdlQBh2ezztybIfLoA/LhEsZhivyco.jpg?size=1337x617&quality=96&sign=effd35934547e79d4294f7e7693150c5&type=album)

## Пример ответа API

```jsonc
{
    "marketCap": {
        "max": {
            "value": 276.76,
            "companyName": "Comcast"
        },
        "min": {
            "value": 0.09,
            "companyName": "Vislink Technologies"
        },
        "median": {
            "value": 8.62,
            "companyName": "Siena"
        },
        "avg": 27.3
    },
    "stockPrice": {
        "max": {
            "value": 800.83,
            "companyName": "Charter Communications"
        },
        "min": {
            "value": 0.04,
            "companyName": "Reliance Communications"
        },
        "median": {
            "value": 9.72,
            "companyName": "Vodacom"
        },
        "avg": 31.97
    },
    "dailyLossGain": {
        "gain": {
            "max": {
                "value": 9.48,
                "companyName": "SoftBank"
            },
            "avg": 1.88
        }, 
        "loss": {
            "max": {
                "value": 23.3,
                "companyName": "XL Axiata"
            },
            "avg": 1.9
        }
    },
    "totalCapByContry": [
        {
            "countryName": "USA",
            "totalCap": 1024.76
        },
        //
    ],
    "companiesCountByCountry": [
        {
            "countryName": "USA",
            "companiesCount": 29
        },
        //
    ],
    "clusterizationResult": {
        "plotBase64": "data:image/png;base64,CODE",
        "inertiaValue": 70.6
    }
}
```