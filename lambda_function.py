"""
This is a Python template for Alexa to get you building skills (conversations) quickly.
"""

"""
This is a Python template for Alexa to get you building skills (conversations) quickly.
"""

from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import nav_functions as nf
import list_item_json as lij

import base64
import json
import urllib
from urllib import request, parse

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--window-size=1280x1696')
chrome_options.add_argument('--user-data-dir=/tmp/user-data')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--enable-logging')
chrome_options.add_argument('--log-level=0')
chrome_options.add_argument('--v=99')
chrome_options.add_argument('--single-process')
chrome_options.add_argument('--data-path=/tmp/data-path')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--homedir=/tmp')
chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
print(chrome_options)
chrome_options.binary_location = "/opt/python/bin/headless-chromium"


# --------------- Helpers that build all of the responses ----------------------

def display_build_speechlet_response(title, output, reprompt_text, should_end_session, session_attributes):
    list_items = session_attributes["json_list_items_dict"]
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        # 'card': {
        #     'type': 'Simple',
        #     'title': "SessionSpeechlet - " + title,
        #     'content': "SessionSpeechlet - " + output
        # },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        "directives": [{
            "type": "Alexa.Presentation.APL.RenderDocument",
            "token": "helloworldToken",
            "document": {
                "type": "APL",
                "version": "1.3",
                "settings": {},
                "theme": "dark",
                "import": [
                    {
                        "name": "alexa-layouts",
                        "version": "1.0.0"
                    }
                ],
                "resources": [
                    {
                        "description": "Stock color for the light theme",
                        "colors": {
                            "colorTextPrimary": "#151920"
                        }
                    },
                    {
                        "description": "Stock color for the dark theme",
                        "when": "${viewport.theme == 'dark'}",
                        "colors": {
                            "colorTextPrimary": "#f0f1ef"
                        }
                    },
                    {
                        "description": "Standard font sizes",
                        "dimensions": {
                            "textSizeBody": 48,
                            "textSizePrimary": 27,
                            "textSizeSecondary": 23,
                            "textSizeDetails": 20,
                            "textSizeSecondaryHint": 25
                        }
                    },
                    {
                        "description": "Common spacing values",
                        "dimensions": {
                            "spacingThin": 6,
                            "spacingSmall": 12,
                            "spacingMedium": 24,
                            "spacingLarge": 48,
                            "spacingExtraLarge": 72
                        }
                    },
                    {
                        "description": "Common margins and padding",
                        "dimensions": {
                            "marginTop": 40,
                            "marginLeft": 60,
                            "marginRight": 60,
                            "marginBottom": 40
                        }
                    }
                ],
                "styles": {
                    "textStyleBase": {
                        "description": "Base font description; set color",
                        "values": [
                            {
                                "color": "@colorTextPrimary"
                            }
                        ]
                    },
                    "textStyleBase0": {
                        "description": "Thin version of basic font",
                        "extend": "textStyleBase",
                        "values": {
                            "fontWeight": "100"
                        }
                    },
                    "textStyleBase1": {
                        "description": "Light version of basic font",
                        "extend": "textStyleBase",
                        "values": {
                            "fontWeight": "300"
                        }
                    },
                    "textStyleBase2": {
                        "description": "Regular version of basic font",
                        "extend": "textStyleBase",
                        "values": {
                            "fontWeight": "500"
                        }
                    },
                    "mixinBody": {
                        "values": {
                            "fontSize": "@textSizeBody"
                        }
                    },
                    "mixinPrimary": {
                        "values": {
                            "fontSize": "@textSizePrimary"
                        }
                    },
                    "mixinDetails": {
                        "values": {
                            "fontSize": "@textSizeDetails"
                        }
                    },
                    "mixinSecondary": {
                        "values": {
                            "fontSize": "@textSizeSecondary"
                        }
                    },
                    "textStylePrimary": {
                        "extend": [
                            "textStyleBase1",
                            "mixinPrimary"
                        ]
                    },
                    "textStyleSecondary": {
                        "extend": [
                            "textStyleBase0",
                            "mixinSecondary"
                        ]
                    },
                    "textStyleBody": {
                        "extend": [
                            "textStyleBase1",
                            "mixinBody"
                        ]
                    },
                    "textStyleSecondaryHint": {
                        "values": {
                            "fontFamily": "Bookerly",
                            "fontStyle": "italic",
                            "fontSize": "@textSizeSecondaryHint",
                            "color": "@colorTextPrimary"
                        }
                    },
                    "textStyleDetails": {
                        "extend": [
                            "textStyleBase2",
                            "mixinDetails"
                        ]
                    }
                },
                "onMount": [],
                "graphics": {},
                "commands": {},
                "layouts": {
                    "FullHorizontalListItem": {
                        "parameters": [
                            "listLength"
                        ],
                        "item": [
                            {
                                "type": "Container",
                                "height": "100vh",
                                "width": "100vw",
                                "alignItems": "center",
                                "justifyContent": "end",
                                "items": [
                                    {
                                        "type": "Image",
                                        "position": "absolute",
                                        "height": "100vh",
                                        "width": "100vw",
                                        "overlayColor": "rgba(0, 0, 0, 0.6)",
                                        "source": "${data.image.sources[0].url}",
                                        "scale": "best-fill"
                                    },
                                    {
                                        "type": "AlexaHeader",
                                        "headerTitle": "${title}",
                                        "headerAttributionImage": "${logo}",
                                        "grow": 1
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${data.textContent.primaryText.text}",
                                        "style": "textStyleBody",
                                        "maxLines": 1
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${data.textContent.secondaryText.text}",
                                        "style": "textStyleDetails"
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${ordinal} | ${listLength}",
                                        "paddingBottom": "20dp",
                                        "color": "white",
                                        "spacing": "5dp"
                                    }
                                ]
                            }
                        ]
                    },
                    "HorizontalListItem": {
                        "item": [
                            {
                                "type": "Container",
                                "maxWidth": 528,
                                "minWidth": 312,
                                "paddingLeft": 16,
                                "paddingRight": 16,
                                "height": "100%",
                                "items": [
                                    {
                                        "type": "Image",
                                        "source": "${data.image.sources[0].url}",
                                        "height": "40vh",
                                        "width": "40vh"
                                    },
                                    {
                                        "type": "Text",
                                        "text": "<b>${ordinal}.</b> ${data.textContent.primaryText.text}",
                                        "style": "textStyleSecondary",
                                        "maxLines": 1,
                                        "spacing": 12
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${data.textContent.secondaryText.text}",
                                        "style": "textStyleDetails",
                                        "spacing": 4
                                    }
                                ]
                            }
                        ]
                    },
                    "ListTemplate2": {
                        "parameters": [
                            "backgroundImage",
                            "title",
                            "logo",
                            "hintText",
                            "listData"
                        ],
                        "items": [
                            {
                                "when": "${viewport.shape == 'round'}",
                                "type": "Container",
                                "height": "100%",
                                "width": "100%",
                                "items": [
                                    {
                                        "type": "Sequence",
                                        "scrollDirection": "horizontal",
                                        "data": "${listData}",
                                        "height": "100%",
                                        "width": "100%",
                                        "numbered": True,
                                        "item": [
                                            {
                                                "type": "FullHorizontalListItem",
                                                "listLength": "${payload.listTemplate2ListData.listPage.listItems.length}"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "Container",
                                "height": "100vh",
                                "width": "100vw",
                                "items": [
                                    {
                                        "type": "Image",
                                        "source": "${backgroundImage}",
                                        "scale": "best-fill",
                                        "width": "100vw",
                                        "height": "100vh",
                                        "position": "absolute"
                                    },
                                    {
                                        "type": "AlexaHeader",
                                        "headerTitle": "${title}",
                                        "headerAttributionImage": "${logo}"
                                    },
                                    {
                                        "type": "Sequence",
                                        "scrollDirection": "horizontal",
                                        "paddingLeft": "@marginLeft",
                                        "paddingRight": "@marginRight",
                                        "data": "${listData}",
                                        "height": "70vh",
                                        "width": "100%",
                                        "numbered": True,
                                        "item": [
                                            {
                                                "type": "HorizontalListItem"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                },
                "mainTemplate": {
                    "parameters": [
                        "payload"
                    ],
                    "item": [
                        {
                            "type": "ListTemplate2",
                            "backgroundImage": "${payload.listTemplate2Metadata.backgroundImage.sources[0].url}",
                            "title": "${payload.listTemplate2Metadata.title}",
                            "hintText": "${payload.listTemplate2Metadata.hintText}",
                            "logo": "${payload.listTemplate2Metadata.logoUrl}",
                            "listData": "${payload.listTemplate2ListData.listPage.listItems}"
                        }
                    ]
                }
            },
            "datasources": {
                "listTemplate2Metadata": {
                    "type": "object",
                    "objectId": "lt1Metadata",
                    "backgroundImage": {
                        "contentDescription": None,
                        "smallSourceUrl": None,
                        "largeSourceUrl": None,
                        "sources": [
                            {
                                "url": "https://d2o906d8ln7ui1.cloudfront.net/images/LT2_Background.png",
                                "size": "small",
                                "widthPixels": 0,
                                "heightPixels": 0
                            },
                            {
                                "url": "https://d2o906d8ln7ui1.cloudfront.net/images/LT2_Background.png",
                                "size": "large",
                                "widthPixels": 0,
                                "heightPixels": 0
                            }
                        ]
                    },
                    "title": "Results for \"Eaze Menu\"",
                    "logoUrl": "https://d2o906d8ln7ui1.cloudfront.net/images/cheeseskillicon.png"
                },
                "listTemplate2ListData": {
                    "type": "list",
                    "listId": "lt2Sample",
                    "totalNumberOfItems": 10,
                    "hintText": "Try, \"Alexa, select number 1\"",
                    "listPage": {
                        "listItems": list_items
                    }
                }
            }
            #   "document": {
            #     "type": "APL",
            #     "version": "1.3",
            #     "mainTemplate": {
            #       "parameters": [
            #         "payload"
            #       ],
            #       "items": [
            #         {
            #           "type": "Container",
            #           "height": "100%",
            #           "width": "100%",
            #           "items": [
            #             {
            #               "type": "Text",
            #               "id": "helloTextComponent",
            #               "text": "${payload.helloworldData.properties.helloText}",
            #               "textAlign": "center",
            #               "textAlignVertical": "center",
            #               "maxLines": 3,
            #               "grow": 1
            #             },
            #             {
            #               "type": "Text",
            #               "id": "newHelloTextComponent",
            #               "text": "${payload.helloworldData.properties.newHelloText}",
            #               "textAlign": "center",
            #               "textAlignVertical": "bottom",
            #               "maxLines": 3,
            #               "opacity": 0
            #             }
            #           ]
            #         }
            #       ]
            #     }
            #   },
            #   "datasources": {
            #     "helloworldData": {
            #       "type": "object",
            #       "objectId": "helloworld",
            #       "properties": {
            #         "helloText": "Hello world! This APL document displays text from a datasource called helloworldData.",
            #         "newHelloText": "I hid the original hello text and then displayed this!"
            #       }
            #     }
            #   }
        }],
        'shouldEndSession': should_end_session
    }


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    section = [{
        'type': 'PlainText',
        'text': output
    },
        {
            'type': 'PlainText',
            'text': output
        }]
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        # 'card': {
        #     'type': 'Simple',
        #     'title': "SessionSpeechlet - " + title,
        #     'content': "SessionSpeechlet - " + output
        # },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        "directives": [{
            "type": "Alexa.Presentation.APL.RenderDocument",
            "token": "helloworldToken",
            "document": {
                "type": "APL",
                "version": "1.3",
                "settings": {},
                "theme": "dark",
                "import": [
                    {
                        "name": "alexa-layouts",
                        "version": "1.0.0"
                    }
                ],
                "resources": [
                    {
                        "description": "Stock color for the light theme",
                        "colors": {
                            "colorTextPrimary": "#151920"
                        }
                    },
                    {
                        "description": "Stock color for the dark theme",
                        "when": "${viewport.theme == 'dark'}",
                        "colors": {
                            "colorTextPrimary": "#f0f1ef"
                        }
                    },
                    {
                        "description": "Standard font sizes",
                        "dimensions": {
                            "textSizeBody": 48,
                            "textSizePrimary": 27,
                            "textSizeSecondary": 23,
                            "textSizeDetails": 20,
                            "textSizeSecondaryHint": 25
                        }
                    },
                    {
                        "description": "Common spacing values",
                        "dimensions": {
                            "spacingThin": 6,
                            "spacingSmall": 12,
                            "spacingMedium": 24,
                            "spacingLarge": 48,
                            "spacingExtraLarge": 72
                        }
                    },
                    {
                        "description": "Common margins and padding",
                        "dimensions": {
                            "marginTop": 40,
                            "marginLeft": 60,
                            "marginRight": 60,
                            "marginBottom": 40
                        }
                    }
                ],
                "styles": {
                    "textStyleBase": {
                        "description": "Base font description; set color",
                        "values": [
                            {
                                "color": "@colorTextPrimary"
                            }
                        ]
                    },
                    "textStyleBase0": {
                        "description": "Thin version of basic font",
                        "extend": "textStyleBase",
                        "values": {
                            "fontWeight": "100"
                        }
                    },
                    "textStyleBase1": {
                        "description": "Light version of basic font",
                        "extend": "textStyleBase",
                        "values": {
                            "fontWeight": "300"
                        }
                    },
                    "textStyleBase2": {
                        "description": "Regular version of basic font",
                        "extend": "textStyleBase",
                        "values": {
                            "fontWeight": "500"
                        }
                    },
                    "mixinBody": {
                        "values": {
                            "fontSize": "@textSizeBody"
                        }
                    },
                    "mixinPrimary": {
                        "values": {
                            "fontSize": "@textSizePrimary"
                        }
                    },
                    "mixinDetails": {
                        "values": {
                            "fontSize": "@textSizeDetails"
                        }
                    },
                    "mixinSecondary": {
                        "values": {
                            "fontSize": "@textSizeSecondary"
                        }
                    },
                    "textStylePrimary": {
                        "extend": [
                            "textStyleBase1",
                            "mixinPrimary"
                        ]
                    },
                    "textStyleSecondary": {
                        "extend": [
                            "textStyleBase0",
                            "mixinSecondary"
                        ]
                    },
                    "textStyleBody": {
                        "extend": [
                            "textStyleBase1",
                            "mixinBody"
                        ]
                    },
                    "textStyleSecondaryHint": {
                        "values": {
                            "fontFamily": "Bookerly",
                            "fontStyle": "italic",
                            "fontSize": "@textSizeSecondaryHint",
                            "color": "@colorTextPrimary"
                        }
                    },
                    "textStyleDetails": {
                        "extend": [
                            "textStyleBase2",
                            "mixinDetails"
                        ]
                    }
                },
                "onMount": [],
                "graphics": {},
                "commands": {},
                "layouts": {
                    "FullHorizontalListItem": {
                        "parameters": [
                            "listLength"
                        ],
                        "item": [
                            {
                                "type": "Container",
                                "height": "100vh",
                                "width": "100vw",
                                "alignItems": "center",
                                "justifyContent": "end",
                                "items": [
                                    {
                                        "type": "Image",
                                        "position": "absolute",
                                        "height": "100vh",
                                        "width": "100vw",
                                        "overlayColor": "rgba(0, 0, 0, 0.6)",
                                        "source": "${data.image.sources[0].url}",
                                        "scale": "best-fill"
                                    },
                                    {
                                        "type": "AlexaHeader",
                                        "headerTitle": "${title}",
                                        "headerAttributionImage": "${logo}",
                                        "grow": 1
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${data.textContent.primaryText.text}",
                                        "style": "textStyleBody",
                                        "maxLines": 1
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${data.textContent.secondaryText.text}",
                                        "style": "textStyleDetails"
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${ordinal} | ${listLength}",
                                        "paddingBottom": "20dp",
                                        "color": "white",
                                        "spacing": "5dp"
                                    }
                                ]
                            }
                        ]
                    },
                    "HorizontalListItem": {
                        "item": [
                            {
                                "type": "Container",
                                "maxWidth": 528,
                                "minWidth": 312,
                                "paddingLeft": 16,
                                "paddingRight": 16,
                                "height": "100%",
                                "items": [
                                    {
                                        "type": "Image",
                                        "source": "${data.image.sources[0].url}",
                                        "height": "40vh",
                                        "width": "40vh"
                                    },
                                    {
                                        "type": "Text",
                                        "text": "<b>${ordinal}.</b> ${data.textContent.primaryText.text}",
                                        "style": "textStyleSecondary",
                                        "maxLines": 1,
                                        "spacing": 12
                                    },
                                    {
                                        "type": "Text",
                                        "text": "${data.textContent.secondaryText.text}",
                                        "style": "textStyleDetails",
                                        "spacing": 4
                                    }
                                ]
                            }
                        ]
                    },
                    "ListTemplate2": {
                        "parameters": [
                            "backgroundImage",
                            "title",
                            "logo",
                            "hintText",
                            "listData"
                        ],
                        "items": [
                            {
                                "when": "${viewport.shape == 'round'}",
                                "type": "Container",
                                "height": "100%",
                                "width": "100%",
                                "items": [
                                    {
                                        "type": "Sequence",
                                        "scrollDirection": "horizontal",
                                        "data": "${listData}",
                                        "height": "100%",
                                        "width": "100%",
                                        "numbered": True,
                                        "item": [
                                            {
                                                "type": "FullHorizontalListItem",
                                                "listLength": "${payload.listTemplate2ListData.listPage.listItems.length}"
                                            }
                                        ]
                                    }
                                ]
                            },
                            {
                                "type": "Container",
                                "height": "100vh",
                                "width": "100vw",
                                "items": [
                                    {
                                        "type": "Image",
                                        "source": "${backgroundImage}",
                                        "scale": "best-fill",
                                        "width": "100vw",
                                        "height": "100vh",
                                        "position": "absolute"
                                    },
                                    {
                                        "type": "AlexaHeader",
                                        "headerTitle": "${title}",
                                        "headerAttributionImage": "${logo}"
                                    },
                                    {
                                        "type": "Sequence",
                                        "scrollDirection": "horizontal",
                                        "paddingLeft": "@marginLeft",
                                        "paddingRight": "@marginRight",
                                        "data": "${listData}",
                                        "height": "70vh",
                                        "width": "100%",
                                        "numbered": True,
                                        "item": [
                                            {
                                                "type": "HorizontalListItem"
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                },
                "mainTemplate": {
                    "parameters": [
                        "payload"
                    ],
                    "item": [
                        {
                            "type": "ListTemplate2",
                            "backgroundImage": "${payload.listTemplate2Metadata.backgroundImage.sources[0].url}",
                            "title": "${payload.listTemplate2Metadata.title}",
                            "hintText": "${payload.listTemplate2Metadata.hintText}",
                            "logo": "${payload.listTemplate2Metadata.logoUrl}",
                            "listData": "${payload.listTemplate2ListData.listPage.listItems}"
                        }
                    ]
                }
            },
            "datasources": {
                "listTemplate2Metadata": {
                    "type": "object",
                    "objectId": "lt1Metadata",
                    "backgroundImage": {
                        "contentDescription": None,
                        "smallSourceUrl": None,
                        "largeSourceUrl": None,
                        "sources": [
                            {
                                "url": "https://d2o906d8ln7ui1.cloudfront.net/images/LT2_Background.png",
                                "size": "small",
                                "widthPixels": 0,
                                "heightPixels": 0
                            },
                            {
                                "url": "https://d2o906d8ln7ui1.cloudfront.net/images/LT2_Background.png",
                                "size": "large",
                                "widthPixels": 0,
                                "heightPixels": 0
                            }
                        ]
                    },
                    "title": "Results for \"Eaze Menu\"",
                    "logoUrl": "https://d2o906d8ln7ui1.cloudfront.net/images/cheeseskillicon.png"
                },
                "listTemplate2ListData": {
                    "type": "list",
                    "listId": "lt2Sample",
                    "totalNumberOfItems": 10,
                    "hintText": "Try, \"Alexa, select number 1\"",
                    "listPage": {
                        "listItems": [
                            {
                                "listItemIdentifier": "brie",
                                "ordinalNumber": 1,
                                "textContent": {
                                    "primaryText": {
                                        "type": "PlainText",
                                        "text": "Brie"
                                    },
                                    "secondaryText": {
                                        "type": "PlainText",
                                        "text": "Origin: France"
                                    }
                                },
                                "image": {
                                    "contentDescription": None,
                                    "smallSourceUrl": None,
                                    "largeSourceUrl": None,
                                    "sources": [
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/md_brie.png",
                                            "size": "small",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        },
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/md_brie.png",
                                            "size": "large",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        }
                                    ]
                                },
                                "token": "brie"
                            },
                            {
                                "listItemIdentifier": "gruyere",
                                "ordinalNumber": 2,
                                "textContent": {
                                    "primaryText": {
                                        "type": "PlainText",
                                        "text": "Gruyere"
                                    },
                                    "secondaryText": {
                                        "type": "RichText",
                                        "text": "Origin: Switzerland"
                                    }
                                },
                                "image": {
                                    "contentDescription": None,
                                    "smallSourceUrl": None,
                                    "largeSourceUrl": None,
                                    "sources": [
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/md_gruyere.png",
                                            "size": "small",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        },
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/md_gruyere.png",
                                            "size": "large",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        }
                                    ]
                                },
                                "token": "gruyere"
                            },
                            {
                                "listItemIdentifier": "gorgonzola",
                                "ordinalNumber": 3,
                                "textContent": {
                                    "primaryText": {
                                        "type": "PlainText",
                                        "text": "Gorgonzola"
                                    },
                                    "secondaryText": {
                                        "type": "RichText",
                                        "text": "Origin: Italy"
                                    }
                                },
                                "image": {
                                    "contentDescription": None,
                                    "smallSourceUrl": None,
                                    "largeSourceUrl": None,
                                    "sources": [
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/md_gorgonzola.png",
                                            "size": "small",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        },
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/md_gorgonzola.png",
                                            "size": "large",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        }
                                    ]
                                },
                                "token": "gorgonzola"
                            },
                            {
                                "listItemIdentifier": "brie",
                                "ordinalNumber": 1,
                                "textContent": {
                                    "primaryText": {
                                        "type": "PlainText",
                                        "text": "Brie"
                                    },
                                    "secondaryText": {
                                        "type": "PlainText",
                                        "text": "Origin: France"
                                    }
                                },
                                "image": {
                                    "contentDescription": None,
                                    "smallSourceUrl": None,
                                    "largeSourceUrl": None,
                                    "sources": [
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/tl_brie.png",
                                            "size": "small",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        },
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/tl_brie.png",
                                            "size": "large",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        }
                                    ]
                                },
                                "token": "tl_brie"
                            },
                            {
                                "listItemIdentifier": "gruyere",
                                "ordinalNumber": 2,
                                "textContent": {
                                    "primaryText": {
                                        "type": "PlainText",
                                        "text": "Gruyere"
                                    },
                                    "secondaryText": {
                                        "type": "RichText",
                                        "text": "Origin: Switzerland"
                                    }
                                },
                                "image": {
                                    "contentDescription": None,
                                    "smallSourceUrl": None,
                                    "largeSourceUrl": None,
                                    "sources": [
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/tl_gruyere.png",
                                            "size": "small",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        },
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/tl_gruyere.png",
                                            "size": "large",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        }
                                    ]
                                },
                                "token": "tl_gruyere"
                            },
                            {
                                "listItemIdentifier": "gorgonzola",
                                "ordinalNumber": 3,
                                "textContent": {
                                    "primaryText": {
                                        "type": "PlainText",
                                        "text": "Gorgonzola"
                                    },
                                    "secondaryText": {
                                        "type": "RichText",
                                        "text": "Origin: Italy"
                                    }
                                },
                                "image": {
                                    "contentDescription": None,
                                    "smallSourceUrl": None,
                                    "largeSourceUrl": None,
                                    "sources": [
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/tl_gorgonzola.png",
                                            "size": "small",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        },
                                        {
                                            "url": "https://d2o906d8ln7ui1.cloudfront.net/images/tl_gorgonzola.png",
                                            "size": "large",
                                            "widthPixels": 0,
                                            "heightPixels": 0
                                        }
                                    ]
                                },
                                "token": "tl_gorgonzola"
                            }
                        ]
                    }
                }
            }
            #   "document": {
            #     "type": "APL",
            #     "version": "1.3",
            #     "mainTemplate": {
            #       "parameters": [
            #         "payload"
            #       ],
            #       "items": [
            #         {
            #           "type": "Container",
            #           "height": "100%",
            #           "width": "100%",
            #           "items": [
            #             {
            #               "type": "Text",
            #               "id": "helloTextComponent",
            #               "text": "${payload.helloworldData.properties.helloText}",
            #               "textAlign": "center",
            #               "textAlignVertical": "center",
            #               "maxLines": 3,
            #               "grow": 1
            #             },
            #             {
            #               "type": "Text",
            #               "id": "newHelloTextComponent",
            #               "text": "${payload.helloworldData.properties.newHelloText}",
            #               "textAlign": "center",
            #               "textAlignVertical": "bottom",
            #               "maxLines": 3,
            #               "opacity": 0
            #             }
            #           ]
            #         }
            #       ]
            #     }
            #   },
            #   "datasources": {
            #     "helloworldData": {
            #       "type": "object",
            #       "objectId": "helloworld",
            #       "properties": {
            #         "helloText": "Hello world! This APL document displays text from a datasource called helloworldData.",
            #         "newHelloText": "I hid the original hello text and then displayed this!"
            #       }
            #     }
            #   }
        }],
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def send_receipt(intent, session):
    TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
    TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"

    session_attributes = session["attributes"]
    cart_list = session_attributes["cart_list"]

    to_number = "+16613029696"
    from_number = "+12019077822"
    body = cart_list

    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not body:
        return "The function needs a 'Body' message to send."

    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": to_number, "From": from_number, "Body": body}

    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()

    req = request.Request(populated_url)

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
    except Exception as e:
        # something went wrong!
        return e

    card_title = "Test"
    speech_output = "I just texted you a receipt, yeet!"

    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = True
    return build_response(session_attributes, display_build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session, session_attributes))


def checkout(intent, session):
    # Text the cart list item name and price

    session_attributes = session["attributes"]

    # key: item name - value:tuple(url, price)
    img_dict = session_attributes["img_dict"]

    # list of name_price tuples
    cart_list = session_attributes["cart_list"]

    item_json = []
    total_price = 0

    for item_tuple in cart_list:
        item_name = item_tuple[0]

        img_tuple = img_dict[item_name]
        item_url = img_tuple[0]
        item_price = img_tuple[1]

        # removes dollar sign from price
        raw_price = item_price.replace('$', '')
        raw_price = int(raw_price)

        total_price += raw_price

        json_list_item = lij.json_display(item_url, item_name, item_price)
        item_json.append(json_list_item)

    session_attributes["json_list_items_dict"] = item_json
    card_title = "Test"
    speech_output = "Your total is $" + str(total_price) + ". If everything looks good say confirm, \
                        else continue shopping or say remove to delete an item."

    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, display_build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session, session_attributes))


