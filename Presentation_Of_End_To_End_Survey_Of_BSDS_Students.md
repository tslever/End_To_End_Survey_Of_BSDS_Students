# Presentation of End-To-End Survey of BSDS Students

Created on 07/10/2024 by Tom Lever

Updated on 07/10/2024 by Tom Lever


## Slide 1: End-to-End Survey of BSDS Students

Ms. Kester tasked me with presenting how I would create an end-to-end survey of the students in the BS in Data Science program.

To be concrete, I would like to consider a retrospective questionnaire of recent graduates of the BSDS program.

This questionnaire could be broken up across a student’s program.


## Slide 2: End to End Survey

Here I would like to define “end-to-end survey”.

An end-to-end survey is the process of creating and distributing questions; collecting, analyzing, and reporting on answers; and planning the above.

I would also like to define questionnaire. For our purposes, let a questionnaire be a set of questions.


## Slide 3: General Objectives

I would like to present some general objectives.

We might wish to…

1.	gather comprehensive feedback from recent graduates of the BSDS program;

2.	evaluate various aspects of the BSDS program from the perspectives of recent graduates;

3.	gather insights to improve the BSDS program and better support future students;


## Slide 4: Specific Objectives

I would like to present some specific objectives.

We might wish to...

1.  create a binary classifier, multiclass classifier, or regression model that may predict whether a student found the BSDS program to be satisfying overall; and

2.  understand which predictors are most likely to determine whether a student found the BSDS program to be satisfying overall.


## Slide 5: Collaborators

I would like to consider who I would collaborate with to develop the survey.

Collaborators may include…

1.	you all;

2.	every faculty member, staff member, PhD student, MSDS student, and BSDS student who is willing to respond to an email requesting questions for a hypothetical questionnaire that meets objectives; and

3.	stakeholders, administrative support people, and advisors listed in “Table of Collaborators”.


## Slide 6: Questionnaire to Improve Course

Before creating questions, we may want to consider the questions and feel of existing questionnaire.

Here is an appealing questionnaire that I personally intend to take in August.

The questionnaire is a web app hosted by Qualtrics, which offers online survey software.


## Slide 7: Comparing Existing Questionnaires

We may want to formally compare existing questionnaires using metadata.

On the right here is the beginning of “Table of Quality Metrics”, which right now has 42 metrics.

We might compare surveys by response rate.

We could use the questions and/or format of the survey with the highest response rate.


## Slide 8: Retrospective Survey of BSDS Program

Here is a screenshot of the beginning of “Retrospective Survey of BSDS Program”, which right now has 50 questions.

The first question, and many questions, ask a student to provide scores for the BSDS program and specific criteria.

Scores are numerical, quantitative, ratio data.

Scores may be used to construct point estimates, visualizations, distributions, confidence intervals, hypothesis tests, functional models, and machine learning models.

Some questions that ask for text responses might provide context, validation, student information, or ideas for new questions. Some text might be converted into numbers manually or using a machine learning model.

After developing the survey, we could conduct a pilot test by offering the questions to collaborators. 


## Slide 9: Deployment

We could have our questionnaire be a web app hosted by Qualtrics.

We could email an introduction and link to our survey as finals are winding down.

We could offer money, swag, or other incentives.

We could send out reminders.


## Slide 10: Data Collection

Qualtrics might record responses in a secure and organized way.

I might talk to advisors about how metadata might map to our “Table of Quality Metrics”.

I might talk to advisors about how questionnaire data might map to a “Feature Matrix”, or whether the questionnaire needs to look like a feature matrix.

So what feature matrix do I have in mind?


## Slide 11: Feature Matrix

I envision constructing a two-dimensional table of data from all questionnaires.

The table would have a column for every questionnaire that was at least partially completed.

Right now, the matrix has about 527 features.

Metadata could be added before modeling.

Qualtrics might fill missing values with “NULL”.

Qualtrics might prevent entering invalid values.

We might remove irrelevant text.

We might prefer a score or text when one contradicts the other.

We might convert text to numbers representing certain ideas and/or sentiments.


## To-Do Items

Add additional slides.

Answer, “What technologies would I use to interpret the data?”

Answer, “How would I present the results?”