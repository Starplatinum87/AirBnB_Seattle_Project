# Seattle AirBnB Project Writeup

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

