class job_data:
    USERNAME = "d.samyu2626@gmail.com"
    PASSWORD = "ammu2006"
    CHROMEDRIVER_PATH = r"C:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    List_comp = ["ABB","ABCAPITAL","ABFRL","ACC","ADANIENT","ADANIENSOL","ADANIGREEN","ADANIPORTS","ADANIPOWER","ALKEM","AMBUJACEM"
                 ,"APOLLOHOSP","APOLLOTYRE","APLAPOLLO","ASHOKLEY","ASIANPAINT","ASTRAL","ATGL","AUROPHARMA","AUBANK","AXISBANK",
                 "BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE","BAJAJHFL","BAJAJHLDNG","BANDHANBNK","BANKBARODA","BANKINDIA","BDL","BEL",
                 "BHARATFORG","BHARTIARTL","BHARTIHEXA","BHEL","BIOCON","BOSCHLTD","BPCL","BRITANNIA","BSE","CANBK","CGPOWER","CHOLAFIN",
                 "CIPLA","COALINDIA","COCHINSHIP","COLPAL","CONCOR","COFORGE","CUMMINSIND","DABUR","DIVISLAB","DLF","DIXON","DMART","DRREDDY",
                 "EICHERMOT","ESCORTS","EXIDEIND","FEDERALBNK","GAIL","GLENMARK","GMRAIRPORT","GODREJCP","GODREJPROP","GRASIM",
                 "HAVELLS","HCLTECH","HDFCAMC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","HINDZINC","HAL","HUDCO","HYUNDAI",
                 "ICICIBANK","ICICIGI","ICICIPRULI","IDFCFIRSTB","IGL","INDHOTEL","INDIANB","INDIGO","INDUSINDBK","INDUSTOWER","INFY","IOC","IREDA","IRB",
                 "IRCTC","IRFC","ITC","JINDALSTEL","JIOFIN","JUBLFOOD","JSWENERGY","JSWSTEEL","KALYANKJIL","KOTAKBANK","KPITTECH","LICHSGFIN","LICI"
                 ,"LODHA","LT","LTIM","LTF","LUPIN","M&MFIN","M&M","MANKIND","MARICO","MARUTI","MAXHEALTH","MAHABANK","MAZDOCK","MFSL","M&MFIN","MOTHERSON"
                 ,"MOTILALOFS","MPHASIS","MRF","MUTHOOTFIN","NAUKRI","NATIONALUM","NESTLEIND","NHPC","NMDC","NTPC","NTPCGREEN","NYKAA","OBEROIRLTY","OFSS",
                 "OIL","OLAELEC","ONGC","PAGEIND","PATANJALI","PAYTM","PERSISTENT","PETRONET","PFC","PHOENIXLTD","PIDILITIND","PIIND","PNB","POLICYBZR","POLYCAB",
                 "POWERGRID","PREMIERENE","PRESTIGE","RECLTD","RELIANCE","RVNL","SAIL","SBICARD","SBILIFE","SBIN","SHREECEM","SHRIRAMFIN","SIEMENS","SJVN",
                 "SOLARINDS","SONACOMS","SRF","SUZLON","SUPREMEIND","SWIGGY","SUNPHARMA","TATACOMM","TATACONSUM","TATAELXSI","TATAMOTORS","TATAPOWER","TATASTEEL",
                 "TATATECH","TCS","TECHM","TIINDIA","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","ULTRACEMCO","UNIONBANK","UNITDSPR","UPL","VBL","VEDL","VMM",
                 "VOLTAS","WAAREEENER","WIPRO","YESBANK","ETERNAL","ZYDUSLIFE"]
    
    parameters = {
    "Annual P&L": {
        "Recent": [
            "Sales", "OPM", "Profit after tax", "Return on capital employed", "EPS", "Change in promoter holding",
            "Operating profit", "Interest", "Depreciation", "EBIT", "Net profit", "Current Tax", "Tax",
            "Other income", "Last annual result date", "Sales last year", "Operating profit last year", "Other income last year",
            "EBIDT last year", "Depreciation last year", "EBIT last year", "Interest last year", "Profit before tax last year",
            "Tax last year", "Profit after tax last year", "Extraordinary items last year", "Net Profit last year",
            "Dividend last year", "Material cost last year", "Employee cost last year", "OPM last year",
            "NPM last year", "EPS last year"
        ],
        "Preceding": [
            "Sales preceding year", "Operating profit preceding year", "Other income preceding year",
            "EBIDT preceding year", "Depreciation preceding year", "EBIT preceding year", "Interest preceding year",
            "Profit before tax preceding year", "Tax preceding year", "Profit after tax preceding year",
            "Extraordinary items preceding year", "Net Profit preceding year", "Dividend preceding year",
            "OPM preceding year", "NPM preceding year", "EPS preceding year", "Sales preceding 12months",
            "Net profit preceding 12months"
        ],
        "Historical": [
            "Sales growth 3Years", "Sales growth 5Years", "Profit growth 3Years", "Profit growth 5Years",
            "Sales growth 10years median", "Sales growth 5years median", "Sales growth 7Years", "Sales growth 10Years",
            "EBIDT growth 3Years", "EBIDT growth 5Years", "EBIDT growth 7Years", "EBIDT growth 10Years",
            "EPS growth 3Years", "EPS growth 5Years", "EPS growth 7Years", "EPS growth 10Years",
            "Profit growth 7Years", "Profit growth 10Years", "Change in promoter holding 3Years",
            "Average Earnings 5Year", "Average Earnings 10Year", "Average EBIT 5Year", "Average EBIT 10Year"
        ]
    },

    "Quarter P&L": {
        "Recent": [
            "Sales latest quarter", "Profit after tax latest quarter", "YOY Quarterly sales growth", "YOY Quarterly profit growth",
            "Sales growth", "Profit growth", "Operating profit latest quarter", "Other income latest quarter",
            "EBIDT latest quarter", "Depreciation latest quarter", "EBIT latest quarter", "Interest latest quarter",
            "Profit before tax latest quarter", "Tax latest quarter", "Extraordinary items latest quarter", "Net Profit latest quarter",
            "GPM latest quarter", "OPM latest quarter", "NPM latest quarter", "Equity Capital latest quarter", "EPS latest quarter",
            "Operating profit 2quarters back", "Operating profit 3quarters back", "Sales 2quarters back",
            "Sales 3quarters back", "Net profit 2quarters back", "Net profit 3quarters back", "Operating profit growth",
            "Last result date", "Expected quarterly sales growth", "Expected quarterly sales",
            "Expected quarterly operating profit", "Expected quarterly net profit", "Expected quarterly EPS"
        ],
        "Preceding": [
            "Sales preceding quarter", "Operating profit preceding quarter", "Other income preceding quarter",
            "EBIDT preceding quarter", "Depreciation preceding quarter", "EBIT preceding quarter", "Interest preceding quarter",
            "Profit before tax preceding quarter", "Tax preceding quarter", "Profit after tax preceding quarter",
            "Extraordinary items preceding quarter", "Net Profit preceding quarter", "OPM preceding quarter",
            "NPM preceding quarter", "Equity Capital preceding quarter", "EPS preceding quarter"
        ],
        "Historical": [
            "Sales preceding year quarter", "Operating profit preceding year quarter", "Other income preceding year quarter",
            "EBIDT preceding year quarter", "Depreciation preceding year quarter", "EBIT preceding year quarter",
            "Interest preceding year quarter", "Profit before tax preceding year quarter", "Tax preceding year quarter",
            "Profit after tax preceding year quarter", "Extraordinary items preceding year quarter",
            "Net Profit preceding year quarter", "OPM preceding year quarter", "NPM preceding year quarter",
            "Equity Capital preceding year quarter", "EPS preceding year quarter"
        ]
    },

    "Balance Sheet": {
        "Recent": [
            "Debt", "Equity capital", "Preference capital", "Reserves", "Secured loan", "Unsecured loan",
            "Balance sheet total", "Gross block", "Revaluation reserve", "Accumulated depreciation", "Net block",
            "Capital work in progress", "Investments", "Current assets", "Current liabilities",
            "Book value of unquoted investments", "Market value of quoted investments", "Contingent liabilities",
            "Total Assets", "Working capital", "Lease liabilities", "Inventory", "Trade receivables", "Face value",
            "Cash Equivalents", "Advance from Customers", "Trade Payables"
        ],
        "Preceding": [
            "Number of equity shares preceding year", "Debt preceding year", "Working capital preceding year",
            "Net block preceding year", "Gross block preceding year", "Capital work in progress preceding year"
        ],
        "Historical": [
            "Working capital 3Years back", "Working capital 5Years back", "Working capital 7Years back",
            "Working capital 10Years back", "Debt 3Years back", "Debt 5Years back", "Debt 7Years back",
            "Debt 10Years back", "Net block 3Years back", "Net block 5Years back", "Net block 7Years back"
        ]
    }
    }
