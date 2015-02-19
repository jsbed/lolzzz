import os

from Robot.configuration.config import Config
from Robot.filler import country_repository_filler


# Initiate configuration
Config().loadConfig()

# Fill Country repository
flags_file_path = os.path.join("resources", "flags.csv")
country_repository_filler.fill_repository_from_file(flags_file_path)
