{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b97d4a68",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c1790369",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "myarray = np.array(a)\n",
    "mask = myarray <0\n",
    "a[mask]\n",
    "len(a[mask])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 155,
   "id": "5bc3b342",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5"
      ]
     },
     "execution_count": 155,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mask = myarray >(0)\n",
    "a[mask]\n",
    "len(a[mask])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "e6b9d9be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mask = (myarray %2==0)& (myarray >=2)\n",
    "myarray[mask]\n",
    "len(myarray[mask])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "a8fa5c3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 132,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "moreray = myarray+3\n",
    "mask = moreray >0\n",
    "\n",
    "len(moreray[mask])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "f7960bd6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(144.0243035046516, 74.0)"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hellray = myarray**2\n",
    "np.std(hellray),np.mean(hellray)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "91dde9f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[  1.   7.   9.  20.  -5.  -4.  -3.  -3.  -3.  -9.   0. -10.]\n",
      "0.0\n"
     ]
    }
   ],
   "source": [
    "center_function = lambda x: x - x.mean()\n",
    "data_centered = center_function(a)\n",
    "print(data_centered)\n",
    "print(data_centered.mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "4cb322bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.11875421719907088, 0.8312795203934962, 1.068787954791638, 2.3750843439814178, -0.5937710859953544, -0.4750168687962835, -0.35626265159721265, -0.35626265159721265, -0.35626265159721265, -1.068787954791638, 0.0, -1.1875421719907089]\n"
     ]
    }
   ],
   "source": [
    "mean = sum(myarray) / len(myarray)\n",
    "differences = [(value - mean)**2 for value in myarray]\n",
    "sum_of_differences = sum(differences)\n",
    "standard_deviation = (sum_of_differences / (len(myarray) - 1)) ** 0.5\n",
    "zscores = [(value - mean) / standard_deviation for value in myarray]\n",
    "print(zscores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "04e8de9a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "# Life w/o numpy to life with numpy\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "59c3b2f2",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10])"
      ]
     },
     "execution_count": 166,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Setup 1\n",
    "n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
    "a= np.array(n)\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "713734d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "55"
      ]
     },
     "execution_count": 167,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use python's built in functionality/operators to determine the following:\n",
    "# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list\n",
    "sum(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "f3ecee12",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 168,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list\n",
    "min(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "df588db5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10"
      ]
     },
     "execution_count": 169,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list\n",
    "max(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 171,
   "id": "c4c84b3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 171,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list\n",
    "sum(a)/len(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 173,
   "id": "2edf86a1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3628800"
      ]
     },
     "execution_count": 173,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together\n",
    "total=1\n",
    "for x in a:\n",
    "    total *= x\n",
    "total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "id": "341b73a2",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'numpy.int64' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [215]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m squares_of_a \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m row \u001b[38;5;129;01min\u001b[39;00m a:\n\u001b[0;32m----> 4\u001b[0m     \u001b[38;5;28;01mfor\u001b[39;00m number \u001b[38;5;129;01min\u001b[39;00m row:\n\u001b[1;32m      5\u001b[0m         squares_of_a\u001b[38;5;241m.\u001b[39mappend(number\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m2\u001b[39m)\n\u001b[1;32m      6\u001b[0m squares_of_a\n",
      "\u001b[0;31mTypeError\u001b[0m: 'numpy.int64' object is not iterable"
     ]
    }
   ],
   "source": [
    "# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]\n",
    "squares_of_a = []\n",
    "for row in a:\n",
    "    for number in row:\n",
    "        squares_of_a.append(number**2)\n",
    "squares_of_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 216,
   "id": "1d0b0b6c",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'numpy.int64' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [216]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m odds_in_a \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m row \u001b[38;5;129;01min\u001b[39;00m a:\n\u001b[0;32m----> 4\u001b[0m     \u001b[38;5;28;01mfor\u001b[39;00m number \u001b[38;5;129;01min\u001b[39;00m row:\n\u001b[1;32m      5\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m(number \u001b[38;5;241m%\u001b[39m \u001b[38;5;241m2\u001b[39m \u001b[38;5;241m!=\u001b[39m \u001b[38;5;241m0\u001b[39m):\n\u001b[1;32m      6\u001b[0m             odds_in_a\u001b[38;5;241m.\u001b[39mappend(number)\n",
      "\u001b[0;31mTypeError\u001b[0m: 'numpy.int64' object is not iterable"
     ]
    }
   ],
   "source": [
    "# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers\n",
    "odds_in_a = []\n",
    "for row in a:\n",
    "    for number in row:\n",
    "        if(number % 2 != 0):\n",
    "            odds_in_a.append(number)\n",
    "odds_in_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "id": "b310b5aa",
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'numpy.int64' object is not iterable",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[0;32mIn [217]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m evens_in_a \u001b[38;5;241m=\u001b[39m []\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m row \u001b[38;5;129;01min\u001b[39;00m a:\n\u001b[0;32m----> 4\u001b[0m     \u001b[38;5;28;01mfor\u001b[39;00m number \u001b[38;5;129;01min\u001b[39;00m row:\n\u001b[1;32m      5\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m(number \u001b[38;5;241m%\u001b[39m \u001b[38;5;241m2\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m0\u001b[39m):\n\u001b[1;32m      6\u001b[0m             evens_in_a\u001b[38;5;241m.\u001b[39mappend(number)\n",
      "\u001b[0;31mTypeError\u001b[0m: 'numpy.int64' object is not iterable"
     ]
    }
   ],
   "source": [
    "# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.\n",
    "evens_in_a = []\n",
    "for row in a:\n",
    "    for number in row:\n",
    "        if(number % 2 == 0):\n",
    "            evens_in_a.append(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 175,
   "id": "3d7b1603",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 4, 5],\n",
       "       [6, 7, 8]])"
      ]
     },
     "execution_count": 175,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...\n",
    "## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.\n",
    "b = [\n",
    "    [3, 4, 5],\n",
    "    [6, 7, 8]\n",
    "]\n",
    "b = np.array(b)\n",
    "b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "671543d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "33"
      ]
     },
     "execution_count": 176,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the \"b\" variable is a numpy array**\n",
    "sum_of_b = 0\n",
    "for row in b:\n",
    "    sum_of_b += sum(row)\n",
    "np.sum(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 177,
   "id": "1fee575b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 177,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 2 - refactor the following to use numpy. \n",
    "min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  \n",
    "np.min(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "426dc29e",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.\n",
    "max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])\n",
    "\n",
    "np.max(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "id": "36a89b49",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.5"
      ]
     },
     "execution_count": 203,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 4 - refactor the following using numpy to find the mean of b\n",
    "mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))\n",
    "\n",
    "mean_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "id": "05014c76",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "20160"
      ]
     },
     "execution_count": 202,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.\n",
    "product_of_b = 1\n",
    "for row in b:\n",
    "    for number in row:\n",
    "        product_of_b *= number\n",
    "\n",
    "product_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "id": "6c91e5b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[9, 16, 25, 36, 49, 64]"
      ]
     },
     "execution_count": 201,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 6 - refactor the following to use numpy to find the list of squares \n",
    "squares_of_b = []\n",
    "for row in b:\n",
    "    for number in row:\n",
    "        squares_of_b.append(number**2)\n",
    "\n",
    "\n",
    "squares_of_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 200,
   "id": "d0ea4001",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 5, 7]"
      ]
     },
     "execution_count": 200,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 7 - refactor using numpy to determine the odds_in_b\n",
    "odds_in_b = []\n",
    "for row in b:\n",
    "    for number in row:\n",
    "        if(number % 2 != 0):\n",
    "            odds_in_b.append(number)\n",
    "\n",
    "\n",
    "odds_in_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 199,
   "id": "a3379f2d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4, 6, 8]"
      ]
     },
     "execution_count": 199,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 8 - refactor the following to use numpy to filter only the even numbers\n",
    "evens_in_b = []\n",
    "for row in b:\n",
    "    for number in row:\n",
    "        if(number % 2 == 0):\n",
    "            evens_in_b.append(number)\n",
    "\n",
    "evens_in_b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "id": "f3ae9738",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2, 3)"
      ]
     },
     "execution_count": 179,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 9 - print out the shape of the array b.\n",
    "\n",
    "b.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "b58d7906",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 6],\n",
       "       [4, 7],\n",
       "       [5, 8]])"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 10 - transpose the array b.\n",
    "b.T\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "025b1c96",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3, 4, 5, 6, 7, 8]])"
      ]
     },
     "execution_count": 186,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)\n",
    "\n",
    "b.reshape(1,6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "id": "92c92142",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[3],\n",
       "       [4],\n",
       "       [5],\n",
       "       [6],\n",
       "       [7],\n",
       "       [8]])"
      ]
     },
     "execution_count": 187,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)\n",
    "b.reshape(6,1)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "id": "c40d92a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 8, 9]])"
      ]
     },
     "execution_count": 189,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Setup 3\n",
    "c = [\n",
    "    [1, 2, 3],\n",
    "    [4, 5, 6],\n",
    "    [7, 8, 9]\n",
    "]\n",
    "\n",
    "c = np.array(c)\n",
    "c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "id": "41e6e7d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 9, 362880)"
      ]
     },
     "execution_count": 190,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# HINT, you'll first need to make sure that the \"c\" variable is a numpy array prior to using numpy array methods.\n",
    "# Exercise 1 - Find the min, max, sum, and product of c.\n",
    "\n",
    "c.min(), c.max(), c.prod()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "id": "772b0b98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.581988897471611"
      ]
     },
     "execution_count": 191,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 2 - Determine the standard deviation of c.\n",
    "\n",
    "c.std()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "id": "6678a4bf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "5.0"
      ]
     },
     "execution_count": 198,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 3 - Determine the variance of c.\n",
    "\n",
    "c.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "id": "19a9676e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 3)"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 4 - Print out the shape of the array c\n",
    "\n",
    "c.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "id": "58e7e473",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 8],\n",
       "       [3, 6, 9]])"
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 5 - Transpose c and print out transposed result.\n",
    "c.T\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "id": "bdafdadd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 30,  36,  42],\n",
       "       [ 66,  81,  96],\n",
       "       [102, 126, 150]])"
      ]
     },
     "execution_count": 194,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 6 - Get the dot product of the array c with c. \n",
    "\n",
    "np.dot(c,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "375facfa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "261"
      ]
     },
     "execution_count": 196,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261\n",
    "(c.T*c).sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "id": "ef64ce94",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "131681894400"
      ]
     },
     "execution_count": 197,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.\n",
    "(c.T*c).prod()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "id": "433c5e4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "## Setup 4\n",
    "d = [\n",
    "    [90, 30, 45, 0, 120, 180],\n",
    "    [45, -90, -30, 270, 90, 0],\n",
    "    [60, 45, -45, 90, -45, 180]\n",
    "]\n",
    "\n",
    "d = np.array(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "id": "9bad087b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,\n",
       "        -0.80115264],\n",
       "       [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,\n",
       "         0.        ],\n",
       "       [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,\n",
       "        -0.80115264]])"
      ]
     },
     "execution_count": 205,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 1 - Find the sine of all the numbers in d\n",
    "\n",
    "np.sin(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "id": "bb6ac19c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,\n",
       "        -0.59846007],\n",
       "       [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,\n",
       "         1.        ],\n",
       "       [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,\n",
       "        -0.59846007]])"
      ]
     },
     "execution_count": 206,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 2 - Find the cosine of all the numbers in d\n",
    "\n",
    "np.cos(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "id": "4baa6765",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,\n",
       "         1.33869021],\n",
       "       [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,\n",
       "         0.        ],\n",
       "       [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,\n",
       "         1.33869021]])"
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 3 - Find the tangent of all the numbers in d\n",
    "\n",
    "np.tan(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 208,
   "id": "6e88772f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-90, -30, -45, -45])"
      ]
     },
     "execution_count": 208,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 4 - Find all the negative numbers in d\n",
    "d[d<0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 209,
   "id": "e697a8cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180])"
      ]
     },
     "execution_count": 209,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 5 - Find all the positive numbers in d\n",
    "d[d>0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 210,
   "id": "8f340aa2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])"
      ]
     },
     "execution_count": 210,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 6 - Return an array of only the unique numbers in d.\n",
    "np.unique(d)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 211,
   "id": "278223a9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "11"
      ]
     },
     "execution_count": 211,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 7 - Determine how many unique numbers there are in d.\n",
    "len(np.unique(d))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "id": "5684c959",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 6)"
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 8 - Print out the shape of d.\n",
    "d.shape\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "id": "5fce7c7c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  45,  60],\n",
       "       [ 30, -90,  45],\n",
       "       [ 45, -30, -45],\n",
       "       [  0, 270,  90],\n",
       "       [120,  90, -45],\n",
       "       [180,   0, 180]])"
      ]
     },
     "execution_count": 213,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 9 - Transpose and then print out the shape of d.\n",
    "d.T\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "id": "d70dc86d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 90,  30],\n",
       "       [ 45,   0],\n",
       "       [120, 180],\n",
       "       [ 45, -90],\n",
       "       [-30, 270],\n",
       "       [ 90,   0],\n",
       "       [ 60,  45],\n",
       "       [-45,  90],\n",
       "       [-45, 180]])"
      ]
     },
     "execution_count": 214,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Exercise 10 - Reshape d into an array of 9 x 2\n",
    "d.reshape(9,2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97f63de5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
