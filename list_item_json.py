def json_display(url, item_name, item_price):
    list_item_json = {
        "listItemIdentifier": item_name,
        "ordinalNumber": 1,
        "textContent": {
            "primaryText": {
                "type": "PlainText",
                "text": item_name
            },
            "secondaryText": {
                "type": "PlainText",
                "text": item_price
            }
        },
        "image": {
            "contentDescription": None,
            "smallSourceUrl": None,
            "largeSourceUrl": None,
            "sources": [
                {
                    "url": url,
                    "size": "small",
                    "widthPixels": 0,
                    "heightPixels": 0
                },
                {
                    "url": url,
                    "size": "large",
                    "widthPixels": 0,
                    "heightPixels": 0
                }
            ]
        },
        "token": item_name
    }
    return list_item_json