def order(intent, session):
    # Initiate driver and get site
    driver = webdriver.Chrome(chrome_options=chrome_options)
    site = "https://www.eaze.com/menu"
    driver.get(site)

    # Intiate menu variables
    menu = ""
    title_menu = ""
    short_menu = ""

    time.sleep(1)

    # Set "count" @ 1 because
    count = 1
    p = 0

    # Get menu from the "session" dictionary
    session_attributes = session['attributes']
    menu = session_attributes['menu']

    # h2_menu_items = session_attributes['menu_items']
    # print("session_attributes>>>", session_attributes)

    # Get the order number from the intent dictionary
    orderNum = intent["slots"]["number"]["value"]

    # Get h2 you are looking for menu[orderNum]
    text = menu[orderNum]

    # Geting all the h2 tags
    page_data = driver.find_elements(By.TAG_NAME, 'h2')
    # item_list = session_attributes["item_list"]

    for header in page_data:

        # Use if statement to find the selected item
        # if header == text:
        if header.text == text:

            # Find button tag for selected header item
            buttons = header.find_element_by_xpath('..')
            buttons = buttons.find_element_by_xpath('..')

            # Returns "goToMenuGroupPage_xxxxxxx"
            buttons = buttons.find_element_by_xpath(".//button").get_attribute('data-e2eid')

            # Remove "goToMenuGroupPage_" from data-e2eid attribute
            buttons = buttons[18:]

            # Create site string url for selected item
            site = "https://www.eaze.com/groups/" + buttons

            # Get the selected item url
            driver.get(site)

            time.sleep(1)

            menu_elms = driver.find_element_by_xpath("//div[2]/div/div[2]")

            menu_items = menu_elms.find_elements_by_xpath("./div[2]/div")
            num_menu_items = len(menu_items)

            # Get Menu Type Items
            menu_types = menu_elms.find_element_by_xpath("./div[1]/div/div[1]")
            type_title = menu_types.find_element_by_xpath("./div[1]").text
            type_items = menu_types.find_elements_by_xpath("./div[2]/button")

            type_items_list = []
            counter = 1
            for item in type_items:
                type_items_list.append(item.text.strip())

                if counter == 1:
                    say_types = item.text
                elif counter < len(type_items):
                    say_types += ", " + item.text
                else:
                    say_types += ", " + ", " + item.text + "."

            # Get Menu Brands
            menu_brands = menu_elms.find_element_by_xpath("./div[1]/div/div[2]/div[1]")
            brand_items = menu_elms.find_elements_by_xpath("./div[1]/div/div[2]/div[2]")
            brand_items = brand_items[0].text
            brand_items = brand_items.split('\n')

            menu_brands_list = []
            counter = 1

            for item in brand_items:
                print("an item", item)
                the_item = item
                menu_brands_list.append(the_item)

                if counter == 1:
                    say_brands = the_item
                elif counter < len(brand_items):
                    say_brands += ", " + the_item
                else:
                    say_brands += ", " + the_item + "."

                counter += 1

            driver.close()
            break

    card_title = "Test"
    speech_output = "There are " + str(num_menu_items) + " items on the menu." + " The brands are " + say_brands
    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def section_page(intent, session):
    # Initiate driver and get site
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # Get menu from the "session" dictionary
    session_attributes = session['attributes']

    # Get order number from session_attributes
    orderNum = session_attributes["orderNum"]

    h2_mm_item_button_dict = session_attributes["h2_mm_item_button_dict"]
    item_tuple = h2_mm_item_button_dict[orderNum]

    section = item_tuple[0]

    # Create site string url for selected item
    site = "https://www.eaze.com/groups/" + section

    # Get the selected item url
    driver.get(site)

    time.sleep(1)

    # Get the order number from the intent dictionary
    shop_by_selection = intent["name"]

    menu_elms = driver.find_element_by_xpath("//div[2]/div/div[2]")

    # I have this info already
    menu_items = menu_elms.find_elements_by_xpath("./div[2]/div")
    num_menu_items = len(menu_items)

    # Get Menu Type Items
    menu_types = menu_elms.find_element_by_xpath("./div[1]/div/div[1]")
    type_title = menu_types.find_element_by_xpath("./div[1]").text
    type_items = menu_types.find_elements_by_xpath("./div[2]/button")

    if shop_by_selection == "shop_by_type":

        type_items_list = []
        counter = 1
        for item in type_items:
            type_items_list.append(item.text.strip())

            if counter == 1:
                say_types = item.text
            elif counter < len(type_items):
                say_types += ", " + item.text
            else:
                say_types += ", " + ", " + item.text + "."

            counter += 1

        speech_output = say_types

    elif shop_by_selection == "shop_by_brand":
        # Get Menu Brands
        menu_brands = menu_elms.find_element_by_xpath("./div[1]/div/div[2]/div[1]")
        brand_items = menu_elms.find_elements_by_xpath("./div[1]/div/div[2]/div[2]")
        brand_items = brand_items[0].text
        brand_items = brand_items.split('\n')

        menu_brands_list = []
        counter = 1

        for item in brand_items:
            print("an item", item)
            the_item = item
            menu_brands_list.append(the_item)

            if counter == 1:
                say_brands = the_item
            elif counter < len(brand_items):
                say_brands += ", " + the_item
            else:
                say_brands += " " + the_item + "."

            counter += 1

        speech_output = say_brands

    elif shop_by_selection == "shop_all":

        section_items = menu_elms.find_element_by_xpath('./div[2]')
        section_items = section_items.find_elements_by_xpath("./div[contains(@class, 'css-1s0dkrt e17jdd020')]")

        menu_num = 1
        short_menu = ""
        item_list = []
        name_price_dict = {}
        img_dict = {}

        p = 0
        for item in section_items:
            item_price = item.find_element_by_xpath('./div/div/div[2]/div[1]')
            item_price = item_price.text

            # Get the name of the item
            item_name = item.find_element_by_xpath('./div/div/div[2]/div[2]')
            item_name = item_name.text

            # Get the item url
            item_url = item.find_element_by_xpath('./div/div/div[1]/div[1]/img')
            item_url = item_url.get_attribute("src")

            name_price_dict[menu_num] = (item_name, item_price)

            # Creates abbreviated menu so alexa doesnt have to repeat the entire menu
            if p < 7:
                short_menu += str(menu_num) + ". " + item_name + ", "
                json_list_item = lij.json_display(item_url, item_name, item_price)
                img_dict[item_name] = (item_url, item_price)
                item_list.append(json_list_item)

            # Incrament variables
            menu_num += 1
            p += 1

            # Add the following pharse before the loop ends
            if p == len(section_items):

                short_menu += "Say Repeat if you were too high the first time"

                if p > 7:
                    short_menu += ", or Say More to hear the rest of the menu."

                else:
                    short_menu += "."

        # print(section_items.get_attribute('class'))
        speech_output = short_menu

    driver.close()

    session_attributes["json_list_items_dict"] = item_list
    session_attributes["last_func"] = "section_page"
    session_attributes["name_price_dict"] = name_price_dict
    session_attributes["img_dict"] = img_dict

    card_title = "Test"

    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, display_build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session, session_attributes))


