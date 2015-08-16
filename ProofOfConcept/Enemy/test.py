from Ogre import Ogre
from Okabe import Okabe
from Simon import Simon
from Link import Link
from battle import battle

ogre = Ogre()
okabe = Okabe()
simon = Simon()
link = Link()

battle([okabe,simon,link],[ogre])
