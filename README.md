# Сайт для анализа данных о поставщиках телекоммуникационных услуг

Приложение позволяет получить текстовый и графический отчёт о результатах анализа данных, загружаемых в виде CSV-файла

## Скриншоты

Пример CSV-файла

![](https://sun9-13.userapi.com/impg/CmAP3-j6yDAyj_rERx2SkQF9RnXbJf_oKLyS9A/PXXm4MKW5UM.jpg?size=1177x323&quality=96&sign=b7a57bd285aec1caa4f73705cc10f8db&type=album)

![](https://sun9-74.userapi.com/impg/UQOMKDQIhY2Q-AaEWrsBo7vNkPZSC_09fl9UFg/HA9ZMSRy_9E.jpg?size=1344x624&quality=96&sign=2368380b1df81912f2244363075087ef&type=album)

![](https://sun9-29.userapi.com/impg/rSPiiQEfPW9V1UJVGO3v4pIxO4LsAUOyXQ9N5Q/wPNu2oSrQ8I.jpg?size=1337x617&quality=96&sign=1b1cb72cce14f12350e47b8c1afb3e5a&type=album)

![](https://sun9-16.userapi.com/impg/TeLSgZjjG2QeyidRsHaAppYlej6Z0a_pCejXuw/RuyNrPcOE8s.jpg?size=1345x620&quality=96&sign=2d9692fdb45eb2ec38bdefbd8b0c7326&type=album)

![](https://sun9-18.userapi.com/impg/roJzbXh3mbaCu8WBpAUcdVyi7N-LIWh5dwGmDw/k1SRXVzwNSY.jpg?size=1345x618&quality=96&sign=33281b8e1e059f1d86eb9b065d7c9070&type=album)

![](https://sun9-8.userapi.com/impg/VyVfD-4-r8LGj4fwqlyqwsnSrKulkJ9yjV79Aw/e2yBl93C8sk.jpg?size=1339x615&quality=96&sign=309cfba9b39aaab7aa75881415fc75a2&type=album)

## Пример ответа API

```json
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
    ]
}
```