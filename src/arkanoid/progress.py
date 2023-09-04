import sqlite3
from arkanoid import constants


def get_value(table, column, condition=None):
    connection = sqlite3.connect('arkanoid/progress.db')
    cursor = connection.cursor()
    if condition:
        cursor.execute(f"SELECT {column} FROM {table} WHERE {condition}")
    else:
        cursor.execute(f"SELECT {column} FROM {table}")
    value = cursor.fetchall()
    cursor.close()
    connection.close()
    return value[0][0]


def update_value(table, column, new_value, condition=None):
    connection = sqlite3.connect('arkanoid/progress.db')
    cursor = connection.cursor()
    if condition:
        cursor.execute(f"UPDATE {table} SET {column}=? WHERE {condition}", (new_value,)) # execute() method expects the binding values to be supplied as a tuple, even when passing a single value. That's why the comma is added to make sure the values are correctly treated as a tuple, regardless of whether there's one or more values being passed
    else:
        cursor.execute(f"UPDATE {table} SET {column}=?", (new_value,))
    connection.commit()
    cursor.close()
    connection.close()


def update_game_progress(passed_level):
    if constants.PASSED_LEVELS != '':
        updated_value = f'{constants.PASSED_LEVELS},{passed_level}'
        update_value('level_progress', 'passed_levels', updated_value)
    else:
        update_value('level_progress', 'passed_levels', passed_level)
    constants.PASSED_LEVELS = get_value('level_progress', 'passed_levels')
    constants.PASSED_LEVELS_LIST = constants.PASSED_LEVELS.split(',')
    if len(constants.BALL_SHAPES) != len(constants.AVAILABLE_SHAPES.split(',')):
        updated_value = f'{constants.AVAILABLE_SHAPES},{constants.BALL_SHAPES[len(constants.AVAILABLE_SHAPES.split(","))]}'
        update_value('ball_shapes', 'available', updated_value)
        constants.AVAILABLE_SHAPES = get_value('ball_shapes', 'available')
