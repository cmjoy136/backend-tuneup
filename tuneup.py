#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "cmjoy136"

import cProfile
import pstats
import functools
import timeit
import collections

def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    def inner(*args, **kwargs):
        prof = cProfile.Profile()
        prof.enable()
        results = func(*args, **kwargs)
        prof.disable()
        ps = pstats.Stats(prof).sort_stats('cumulative')
        ps.print_stats()
        return results
    return inner

def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()

def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False

@profile
def new_and_improved_moviefinder(src):
    movies = [movie.lower() for movie in read_movies(src)]
    duplicates = []
    movie_counter = collections.Counter(movies)
    for mov, count in movie_counter.items():
        if count > 1:
           duplicates.append(mov)
    return duplicates

def timeit_helper(reps, runs_per_rep):
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    t = timeit.Timer(stmt="new_and_improved_moviefinder('movies.txt')",
                     setup="from __main__ import new_and_improved_moviefinder")
    result = t.repeat(reps, runs_per_rep)
    best_time = min(result)/float(runs_per_rep)
    print('Best time across {} repeats of {} runs per repeat: {} sec'.format(
        reps, runs_per_rep, best_time))

def main():
    """Computes a list of duplicate movie entries"""
    timeit_helper(7, 5)
    result = new_and_improved_moviefinder('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))

if __name__ == '__main__':
    main()
