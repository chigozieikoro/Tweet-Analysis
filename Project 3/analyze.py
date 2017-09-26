#!/usr/bin/env python3
from functools import *
import json



with open("tweets.json", "r") as tweet_db:
    tweets = json.load(tweet_db)

# TODO: implement assigned functions

def flatten(xs):
    flattened = reduce((lambda x, y: x + y), xs, [])
    return list(flattened)


def difference(xs, ys):
    x = set(xs)
    y = set(ys)
    result = x ^ y
    return list(result)




def to_text(tweets):
    contents = map((lambda x: x["content"]), tweets)
    return list(contents)

def to_lowercase(tweets):
    #contents = to_text(tweets)
    #ILC S131 monday
    lowercase_tweets = map((lambda x: {'username': x['username'], 'source': x['source'],
                                       'content': x['content'].lower(), 'favorites': x['favorites'],
                                       'retweets': x['retweets']}), tweets)
    result = list(lowercase_tweets)
    return result


def nonempty(tweets):
    result = filter((lambda x: x['content'] != ""), tweets)
    return list(result)

def total_word_count(tweets):
    words = map((lambda x: x['content'].split()), tweets)
    list1 = list(words)
    word_list = flatten(list1)
    return len(word_list)

def hashtags(tweet):
    dict_values = tweet.values()
    list1 = list(dict_values)
    values = list1[2].split()
    value2 = filter((lambda x: x[0] == '#'), values)
    return list(value2)

def mentions(tweet):
    dict_values = tweet.values()
    list1 = list(dict_values)
    values = list1[2].split()
    values2 = filter((lambda x: x[0] == '@'), values)
    return list(values2)


def all_hashtags(tweets):
    tweet_hashtags = map((lambda x: hashtags(x)), tweets)
    list_hash = list(tweet_hashtags)
    final_hashtags = filter((lambda x: len(x) != 0), list_hash)
    lister = list(final_hashtags)
    formated_list = flatten(lister)
    return formated_list

def all_mentions(tweets):
    tweet_mentions = map((lambda x: mentions(x)), tweets)
    list_ment = list(tweet_mentions)
    final_ment = filter((lambda x: len(x) != 0), list_ment)
    lister = list(final_ment)
    formated_list = flatten(lister)
    return formated_list

def all_caps_tweets(tweets):
    tweet_cap = filter((lambda x: x['content'].isupper()), tweets)
    return tweet_cap

def count_individual_words(tweets):
    content = to_text(tweets)
    cut_words = map((lambda x: x.split()), content)
    list1 = list(cut_words)
    words = flatten(list1)
    word_list = list(words)
    dict1 = map((lambda x: {x: word_list.count(x)}), word_list)
    list_dict = list(dict1)
    final_dict = reduce(lambda x,y: {**x, **y}, list_dict, {})
    return final_dict

def count_individual_hashtags(tweets):
    hashtag_set = map((lambda x: hashtags(x)), tweets)
    list_hashtag = list(hashtag_set)
    flatten_hashtags = flatten(list_hashtag)
    dictionary_map = map((lambda x: {x: flatten_hashtags.count(x)}), flatten_hashtags)
    dict_list = list(dictionary_map)
    final_dict = reduce((lambda x, y: {**x, **y}), dict_list, {})
    return final_dict


def count_individual_mentions(tweets):
    mention_list = all_mentions(tweets)
    mention_map = map((lambda x: {x: mention_list.count(x)}), mention_list)
    list1 = list(mention_map)
    final_dict = reduce((lambda x, y: {**x, **y}), list1, {})
    return final_dict


def n_most_common(n, word_count):
    words = map((lambda x: (x, word_count[x])), word_count)
    word_list = list(words)
    sorted_list = sorted(word_list, key=lambda k: (k[1]), reverse=True)
    sorter = sorted(sorted_list, key = lambda k: (-k[1], k[0].lower()))
    split_list = sorter[0:n]
    return split_list



def iphone_tweets(tweets):
    iphones = filter((lambda x: x['source'] == "Twitter for iPhone"), tweets)
    list_phone = list(iphones)
    return list_phone


def android_tweets(tweets):
    android = filter((lambda x: x['source'] == "Twitter for Android"), tweets)
    list_and = list(android)
    return list_and


def average_favorites(tweets):
    favorites = map((lambda x: x['favorites']), tweets)
    fav_list = list(favorites)
    divisor = len(fav_list)
    total_favs = reduce((lambda x,y: x+y), fav_list, 0)
    answer = total_favs/divisor
    rounded = int(round(answer))
    return rounded


def average_retweets(tweets):
    retweets = map((lambda x: x['retweets']), tweets)
    retweet_list = list(retweets)
    divisor = len(retweet_list)
    total_retweets = reduce((lambda x,y: x + y), retweet_list, 0)
    answer = total_retweets/divisor
    rounded = int(round(answer))
    return rounded


def sort_by_favorites(tweets):
    sorter = sorted(tweets, key = lambda k: k['favorites'])
    return sorter

def sort_by_retweets(tweets):
    sorter = sorted(tweets, key = lambda k: k['retweets'])
    return sorter


def upper_quartile(tweets):
    list_len = len(tweets)
    input_pos = list_len * (3/4)
    rounded = int(round(input_pos))
    final_num = rounded - 1
    result = tweets[final_num]
    return result

def lower_quartile(tweets):
    list_len = len(tweets)
    input_pos = list_len * (1/4)
    rounded = int(round(input_pos))
    final_num = rounded
    result = tweets[final_num]
    return result


def top_quarter_by(tweets, factor):
    cut_quart = upper_quartile(tweets)
    index_tweet = tweets.index(cut_quart)
    sub_list = tweets[index_tweet:]
    return sub_list

def bottom_quarter_by(tweets, factor):
    cut_quart = lower_quartile(tweets)
    index_tweet = tweets.index(cut_quart)
    incremented_index = index_tweet + 1
    sub_list = tweets[:incremented_index]
    return sub_list
