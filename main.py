from AuthorizationWindow import run_authorization
from MainActivityWindow import *
import pypyodbc

# run_authorization()
c = Main_activity_window()
#
con = c.connection()
c.cursor(con, "Смета")
# c.show()