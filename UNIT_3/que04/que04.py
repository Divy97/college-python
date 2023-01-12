# Write a Python program that creates a package called “SEM6” which consists of core.py,
# foundation.py and elective.py. core.py contains 3 function called python(), infosec(),
# android(), ios(). foundation.py contains 2 function called erp() and mis(). Also
# elective.py contains 3 functions called joomla(), ror() and drupal(). Create one main file
# outside the SEM6 package and import SEM6 to access core.py, elective.py and
# foundation.py file using init.py file. Call all the functions in main file using the concept
# of Package.

from SEM_6 import core, elective, foundation


core.android()
core.infoSec()
core.ios()
core.android()

foundation.erp()
foundation.mis()

elective.drupal()
elective.joomla()
elective.ror()
