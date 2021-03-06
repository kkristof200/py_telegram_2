# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# System
from enum import Enum

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- enum: ChatType -------------------------------------------------------- #

class ChatType(Enum):
    Private    = 'private'
    Group      = 'group'
    SuperGroup = 'supergroup'
    Channel    = 'channel'


# -------------------------------------------------------------------------------------------------------------------------------- #