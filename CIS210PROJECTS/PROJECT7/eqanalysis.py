"""
eqanalysis.py: analyze and plot earthquake data
Authors: Austin Robison

CIS 210 assignment 7, Fall 2016
"""

# a set of modules that we need to use in the code below
import math
import random
import argparse
import data
import turtle
import sys

# constants for the k-means clustering algorithm
# if you change these in your experimentation, you will need to look at 
# all parts of the code that refer to them, as there is some dependence
# on them (such as number of colors used in plotting clusters)
#
# IF YOU DO CHANGE THEM, YOU MUST PUT THEM BACK TO THE ORIGINAL VALUES
# BEFORE SUBMITTING YOUR WORK!!!!!
NO_OF_CLUSTERS = 6
NO_OF_ITERATIONS = 7

def euclid_distance(point1, point2):
    """
    computes the euclidean distance between two points
    Args:
        point1: list of floats, index 0 is longitude, index 1 is latitude
        point2: list of floats, index 0 is longitude, index 1 is latitude
    Returns:
        float, sqrt((x1-x2)**2 + (y1-y2)**2)
    """

    total = 0
    for index in range(2):
        diff = point1[index] - point2[index]
        total += diff * diff

    return math.sqrt(total)

def create_centroids(k, datadict):
    """
    randomly selects 'k' points from 'datadict' as the starting
        centroids for the k-means clustering algorithm
    Args:
        k: int, number of clusters desired
        datadict: list of lists, each contained list represents an EQ event
    Returns:
        list of lists, each contained list is an event to act as the centroid
    """
    centroids = []
    count = 0
    centroid_keys = []

    while count < k:
        rkey = random.randint(1, len(datadict))
        if rkey not in centroid_keys:
            centroids.append(datadict[rkey])
            centroid_keys.append(rkey)
            count += 1

    return centroids

def create_clusters(k, centroids, datadict, iterations):
    """
    k-means clustering algorithm - implementation taken from page 249 of
        ranum and miller text, with some modifications
    Args:
        k: integer, number of clusters
        centroids: list of events, each event is the centroid of its cluster
        datadict: dictionary of all EQ events
        iterations: int, number of clustering iterations to perform
    Returns:
        list of lists: each contained list is the set of indices into 'datadict'
           for events that belong to that cluster
    """
    for iteration in range(iterations):
        #print("****Iteration", iteration, "****")
        clusters = []
        for i in range(k):
            clusters.append([])

        for key in datadict:
            distances = []
            for cl_index in range(k):
                dist = euclid_distance(datadict[key], centroids[cl_index])
                distances.append(dist)
            min_dist = min(distances)
            index = distances.index(min_dist)
            clusters[index].append(key)

        dimensions = 2
        for cl_index in range(k):
            sums = [0]*dimensions
            for key in clusters[cl_index]:
                data_points = datadict[key]
                for ind in range(2):
                    sums[ind] = sums[ind] + data_points[ind]
            for ind in range(len(sums)):
                cl_len = len(clusters[cl_index])
                if cl_len != 0:
                    sums[ind] /= cl_len
            centroids[cl_index] = sums

        #for c in clusters:
            #print("CLUSTER")
            #for key in c:
                #print(datadict[key], end=" ")
            #print()

    return clusters


def read_file(filename):
    """
    read the EQ events from the csv file, 'filename'; any lines starting with
        # are skipped; the longitude, latitude, magnitude, and depth (in miles)
        is extracted from each event record, and stored as a list against its
        record number in a dictionary
    Args:
        filename: string, name of a CSV file containing the EQ data
    Returns:
        dictionary, indexed by integers, each value is a list of floats
            representing an EQ event
    """
    dict = {}
    key = 0

    fd = open(filename, "r")
    for line in fd:
        if line[0] == '#':
            continue            # causes the loop to grab another line
        key += 1
        values = line.rstrip('\n').split(',')
        lat = float(values[7])
        lon = float(values[8])
        mag = float(values[1])
        dep = float(values[10])
        dict[key] = [lon, lat, mag, dep]
    fd.close()
    return dict

