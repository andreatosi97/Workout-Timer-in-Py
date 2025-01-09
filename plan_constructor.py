# Block of same exercises
class ExerciseBlock:
    def __init__(self, name, single_rep_secs, sets_plan):
        self.name = name
        self.single_rep_secs = single_rep_secs
        self.sets_plan = sets_plan


### PLAN ( where single_set = ("reps", "chilos", "rest") )

## 1 ##


# set Biceps: 4 + 1
def biceps_block():
    sets_plan = [
        (6, 4, "1:00"),
        (6, 4, "1:00"),
        (6, 4, "1:00"),
        (6, 4, "1:00"),
    ]
    return [ExerciseBlock("Biceps", 3, sets_plan)]


# set Triceps: 3
def triceps_block():
    sets_plan = [
        (6, 2, "1:00"),
        (6, 2, "1:00"),
        (6, 2, "1:00"),
    ]
    return [ExerciseBlock("Triceps", 3, sets_plan)]


# set Chest: 4
def chest_block():
    sets_plan = [
        (6, 6, "1:00"),
        (6, 6, "1:00"),
        (6, 6, "1:00"),
        (6, 6, "1:00"),
    ]
    return [ExerciseBlock("Chest", 4, sets_plan)]


# set Legs: 5
def legs_block():
    sets_plan = [
        (6, 8, "1:00"),
        (6, 8, "1:00"),
        (6, 8, "1:00"),
        (6, 8, "1:00"),
        (6, 8, "0:00"),
    ]
    return [ExerciseBlock("Legs", 4, sets_plan)]


## 2 ##


# set Lateral Delts: 4
def latdelts_block():
    sets_plan = [
        (6, 2, "1:00"),
        (6, 2, "1:00"),
        (6, 2, "1:00"),
        (6, 2, "1:00"),
    ]
    return [ExerciseBlock("Lateral Delts", 3, sets_plan)]


# set Anterior Delts: 2
def anteriordelts_block():
    sets_plan = [
        (6, 4, "1:00"),
        (6, 4, "1:00"),
    ]
    return [ExerciseBlock("Anterior Delts", 4, sets_plan)]


# set Abs: 6
def abs_block():
    sets_plan = [
        (6, 0, "1:00"),
        (6, 0, "1:00"),
        (6, 6, "1:00"),
        (6, 6, "1:00"),
        (6, 6, "1:00"),
        (6, 4, "1:00"),
    ]
    return [ExerciseBlock("Abs", 4, sets_plan)]


# set Back: 4
def back_block():
    sets_plan = [
        (6, 6, "1:00"),
        (6, 6, "1:00"),
        (6, 4, "1:00"),
        (6, 2, "0:00"),
    ]
    return [ExerciseBlock("Back", 4, sets_plan)]


def constructor(plan_number):
    if plan_number == 1:
        return biceps_block() + triceps_block() + chest_block() + legs_block()
    else:
        return latdelts_block() + anteriordelts_block() + abs_block() + back_block()
