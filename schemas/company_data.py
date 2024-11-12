from typing import List, Optional
from pydantic import BaseModel, field_validator


class Campaign(BaseModel):
    """
    Represents a marketing campaign with specific attributes.

    Attributes:
        name (str): Name of the campaign.
        description (Optional[str]): Description of the campaign (optional).
        year (int): Year when the campaign took place.
        investment (float): Investment made in the campaign.
        ROI (float): Return on Investment (ROI) achieved by the campaign.
        sales_increase_percent (Optional[float]): Percentage increase in sales due to the campaign (optional).
        social_media_reach (Optional[float]): Reach of the campaign on social media (optional).
        success_rate (float): Success rate of the campaign, must be between 0 and 1.

    Raises:
        ValueError: If success_rate is not between 0 and 1.
    """
    name: str
    description: Optional[str] = None
    year: int
    investment: float
    ROI: float
    sales_increase_percent: Optional[float] = None
    social_media_reach: Optional[float] = None
    success_rate: float

    @field_validator('success_rate')
    def check_success_rate(cls, v):
        """
        Validator to ensure success_rate is between 0 and 1.

        Args:
            v (float): Value of success_rate to validate.

        Returns:
            float: Validated success_rate.

        Raises:
            ValueError: If success_rate is not between 0 and 1.
        """
        if not 0 <= v <= 1:
            raise ValueError('success_rate must be between 0 and 1')
        return v


class Company(BaseModel):
    """
    Represents a company with its marketing campaigns and aggregated metrics.

    Attributes:
        name (str): Name of the company.
        campaigns (List[Campaign]): List of Campaign objects representing the company's campaigns.
        total_investment (float): Total investment made by the company across all campaigns.
        total_return (float): Total return achieved by the company across all campaigns.
        total_successes (float): Total number of successful campaigns.
        total_failures (float): Total number of failed campaigns.
        total_success_rate (float): Overall success rate of the company's campaigns, must be between 0 and 1.
        overall_ROI (float): Overall Return on Investment (ROI) achieved by the company.
        recommendations (Optional[str]): Recommendations for the company (optional).

    Raises:
        ValueError: If total_success_rate is provided and not between 0 and 1.
    """
    name: str
    campaigns: List[Campaign]
    total_investment: float
    total_return: float
    total_successes: float
    total_failures: float
    total_success_rate: float
    overall_ROI: float
    recommendations: Optional[str] = None

    @field_validator('total_success_rate')
    def check_total_success_rate(cls, v):
        """
        Validator to ensure total_success_rate is between 0 and 1.

        Args:
            v (float): Value of total_success_rate to validate.

        Returns:
            float: Validated total_success_rate.

        Raises:
            ValueError: If total_success_rate is provided and not between 0 and 1.
        """
        if v is not None and not 0 <= v <= 1:
            raise ValueError('total_success_rate must be between 0 and 1')
        return v


class CompanyData(BaseModel):
    """
    Represents structured data containing multiple companies and their details.

    Attributes:
        companies (List[Company]): List of Company objects representing multiple companies.

    """
    companies: List[Company]