def shop_by(intent, session):
    # Get the order number from the intent dictionary
    orderNum = intent["slots"]["number"]["value"]

    # Get menu from the "session" dictionary
    session_attributes = session['attributes']
    last_func = session_attributes["last_func"]

    if last_func == "eaze_up":
        h2_mm_item_button_dict = session_attributes["h2_mm_item_button_dict"]
        item_tuple = h2_mm_item_button_dict[orderNum]

        section = item_tuple[0]
        num_cat_items = item_tuple[1]

        # Add orderNum value session_attributes
        session_attributes["orderNum"] = orderNum
        session_attributes["last_func"] = "shop_by"

        card_title = "Test"
        speech_output = "There are " + str(num_cat_items) + " items in the " + \
                        section + " section. Would you like to shop by type, category or shop all?"

    elif last_func == 'section_page':
        name_price_dict = session_attributes["name_price_dict"]
        name_price_tuple = name_price_dict[orderNum]

        item_name = name_price_tuple[0]
        item_price = name_price_tuple[1]

        cart_list = session_attributes["cart_list"]
        cart_list.append(name_price_tuple)
        session_attributes["cart_list"] = cart_list

        item_json = []
        for item_tuple in cart_list:
            item_name = item_tuple[0]

            img_tuple = session_attributes["img_dict"][item_name]
            item_url = img_tuple[0]
            item_price = img_tuple[1]

            json_list_item = lij.json_display(item_url, item_name, item_price)
            item_json.append(json_list_item)

        session_attributes["json_list_items_dict"] = item_json
        card_title = "Test"
        speech_output = item_name + " was added to your cart. Order another item to continue shopping or say checkout?"

    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, display_build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session, session_attributes))


