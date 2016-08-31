def init(context):
    context.stocks = ['中证500']
    update_universe(context.stocks)

def handle_bar(context, bar_dict):
    #stocknum = 50
    his = history(10, '1d', 'close')['000001.XSHG']
    
    #print(his)
    
    if his[9] / his[8] <  0.97:
        if len(context.portfolio.positions) > 0:
            for stock in context.portfolio.positions.keys():
                order_target_percent(stock, 0)
        return

    for stock in context.stocks:
        #求出持有该股票的仓位，买入没有持仓并符合条件股票
        position = context.portfolio.positions[stock].quantity
        print(stock)
        #print(position)
        if position < 50:
            High = history(3, '1d', 'high')[stock]
            Low = history(3, '1d', 'low')[stock]

            Close = history(3, '1d', 'close')[stock]
            Open = history(3, '1d', 'open')[stock]
            
            #logger.info(High)
    
            HH = max(High[:2])
            LC = min(Close[:2])

            HH = HH - LC  #当前最高-当前最低

            HC = max(Close[:2])
            LL = min(Low[:2])

            HC = HC - LL

            if HH > 0.8:
                order_target_percent(stock, 1)

    # Sell
    for stock in context.portfolio.positions.keys():
        hist = history(3, '1m', 'close')[stock]
        case1 = (hist[2] - hist[0]) >= 0.8
        case2 = (hist[1] - hist[0]) >= 0.55
        if case1 or case2:
            order_target_percent(stock, 0)
