from socket import gethostname
from os.path import expanduser, join
from os import environ

hostname = gethostname()
dropbox_home = environ["DROPBOX_HOME"] if environ.has_key("DROPBOX_HOME") else join(expanduser("~"), "Dropbox")
dbssh_home = join(dropbox_home, "dbssh", hostname)

