# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Waste Collection Data Analysis: England 2024–2025


## Project Overview

This project analyses waste collection and recycling data for England for the 2024–2025 reporting year. I used Python, Pandas and data visualisation techniques to explore recorded recycling tonnage across reporting periods, local authorities and material categories. I also developed an interactive Streamlit dashboard to help users explore the findings through charts, summary figures and filters.

## Dataset Content

The dataset used in this project was obtained from the UK Government's data.gov.uk website. It contains waste collection data for England for the 2024–2025 reporting year.

The data was published by the Department for Environment, Food and Rural Affairs (Defra) and includes information about local authorities, reporting periods, waste materials and recorded tonnage.

**Dataset source:** https://www.data.gov.uk/dataset/0e0c12d8-24f6-461f-b4bc-f6d6a5bf2de5/waste-data-flow

**Licence:** Open Government Licence.

## Business Requirements

The aim of this project is to analyse waste collection data for England for the 2024–2025 reporting year and present useful findings through data visualisations and an interactive dashboard.

The project addresses the following business requirements:

1. Identify changes in recorded recycling tonnage across the four reporting periods.
2. Compare recorded recycling tonnage across local authorities.
3. Identify the materials with the highest recorded recycling tonnage.
4. Explore recorded co-mingled collection responses and rejected recycling.
5. Present the findings in an interactive Streamlit dashboard with filters.

## Hypothesis and how to validate?

**Hypothesis**

I expect recorded recycling tonnage to differ across reporting periods, local authorities and material categories.

**How I will validate the hypothesis**

I will use Python and Pandas to group and compare recycling tonnage by reporting period, local authority and material category. I will use charts to identify patterns and differences in the data.

I will also examine co-mingled collection responses and recorded rejected recycling. These comparisons will help me assess the hypothesis using the available data. The analysis will identify patterns but will not establish the causes of any differences.

## Project Plan

### Outline the high-level steps taken for the analysis

1. I collected the waste collection dataset from the UK Government's data.gov.uk website.
2. I loaded and inspected the dataset using Python and Pandas.
3. I selected the relevant records for kerbside waste collection and prepared the data for analysis.
4. I cleaned the relevant data, converted recycling tonnage values to numeric format and checked for missing values.
5. I explored recycling tonnage by reporting period, local authority and material category using charts and summary statistics.
6. I prepared a cleaned CSV file and used it to build an interactive Streamlit dashboard.
7. I tested the dashboard in a web browser and documented the findings and limitations.

### How was the data managed throughout the collection, processing, analysis and interpretation steps?

I obtained the dataset from the UK Government's data.gov.uk website. I loaded it into Python using Pandas and inspected its columns, data types, missing values and structure. I selected the relevant records, cleaned and converted the required values, and saved the prepared recycling data as a CSV file for the dashboard. I used charts and summary statistics to interpret the results. I also considered the limitations of the data when explaining the findings.

### Why did you choose the research methodologies you used?

I chose a quantitative approach because the dataset contains numerical information about recorded waste collection and recycling tonnage. I used exploratory data analysis to identify patterns and differences across reporting periods, local authorities and material categories. I used charts to make comparisons easier to understand and a Streamlit dashboard to present the findings interactively. These methods were suitable for exploring the available data, although they cannot explain the causes of the differences on their own.

## The rationale to map the business requirements to the Data Visualisations

I selected visualisations that help me answer the business requirements and communicate the findings clearly.

- **Recorded recycling tonnage by reporting period (bar chart):** I used a bar chart to compare recorded recycling tonnage across the four reporting periods.
- **Recorded recycling tonnage by reporting period (line chart):** I used a line chart to show how recorded recycling tonnage changed across the reporting periods.
- **Top 10 local authorities by recorded recycling tonnage (bar chart):** I used a bar chart to compare the ten local authorities with the highest recorded recycling tonnage.
- **Recorded recycling tonnage for the top 5 local authorities (line chart):** I used a line chart to compare recorded recycling tonnage across the selected local authorities.
- **Share of recorded tonnage: top 5 recycling materials (pie chart):** I used a pie chart to show the share of recorded tonnage represented by the five leading recycling materials.
- **Recorded co-mingled collection responses (bar chart):** I used a bar chart to compare the recorded Yes and No responses.

I also developed a Streamlit dashboard with reporting-period and local-authority filters. The dashboard presents key figures and charts in one place, allowing users to explore the available data. Each visualisation supports comparison and helps communicate patterns, while the findings remain limited to the information recorded in the dataset.

### How will the project be implemented and maintained?

I implemented the analysis using Python and Pandas in a Jupyter Notebook. I saved the prepared recycling data in a CSV file and used Streamlit to build an interactive dashboard. I tested the dashboard locally to check that the charts, summary figures and filters worked as expected.

