from src.DataScienceProject import logger
import pandas as pd
import os
import joblib
from sklearn.linear_model import ElasticNet
from src.DataScienceProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config: ModelTrainerConfig ):
        self.config = config
    
    def train(self):
        train_data = pd.read_csv(self.config.train_path)
        test_data = pd.read_csv(self.config.test_path)

        target_col = str(self.config.target_column)

        train_x = train_data.drop([target_col], axis=1)
        train_y = train_data[target_col]
        test_x = test_data.drop([target_col], axis=1)
        test_y = test_data[target_col]

        lr = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )
        lr.fit(train_x, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
