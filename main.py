def min_coins(coins, target_amount):
    arr=[float('inf')] *(target_amount+1)
    arr[0]=0
    for amount in range (1, target_amount+1):
        for coin in coins:
            if amount-coin>=0:
                arr[amount]=min(arr[amount],arr[amount-coin]+1)
    return arr[target_amount]
# coins = [1, 4, 6, 9, 14]
# target_amount = 26
# print(min_coins(coins, target_amount))
    
    


    