To maintain the project, I will keep the notebook, dashboard code, cleaned CSV file and README organised in my GitHub repository. If I update the analysis or dashboard, I will test the changes before committing them to GitHub. I will also review the code and documentation when the dataset, requirements or dashboard features change.

### How will the project be evaluated and updated?

I will evaluate the project by checking whether the analysis answers the stated business requirements, whether the visualisations communicate the findings clearly, and whether the dashboard works correctly. I will review the results against the original hypothesis and explain any limitations.

If a newer reporting period becomes available, I could update the analysis with the new data. Before doing so, I would check the source, reporting period, column structure and data quality, and repeat the cleaning and testing process. Any updated results would be checked before being presented in the dashboard.

## Analysis techniques used

### List the data analysis methods used and explain limitations or alternative approaches.

I used data inspection, data cleaning, grouping, aggregation, exploratory data analysis and data visualisation. I used Pandas to prepare and summarise the data and Matplotlib to create bar charts, pie charts and line charts. I also developed an interactive Streamlit dashboard.

These methods helped me identify patterns and compare recorded recycling tonnage across reporting periods, local authorities and material categories. Grouping and aggregation were effective because they summarised the large dataset into results that were easier to compare. Bar charts helped me compare quantities, line charts showed changes across reporting periods, and the pie chart showed the share represented by the five leading recycling materials.

However, these methods are descriptive and do not explain the causes of differences. The results may also be affected by differences in the amount of waste generated, population size and local collection arrangements. Statistical hypothesis testing could be considered if I had a suitable research question and the necessary assumptions were met. Population or household data could also support more meaningful comparisons, provided the measures were consistent and appropriate.

## Ethical considerations (optional)

I have kept this section because my Unit 3 project involves data analysis and visualisation.

### Data privacy, bias and fairness

I used publicly available waste collection data published by Defra through data.gov.uk. The data used in my analysis contains records about waste collection and recycling rather than information intended to identify individual residents. However, I recognise that public data must still be handled responsibly.

I considered fairness when comparing recycling tonnage across local authorities. Authorities may differ in population size, the amount of waste generated, collection arrangements and the types of materials recorded. Therefore, a higher recorded tonnage does not automatically mean that an authority performs better than another. I have presented the results as differences in the available records rather than as a ranking of overall performance.

I also considered the risk of misleading readers through incomplete explanations or visualisations. I used clear chart titles, labels, filters and explanatory notes to help users understand the findings and their limitations.

### Legal and societal considerations

I used a dataset available under the Open Government Licence and acknowledged the original source. I must continue to follow the licence conditions when sharing the dataset or information derived from it.

I also considered relevant data protection and governance principles, including using data appropriately, maintaining transparency and avoiding unsupported conclusions. Although the selected data is publicly available and aggregated, I should not assume that every use of public data is automatically free from ethical or legal concerns.

The findings may help readers understand recorded recycling patterns across reporting periods, authorities and material categories. However, I cannot use these figures alone to explain why differences occur or to judge the environmental performance of an authority. I have therefore aimed to communicate the results accurately, acknowledge limitations and avoid claims that are not supported by the analysis.

## Dashboard Design (optional)

I have kept this section because my Unit 3 project includes an interactive Streamlit dashboard.

### Dashboard pages and content

My dashboard contains one main page titled **Waste Collection Data Analysis: England 2024–2025**.

The page includes:

- **Introduction:** A short explanation of the purpose of the dashboard.
- **Filters:** Sidebar multiselect filters for reporting periods and local authorities.
- **Key figures:** Three metric cards showing recorded recycling tonnage, the number of local authorities and the number of material categories in the filtered data.
- **Bar chart:** Recorded recycling tonnage by reporting period.
- **Pie chart:** The share of recorded tonnage represented by the five materials with the highest totals.
- **Filtered data table:** An expandable section allowing users to view the records matching their selections.
- **Data limitation note:** A caption explaining that recorded tonnage alone does not measure overall recycling performance.

### Changes made during development

I developed the dashboard using the cleaned CSV dataset prepared during my analysis. I used a bar chart to compare reporting periods and a pie chart to present the distribution of recorded tonnage among the top five materials. I also added filters so users could explore different reporting periods and local authorities.

### How were data insights communicated to technical and non-technical audiences?

I presented the findings using clear headings, summary figures and charts. Technical users can examine the filtered records, while non-technical users can use the summary figures and visualisations to understand the main patterns without needing to read the original dataset.

### How was the dashboard designed to communicate complex data insights to different audiences?

I used a simple layout with key figures near the top, followed by charts and an expandable data table. The reporting-period and local-authority filters allow users to focus on specific parts of the dataset. I also included a note explaining the limitations of the figures to encourage responsible interpretation of the results.

