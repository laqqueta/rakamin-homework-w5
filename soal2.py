import pandas as pd


def main():
    df = pd.read_excel('__files__/superstore.xls')
    df = pd.DataFrame(df.loc[df['Order Date'] >= '2017-01-01'])

    print(df.columns)

    percentiles = df['Sales'].quantile([0.25, 0.50, 0.75])
    df['Category'] = df['Sales'].apply(lambda x:
                                       'High' if x > percentiles[0.75] else
                                       'Medium' if x > percentiles[0.50] else
                                       'Low')

    category_data_count = []

    for category in ['High', 'Medium', 'Low']:
        category_data_count.append(df['Category'].value_counts()[category])

    print(f'High segment costumer total\t\t: {category_data_count[0]}\n'
          f'Medium segment costumer total\t: {category_data_count[1]}\n'
          f'Low segment costumer total\t\t: {category_data_count[2]}')

    print(df.values)

    # save output to a file
    # df.to_excel('__files__/output.xlsx', index=False)


if __name__ == '__main__':
    main()
