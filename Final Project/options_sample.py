{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy.stats import norm, binom\n",
    "from typing import Callable\n",
    "\n",
    "\n",
    "## Payoff functions\n",
    "def call_payoff(spot, strike):\n",
    "    return np.maximum(spot - strike, 0.0)\n",
    "\n",
    "def put_payoff(spot, strike):\n",
    "    return np.maximum(strike - spot, 0.0)\n",
    "\n",
    "\n",
    "## Pricing functions\n",
    "def european_binomial_pricer(spot: float, strike: float, expiry: float, rate: float, div: float, vol: float, num: int, payoff: Callable) -> float:\n",
    "    pass\n",
    "\n",
    "def american_binomial_pricer(spot: float, strike: float, expiry: float, rate: float, div: float, vol: float, num: int, payoff: Callable) -> float:\n",
    "    pass \n",
    "\n",
    "def black_scholes_call(spot: float, strike: float, expiry: float, rate: float, div: float, vol: float) -> float:\n",
    "    d1 = (np.log(spot/strike) + (rate - div + 0.5 * vol * vol) * expiry) / (vol * np.sqrt(expiry))\n",
    "    d2 = d1 - vol * np.sqrt(expiry) \n",
    "    return (spot * np.exp(-div * expiry) * norm.cdf(d1)) - (strike * np.exp(-rate * expiry) * norm.cdf(d2))\n",
    "\n",
    "def black_scholes_put(spot: float, strike: float, expiry: float, rate: float, div: float, vol: float) -> float:\n",
    "    d1 = (np.log(spot/strike) + (rate - div + 0.5 * vol * vol) * expiry) / (vol * np.sqrt(expiry))\n",
    "    d2 = d1 - vol * np.sqrt(expiry) \n",
    "    return (strike * np.exp(-rate * expiry) * norm.cdf(-d2)) - (spot * np.exp(-div * expiry) * norm.cdf(-d1))\n",
    "\n",
    "\n",
    "## Delta\n",
    "def black_scholes_call_delta(spot: float, strike: float, tau: float, rate: float, div: float, vol: float) -> float:\n",
    "    d1 = (np.log(spot/strike) + (rate - div + 0.5 * vol * vol) * tau) / (vol * np.sqrt(tau))\n",
    "    return np.exp(-div * tau) * norm.cdf(d1)\n",
    "\n",
    "\n",
    "## Simulations\n",
    "def binomial_path(spot: float, expiry: float, rate: float, div: float, vol: float, num: int) -> np.ndarray:\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