## Unfixed Bugs

### Unfixed bugs and shortcomings

During testing, I confirmed that the main dashboard features displayed correctly and that the reporting-period filter updated the results. I have not identified any unresolved bugs at this stage.

One limitation is that the dashboard depends on the cleaned CSV file being available in the expected project location. If the file is missing or its column names change, the dashboard may fail to load correctly. The dashboard also presents recorded recycling tonnage, which does not account for all the factors needed to assess overall recycling performance.

### Gaps in my knowledge and how I addressed them

During this project, I developed my understanding of data cleaning, grouping and aggregation in Pandas, data visualisation, and building interactive dashboards with Streamlit. I used learning resources and generative AI assistance to help me understand unfamiliar code and resolve implementation questions. I then ran and tested my code to check that it worked as expected.

### Feedback received and how it improved my approach

I used the project requirements and my dashboard testing to review my work and identify areas for improvement. Testing the reporting-period filter helped me confirm that the dashboard updated its figures correctly. I also recognised the importance of explaining the limitations of the data so that users do not interpret recorded tonnage as a complete measure of recycling performance.

No specific peer or instructor feedback is reported in this section unless I have received and documented it.

## Development Roadmap

### What challenges did you face, and what strategies were used to overcome these challenges?

One challenge I faced was understanding the structure of the original dataset and identifying the records relevant to my analysis. I addressed this by inspecting the columns, selecting the relevant kerbside collection records and cleaning the data using Pandas.

Another challenge was developing an interactive dashboard using Streamlit. I worked through the implementation step by step, tested the dashboard in my browser and checked that the reporting-period filter updated the displayed figures correctly. I also used generative AI assistance to help me understand unfamiliar code and resolve problems.

### What new skills or tools do you plan to learn next based on your project experience?

I plan to improve my knowledge of statistical analysis, hypothesis testing and machine learning using Python and Scikit-learn. I also want to develop my skills in building interactive dashboards, writing more efficient code and presenting data insights clearly. These skills will help me carry out more advanced analysis and communicate findings effectively to different audiences.

## Deployment

My project includes an interactive Streamlit dashboard developed using Python and the cleaned recycling dataset.

I ran and tested the dashboard locally using Streamlit in my web browser. At the time of writing, the dashboard has not been deployed to a public hosting platform, so there is no public dashboard link available.

The dashboard can be run locally from the project folder using the following command in the terminal:

`python -m streamlit run app.py`

The cleaned dataset, `cleaned_recycling_dashboard.csv`, must be available in the expected project location for the dashboard to load successfully.


## Main Data Analysis Libraries

I used the following Python libraries and tools in my project:

- **Pandas:** I used Pandas to load, inspect, clean, filter and group the waste collection dataset. For example, I grouped recycling tonnage by reporting period and local authority to compare the recorded totals.

- **Matplotlib:** I used Matplotlib to create charts to communicate the findings. For example, I created a pie chart showing the share of recorded tonnage represented by the five materials with the highest totals.

- **Streamlit:** I used Streamlit to build an interactive dashboard. For example, I created metric cards, reporting-period and local-authority filters, charts and an expandable table of filtered records.

- **Jupyter Notebook:** I used Jupyter Notebook to organise my Python code, document the analysis and display the results alongside explanations.

- **Scikit-learn:** This library is part of my planned further learning in statistical modelling and machine learning. It was not used in the current dashboard implementation.

These tools helped me prepare the data, explore patterns, visualise findings and present the results in an interactive format.

## Credits

### Content

- **Department for Environment, Food and Rural Affairs (Defra):** I obtained the waste collection dataset from the UK Government's [data.gov.uk Waste Data Flow dataset](https://www.data.gov.uk/dataset/0e0c12d8-24f6-461f-b4bc-f6d6a5bf2de5/waste-data-flow). The dataset was used for the analysis of recorded recycling tonnage across England for the 2024–2025 reporting year.
- **Python and Pandas documentation:** I used these tools and their documentation to support data preparation, cleaning and analysis.
- **Streamlit documentation:** I used Streamlit to develop the interactive dashboard.
- **Generative AI assistance:** I used ChatGPT to help me understand code, plan sections of the project and improve my documentation. I reviewed and tested the code used in my project.

### Media

I created the charts and dashboard visualisations using Python libraries. I did not use external photographs or other media in the dashboard.


## Acknowledgements (optional)

I would like to thank Code Institute for providing the learning materials and project guidance that supported my development throughout this course.

I am also grateful for the publicly available waste collection dataset provided by the Department for Environment, Food and Rural Affairs (Defra) through data.gov.uk.

Finally, I acknowledge the support of generative AI tools in helping me understand unfamiliar code, organise my project documentation and improve my learning throughout the development process.