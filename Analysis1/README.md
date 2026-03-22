Economic analyses of markets are commonplace, but frequently constrained to markets with immediate practical applications.
However, video games such as Hypixel's Skyblock (which is a open-world RPG programmed inside of Minecraft), often offer advanced economies with unusual governmental policies, economic systems, and social cultures.
As a result, we've elected to study the a subset of the economy of Hypixel Skyblock.

In particular, we observed the stock of eight in-game items and analyzed their behavior in several ways.
The item names are in the following table.
We used a line-plot, an inter-item correlation, lag-price correlation, and a volatility metric.

| Item name            | Item ID              |
|----------------------|----------------------|
| Diamond              | DIAMOND              |
| Redstone             | REDSTONE             |
| Magical Mushroom Soup | MAGIC_MUSHROOM_SOUP |
| Vial of Venom        | VIAL_OF_VENOM        |
| Salt Cube            | SALT_CUBE            |
| Diamonite            | DIAMONITE            |
| Wither Essence       | ESSENCE_WITHER       |
| Crimson Essence      | ESSENCE_CRIMSON      |

# Item Stock Behavior

Eight items were tested.
We analyzed the behavior of the returns over time, quantized to one-hour blocks.
The items exhibit a timeseries plot that visually appears consistent with the random behavior of Brownian motion, which may be worth studying.

![Timeseries](figures/timeseries.png)

| Item | Mean Price | Std | CV | Min | Max | N |
|------|------------|-----|----|-----|-----|---|
| Diamond | 9.44 | 3.14 | 0.3320 | 5.50 | 26.20 | 181 |
| Diamonite | 2620790.54 | 369648.80 | 0.1410 | 1499999.80 | 4999999.70 | 180 |
| Crimson Essence | 1257.27 | 155.32 | 0.1235 | 982.20 | 1742.50 | 181 |
| Wither Essence | 2858.64 | 220.34 | 0.0771 | 2274.80 | 3698.20 | 181 |
| Magical Mushroom Soup | 1592.08 | 1309.32 | 0.8224 | 169.00 | 8073.90 | 178 |
| Redstone | 6.78 | 3.68 | 0.5428 | 2.00 | 39.90 | 179 |
| Salt Cube | 107940.93 | 150386.84 | 1.3932 | 949.90 | 649999.80 | 164 |
| Vial of Venom | 3399032.62 | 1114057.26 | 0.3278 | 1412265.80 | 8999997.50 | 181 |

# Inter-Item Correlations

There exists no statistically significant correlation between any two nonsame items.
That is, of the items tested, for any items i and j, where i and j are not the same item, there is no correlation between the price of i and the price of j.
Knowing the price of one gives no information about the price of another.

![Correlation Heatmap](figures/heatmap.png)

# Autocorrelation using Lag-Prices

Diamond and Crimson Essence are the only items to have a statistically significant correlation between price and lag-price, and this correlation occurs between the current price and the price from one hour ago.
In my experience, these are also some of the most intensely traded items, with a significant trade market due to players speculating on prices in order to profit.
As a result, I hypothesize that the one-hour significant lag relation may be caused by speculators attempting to predict future price based on current price, and thus causing a relation to exist.

![Correlation Heatmap](figures/autocorrelation.png)

From a (somewhat) practical perspective, this implies that a profitable strategy could be created using pure Bazaar trading.
More particularly, the evidence suggests that the Bazaar may not be weak-form efficient for these items, and a simple momentum strategy may be capable of yielding positive returns.

# Volatility

The market is very volatile, but the volatility varies.
Some items are more volatile than others.
The lowest volatilities were the Salt Cube and the Magical Mushroom Soup, with volatilities of roughly 5.57 and 5.89, respectively.
Meanwhile, the highest volatility is Crimson Essence, whose volatility is about 352.53.
This means that the Crimson Essence item's noise is over 350 times larger than the signal, whereas the Salt Cube item's noise is merely 5 times larger than signal.

A comparison may be drawn:

Salt Cubes and Magical Mushroom Soups may be considered stable investments, akin to buying stock in utilities.
While they may vary heavily, they still vary minimally compared to other investments, and thus are far better than other investments.
We expect them not to dip too heavily, at the expense of also not rising enough to be a viable speculation.

Meanwhile, Crimson Essence is so incredibly volatile that it's value can not reliably be estimated without a very large sample size.
It is extremely liable to jump around.
It may be useful for speculation, as it can sometimes increase in value dramatically, but it can decrease as readily as it can increase, making it an unreliable investment.

| Item | Volatility |
|------|------------|
| Diamond | 37.205532 |
| Diamonite | 10.758417 |
| Crimson Essence | 4.239828 |
| Wither Essence | 4.052143 |
| Magical Mushroom Soup | 94.032288 |
| Redstone | 65.777288 |
| Salt Cube | 203.812004 |
| Vial of Venom | 20.957374 |

# Future Steps

We are currently interested in analyzing a subset of the S&P 500 in a similar way.
Comparing Hypixel Skyblock to the S&P 500 will inform us of the sophistication of gamers, and possibly also give us an idea of what strategies they may be using.