# global data for map - if we had ;earmed about classes yet, this would have
# been hidden in a class instance, and the plot_*() functions would be methods
# on that class instance.  for now, these are global variables, and the
# plot functions access them

eq_turtle = None
eq_win = None
# these are the longitudes and latitudes for the Pacific NorthWest map that
# I have provided to you; do not change them!
left_lon = -128.608689
right_lon = -114.084764
top_lat = 51.248522
bot_lat = 38.584004
lon_diff = 0
lat_diff = 0
size_x = 0
size_y = 0
left_x = 0
bot_y = 0
              

def prepare_turtle():
    """
    Prepares the turtle and the window to plot magnitudes, depths, or clusters
    Args:
        None
    Outputs:
        creates turtle, sets window size, defines remainder of global
        data needed for plot_routines
    """
    global eq_turtle, eq_win
    global left_lon, right_lon, top_lat, bot_lat
    global lon_diff, lat_diff
    global size_x, size_y, left_x, bot_y

    eq_turtle = turtle.Turtle()
    eq_turtle.speed(10)
    eq_win = turtle.Screen()
    eq_win.screensize(655,808)  # number of pixels in the map I have provided
    lon_diff = right_lon - left_lon
    lat_diff = top_lat - bot_lat
    size_x = eq_win.screensize()[0]
    left_x = -size_x/2
    size_y = eq_win.screensize()[1]
    bot_y = -size_y/2
    eq_win.bgpic("PacificNW.gif")       # the map I have provided
    eq_turtle.hideturtle()
    eq_turtle.up()

def xy_calculate(lon, lat):
    """
    compute (x, y) given lon[gitude] and lat[itude]
    Args:
        lon: float, longitude value for point on map
        lat: float, latitude value for point on map
    Returns:
        tuple, corresponding pixel x and y values for use in turtle methods
    """
    global left_lon, right_lon, top_lat, bot_lat
    global lon_diff, lat_diff
    global size_x, size_y, left_x, bot_y

    x = left_x + (lon - left_lon) / lon_diff * size_x
    y = bot_y + (lat - bot_lat) / lat_diff * size_y
    return (x, y)

def plot_clusters(eq_clusters, eq_dict):
    """
    plot the clusters - use turtle.dot() at the appropriate location on the
        map for each event; use a different color for the events in each
        cluster - e.g. for cluster 0, use 'red', for 1, use 'violet' ...
    Args:
        eq_clusters: list of lists, each contained list has the indices for
                     events in that cluster in eq_dict
        eq_dict: list of lists, each contained list represents an EQ event
    Outputs:
        plots all events in a particular cluster as dots on the map
    """
    global eq_turtle

    def rand_color(color_list):
        '''
        makes turtle a random color from  a list
        Args:
            a color list
        Effects:
            takes a color from a list, sets the turtle to that color,
                removes the color so it cannot be repeated
        Restrictions: 
            the length of the color list has to be greater than or equal to
                NO_OF_CLUSTERS, if NO_OF_CLUSTERS is more than 6, add colors to  c_list
                accordingly

        '''

        color_index = random.randint(0, len(color_list)-1)
        turtle.color(color_list[color_index])
        color_list.remove(color_list[color_index])

    c_list = ['magenta','blue','DarkGreen','brown','red','orange']
    # if NO_OF_CLUSTERS > len(c_list) then you must add more colors to c_list

    for cluster in eq_clusters:
        rand_color(c_list)
        for index in cluster:
            if index in eq_dict:
               lon_val = eq_dict[index][0]
               lat_val = eq_dict[index][1]
               turtle.up()
               turtle.goto(xy_calculate(lon_val, lat_val))
               turtle.down()
               turtle.dot(10)

def bin_value(value, bounds):
    """
    'bounds' defines a set of bins; this function returns the index of the
        first bin that contains 'value'
    Args:
        value: float, value to place in bin
        bounds: list of floats, bounds[i] is the top value of the bin
                code assumes that bounds is an increasing set of values
    Returns:
        integer, index of smallest value of bounds[] that is >= value
            if value > bounds[-1], returns len(bounds)
    """
    for i in range(len(bounds)):
        if value <= bounds[i]:
            return i
    return len(bounds)

