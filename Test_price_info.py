import price_info

price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}

def test_total_cost_shopping():
    expectedtotalcost = 5 * 1.20 + 5 * 1.40 + 1 * 6.50 + 2 * 2.70 + 10 * 0.90 + 1 * 2.95 + 2 * 4.95
    assert(expectedtotalcost == price_info.total_cost_shopping())

def test_cost_of_fruits():
    costofapples = 10 * 1.20
    assert(price_info.cost_of_fruits('apple', 10) == costofapples)
