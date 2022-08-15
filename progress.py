import sqlite3


def get_value(table, column, condition):
    connection = sqlite3.connect('progress.db')
    cursor = connection.cursor()
    if condition:
        cursor.execute(f"""
        SELECT "{column}" FROM "{table}" WHERE {condition}
        """)
    else:
        cursor.execute(f"""
        SELECT "{column}" FROM "{table}"
        """)
    value = cursor.fetchall()
    connection.close()
    return value[0][0]


def update_value(table, column, condition, new_value):
    connection = sqlite3.connect('progress.db')
    if condition:
        connection.execute(f"""
            UPDATE "{table}" SET "{column}"={new_value} WHERE {condition}
            """)
    else:
        connection.execute(f"""
            UPDATE "{table}" SET "{column}"={new_value}
            """)
    connection.commit()
    connection.close()


def update_game_progress(passed_level):
    import basics
    if passed_level not in basics.PASSED_LEVELS:
        if basics.PASSED_LEVELS != '':
            updated_value = f'"{basics.PASSED_LEVELS},{passed_level}"'
            update_value('Level Progress', 'passed_levels', None, updated_value)
        else:
            update_value('Level Progress', 'passed_levels', None, f'"{passed_level}"')
        basics.PASSED_LEVELS = get_value('Level Progress', 'passed_levels', None)
        basics.PASSED_LEVELS_LIST = basics.PASSED_LEVELS.split(',')
        if len(basics.BALL_SHAPES) != len(basics.AVAILABLE_SHAPES.split(',')):
            updated_value = f'"{basics.AVAILABLE_SHAPES},{basics.BALL_SHAPES[len(basics.AVAILABLE_SHAPES.split(","))]}"'
            update_value('Ball Shapes', 'available', None, updated_value)
            basics.AVAILABLE_SHAPES = get_value('Ball Shapes', 'available', None)
            return True
    else:
        return False
