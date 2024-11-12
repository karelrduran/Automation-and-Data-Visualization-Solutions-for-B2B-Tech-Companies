import streamlit as st
import plotly.express as px
from src.data_utils import create_companies_dataframe
from src.file_utils import FileUtils
from src.json_utils import JsonUtils


def charts_generator() -> None:

    col1, col2 = st.columns(2)

    with col1:
        contL1 = st.container(border=True)
        contL2 = st.container(border=True)
        contL3 = st.container(border=True)
        contL4 = st.container(border=True)

    with col2:
        contR1 = st.container(border=True)
        contR2 = st.container(border=True)
        contR3 = st.container(border=True)
        contR4 = st.container(border=True)

    with contL1:
        selected_company_data = st.selectbox('Company reporting data:', FileUtils.get_company_data_files_list())

    if selected_company_data is not None:

        data = JsonUtils.read_json(filename=f"data/json/{selected_company_data}")

        companies_data = create_companies_dataframe(data)

        with contR1:
            col3, col4 = st.columns(2)
            # Get the list of available years
            available_years = companies_data['Year'].unique()

            # Year selection via a Streamlit widget
            selected_year = col3.selectbox("Select Year", available_years)

            chart_type = col4.selectbox("Chart type",
                                        ["Bar", "Pie", "Bubble", "Funnel", "Sunburst", "Treemap", "Histogram"])

        # Filter the DataFrame according to the selected yeardo
        filtered_df = companies_data[companies_data['Year'] == selected_year]

        if not filtered_df.empty:

            if chart_type == "Bar":
                fig_investment = px.bar(filtered_df, x='Campaign', y='Investment', color='Company', barmode='group',
                                        title=f"Investments by Campaign for {selected_year}",
                                        hover_data=['Description'])
                fig_roi = px.bar(filtered_df, x='Campaign', y='ROI', color='Company', barmode='group',
                                 title=f"ROI by Campaign for {selected_year}",
                                 hover_data=['Description'])
                fig_success_rate = px.bar(filtered_df, x='Campaign', y='Success Rate', color='Company', barmode='group',
                                          title=f"Success Rate by Campaign for {selected_year}",
                                          hover_data=['Description'])
                fig_sales_increase = px.bar(filtered_df, x='Campaign', y='Sales Increase %', color='Company',
                                            barmode='group',
                                            title=f"Sales Increase % by Campaign for {selected_year}",
                                            hover_data=['Description'])
                fig_social_media = px.bar(filtered_df, x='Campaign', y='Social Media Reach', color='Company',
                                          barmode='group',
                                          title=f"Social Media Reach by Campaign for {selected_year}",
                                          hover_data=['Description'])
            elif chart_type == "Pie":
                fig_investment = px.pie(filtered_df, names='Campaign', values='Investment',
                                        title=f"Investments by Campaign for {selected_year}", hover_data=['Description'])
                fig_roi = px.pie(filtered_df, names='Campaign', values='ROI',
                                 title=f"ROI by Campaign for {selected_year}", hover_data=['Description'])
                fig_success_rate = px.pie(filtered_df, names='Campaign', values='Success Rate',
                                          title=f"Success Rate by Campaign for {selected_year}", hover_data=['Description'])
                fig_sales_increase = px.pie(filtered_df, names='Campaign', values='Sales Increase %',
                                            title=f"Sales Increase % by Campaign for {selected_year}",
                                            hover_data=['Description'])
                fig_social_media = px.pie(filtered_df, names='Campaign', values='Social Media Reach',
                                          title=f"Social Media Reach by Campaign for {selected_year}",
                                          hover_data=['Description'])

            elif chart_type == "Bubble":
                fig_investment = px.scatter(filtered_df, x='Campaign', y='Investment', size='Investment', color='Company',
                                            title=f"Investments by Campaign for {selected_year}",
                                            hover_data=['Description'])
                fig_roi = px.scatter(filtered_df, x='Campaign', y='ROI', size='ROI', color='Company',
                                     title=f"ROI by Campaign for {selected_year}", hover_data=['Description'])
                fig_success_rate = px.scatter(filtered_df, x='Campaign', y='Success Rate', size='Success Rate',
                                              color='Company',
                                              title=f"Success Rate by Campaign for {selected_year}",
                                              hover_data=['Description'])
                fig_sales_increase = px.scatter(filtered_df, x='Campaign', y='Sales Increase %', size='Sales Increase %',
                                                color='Company', title=f"Sales Increase % by Campaign for {selected_year}",
                                                hover_data=['Description'])
                fig_social_media = px.scatter(filtered_df, x='Campaign', y='Social Media Reach', size='Social Media Reach',
                                              color='Company', title=f"Social Media Reach by Campaign for {selected_year}",
                                              hover_data=['Description'])
            elif chart_type == "Funnel":
                fig_investment = px.funnel(filtered_df, x='Campaign', y='Investment', color='Company',
                                           title=f"Investments by Campaign for {selected_year}",
                                           hover_data=['Description'])
                fig_roi = px.funnel(filtered_df, x='Campaign', y='ROI', color='Company',
                                    title=f"ROI by Campaign for {selected_year}",
                                    hover_data=['Description'])
                fig_success_rate = px.funnel(filtered_df, x='Campaign', y='Success Rate', color='Company',
                                             title=f"Success Rate by Campaign for {selected_year}",
                                             hover_data=['Description'])
                fig_sales_increase = px.funnel(filtered_df, x='Campaign', y='Sales Increase %', color='Company',
                                               title=f"Sales Increase % by Campaign for {selected_year}",
                                               hover_data=['Description'])
                fig_social_media = px.funnel(filtered_df, x='Campaign', y='Social Media Reach', color='Company',
                                             title=f"Social Media Reach by Campaign for {selected_year}",
                                             hover_data=['Description'])
            elif chart_type == "Sunburst":
                fig_investment = px.sunburst(filtered_df, path=['Company', 'Campaign'], values='Investment',
                                             title=f"Investments by Campaign for {selected_year}",
                                             hover_data=['Description'])
                fig_roi = px.sunburst(filtered_df, path=['Company', 'Campaign'], values='ROI',
                                      title=f"ROI by Campaign for {selected_year}",
                                      hover_data=['Description'])
                fig_success_rate = px.sunburst(filtered_df, path=['Company', 'Campaign'], values='Success Rate',
                                               title=f"Success Rate by Campaign for {selected_year}",
                                               hover_data=['Description'])
                fig_sales_increase = px.sunburst(filtered_df, path=['Company', 'Campaign'], values='Sales Increase %',
                                                 title=f"Sales Increase % by Campaign for {selected_year}",
                                                 hover_data=['Description'])
                fig_social_media = px.sunburst(filtered_df, path=['Company', 'Campaign'], values='Social Media Reach',
                                               title=f"Social Media Reach by Campaign for {selected_year}",
                                               hover_data=['Description'])
            elif chart_type == "Treemap":
                fig_investment = px.treemap(filtered_df, path=['Company', 'Campaign'], values='Investment',
                                            title=f"Investments by Campaign for {selected_year}",
                                            hover_data=['Description'])
                fig_roi = px.treemap(filtered_df, path=['Company', 'Campaign'], values='ROI',
                                     title=f"ROI by Campaign for {selected_year}",
                                     hover_data=['Description'])
                fig_success_rate = px.treemap(filtered_df, path=['Company', 'Campaign'], values='Success Rate',
                                              title=f"Success Rate by Campaign for {selected_year}",
                                              hover_data=['Description'])
                fig_sales_increase = px.treemap(filtered_df, path=['Company', 'Campaign'], values='Sales Increase %',
                                                title=f"Sales Increase % by Campaign for {selected_year}",
                                                hover_data=['Description'])
                fig_social_media = px.treemap(filtered_df, path=['Company', 'Campaign'], values='Social Media Reach',
                                              title=f"Social Media Reach by Campaign for {selected_year}",
                                              hover_data=['Description'])
            elif chart_type == "Histogram":
                fig_investment = px.histogram(filtered_df, x='Investment', color='Company',
                                              title=f"Investment Distribution for {selected_year}",
                                              hover_data=['Description'])
                fig_roi = px.histogram(filtered_df, x='ROI', color='Company',
                                       title=f"ROI Distribution for {selected_year}",
                                       hover_data=['Description'])
                fig_success_rate = px.histogram(filtered_df, x='Success Rate', color='Company',
                                                title=f"Success Rate Distribution for {selected_year}",
                                                hover_data=['Description'])
                fig_sales_increase = px.histogram(filtered_df, x='Sales Increase %', color='Company',
                                                  title=f"Sales Increase % Distribution for {selected_year}",
                                                  hover_data=['Description'])
                fig_social_media = px.histogram(filtered_df, x='Social Media Reach', color='Company',
                                                title=f"Social Media Reach Distribution for {selected_year}",
                                                hover_data=['Description'])

            contL2.plotly_chart(fig_investment, use_container_width=True)
            contR2.plotly_chart(fig_roi, use_container_width=True)
            contL3.plotly_chart(fig_success_rate, use_container_width=True)
            contR3.plotly_chart(fig_sales_increase, use_container_width=True)
            contL4.plotly_chart(fig_social_media, use_container_width=True)

            # Display recommendations by company

            for company in data['companies']:
                contR4.subheader(f"Recommendations for {company['name']}")
                contR4.write(company['recommendations'])
        else:
            st.write(f"No data available for {selected_year}")
    else:
        st.error("There are no data to display, you must first generate data.")