def plot_magnitudes(eq_dict):
    """
    plot the magnitudes - use turtle.dot() at the appropriate location on the
        map for each event; use a different color and size for magnitude
        equivalence classes - e.g. if magnitude of event is <=1, use small dot
        that is 'violet', if between 1 and 2, use slightly larger dot that is
        'blue', ..., if between 9-10, use very large dot that is 'red'
    Args:
        eq_dict: list of lists, each contained list represents an EQ event
    Outputs:
        plots magnitude of all events as dots on the map
    """
    global eq_turtle

    for element in eq_dict.values():
        mag = element[2]
        lon_val = element[0]
        lat_val = element[1]
        turtle.penup()
        turtle.goto(xy_calculate(lon_val, lat_val))
        turtle.pendown()
        if (mag <= 1.0):
            turtle.color('violet')
        if (mag > 1.0) and (mag <= 2.0):
            turtle.color('blue')
        if (mag >= 9.0) and (mag < 10.0):
            turtle.color('red')
        turtle.dot(5 * mag)

def plot_depths(eq_dict):
    """
    plot the depths - use turtle.dot() at the appropriate location on the
        map for each event; use a different color and size for depth
        equivalence classes - e.g. if depth of event is <=1 mile, use small dot
        that is 'violet', if between 1 and 5, use slightly larger dot that is
        'blue', ..., if between 50-100, use very large dot that is 'red'
    Args:
        eq_dict: list of lists, each contained list represents an EQ event
    Outputs:
        plots depth of all events as dots on the map
    """
    global eq_turtle

    for element in eq_dict.values():
        lon_val = element[0]
        lat_val = element[1]
        depth = element[3]
        turtle.up()
        turtle.goto(xy_calculate(lon_val, lat_val))
        if depth <= 1:
           turtle.color('violet')
        if (1 < depth <= 5):
           turtle.color('blue')
        if (5 < depth <= 50):
           turtle.color('yellow')
        if (50 < depth < 100 ):
           turtle.color('red')
        turtle.dot(depth / 2)

def analyze_depths(eq_dict):
    """
    Perform statistical analysis on the depth information in the dictionary
    Args:
        eq_dict: list of lists, each contained list represents an EQ event
    Outputs:
        mean, median, and standard deviation of depth data
        frequency table for the depth data
    """

    depth_list = []
    for element in eq_dict.values():
        depth_list.append(element[3])
    depth_list.sort()
    print('Analysis of Depth data')
    mean = data.data_mean(depth_list)
    print('  Mean of Depths = ', '{:.2}'.format(mean), ' miles')
    median = data.data_median(depth_list) 
    print('  Median of Depths = ', median, ' miles')
    sd_list = []
    for num in depth_list:
        step1 = (num - mean) ** 2
        sd_list.append(step1)
    st_dev = math.sqrt(data.data_mean(sd_list))    
    print('  Standard Deviation =', '{:.3}'.format(st_dev), ' miles')
    data.data_freq_table(depth_list)

def analyze_magnitudes(eq_dict):
    """
    Perform statistical analysis on the magnitude information in the dictionary
    Args:
        eq_dict: list of lists, each contained list represents an EQ event
    Outputs:
        mean, median, and standard deviation of magnitude data
        frequency table for the magnitude data
    """
    
    mag_list = []
    for element in eq_dict.values():
        mag_list.append(element[2])
    mag_list.sort()
    print('Analysis of Magnitude data')
    mean = data.data_mean(mag_list)
    print('  Mean of Magnitudes = ', '{:.2}'.format(mean))
    median = data.data_median(mag_list) 
    print('  Median of Depths = ', median)
    sd_list = []
    for num in mag_list:
        step1 = (num - mean) ** 2
        sd_list.append(step1)
    st_dev = math.sqrt(data.data_mean(sd_list))    
    print('  Standard Deviation =', '{:.2}'.format(st_dev))
    data.data_freq_table(mag_list)

