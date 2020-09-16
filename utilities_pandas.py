import pandas as pd

def read_pandas(filepath, names):
    df= pd.read_csv(
        filepath,
        names=names,
    )

    return df


if __name__ == "__main__":
    filepath= "./data/iris.data"
    names= ['sepal_length','sepal_width','petal_length','pertal_width','class']
    df= read_pandas(filepath, names)
    print(df.head(10))

    sepal_length = df['sepal_length'].to_list()
    print(sepal_length)


    df['sl+pl']=df['sepal_length']+df['petal_length']

    print(df.head())

    df_filtred=df[df['sepal_length']>=5]

    print (df_filtred)
