from data.all_models import *
from utitlities import *

START_TIME = 8
FINISH_TIME = 19

ENTER_UI = 'ui/enter.ui'
REGISTER_UI = 'ui/register.ui'
SPECIALIST_UI = 'ui/medicalCard.ui'
SCHEDULE_UI = 'ui/schedule.ui'

MAIN_UI = 'ui/main.ui'
MEDICAL_CARD_UI = 'ui/medicalCard.ui'

ICON = 'data/icon.png'

DOCTORS = [i.current_name for i in get_without_failing(Doctor, Doctor.id)]
ADMINS = [i.current_name for i in get_without_failing(Admin, Admin.id)]

POSITIONS = {Admin: 0,
             Doctor: 1

             }

DATABESES_KEYS = {"Администратор": Admin,
                  "Доктор": Doctor

                  }