def eaze_up(intent, session):
    session_attributes = session["attributes"]

    # Initiate driver and go to eaze site
    driver = webdriver.Chrome(chrome_options=chrome_options)
    site = "https://www.eaze.com/menu"
    driver.get(site)

    # Intiate menu variables
    menu = ""
    title_menu = ""
    short_menu = ""

    time.sleep(1)

    # Get all h2 elements, which represent the items on the menu
    h2_menu_items = driver.find_elements(By.TAG_NAME, 'h2')

    # Initate variables used in the following loop
    h2_mm_item_dict = {}
    menu_num = 1
    p = 0
    item_list = []
    h2_mm_item_button_dict = {}

    # Loop through each item in the menu_items
    for item in h2_menu_items:

        # Add h2 menu item items to the h2_mm_item_button_dict, use menu num as key variable
        h2_mm_item_button_dict[menu_num] = nf.getAll_Buttons(item)

        # Add menu item text to the h2_mm_item_dict, use menu num as key variable
        h2_mm_item_dict[menu_num] = item.text

        menu += str(menu_num) + " " + item.text + " "

        # Create abbreviated menu for the title
        if p < 4:
            title_menu += str(menu_num) + ". " + item.text + ", "

        # Creates abbreviated menu so alexa doesnt have to repeat the entir menu
        if p < 7:
            short_menu += str(menu_num) + ". " + item.text + ", "

        # Incrament variables
        menu_num += 1
        p += 1

        # Add the following pharse before the loop ends
        if p == len(h2_menu_items):
            short_menu += "Say Repeat if you were too high the first time, \
            or Say More to hear the rest of the menu."

    # Add menu_dict to the session_attributes, key value "menu"
    session_attributes["last_func"] = "eaze_up"
    session_attributes["h2_mm_item_dict"] = h2_mm_item_dict
    session_attributes["h2_mm_item_button_dict"] = h2_mm_item_button_dict
    session_attributes["json_list_items_dict"] = item_list

    driver.close()

    card_title = title_menu
    speech_output = short_menu
    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_test_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "Test"
    speech_output = "This is a test message"
    reprompt_text = "You never responded to the first test message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {"recent": "welcome", "cart_list": []}
    card_title = "Welcome"
    speech_output = "Bet! Let's match, who should we pick up from?"

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hello... who should we pick up from?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    print("intent", intent)

    # Dispatch to your skill's intent handlers
    if intent_name == "test":
        return get_test_response()
    elif intent_name == "orderNumber":
        return shop_by(intent, session)
    elif intent_name == "eaze":
        return eaze_up(intent, session)
    elif (intent_name == "shop_by_type") | (intent_name == "shop_by_band") | (intent_name == "shop_all"):
        return section_page(intent, session)
    elif intent_name == "checkout":
        return checkout(intent, session)
    elif intent_name == "confirm":
        return send_receipt(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
