def main():
    arr = [1, 3, 5, 7, 9]
    arrX = [-45, 43, 3, 56, 5]

    for i in range(len(arr)):
        arr[i] = ((arr[i] * 10) / 3) * arrX[i]

    # find the highest value in array at index
    index = [0, 0]
    val = [arr[0], arr[0]]
    for i in range(len(arr)):
        if arr[i] > val[0]:  # highest value
            val[0] = arr[i]
            index[0] = i

        if arr[i] < val[1]:  # lowest value
            val[1] = arr[i]
            index[1] = i

    print(f'Array: {arr}')
    print(f'Highest value is at index: {index[0]}')
    print(f'Lowest value is at index: {index[1]}')


if __name__ == '__main__':
    main()
