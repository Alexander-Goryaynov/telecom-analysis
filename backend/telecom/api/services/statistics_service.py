from typing import Dict, List
from pandas import DataFrame, read_csv
from sklearn.cluster import KMeans
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from seaborn import scatterplot, color_palette
from base64 import b64encode
import os

class StatisticsService:

    COMPANY_NAME_COL_NAME = 'company_name'
    MARKET_CAP_COL_NAME = 'market_cap'
    STOCK_PRICE_COL_NAME = 'stock_price'
    DAILY_GAIN_COL_NAME = 'daily_gain'
    COUNTRY_NAME_COL_NAME = 'country'

    _dataset: DataFrame

    def __init__(self, dataset_path: str) -> None:
        self._dataset = read_csv(dataset_path)

    def get_market_cap_info(self) -> Dict:
        #
        max_index = self._get_max_value_index(self._dataset, self.MARKET_CAP_COL_NAME)
        max_row = self._dataset.iloc[max_index]
        max_company_name = max_row[self.COMPANY_NAME_COL_NAME]
        max_cap = max_row[self.MARKET_CAP_COL_NAME]
        #
        min_index = self._get_min_value_index(self._dataset, self.MARKET_CAP_COL_NAME)
        min_row = self._dataset.iloc[min_index]
        min_company_name = min_row[self.COMPANY_NAME_COL_NAME]
        min_cap = min_row[self.MARKET_CAP_COL_NAME]
        #
        median_index = self._get_median_index(self._dataset, self.MARKET_CAP_COL_NAME)
        median_row = self._dataset.iloc[median_index]
        median_company_name = median_row[self.COMPANY_NAME_COL_NAME]
        median_cap = median_row[self.MARKET_CAP_COL_NAME]
        return {
            "max": {
                "value": max_cap, 
                "companyName": max_company_name
            },
            "min": {
                "value": min_cap, 
                "companyName": min_company_name
            },
            "median": {
                "value": median_cap, 
                "companyName": median_company_name
            },
            "avg": self._get_avg_value(self._dataset, self.MARKET_CAP_COL_NAME)             
        }

    def get_stock_price_info(self) -> Dict:
        #
        max_index = self._get_max_value_index(self._dataset, self.STOCK_PRICE_COL_NAME)
        max_row = self._dataset.iloc[max_index]
        max_company_name = max_row[self.COMPANY_NAME_COL_NAME]
        max_stock_price = max_row[self.STOCK_PRICE_COL_NAME]
        #
        min_index = self._get_min_value_index(self._dataset, self.STOCK_PRICE_COL_NAME)
        min_row = self._dataset.iloc[min_index]
        min_company_name = min_row[self.COMPANY_NAME_COL_NAME]
        min_stock_price = min_row[self.STOCK_PRICE_COL_NAME]
        #
        median_index = self._get_median_index(self._dataset, self.STOCK_PRICE_COL_NAME)
        median_row = self._dataset.iloc[median_index]
        median_company_name = median_row[self.COMPANY_NAME_COL_NAME]
        median_stock_price = median_row[self.STOCK_PRICE_COL_NAME]
        return {
            "max": {
                "value": max_stock_price, 
                "companyName": max_company_name
            },
            "min": {
                "value": min_stock_price, 
                "companyName": min_company_name
            },
            "median": {
                "value": median_stock_price, 
                "companyName": median_company_name
            },
            "avg": self._get_avg_value(self._dataset, self.STOCK_PRICE_COL_NAME)             
        }

    def get_loss_gain_info(self) -> Dict:
        max_gain_index = self._get_max_value_index(self._dataset, self.DAILY_GAIN_COL_NAME, only_positive=True)
        max_gain_row = self._dataset.iloc[max_gain_index]
        max_gain_company_name = max_gain_row[self.COMPANY_NAME_COL_NAME]
        max_gain = max_gain_row[self.DAILY_GAIN_COL_NAME]
        #
        avg_gain = self._get_avg_from_range(self._dataset, self.DAILY_GAIN_COL_NAME, only_positive=True)
        #
        max_loss_index = self._get_max_value_index(self._dataset, self.DAILY_GAIN_COL_NAME, only_negative=True)
        max_loss_row = self._dataset.iloc[max_loss_index]
        max_loss_company_name = max_loss_row[self.COMPANY_NAME_COL_NAME]
        max_loss = max_loss_row[self.DAILY_GAIN_COL_NAME]
        #
        avg_loss = self._get_avg_from_range(self._dataset, self.DAILY_GAIN_COL_NAME, only_negative=True)
        return {
            "gain": {
                "max": {
                    "value": max_gain,
                    "companyName": max_gain_company_name
                },
                "avg": avg_gain
            },
            "loss": {
                "max": {
                    "value": max_loss,
                    "companyName": max_loss_company_name
                },
                "avg": avg_loss
            },
        }
    
    def get_companies_count_by_country(self) -> List:
        groupping_result = self._get_count_in_groups(self._dataset, self.COUNTRY_NAME_COL_NAME)
        result = []
        for country_name, companies_count in groupping_result.items():
            result.append({"countryName": country_name, "companiesCount": companies_count})
        return result

    def get_companies_total_cap_by_country(self) -> List:
        groupping_result = self._get_sum_in_groups(self._dataset, self.COUNTRY_NAME_COL_NAME, self.MARKET_CAP_COL_NAME)
        result = []
        for country_name, total_cap in groupping_result.items():
            result.append({"countryName": country_name, "totalCap": total_cap})
        return result

    def get_companies_clusters(self) -> Dict:
        plot_image_path = r'..\storage\clusterization_result.png'
        current_folder = os.path.dirname(os.path.abspath(__file__))
        destination_file = os.path.join(current_folder, plot_image_path)
        if (os.path.exists(destination_file)):
            os.remove(destination_file)
        kmeans_input_data = self._dataset[[
            self.MARKET_CAP_COL_NAME, 
            self.DAILY_GAIN_COL_NAME
        ]]
        kmeans = KMeans(n_clusters=3, random_state=0).fit(kmeans_input_data)
        scatterplot(
            x=self._dataset.market_cap,
            y=self._dataset.daily_gain,
            hue=kmeans.labels_,
            palette=color_palette("colorblind", n_colors=3),
            legend=None,
        )
        estimator = make_pipeline(StandardScaler(), kmeans).fit(kmeans_input_data)
        plt.savefig(destination_file)
        plt.close()
        plotBase64 = "data:image/png;base64," + b64encode(open(destination_file, "rb").read()).decode()
        result = {
            "plotBase64": plotBase64,
            "inertiaValue": estimator[-1].inertia_
        }
        return result

    def _get_max_value_index(self, 
            dataset: DataFrame, 
            col_name: str, 
            only_positive: bool=False, 
            only_negative: bool=False
            ) -> int:
        max = 0
        max_i = 0
        for i, row in dataset.iterrows():
            if (i == 0):
                max = row[col_name]
                continue
            if (only_positive and row[col_name] > 0 and row[col_name] > max):
                max = row[col_name]
                max_i = i
                continue
            if (only_negative and row[col_name] < 0 and row[col_name] < max):
                max = row[col_name]
                max_i = i
                continue
            if (only_positive == False and only_negative == False and row[col_name] > max):
                max = row[col_name]
                max_i = i
        return max_i
    
    def _get_min_value_index(self, dataset: DataFrame, col_name: str) -> int:
        min = 0
        min_i = 0
        for i, row in dataset.iterrows():
            if (i == 0):
                min = row[col_name]
                continue
            if (row[col_name] < min):
                min = row[col_name]
                min_i = i
        return min_i

    def _get_median_index(self, dataset: DataFrame, col_name: str) -> int:
        dataset_copy = dataset.copy()
        sorted_dataset = dataset_copy.sort_values([col_name])
        dataset_length = dataset.shape[0]
        median_row_sorted_index = int(dataset_length / 2) - 1 if (dataset_length % 2 == 0) else int(dataset_length / 2)
        median_row = sorted_dataset.iloc[median_row_sorted_index]
        median_company_name = median_row[self.COMPANY_NAME_COL_NAME]
        for i, row in dataset.iterrows():
            if (row[self.COMPANY_NAME_COL_NAME] == median_company_name):
                return i

    def _get_avg_value(self, dataset: DataFrame, col_name: str) -> float:
        return dataset[col_name].mean()

    def _get_avg_from_range(
            self, 
            dataset: DataFrame, 
            col_name: str,
            only_positive: bool=False, 
            only_negative: bool=False
            ) -> float:
        count = 0
        sum = 0
        for i, row in dataset.iterrows():
            if ((only_positive and row[col_name] > 0) or (only_negative and row[col_name] < 0)):
                count += 1
                sum += row[col_name]
        return sum / count
    
    def _get_count_in_groups(self, dataset: DataFrame, group_by_col_name: str) -> Dict:
        result = {}
        for _, row in dataset.iterrows():
            if row[group_by_col_name] in result:
                result[row[group_by_col_name]] += 1
            else:
                result[row[group_by_col_name]] = 1
        return result
    
    def _get_sum_in_groups(self, dataset: DataFrame, group_by_col_name: str, sum_by_col_name: str) -> Dict:
        result = {}
        for _, row in dataset.iterrows():
            if row[group_by_col_name] in result:
                result[row[group_by_col_name]] += row[sum_by_col_name]
            else:
                result[row[group_by_col_name]] = row[sum_by_col_name]
        return result