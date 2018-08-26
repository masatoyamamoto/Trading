mainURL = "https://www.k-zone.co.jp"

loginPath = "/td/users/login"
PositionHoldPath = "/td/dashboards/position_hold"
orderPath = "/td/orders"
dashboardsPath = "/td/dashboards"
suggestPath = ("/td/quotes/query?query=&exch=&"
               "jsec=&command=spot_buy&idx1=&lospl=&losph=&mkcpl=&"
               "mkcph=&cpbrl=&cpbrh=&cperl=&cperh=&suggest=2&"
               "safety=true&sort_rank1=quote_code+asc")

defaultSearchVariables = {
    "traded": False,  # True / False
    "command": "",  # "spot_buy" / "build_long" / "build_short"
    "idx1": None,  # None / True / False
    "minUnitPrice": None,  # None / digits
    "maxUnitPrice": None,  # None / digits
    "minmkcp": None,  # None / digits
    "maxmkcp": None,  # None / digits
    "minPBR": None,  # None / digits
    "maxPBR": None,  # None / digits
    "minPER": None,  # None / digits
    "maxPER": None,  # None / digits
    "suggest": 0,  # -2 / -1 / 0 / 1 / 2
    "safery": False,  # True / False
}
