#trend following: buying/selling when price changes by 10% in 2 hours

currentPosition = 0

profitExitPercent = 0.2 #expected profit threshold, if position is more profitable than threshold, we flatten the position

lossExitPercent = -0.1 #maximum loss threshold, if a position is losing more than this threshold, we flatten the position

#first check if we are flat and prices moved up by 10% - entry signal to go long and send buy order

def onMarketPriceChange(currentPrice, currentTime):
    if currentPosition == 0 and (currentPrice - priceTwoHoursAgo) / currentPrice > 0.1:
        sendBuyOrderAtCurrentPrice()
        currentPosition += 1
    
    elif currentPosition == 0 and (currentPrice - priceTwoHoursAgo) / currentPrice < 0.1:
        sendSellOrderAtCurrentPrice()
        currentPosition -= 1

    # if currently long and market moves in favourable direction, check whether this positions profitability exceeds threshold to flatten our position
    if currentPosition > 0 and currentPrice - positionPrice > profitExitPercent:
        sendSellOrderAtCurrentPrice()
        currentPosition -= 1
    
    # if currently long and market moves against us (price falls), check if loss exceeds thresholds to flatten our position

    if currentPosition > 0 and currentPrice - positionPrice < lossExitPercent:
        sendSellOrderAtCurrentPrice()
        currentPosition -= 1

    # if currently short and market moves favourably (prices fall), check if position profitability exceeds threshold and flatten our position

    if currentPosition < 0 and positionPrice - currentPrice > profitExitPercent:
        sendBuyOrderAtCurrentPrice()
        currentPosition += 1
   
   # if currently short and market moves against us (price increases), check if loss exceeds thresholds to flatten our position
    if currentPosition < 0 and positionPrice - currentPrice < lossExitPercent:
        sendBuyOrderAtCurrentPrice()
        currentPosition += 1

    


