START_TIME = 8
FINISH_TIME = 19
from data.all_models import *
from utitlities import *

ICON = 'data/deltadent1.png'


DOCTORS = [i.current_name for i in get_without_failing(Doctor, Doctor.id)]
ADMINS = [i.current_name for i in get_without_failing(Admin, Admin.id)]
print(DOCTORS, ADMINS)

POSITIONS = {Admin: 0,
             Doctor: 1

             }

DATABESES_KEYS = {0: Admin,
                  1: Doctor

                  }