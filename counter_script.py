import pandas as pd


def compare(first_word, second_word):
    yellow_count = 0
    green_count = 0
    tracker = []
    for i in range(0, 5):
        if first_word[i] == second_word[i]:
            green_count += 1
            if first_word[i] not in tracker:
                tracker.append(first_word[i])
            else:
                yellow_count -= 1
        else:
            if first_word[i] in (second_word) and first_word[i] not in tracker:
                yellow_count += 1
                tracker.append(first_word[i])
    return green_count, yellow_count


def lookup_function(passed_words):
    words = {}
    for i in passed_words:
        words[i] = None
    # For each word, compare against other words in the word list to see how they score and add up these scores
    for i in words.keys():
        green_count = 0
        yellow_count = 0
        for c in words.keys():
            temp_green, temp_yellow = compare(i, c)
            green_count += temp_green
            yellow_count += temp_yellow
        words[i] = (green_count, yellow_count)

    dataframe = pd.DataFrame.from_dict(data=words, orient="index")
    dataframe.head()
    dataframe.rename(columns={0: "Green", 1: "Yellow"}, inplace=True)
    dataframe["Combined_Score"] = dataframe["Green"] + dataframe["Yellow"]
    top_ten = dataframe.nlargest(10, "Combined_Score")
    top_ten_list = top_ten.index.to_list()
    return top_ten_list
