import MySQLdb
import sys
import yaml
import os
import inspect

# Find the top-level directory for the analyzer
analystTop = os.path.dirname(os.path.dirname(os.path.abspath( inspect.getfile( inspect.currentframe()))))
        
# Use top-level directory to load the config file.
configFile = open( analystTop + "/config.yaml" )
config = yaml.load( configFile )
configFile.close()

try:
    dbConn = MySQLdb.connect( host   = config['database']['host'],
                              user   = config['database']['user'],
                              passwd = config['database']['password'],
                              db     = config['database']['name'] )

except MySQLdb.Error, e:
    print "Error %d: %s" % ( e.args[ 0 ], e.args[ 1 ])
    sys.exit( 1 )

# Tag used for edit_activity entries that don't correspond
# to fresh commits in the repository.
DEFAULT_TAG = "default-tag";

# path to the top of the backup directory, date and time
# directories start right under this.
BACKUP_TOP = config['teambackup']['gitdir']

# Static time interval for backups, if it matters, in seconds
BACKUP_INTERVAL = config['teambackup']['interval']
