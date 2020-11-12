# Anomaly Detection in the Curriculum Access Log

## Introduction
My supervisor Maggie needs to address several important questions about the program curriculums in a Morning Board Meeting. As the data scientist in her team, I am tasked to explore the curriculum access log and answer the questions she needs to address. 

## Goals:
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?<br>
2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over?<br> 
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?<br>
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents?<br> 
5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?<br> 
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?<br> 
7. Which lessons are least accessed? 
8. Anything else I should be aware of?<br>

## Executive Summary

![clustering zillow dataset](https://github.com/Yongliang-Shi/anomaly-detection-project/blob/main/executive_summary.png)

- Upper Left: Plot the active hits of the bottom 10% user id who hardly access the curriculum when active<br>
Based on the active hits (defined as the access occurred when the students are active), the bottom 10% percentile belong to 65 user ids, of which 58% is from web development, 11% is from data science, and 31% is from user ids with no program ids. The user ids associated with no program id are very suspicious.<br>

- Upper Right: Foreign access to the data science curriculum<br>
Focusing on the suspicious IP addresses to access the data science curriculum, 331 are located out of the United States. Most of the foreign accesses are from Canada.<br> 

- Lower Left: Cross Access Over Time Based on Program (unit: week)<br>
Web development cross-access significantly more than data science. Before July 2019, no cross-access is observed. After July 2019, there are two windows when the cross-access from web development significantly dropped:<br>
1. Nearly December 2019. It is expected because it is the holiday season.<br>
2. Nearly June 2020. It is unexpected so it may be another time when the cross-access has been shut down.<br> 

- Lower Right: Post graduation access to web development curriculum<br>
The top 3 topics the web development grads continuing to reference after graduation are: spring, appendix and javascript-i.<br>