def analyze_clusters(eq_clusters, eq_dict):
    """
    Perform statistical analysis on the depth and magnitude information
        for each cluster
    Args:
        eq_clusters: list of lists, each contained list has the indices into
                     eq_dict for events in that cluster
        eq_dict: list of lists, each contained list represents an EQ event
    Outputs:
        for each cluster:
            mean, median, and standard deviation of magnitude data
            mean, median, and standard deviation of depth data
    """
    count = 0
    for cluster in eq_clusters:
        mag_list = []
        depth_list = []
        print('Analysis of cluster', count)
        count += 1
        for index in cluster:
            if index in eq_dict:
                mag = eq_dict[index][2]
                depth = eq_dict[index][3]
                mag_list.append(mag)
                depth_list.append(depth)
        #--------------------------MAG DATA-------------------------------------
        mag_list.sort()
        sd_list = []
        print('  Analysis of Magnitude Data')
        mean = data.data_mean(mag_list)
        print('   Mean Magnitudes = ', '{:.2}'.format(mean))
        median = data.data_median(mag_list) 
        print('   Median Magnitude = ', '{:.2}'.format(median))
        for num in mag_list:
            step1 = (num - mean) ** 2
            sd_list.append(step1)
        st_dev = math.sqrt(data.data_mean(sd_list))    
        print('   Standard Deviation magnitude =', '{:.2}'.format(st_dev))
        #---------------------------DEPTH DATA------------------------------------
        depth_list.sort()
        sd_list = []
        print(' Analysis of Depth Data')
        mean = data.data_mean(depth_list)
        print('   Mean Magnitudes = ', '{:.2}'.format(mean), ' miles')
        median = data.data_median(depth_list) 
        print('   Median Magnitude = ', '{:.2}'.format(median), ' miles')
        for num in depth_list:
            step1 = (num - mean) ** 2
            sd_list.append(step1)
        st_dev = math.sqrt(data.data_mean(sd_list))    
        print('   Standard Deviation of depth = ', '{:.2}'.format(st_dev), ' miles')


def main():
    """
    Interaction if run from the command line.
    Usage:  python3 eqanalysis.py eq_data_file.csv command
    """
    parser = argparse.ArgumentParser(description="Earthquake event file stats")
    parser.add_argument('eq_file', type=str,
                 help='A csv file containing earthquake events, one per line.')
    parser.add_argument('command', type=str,
                 help='One of the following strings: plot analyze')
    parser.add_argument('what', type=str,
                 help='One of the following strings: clusters depths magnitudes')
    args = parser.parse_args()
    eq_file = args.eq_file
    cmd = args.command
    what = args.what
    if cmd != 'plot' and cmd != 'analyze':
        print('Illegal command: {}; must be "plot" or "analyze"'.format(cmd))
        sys.exit(1)
    if what != 'clusters' and what != 'magnitudes' and what != 'depths':
        print('Can only process clusters, magnitudes, or depths')
        sys.exit(1)
    eq_dict = read_file(eq_file)
    prepare_turtle()
    if what == 'clusters':
        eq_centroids = create_centroids(NO_OF_CLUSTERS, eq_dict)
        eq_clusters = create_clusters(NO_OF_CLUSTERS, eq_centroids, eq_dict, NO_OF_ITERATIONS)
    if cmd == 'plot':
        if what == 'clusters':
            plot_clusters(eq_clusters, eq_dict)
        elif what == 'magnitudes':
            plot_magnitudes(eq_dict)
        elif what == 'depths':
            plot_depths(eq_dict)
        print("ALL EVENTS HAVE BEEN PLOTTED")
        eq_win.exitonclick()
    else:
        if what == 'clusters':
            analyze_clusters(eq_clusters, eq_dict)
        elif what == 'magnitudes':
            analyze_magnitudes(eq_dict)
        elif what == 'depths':
            analyze_depths(eq_dict)

if __name__ == "__main__":
    main()
                                                                             
