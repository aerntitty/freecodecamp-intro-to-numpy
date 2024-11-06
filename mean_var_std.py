{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNpSCwO5eB4dElYZhenFLeT"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.\n",
        "\n",
        "The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.\n",
        "\n",
        "The returned dictionary should follow this format:\n",
        "\n",
        "{\n",
        "  'mean': [axis1, axis2, flattened],\n",
        "  'variance': [axis1, axis2, flattened],\n",
        "  'standard deviation': [axis1, axis2, flattened],\n",
        "  'max': [axis1, axis2, flattened],\n",
        "  'min': [axis1, axis2, flattened],\n",
        "  'sum': [axis1, axis2, flattened]\n",
        "}\n",
        "If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: \"List must contain nine numbers.\" The values in the returned dictionary should be lists and not Numpy arrays."
      ],
      "metadata": {
        "id": "MR1pqD2_myAY"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "eMeSNpJBmiFb"
      },
      "outputs": [],
      "source": [
        "import numpy as np"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def calculate(list):\n",
        "  if len(list)!=9:\n",
        "    raise ValueError('List must contain nine numbers')\n",
        "  data= np.array(list).reshape((3,3))\n",
        "\n",
        "  calculations = {\n",
        "      'mean': [np.mean(data, axis=0).tolist(), np.mean(data, axis=1).tolist(), np.mean(data).tolist()],\n",
        "      'variance': [np.var(data, axis=0).tolist(), np.var(data, axis=1).tolist(), np.var(data).tolist()],\n",
        "      'max' : [np.max(data, axis= 0).tolist() , np.max(data , axis=1).tolist(), np.max(data).tolist()],\n",
        "    'min' : [np.min(data, axis= 0).tolist() , np.min(data , axis=1).tolist(), np.min(data).tolist()],\n",
        "    'sum': [np.sum(data, axis = 0).tolist(), np.sum(data , axis = 1).tolist(), np.sum(data).tolist()]}\n",
        "\n",
        "  return calculations\n"
      ],
      "metadata": {
        "id": "iYA9InlcnFTX"
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "calculate([2,6,2,8,4,0,1,5,7])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iB3vyOzonb52",
        "outputId": "c77a1eee-4073-40c1-caef-18a959e0ba89"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{'mean': [[3.6666666666666665, 5.0, 3.0],\n",
              "  [3.3333333333333335, 4.0, 4.333333333333333],\n",
              "  3.888888888888889],\n",
              " 'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666],\n",
              "  [3.555555555555556, 10.666666666666666, 6.222222222222221],\n",
              "  6.987654320987654],\n",
              " 'max': [[8, 6, 7], [6, 8, 7], 8],\n",
              " 'min': [[1, 4, 0], [2, 0, 1], 0],\n",
              " 'sum': [[11, 15, 9], [10, 12, 13], 35]}"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "kCPTj83nwEnV"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}