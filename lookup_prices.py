#!/usr/bin/env python

"""This script demonstrates how the amazonproduct API can be used to look up
the price of an item.

"""
import time

import amazonproduct

api = amazonproduct.API(locale='us')

def lookup_item(keywords):
    try:
        items = api.item_search('All', ResponseGroup='OfferSummary, Small', Keywords=keywords)

        # we'll assume it's the first - not much more we can do in an automated fashion
        for item in items:
            asin = item.ASIN
            title = item.ItemAttributes.Title
            offerSummary = item.OfferSummary
            try:
                lowestNewPrice = offerSummary.LowestNewPrice.FormattedPrice
            except:
                lowestNewPrice = None

            try:
                lowestUsedPrice = offerSummary.LowestUsedPrice.FormattedPrice
            except:
                lowestUsedPrice = None
            #import pdb; pdb.set_trace()
            return title.text.encode('utf-8'), asin, lowestNewPrice, lowestUsedPrice
    except:
        pass    
    return '', '', '', ''

amazon_url = "http://www.amazon.com/dp/%s"