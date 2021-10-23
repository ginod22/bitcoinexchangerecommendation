Questionnaire

1 - Sub-optimal choices taken in the implementation:

To got instantaneous updates, you have to refresh the page.
Design is not the best, though it could be worked on.

2 - Over designed:

Everything is simple and optimized, and nothing has been over designed.

3 - Scaling to 100 users/second

Instead of calling for the prices of each exchange per request, we can create a database stored on the cloud which will update the prices every few seconds. 
This will reduce the number of calls to the prices from 100/second to a 1 every few seconds.

4 - Things that I could have optimized:

Backend:
+ Adding the values to a database stored on the cloud (like AWS), and update the values in the database instead of calling the values directly through the backend

Frontend:
+ Created a more interactive website (maybe users can see historical data, get a link to the exchanges, etc...)
+ Refresh the prices automatically instead of having to click on the refresh button

Other ideas:
+ Giving the user a chance to link their Coinbase and Kraken account to be able to buy directly from the website
+ Giving the user the option to look up other kinds of cryptocurrencies
+ Giving the user the option to change currencies
+ Giving the user trading advice or selling them a course and earn a commission
+ Adding other exchanges (possibly even partnering with some of them)
