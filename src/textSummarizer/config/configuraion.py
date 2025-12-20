import sys
import os
from pathlib import Path

# Use absolute path to project root
project_root = Path(r"C:\Users\madar\Text-Summarizer")
print(f"Project root: {project_root}")

# Change to project root
os.chdir(project_root)
print(f"Current directory: {Path.cwd()}")

# Verify config files exist
config_file = project_root / "config" / "config.yaml"
params_file = project_root / "params.yaml"

print(f"Config file exists: {config_file.exists()}")
print(f"Params file exists: {params_file.exists()}")

# Add src to path
sys.path.insert(0, str(project_root / "src"))

# Define paths
CONFIG_FILE_PATH = config_file
PARAMS_FILE_PATH = params_file

from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig)
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])

    

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config