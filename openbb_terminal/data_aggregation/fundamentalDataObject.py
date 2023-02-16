import pandas as pd
import numpy as np
from polygonProvider import PolygonProvider


API_POLYGON_KEY = "INSERT"


class FundamentalDataObject:
    """OpenBB stock object"""

    def __init__(self):
        self.fundamental_schema = {  # base schema
            "price": float,
            "beta": float,
            "market_cap": float,
            "exchange": str,
            "industry": str,
            "website": str,
            "description": str,
            "isin": str,
            "eps": float,
            "dividend_yield": float,
            "free_cash_flow_yield": float,
            "debt_equity": float,
            "return_on_equity": float,
        }

        # metadata
        self.api_name = None
        self.symbol = None
        self.fundamental_data = None
        self.verified = False

    def load_from_api(
        self,
        api_key: str,
        api_name: str,
        symbol: str,
    ) -> pd.DataFrame:
        """Load stock data from API

        Args:
            api (str): api to use
            symbol (str): stock symbol

        Returns:
            pd.DataFrame: stock data from API
        """
        self.api_name = api_name
        self.symbol = symbol
        self.fundamental_data = pd.DataFrame()
        if self.api_name == "polygon":
            self.fundamental_data = PolygonProvider().load_fundamental_data(
                api_key=api_key,
                symbol=self.symbol,
            )
        else:
            raise ValueError("API not supported")
        return self.fundamental_data
