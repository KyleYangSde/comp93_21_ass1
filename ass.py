import numpy as np
import ast
import json
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os

studentid = os.path.basename(sys.modules[__name__].__file__)


#################################################
# Your personal methods can be here ...
#################################################


def log(question, output_df, other):
    print("--------------- {}----------------".format(question))
    if other is not None:
        print(question, other)
    if output_df is not None:
        print(output_df.head(5).to_string())


def question_1(movies, credits):
    """
    :param movies: the path for the movie.csv file
    :param credits: the path for the credits.csv file
    :return: df1
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    movies_df = pd.read_csv(movies, encoding='UTF-8')

    credits_df = pd.read_csv(credits, encoding='UTF-8')

    df1 = pd.merge(movies_df, credits_df, how='inner', on='id')
    #################################################

    log("QUESTION 1", output_df=df1, other=df1.shape)
    return df1


def question_2(df1):
    """
    :param df1: the dataframe created in question 1
    :return: df2
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    a = ['id', 'title', 'popularity', 'cast', 'crew', 'budget', 'genres', 'original_language', 'production_companies',
         'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'vote_average', 'vote_count']
    df2 = df1[a]

    for i in df2.columns.values.tolist():
        if i not in a:
            df2.drop(i, axis=1)
    #################################################

    log("QUESTION 2", output_df=df2, other=(
        len(df2.columns), sorted(df2.columns)))
    return df2


def question_3(df2):
    """
    :param df2: the dataframe created in question 2
    :return: df3
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """
    #################################################
    df2.set_index(["id"], inplace=True)
    df3 = df2
    #################################################

    log("QUESTION 3", output_df=df3, other=df3.index.name)
    return df3


def question_4(df3):
    """
    :param df3: the dataframe created in question 3
    :return: df4
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    df4 = df3.drop(df3[df3.budget == 0].index)
    #################################################

    log("QUESTION 4", output_df=df4, other=(
        df4['budget'].min(), df4['budget'].max(), df4['budget'].mean()))
    return df4


def question_5(df4):
    """
    :param df4: the dataframe created in question 4
    :return: df5
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    df4['success_impact'] = df4.apply(lambda x: (
        x['revenue'] - x['budget']) / x['budget'], axis=1)
    df5 = df4
    #################################################

    log("QUESTION 5", output_df=df5,
        other=(df5['success_impact'].min(), df5['success_impact'].max(), df5['success_impact'].mean()))
    return df5


def question_6(df5):
    """
    :param df5: the dataframe created in question 5
    :return: df6
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    array = []
    new_Arr = []
    for i in df5["popularity"]:
        array.append(i)
    for j in df5["popularity"]:
        new_Arr.append((j - min(array))*100 / (max(array) - min(array)))
    df5["popularity"] = new_Arr

    df6 = df5

    #################################################

    log("QUESTION 6", output_df=df6, other=(
        df6['popularity'].min(), df6['popularity'].max(), df6['popularity'].mean()))
    return df6


def question_7(df6):
    """
    :param df6: the dataframe created in question 6
    :return: df7
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    df6['popularity'] = df6['popularity'].astype('int16')
    df7 = df6
    #################################################

    log("QUESTION 7", output_df=df7, other=df7['popularity'].dtype)
    return df7


def question_8(df7):
    """
    :param df7: the dataframe created in question 7
    :return: df8
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    str_1 = ","
    for i, r in df7.iterrows():
        a = []
        char_list = ast.literal_eval(r["cast"])
        for j in char_list:
            a.append(j['character'])
        df7.loc[i, 'cast'] = str_1.join(sorted(a))
    df8 = df7
    #################################################

    log("QUESTION 8", output_df=df8, other=df8["cast"].head(10).values)
    return df8


def question_9(df8):
    """
    :param df9: the dataframe created in question 8
    :return: movies
            Data Type: List of strings (movie titles)
            Please read the assignment specs to know how to create the output
    """

    #################################################
    chara_num = []
    chara_dict = {}
    for i, r in df8.iterrows():
        single_chara = r["cast"].split(",")
        chara_num.append(len(single_chara))
        chara_dict[i] = len(single_chara)

    chara_num = sorted(chara_num)[:: -1][: 10]
    # print(chara_num)
    index = []
    movies = []
    for i in chara_num:
        for j in chara_dict:
            if chara_dict[j] == i:
                index.append(j)

    index_movie = []
    for i in index:
        if i not in index_movie:
            index_movie.append(i)

    for i in index_movie:
        movies.append(df8.loc[i, "title"])
    # print(movies)
    #################################################

    log("QUESTION 9", output_df=None, other=movies)
    return movies


def question_10(df8):
    """
    :param df8: the dataframe created in question 8
    :return: df10
            Data Type: Dataframe
            Please read the assignment specs to know how to create the output dataframe
    """

    #################################################
    df8["release_date"] = pd.to_datetime(df8["release_date"])
    df8.sort_values("release_date", inplace=True, ascending=False)
    df10 = df8

    # df10['release_date'] = df10['relesase_date'].apply(
    #     lambda x: x.strftime('%d/%m/%Y'))
    # print(df10["release_date"])
    #################################################

    log("QUESTION 10", output_df=df10, other=df10["release_date"].head(
        5).to_string().replace("\n", " "))
    return df10


def question_11(df10):
    """
    :param df10: the dataframe created in question 10
    :return: nothing, but saves the figure on the disk
    """

    #################################################
    plt.clf()
    genres = []
    genres_dict = {}
    types = []
    nums = []
    for i in df10["genres"]:
        for j in i.split("},"):
            j = j.split(": '")[1]
            j = j.strip("]")
            j = j.strip("}")
            j = j.strip("'")
            genres.append(j)

    genres = sorted(set(genres))
    for i in genres:
        genres_dict[i] = 0

    for i in df10["genres"]:
        for j in i.split("},"):
            j = j.split(": '")[1]
            j = j.strip("]")
            j = j.strip("}")
            j = j.strip("'")
            for k in genres_dict.keys():
                if j == k:
                    genres_dict[k] += 1

    for i in genres_dict:
        nums.append(genres_dict[i])
        types.append(i)
    fig = plt.figure()
    plt.pie(nums, labels=types, autopct='%1.1f%%', textprops={'fontsize': 5})
    plt.title("Genres")

    #################################################

    plt.savefig("{}-Q11.png".format(studentid))


def question_12(df10):
    """
    :param df10: the dataframe created in question 10
    :return: nothing, but saves the figure on the disk
    """

    #################################################
    plt.clf()
    country_list = []
    country_dict = {}
    for i in df10["production_countries"]:
        for j in i.split("},"):
            j = j.split(": '")[2]
            j = j.strip("]")
            j = j.strip("}")
            j = j.strip("'")
            country_list.append(j)

    country_list = list(set(country_list))
    for i in country_list:
        country_dict[i] = 0

    for i in df10["production_countries"]:
        for j in i.split("},"):
            j = j.split(": '")[2]
            j = j.strip("]")
            j = j.strip("}")
            j = j.strip("'")
            for k in country_dict.keys():
                if j == k:
                    country_dict[j] += 1

    num_list = []

    country_list = sorted(country_list)
    for i in country_list:
        num_list.append(country_dict[i])

    import numpy as np
    xlocs, xlabs = plt.xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ['0',
                                                                        r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$'], rotation=90)
    xlocs = [i+0.1 for i in range(len(country_list))]

    for i, v in enumerate(num_list):
        plt.text(xlocs[i] - 0.25, v + 0.01, str(v))
    plt.bar(range(len(num_list)), num_list, tick_label=country_list, width=0.4)

    plt.xticks(fontsize=6)

    plt.tight_layout()

    #################################################

    plt.savefig("{}-Q12.png".format(studentid))


def question_13(df10):
    """
    :param df10: the dataframe created in question 10
    :return: nothing, but saves the figure on the disk
    """

    #################################################

    import numpy as np

    lang_vote_success = []
    for i, r in df10.iterrows():
        char_list = ast.literal_eval(r["spoken_languages"])
        # print(char_list)
        for j in char_list:
            if j["name"] != '':
                lang_vote_success.append(
                    [j['name'], df8.loc[i, 'vote_average'], df8.loc[i, 'success_impact']])
    vote_average = []
    success_impact = []
    lang = []
    for i in lang_vote_success:
        lang.append(i[0])
        vote_average.append(i[1])
        success_impact.append(i[2])

    import matplotlib.font_manager as font_manager
    plt.clf()
    fig, ax = plt.subplots()
    fig.set_size_inches(20, 20)
    scatter_x = np.array(vote_average)
    scatter_y = np.array(success_impact)
    group = np.array(lang)

    for g in np.unique(group):
        i = np.where(group == g)
        ax.scatter(scatter_x[i], scatter_y[i], label=g)
    params = {'legend.fontsize': 8,
              'legend.handlelength': 2}
    # fontP = font_manager.FontProperties().set_family('SimHei')
    plt.rcParams.update(params)
    ax.legend()

    plt.savefig("{}-Q13.png".format(studentid))
    #################################################


if __name__ == "__main__":

    df1 = question_1("movies.csv", "credits.csv")
    df2 = question_2(df1)
    df3 = question_3(df2)
    df4 = question_4(df3)
    df5 = question_5(df4)
    df6 = question_6(df5)
    df7 = question_7(df6)
    df8 = question_8(df7)
    movies = question_9(df8)
    df10 = question_10(df8)
    question_11(df10)
    question_12(df10)
    question_13(df10)
