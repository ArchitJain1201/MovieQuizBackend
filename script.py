import csv
import pandas as pd

# Get data from CSV file to DataFrame(Pandas)
with open('Movie.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    columns = [
        'name',
        'option1',
        'option2',
        'option3',
        'option4',
        'actor',
        'img_url',
        'movie_by',
        'answer'
    ]
    df = pd.DataFrame(data=reader, columns=columns)
    df.values.tolist()
    name = df['name'][1]
    print(name)
    for i in range(0,22):
        name = df['name'][i]
        option1 = df['option1'][i],
        option2 = df['option2'][i],
        option3 = df['option3'][i],
        option4 = df['option4'][i],
        actor = df['actor'][i],
        img_url = df['img_url'][i],
        df_by = df['df_by'][i],
        answer = df['answer'][i]  
        print(name)
        print(option1)
    # for i in range(1,20):
    #     name = df['name'][1],
    #     option1 = df['option1'][i],
    #     option2 = df['option2'][i],
    #     option3 = df['option3'][i],
    #     option4 = df['option4'][i],
    #     actor = df['actor'][i],
    #     img_url = df['img_url'][i],
    #     df_by = df['df_by'][i],
    #     answer = df['answer'][i]
    #     print(name)
    # name = df['name'][1]
    # print(name) 
    # print(df)
    # for columns in df.columns:
    #     print(columns)
