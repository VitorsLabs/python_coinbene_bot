#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bot as bot

print('UDST vs. BRL')
print('BOT BY vitorgamer58')
print(bot.get_ticker('USDTBRL'))


# In[2]:


USDTBRL = bot.get_ticker('USDTBRL')

lastPrice = float(USDTBRL['last'])
print(lastPrice)

while lastPrice > 4.00:
    print('Não compre')
    lastPrice = lastPrice - 0.10
else:
    print('compre')


# In[3]:


print(bot.get_orderbook('USDTBRL'))


# In[2]:


bot.limit_order('sell', '1', '4.01', 'BTCUSDT')


# In[2]:


bot.get_balance()


# In[10]:





# In[ ]:




