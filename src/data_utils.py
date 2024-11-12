import pandas as pd


def create_companies_dataframe(data: dict) -> pd.DataFrame:
    """
    Create a Pandas DataFrame from nested dictionary data containing information about companies and their campaigns.

    Args:
        data (dict): Nested dictionary containing company and campaign data.

    Returns:
        pd.DataFrame: DataFrame containing company campaign data with columns:
            - 'Company': Name of the company
            - 'Campaign': Name of the campaign
            - 'Year': Year of the campaign
            - 'Investment': Investment made in the campaign
            - 'ROI': Return on Investment (ROI) of the campaign
            - 'Success Rate': Success rate of the campaign
            - 'Sales Increase %': Percentage increase in sales due to the campaign
            - 'Social Media Reach': Reach of the campaign on social media
            - 'Description': Description of the campaign
    """
    campaign_data = []
    for company in data['companies']:
        for campaign in company['campaigns']:
            campaign_data.append({
                'Company': company['name'],
                'Campaign': campaign['name'],
                'Year': campaign['year'],
                'Investment': campaign['investment'],
                'ROI': campaign['ROI'],
                'Success Rate': campaign['success_rate'],
                'Sales Increase %': campaign['sales_increase_percent'],
                'Social Media Reach': campaign['social_media_reach'],
                'Description': campaign['description']
            })

    df = pd.DataFrame(campaign_data)

    return df
