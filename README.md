# Seattle AirBnB Project 

![](writeup/images/seattle_skyline_4_milkovi-skUTVJi8-jc-unsplash.jpg)

Photo by [MILKOVÍ](https://unsplash.com/@milkovi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/seattle?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

## Project Overview

This is a project that I felt would be relatively simple, but that turned out to be much more involved. While I have done several machine learning projects before this was the first time that I had such a high number of features that I couldn't practically dive deep on each one individually. This gave me valuable experience in coming up with strategies to deal with large numbers of features and prioritizing the methods to deal with them efficiently, while still maintaining some time constraints for the project. 

The goal of this project was to take an AirBnB dataset for all of the properties in Seattle, Washington 2016 and use it to answer 3 questions about the data and then come up with a predictive model for a feature of the data. 

### Data

The data consisted of 3 datasets:

- **calendar** (1.4M rows, 4 columns): Covers listing ids of properties, dates, availability of the property and the daily price of staying at the property.
- **listings** (3818 rows, 92 columns): Covers many aspects of each listing such as descriptions and details of the property and host, review scores, location, amenities, etc.
- **reviews** (84,849 rows, 6 columns) Focuses on written reviews for stays at each property. 

My questions and modeling focused on the property listings, so I didn't end up using the reviews dataset.

### 3 Questions to Answer:

1. **What is the overall occupancy in Seattle over the course of the year?** 
   - Are there periodic shifts in the overall AirBnB occupancy in Seattle over the course of the year and if so what does this look like? This can help the company decide when and how to run promotions of various kinds and to work with hosts to help them get the most out of these time frames. 
2. **Does it pay to be a Superhost? How do the occupancy, prices and reviews of Superhosts compare to normal hosts?**
   - Superhost is a special title that is automatically applied to listings where the host maintains high marks in many areas and has an established positive trend with AirBnB overall. 

   - I'm interested in seeing if there is a correlation between being a superhost and other metrics, such as overall rating/reviews, occupancy, and rental prices. I'll compare these same metrics to non-Superhost listings. 
3. **What neighborhoods have the highests occupancy rates?** 
   - Knowing where to have a property for an AirBnB residence can be an important decision for hosts to make. Providing that information to them can help hosts be more effective, as well as helping AirBnB know how to focus its promotional efforts.

### Prediction: Mean Annual Occupancy Rate

My predictive model will attempt to predict the mean occupancy rate for a given property listing for the year. The independent variables will be details about the listing,  primarily from the listings dataset.

## Project Conclusions

### 3 Key Questions: Conclusions

1. **What is the overall occupancy trend in Seattle over the course of the year?** 
   -  There are three distinct periods where we see a dramatic buildup of reservations followed by a leveling off: spring break, July 4th/early summer, and New Year's.
   -  The New Year's spike is the largest and there is a dramatic drop right before New Year's. 
   -  New Year's is the time we see the greatest spike in occupancy for AirBnB in Seattle, as occupancy never gets close to that level throughout the rest of the year. 
2. **Does it pay to be a Superhost? How do the occupancy, prices and reviews of Superhosts compare to normal hosts?**
   - The occupancy rates of Superhosts and hosts are very close to each other, but the mean price of a Superhost listing is notably higher than that of a normal host, about 8% higher.
   - The higher mean listing price for Superhosts does not seem attributable to outliers skewing the metric. 
   - Base on this preliminary analysis it appears that Superhosts tend to earn more with their listings than normal hosts, so it may be worth it to attempt to achieve that status. Further study is needed however.
3. **What neighborhoods have the highest occupancy rates?**
   - The specific neighborhoods with the highest occupancy are:
     - North College Park
     - South Lake Union
     - South Beacon Hill
     - Broadway
     - North Beach/Blue Ridge
   - This is useful information to have, as it can be the basis for further exploration into specific details of these neighborhoods that leads to their occupancy rates, but that is outside the scope of this analysis. 
   - We have per neighborhood occupancy clustering around 30% over the course of the year with some clear outliers on the high end and low end. So  there is definitely a difference between different neighborhoods in terms of occupancy, but most hover in the 20-40% range. 
   - The histogram indicates that neighborhood occupancy is relatively normally distributed. 
   - There seems to be no relationship between neighborhood occupancy and listing price. 

### Modeling Conclusions

- In the end, of the algorithms used (Lasso, Ridge, Support Vector Machines, Random Forests) **random forests had the best model performance** of all of the modeling techniques tried. Random forests tend to perform quite well on more complex modeling tasks, so this isn't terribly surprising. It also generates useful outputs like feature importance, which can be a very important component of a project. 
- We ended up with a final **mean squared error on test of 0.0994**, which was **~15.62% better than baseline** (0.1178) and only **0.2% worse than validation** (0.0992), which means that the model is likely **highly generalizable** to new data with the same features. 
- While random forests did generate the best model in terms of predictive power, it was the **worst in terms of performance**. This is not a major concern for this project, but must always be considered. 
- In terms of feature importances **many of the engineered features ended up being in the top features in terms of relevance to the model**. This shows how important feature engineering can be to a project. 
- This Mean Squared Error of 0.0994 means that, considering that a single listing can have an occupancy rate of 0 (no one stays at the listing over the entire year) to 1.0 (the listing is rented for every day of the year) that **on average our prediction of occupancy rate will, on average, be off by 9.94%**. Certainly better than being off by the baseline of 11.78%, but there is definitely room for improvement. 

## Future Work

* There are many different ways this data could be used and explored, but for the 3 questions I'm currently satisfied with the analysis as it is currently.
* However, for the machine learning prediction there is definitely room to improve on the current performance. If I were to continue this project the next steps would include exploring gradient boosted algorithms, especially XGBoost and related approaches, as they have proven to be both performant both in terms of model prediction and in terms of processing overhead. 

## [Project Repository](https://github.com/Starplatinum87/AirBnB_Seattle_Project) 

### File Tree

├── README.md
├── data
│   ├── calendar.csv
│   ├── listings.csv
│   ├── pickles
│   │   ├── calendar_munged.pkl
│   │   ├── listings_munged.pkl
│   │   ├── listings_munged2.pkl
│   │   └── reviews_munged.pkl
│   └── reviews.csv
├── notebooks
│   ├── airbnb_seattle_data_processing.ipynb
│   ├── airbnb_seattle_data_processing_2.ipynb
│   ├── airbnb_seattle_datasets.ipynb
│   ├── airbnb_seattle_key_questions.ipynb
│   └── airbnb_seattle_modeling.ipynb
├── scripts
│   └── airbnb_functions.py
└── writeup
    ├── Seattle_AirBnB_Project_Writeup.md
    └── images

### File Descriptions

* README.md - Description of projects libraries and files
* /data/ - Folder containing source data files and pickled files
  * calendar.csv - (1.4M rows, 4 columns): Covers listing ids of properties, dates, availability of the property and the daily price of staying at the property.
  * listings.csv - (3818 rows, 92 columns): Covers many aspects of each listing such as descriptions and details of the property and host, review scores, location, amenities, etc.
  * reviews.csv - (84,849 rows, 6 columns) Focuses on written reviews for stays at each property.
  * /pickles/ - Processed datasets created during the project
    * calendar_munged.pkl - Processed calendar.csv dataset
    * listings_munged.pkl - Initial processing of listings dataset
    * listings_munged2.pkl - Additional processing of listings dataset
    * reviews_munged.pkl - Processing of reviews dataset
* /notebooks/ - All Jupyter notebooks for the project, containing all project work
  * airbnb_seattle_data_processing.ipynb - Processing of listings and calendar datasets
  * airbnb_seattle_data_processing_2.ipynb - Additional processing of listings dataset
  * airbnb_seattle_datasets.ipynb - Initial data exploration of all 3 datasets
  * airbnb_seattle_key_questions.ipynb - Scripts, visualizations and summaries of 3 primary project questions
  * airbnb_seattle_modeling.ipynb - Machine learning modeling and results
* /scripts/ - Module containing functions used in the project
  * airbnb_functions.py - Module containing functions used in the project
* /writeup/ - Detailed writeup of project and images contained in the writeup
  * Seattle_AirBnB_Project_Writeup.md - Detailed writeup of entire project
  * /images/ - Images used in the writeup document

### Libraries

Below are the libraries and tools used in the project:

* Anaconda
* Jupyter Notebooks
* Pandas
* Numpy
* Scikit-learn
* Matplotlib
* Seaborn
* Time
* Pickle

## Resources

Links to project resources:

- [GitHub Repository](https://github.com/Starplatinum87/AirBnB_Seattle_Project) - All data, scripts, notebooks and documents for the project.

- Medium Article](https://torin-rettig.medium.com/3-questions-and-1-prediction-for-seattle-airbnb-240aed8b5c72) - High level overview of the project and it's conclusions.

- [Blog Post @ torinrettig.net](https://torinrettig.net/Seattle_AirBnB_Project_Writeup/) - A much more detailed version of the Medium article, going into more depth on data processing, metrics and modeling.

  

