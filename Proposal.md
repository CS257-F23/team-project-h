**Team Contract**

**Devin, Dexter, Alisa, Lucy**

**Project Name: Carleton Stock Tracker**

**Goals Statement:** We as a team want to better understand the architecture behind an interactive database-driven website and learn valuable team collaboration skills.

**Meaningful User Interaction:** The user will be able to pick and choose stocks from the list of stocks Carleton invests in. The system will then tell them whether the stocks chosen outperformed Carleton's entire repertoire. 

**Strengths of our team:**

- Devin: I am familiar with HTML, and CSS, but not Python.
- Dexter: Python, flask, data visualization, and database modeling. 
- Lucy: I am a good listener and I am willing to resolve disagreements. I am also pretty confident in my learning ability.  
- Alisa: I have good artistic skills and am good at making artistic decisions. 

**How will we capitalize on the strengths of each member?**

Some of the team members have experience building websites, so they are good resources for everyone. We want to collaborate with each other to learn from one another and build a great project. Everyone in the groupchat can request to hold an extra meeting in addition to the weekly-scheduled one. 

**What are the rules that will guide your team?** 

**Features** 

Feature: (**get\_all**) - get all historical stock data for each company.

Usage: 

`python3` `stock_data.py` `--get_all`

Feature:  (**get\_by\_company**) - get all stock prices for one company, options for date and extra information

Usage: 

`python3` `stock_data.py` `--get_by_company` `“company1…”` `-date` `“date1,date2”` `-i`

Feature: **(get\_by\_date)** - look up stock values on a specific date, option for extra information

default: all companies by month

Usage: 

`python3` `stock_data.py` `--get_by_date` `“date”` `-i`

Feature: **(get\_help)** - get help on how to use the previous features 

Usage:

&#x20;`python3` `stock_data.py` `–h`

**How user can interact with the data** 

Users will be able to look up specific stock information based on a company or date they are interested in. 

- Devin is in charge of get\_by\_company
- Dexter is in charge of get\_by\_date 
- Lucy and Alisa are in charge of get\_all and get\_help 
- We will work together to load and organize the data and to implement the main function. 

<!---->

- We plan to meet every week on Tuesday at 2 p.m for an hour. 
- We also have a Discord server to give each other quick updates or set up more time to meet. Communication on the server will be more professional than casual to ensure respectfulness.
- Every member will send updates every Thursday and Sunday nights on Discord about what they’ve worked on. 
- Decisions should be unanimous.
- Work will be divided into small groups of 2//individuals by site feature and will be recorded to ensure everybody has satisfactory participation
- We will aim for each individual to have 3 hours of work to do per week. So, we will spend around 3 hours of work a week on this project outside of group meetings. 
- When features are pushed onto github, members of the group will double-check that it does not interfere with previous functions, and Devin will be in charge of the final quality control. 
- Alisa will be in charge of making sure we don’t miss revision windows. 
- If a group member is not participating satisfactorily or if there are conflicts and disagreements, then there will first be a group call, and later communication with Anya regarding the matter if it cannot be resolved. 
- If someone needs help, they will send a help sticker in the Discord.

**Metadata on our dataset**

**AUTHOR NAME**

Oleh Onyshchak


##### DOI Citation

10.34740/kaggle/dsv/1054465

**SOURCES**

<https://pypi.org/project/yfinance/>, <http://www.nasdaqtrader.com/>

**COLLECTION METHODOLOGY**

Collected via <https://www.kaggle.com/jacksoncrow/download-nasdaq-historical-data>


##### License: [CC0: Public Domain](https://creativecommons.org/publicdomain/zero/1.0/)

##### Expected Update Frequency

Quarterly (Updated 3 years ago)

**Citation**

Oleh Onyshchak. (2020). \<i>Stock Market Dataset\</i> \[Data set]. Kaggle. <https://doi.org/10.34740/KAGGLE/DSV/1054465>
