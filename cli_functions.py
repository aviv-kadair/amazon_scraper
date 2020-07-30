"""This file contains all the functions to filter the scraping using the command line
Author: Aviv
"""
import queries_url


def filter_not():
    """Asks the user for filtered search"""
    filter_q = input('Would you like to filter results? Y/N : ').upper()
    return filter_q


def choose_filter():
    """This method gets an input from the user stating the required search filter"""
    parameter = input(f'Choose a filter from the following list: {queries_url.filtering_choice} ')

    if parameter.isdigit():
        parameter = int(parameter)
        operation = list(queries_url.filtering_choice.keys())[parameter - 1]
        # operation = queries_url.filtering_choice.keys()[parameter - 1]
        # print(operation)
        if parameter == 1:
            user_filter = input('Please choose a minimal item ranking, from 1 to 4: ')
            rank_list = {1,2,3,4}
            if int(user_filter) not in rank_list:
                user_filter = input('Ranking was not recognised, please try again: ')
        elif 2 <= parameter <= 6:
            filter_list = get_choice(parameter)
            user_filter = input(f'Please refine your search: {filter_list} ')
            if user_filter not in filter_list:
                user_filter = input('Your choice was not recognised, please try again: ')

        else:
            print('Your filter was not recognised, exiting')
            quit()
        print(f'The following search parameters were chosen: {operation}, {user_filter}')
        return parameter, user_filter
    else:
        print('Chosen parameter is not recognised, exiting')
        quit()


def get_choice(choice):
    """This function imports the relevant choice list"""
    choices = {2: queries_url.manufactures_list, 3: queries_url.screen_sizes, 4: queries_url.RAM_sizes,
               5: queries_url.weights_list, 6: queries_url.HD_type_list}
    choice_list = choices.get(choice)
    # print(choice_list)
    return choice_list


def function_map(parameter, user_filter):
    """This function is designed to call the appropriate function from the function map"""
    function_mapping = {1: query_builder_ranking(user_filter),
                        2: query_builder_manufacture(user_filter),
                        3: query_builder_screen(user_filter),
                        4: query_builder_ram(user_filter),
                        5: query_builder_weight(user_filter),
                        6: query_builder_hd_type(user_filter)
                        }
    if parameter in function_mapping.keys():
        return function_mapping.get(parameter)


def query_builder_ranking(spec_param):
    """This function builds the query form and returns the relevant URL"""
    # print(f'The following search parameters were chosen: ranking, {spec_param}')
    var_name = 'ranking_' + spec_param
    my_url = queries_url.ranking.get(var_name)
    return my_url


def query_builder_manufacture(spec_param):
    """This function builds the query form and returns the relevant URL"""
    # print(f'The following search parameters were chosen: manufacturer, {spec_param}')
    var_name = 'manufacture_' + spec_param

    my_url = queries_url.manufacture.get(var_name)

    return my_url


def query_builder_screen(spec_param):
    """This function builds the query form and returns the relevant URL"""
    # print(f'The following search parameters were chosen: screen size, {spec_param}')
    var_name = ('screen_' + spec_param).replace('-', '_2_')

    my_url = queries_url.screen.get(var_name)
    return my_url


def query_builder_ram(spec_param):
    """This function builds the query form and returns the relevant URL"""
    # print(f'The following search parameters were chosen: RAM size, {spec_param}')
    var_name = 'RAM_' + spec_param
    my_url = queries_url.RAM.get(var_name)
    return my_url


def query_builder_weight(spec_param):
    """This function builds the query form and returns the relevant my_url"""
    # print(f'The following search parameters were chosen: weight, {spec_param}')
    var_name = 'weight_' + spec_param
    var_name = var_name.replace('-', '_2_')

    my_url = queries_url.weight.get(var_name)

    return my_url


def query_builder_hd_type(spec_param):
    """This function builds the query form and returns the relevant my_url"""
    # print(f'The following search parameters were chosen: HD type, {spec_param}')

    var_name = 'HD_type_' + spec_param
    my_url = queries_url.HD_type.get(var_name)
    return my_url
