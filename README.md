# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Waste Collection Data Analysis: England 2024–2025

## Project Overview

This project analyses waste collection and recycling data for England for the 2024–2025 reporting year. I used Python, Pandas and data visualisation techniques to explore recorded recycling tonnage across reporting periods, local authorities and material categories.

I also examined recorded rejected recycling, co-mingled collection responses, and the relationship between household coverage and recycling tonnage. I developed an interactive Streamlit dashboard to present the findings through summary figures, charts and filters.

The aim of this project was to identify patterns in the recorded data, communicate the findings clearly and make the results easier to explore. The analysis focuses on the information available in the dataset and does not claim to explain every factor affecting recycling performance.

## Dataset Content

The dataset was obtained from the UK Government's data.gov.uk website and published by the Department for Environment, Food and Rural Affairs (Defra).

It contains information about waste collection in England, including local authorities, reporting periods, collection measures, material categories and recorded tonnage.

**Dataset source:** [Waste Data Flow – data.gov.uk](https://www.data.gov.uk/dataset/0e0c12d8-24f6-461f-b4bc-f6d6a5bf2de5/waste-data-flow)

**Data publisher:** Department for Environment, Food and Rural Affairs (Defra)

**Licence:** Open Government Licence, as identified for the source data.

The analysis focuses on the four reporting periods covering April 2024 to March 2025.

## Business Requirements

The project addresses the following business requirements:

1. Identify changes in recorded recycling tonnage across the four reporting periods.
2. Compare recorded recycling tonnage across local authorities.
3. Identify the materials with the highest recorded recycling tonnage.
4. Explore recorded co-mingled collection responses and rejected recycling.
5. Investigate the relationship between household coverage and recorded recycling tonnage.
6. Present the findings in an interactive Streamlit dashboard with filters.

These requirements guided my data preparation, exploratory data analysis, visualisations and dashboard development.

## Hypothesis and Validation

### Hypothesis

I expected recorded recycling tonnage to vary across reporting periods, local authorities and material categories.

### How I validated the hypothesis

I used Python and Pandas to group and compare recycling tonnage by reporting period, local authority and material category. I used summary statistics and charts to identify patterns and differences in the recorded figures.

I also examined rejected recycling and co-mingled collection responses. In addition, I compared household coverage for co-mingled materials with recorded recycling tonnage and calculated the Pearson correlation coefficient.

The analysis supported my hypothesis that recorded recycling tonnage varied across the dataset. However, these comparisons identify patterns and associations rather than establish the causes of the differences.

## Project Plan

### High-level steps taken for the analysis

1. I obtained the waste collection dataset from the UK Government's data.gov.uk website.
2. I loaded and inspected the dataset using Python and Pandas.
3. I selected the relevant records for kerbside waste collection.
4. I cleaned the relevant data, converted the required tonnage values to numeric format and checked for missing values.
5. I explored recorded recycling tonnage by reporting period, local authority and material category.
6. I examined recorded rejected recycling, co-mingled collection responses and household coverage.
7. I created charts and summary statistics to communicate the findings.
8. I prepared a cleaned CSV file for the dashboard.
9. I developed and tested an interactive Streamlit dashboard.
10. I documented the findings, limitations and possible future improvements.

### Data management throughout the project

I obtained the dataset from data.gov.uk and loaded it into Python using Pandas. I inspected its structure, columns, data types and missing values before selecting the relevant records.

I cleaned the selected data, converted the required values to numeric format and prepared separate dataframes for different parts of the analysis. I then saved the cleaned recycling data as a CSV file for use in the dashboard.

I used grouping, aggregation, summary statistics and charts to examine the recorded figures. I also considered the limitations of the dataset when interpreting the results. The prepared CSV file supports consistency between my analysis and dashboard.

### Research methodology

I chose a quantitative approach because the dataset contains numerical information about waste collection and recycling tonnage. I used exploratory data analysis to identify patterns and differences across reporting periods, local authorities and material categories.

Pandas was suitable for filtering, grouping and summarising the records. Matplotlib helped me present comparisons visually, while Streamlit allowed me to build an interactive dashboard.

These methods were appropriate for exploring the available data. However, descriptive analysis alone cannot establish why the recorded figures differ.

## Data Analysis and Visualisations

I selected visualisations that addressed the business requirements and helped communicate the findings.

### Recorded recycling tonnage by reporting period

I used a bar chart to compare recorded recycling tonnage across the four reporting periods. This helped me identify the highest and lowest recorded totals.

I also used a line chart to show the change in recorded recycling tonnage across the reporting periods.

### Top 10 local authorities by recorded recycling tonnage

I used a bar chart to compare the ten local authorities with the highest recorded recycling tonnage. This made it easier to identify authorities with the largest recorded totals in the selected measure.

### Recorded recycling tonnage for the top five local authorities

I used a line chart to compare the recorded recycling tonnage of the five local authorities with the highest totals across the four reporting periods. This helped me examine how their recorded figures changed over time.

### Leading recycling materials

I used a pie chart to show the share of recorded tonnage represented by the five materials with the highest totals. This helped me compare the contribution of the leading material categories to the recorded total.

### Rejected recycling

I examined the recorded amount of recycling material collected but subsequently rejected or disposed of. I compared this amount with the total recorded recycling tonnage.

The recorded rejected amount was 1,756.011 tonnes, compared with approximately 7.20 million tonnes of recorded recycling tonnage. This represents approximately 0.024% of the recorded recycling total.

I treated this percentage as a comparison of the recorded measures, rather than an official recycling rejection rate, because the definitions and reporting of the measures would need to be confirmed before making a broader claim.

### Co-mingled collection responses

I used a bar chart to compare the recorded Yes and No responses for co-mingled collection.

The dataset contained 3,113 No responses and 1,096 Yes responses. These represented 73.96% and 26.04% of the recorded responses respectively.

These percentages describe the responses in the selected records. They should not be interpreted as the percentage of all local authorities using or not using co-mingled collection, because authorities may have multiple records across materials and reporting periods.

### Household coverage and recycling tonnage

I compared recorded recycling tonnage with the number of households reported as receiving a co-mingled materials collection. The comparison included 282 local authorities and 1,124 matched authority-period records.

The Pearson correlation coefficient was 0.757, indicating a strong positive relationship between the two recorded measures.

This suggests that authorities reporting higher household coverage generally also recorded higher recycling tonnage. However, correlation does not prove causation. Differences in population size, waste generation and local collection arrangements may influence the results.

## Main Findings

My analysis identified several patterns in the recorded waste collection data.

- **Changes across reporting periods:** Total recorded recycling tonnage decreased across the four reporting periods, from approximately 2.12 million tonnes in April–June 2024 to approximately 1.49 million tonnes in January–March 2025.
- **Differences between local authorities:** The recorded recycling totals varied between authorities.
- **Differences between materials:** Co-mingled materials and green garden waste only accounted for the largest recorded material tonnages in the selected measure.
- **Rejected recycling:** The recorded rejected amount was small compared with the total recorded recycling tonnage, although the comparison should not be treated as an official rejection rate.
- **Co-mingled collection:** No was the more common response in the selected records.
- **Household coverage:** Household coverage and recorded recycling tonnage showed a strong positive association, with a correlation coefficient of 0.757.

These findings describe the available records. They do not, on their own, explain why the differences occurred or establish the overall recycling performance of each local authority.

## Preparing Data for the Dashboard

I prepared a cleaned dashboard dataset using the selected recycling records. I retained the columns needed for the dashboard:

- `Authority`
- `Period`
- `RowText`
- `Recycling_Tonnage`

I renamed the numeric tonnage column to `Recycling_Tonnage`, removed records with missing values in that column and checked the resulting dataset.

The cleaned dashboard dataset contains 6,330 records and four columns, with no missing values in those columns.

I saved the prepared data as `cleaned_recycling_dashboard.csv` for use by the Streamlit application.

## Interactive Dashboard

### Dashboard purpose

I developed an interactive Streamlit dashboard to make the findings easier to explore. It presents summary figures and charts in one place and allows users to filter the data by reporting period and local authority.

### Dashboard features

The dashboard contains one main page titled **Waste Collection Data Analysis: England 2024–2025**.

Its features include:

- **Introduction:** A short explanation of the dashboard's purpose.
- **Reporting-period filter:** Allows users to select the reporting periods they want to explore.
- **Local-authority filter:** Allows users to focus on selected authorities.
- **Key figures:** Three metric cards showing recorded recycling tonnage, the number of local authorities and the number of material categories in the filtered data.
- **Bar chart:** Compares recorded recycling tonnage by reporting period.
- **Pie chart:** Shows the share of recorded tonnage represented by the five materials with the highest totals.
- **Filtered data table:** An expandable section that allows users to inspect records matching their selections.
- **Data limitation note:** Explains that recorded tonnage alone does not measure overall recycling performance.

### Dashboard design and communication

I used a simple layout with summary figures near the top, followed by charts and an expandable data table. The filters allow users to focus on specific reporting periods and local authorities.

I used clear titles, labels and explanatory notes to help technical and non-technical users understand the visualisations. Technical users can inspect the filtered records, while other users can use the charts and summary figures to explore the main patterns.

### Changes made during development

During development, I prepared the cleaned CSV file for the dashboard and added reporting-period and local-authority filters. I included summary figures, a bar chart, a pie chart and an expandable table so users could explore the recorded data.

I also tested the reporting-period filter to check that the displayed figures changed when a different period was selected.

## Dashboard Testing

I tested my Streamlit dashboard in Chrome to check that it displayed correctly. I confirmed that the dashboard showed its title, key figures, bar chart and pie chart.

I tested the reporting-period filter by selecting April–June 2024. The recorded recycling tonnage changed from approximately 7,201,391 tonnes in the default view to approximately 2,120,028 tonnes for the selected period. This confirmed that the reporting-period filter updated the displayed figure as expected.

I then restored the default view and confirmed that all four reporting periods and 294 local authorities were included again.

The dashboard uses the cleaned recycling dataset prepared during my analysis. The figures describe recorded recycling tonnage and should not be treated as a complete measure of recycling performance.

## Ethical Considerations

### Data privacy, bias and fairness

I used publicly available waste collection data published by Defra through data.gov.uk. The data used in my analysis relates to waste collection records rather than information intended to identify individual residents. However, I recognise that public data must still be handled responsibly.

I considered fairness when comparing recycling tonnage across local authorities. Authorities may differ in population size, the amount of waste generated, collection arrangements and the types of materials recorded. Therefore, a higher recorded tonnage does not automatically mean that an authority performs better than another.

I presented the results as differences in the available records rather than as a definitive ranking of overall recycling performance. I also used clear chart titles, labels and explanatory notes to reduce the risk of misleading readers.

### Legal and societal considerations

I acknowledged the original data source and identified the licence stated for the dataset. I will continue to follow the applicable licence conditions when sharing the data or information derived from it.

I also considered transparency, responsible data use and the importance of avoiding unsupported conclusions. Public availability does not automatically make every possible use of data appropriate.

The findings may help readers understand recorded recycling patterns across reporting periods, local authorities and material categories. However, the figures alone cannot explain why differences occur or provide a complete assessment of environmental performance. I have therefore aimed to communicate the findings accurately and acknowledge the limitations of the analysis.

## Limitations and Unfixed Bugs

### Limitations of the analysis

The analysis is based on the measures available in the dataset. Recorded recycling tonnage alone does not account for every factor that may affect recycling performance.

Differences between local authorities may be influenced by population size, waste generation, collection arrangements, reporting practices and the types of materials recorded.

The co-mingled collection percentages describe the responses in the selected records rather than the proportion of all local authorities using a particular collection method.

The household coverage comparison uses the recorded number of households receiving a co-mingled materials collection. Its correlation with recycling tonnage indicates an association, not a causal relationship.

### Unfixed bugs and technical shortcomings

During testing, I confirmed that the main dashboard features displayed correctly and that the reporting-period filter updated the results as expected. I did not identify any unresolved bugs during these checks.

One technical limitation is that the dashboard depends on the cleaned CSV file being available at the file path expected by the application. If the file is missing or its column names change, the application may fail to load correctly.

The dashboard also depends on the Python libraries and configuration required by the application. These should be maintained and checked when the project is updated.

## Learning and Development

### Skills developed

During this project, I developed my understanding of data inspection, cleaning, grouping, aggregation, exploratory data analysis and visualisation using Python and Pandas.

I also gained practical experience preparing a CSV file for an application, creating an interactive dashboard with Streamlit and testing dashboard filters in a web browser.

### Gaps in my knowledge and how I addressed them

Some parts of the dataset structure, data preparation and dashboard development were unfamiliar to me. I addressed these challenges by working through the implementation step by step, consulting learning resources and using generative AI assistance to understand unfamiliar code and resolve implementation questions.

I ran and tested the code to check that it worked as expected and reviewed the results before documenting my findings.

### Feedback and improvement

I reviewed my work against the project requirements and used dashboard testing to check whether the main features worked as expected. Testing the reporting-period filter helped me confirm that the dashboard updated its displayed figures correctly.

I also recognised the importance of explaining data limitations so that users do not interpret recorded tonnage as a complete measure of recycling performance.

I have not reported specific peer or instructor feedback here because I have not documented any such feedback in this section.

## Development Roadmap

### Challenges and how I addressed them

One challenge was understanding the structure of the original dataset and identifying the records relevant to my analysis. I addressed this by inspecting the columns, selecting the relevant kerbside collection records and cleaning the data using Pandas.

Another challenge was developing an interactive dashboard with Streamlit. I worked through the implementation step by step, tested the dashboard in my browser and checked that the reporting-period filter updated the displayed figures.

I also used generative AI assistance to help me understand unfamiliar code and resolve implementation questions.


### Project Reflection

Completing my Waste Management and Recycling Data Analysis project has been a valuable learning experience. I used Python, Pandas, Matplotlib, Jupyter Notebook and Streamlit to prepare and analyse waste collection data for England for the 2024–2025 reporting year. I also developed an interactive dashboard and deployed it using Heroku.

One of the main challenges I faced was understanding the structure of the original dataset, cleaning the data and selecting the correct information for analysis. I also encountered technical issues while writing and testing code, preparing the dashboard dataset and deploying the application. I addressed these challenges by reviewing error messages, researching solutions, asking follow-up questions and testing changes in small steps until I achieved the expected results.

I used ChatGPT as a learning support tool to understand unfamiliar code, troubleshoot errors, improve my documentation and organise my project sections. However, I learned that AI suggestions do not always work correctly with my dataset or project structure. I therefore reviewed the suggested solutions, tested the code and checked my outputs before using them in my analysis. This helped me develop my problem-solving skills and become more confident in working independently.

Through my analysis, I identified differences in recorded recycling tonnage across reporting periods, local authorities and material categories. I also explored the relationship between household coverage and recycling tonnage. The findings helped me understand the importance of checking data quality, interpreting results carefully and recognising that a relationship between two variables does not necessarily mean that one causes the other.

Developing the Streamlit dashboard helped me understand how data analysis can be presented in a clear and interactive way. I learned how to use filters, summary metrics and charts to help users explore the findings. Testing the dashboard also showed me the importance of checking that the displayed results respond correctly to user selections.

I considered ethical issues by acknowledging the data source, checking the stated data licence, presenting findings responsibly and explaining the limitations of my analysis. I also recognised the importance of verifying AI-generated suggestions rather than accepting them without review.

If I were to develop this project further, I would explore additional ways to compare local authorities fairly, investigate possible reasons for changes in recorded recycling tonnage and improve the dashboard's accessibility and visual presentation. I would also continue developing my Python, data visualisation and dashboard deployment skills.

Overall, this project has strengthened my understanding of the data analytics process, from data preparation and exploratory analysis to visualisation, dashboard development and communication of findings. It has also improved my confidence, patience and ability to solve technical problems. I am proud of the progress I have made and will use the knowledge and experience gained from this project in my future data analytics work.

### Future learning and improvements

I plan to improve my knowledge of statistical analysis, hypothesis testing and machine learning using Python and Scikit-learn. I also want to develop my skills in writing efficient code, building interactive dashboards and presenting data insights clearly.

For future work, I could investigate whether newer reporting periods are available and update the analysis with additional data. I would first check the source, reporting periods, column structure and data quality, then repeat the cleaning and testing process.

I could also explore appropriate population or household measures to support more meaningful comparisons between authorities, provided the measures are consistent and suitable for the research question.

## Deployment

I deployed my Streamlit dashboard to Heroku.

**Live dashboard:** [Waste Collection Data Analysis: England 2024–2025](https://waste-management-recycling-a849fa5cf04a.herokuapp.com/)

The dashboard allows users to explore recorded waste collection and recycling tonnage data for England for the 2024–2025 reporting year. Users can filter the data by reporting period and local authority and view summary figures and visualisations.

### Running the application locally

To run the application locally, I open a terminal in the project folder and run:

```bash
python -m streamlit run app.py
```

The application uses the Python libraries listed in `requirements.txt`. The cleaned dataset, `cleaned_recycling_dashboard.csv`, must also be available at the file path expected by the application.

## Main Data Analysis Libraries and Tools

### Pandas

I used Pandas to load, inspect, clean, filter, group and summarise the waste collection dataset. For example, I grouped recycling tonnage by reporting period and local authority to compare recorded totals.

### Matplotlib

I used Matplotlib to create charts that communicate the findings, including bar charts and line charts. I also used a pie chart to show the share of recorded tonnage represented by the five leading material categories.

### Streamlit

I used Streamlit to build the interactive dashboard. I created metric cards, reporting-period and local-authority filters, charts and an expandable table of filtered records.

### Jupyter Notebook

I used Jupyter Notebook to organise my Python code, document the analysis and display the results alongside explanations.

### Scikit-learn

Scikit-learn is part of my planned further learning in statistical modelling and machine learning. It was not used in the current dashboard implementation.

## Credits

### Data Source

- **Department for Environment, Food and Rural Affairs (Defra):** I obtained the waste collection dataset from the UK Government's [Waste Data Flow dataset on data.gov.uk](https://www.data.gov.uk/dataset/0e0c12d8-24f6-461f-b4bc-f6d6a5bf2de5/waste-data-flow). I used this dataset to explore recorded recycling tonnage across England for the 2024–2025 reporting year.

### Documentation and Development Tools

- **[Python](https://docs.python.org/3/):** I used Python to write and run the code for data preparation, cleaning and analysis.

- **[Pandas](https://pandas.pydata.org/docs/):** I used Pandas to load, organise, clean and analyse the dataset, as well as prepare the data for visualisation and the dashboard.

- **[Matplotlib](https://matplotlib.org/stable/):** I used Matplotlib to create charts that helped me identify patterns and compare recycling tonnage across reporting periods, local authorities and material categories.

- **[Streamlit](https://docs.streamlit.io/):** I used Streamlit to develop an interactive dashboard with filters, summary metrics, charts and a data table, allowing users to explore the results.

- **[Jupyter Notebook](https://jupyter.org/):** I used Jupyter Notebook to organise my Python code, document my analytical process, display visualisations and explain my findings.

- **[Code Institute](https://codeinstitute.net/):** I used the Code Institute Learning Management System (LMS) to access course materials, learning resources, project guidance and assessment requirements that supported my learning and project development.

- **[Heroku](https://www.heroku.com/):** I used Heroku to deploy and host my Streamlit dashboard online so that it could be accessed through a web browser. I published my dashboard here: [Waste Collection Data Analysis Dashboard](https://waste-management-recycling-a849fa5cf04a.herokuapp.com/).

### Writing and Generative AI Assistance

- **[ChatGPT](https://chatgpt.com/):** I used ChatGPT to help me understand unfamiliar code, troubleshoot technical issues, organise sections of my project and improve my written explanations. I reviewed the code, checked the outputs and considered the results before including my findings in the project.

- **[Grammarly](https://www.grammarly.com/):** I used Grammarly to check spelling, grammar and clarity in my written documentation, helping me communicate my work more clearly.

### Media

I created the charts and dashboard visualisations using Python libraries. I did not use external photographs or other media in the dashboard.


### Acknowledgements

I would like to express my sincere gratitude to the entire **Code Institute team** for their teaching, guidance, encouragement and support throughout my Data Analytics with AI learning journey. The learning resources, feedback and explanations provided during our Stand-up and Stand-down sessions helped me better understand the project guidelines and assessment requirements. This support has contributed to my understanding of data analytics and strengthened my confidence in applying my skills.

I am also grateful for the learning materials and support available through the Code Institute Learning Management System, which helped me develop my knowledge and work towards completing this project.

A special thank you goes to my husband and children for their patience, encouragement and support throughout my learning journey. Their understanding, especially during the time I spent studying, practising and completing this project, have meant a great deal to me.

Finally, I acknowledge the support of generative AI tools in helping me understand unfamiliar code, organise my project documentation and improve my learning throughout the development process. I reviewed my work and checked the outputs before presenting my analysis and conclusions.

