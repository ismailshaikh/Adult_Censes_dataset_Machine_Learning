import yaml
from income_census.exception import IC_Exception
import os,sys
import json
import os







def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML File and returns the contents as a dictionary.
    file_path: str
    """
    try:

        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise IC_Exception(e,sys) from e





def read_kaggle_creds():
    try:

        if os.path.exists('D:\Education Ds\Ineoron_DS\ML\Project\Adult_Censes_dataset_Machine_Learning\kaggle.json'):

            with open('D:\Education Ds\Ineoron_DS\ML\Project\Adult_Censes_dataset_Machine_Learning\kaggle.json', 'r') as f:
                key = f.read()
                data = json.loads(key)

                if 'username' in data and 'key' in data:
                    os.environ['KAGGLE_USERNAME'] = data['username']
                    os.environ['KAGGLE_KEY'] = data['key']
                    return True

    except Exception as e:
        raise IC_Exception(e,sys) from e




