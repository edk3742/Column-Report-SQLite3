# Column Report

Bentley System's "RAM Structural Systems" is a commonly used modelling program for the design of steel buildings. For the gravity design of members, RAM SS is very effective because of its superior tooling, diverse report options, and the familiarity engineers have with the software. In the program, gridlines are layed out, beams/columns are added level by level along with the deck diaphragm and the imposed loads at each story.



The script in this repository makes use of python to increase interoperability between modelling data, SQLite3, Python Pandas, and MS Excel. Full modelling data is saved into a ".db" file where story data is extracted and iterated over to produce a dataframe that houses all gridline intersections and the column size that exists per each level. One of the trickier parts of this exercise was string synxtax issues between Python and the SQLite3 query in order to exchange variables names and variable values.



The output of this script will be used for further post processing, namely, Particle Swarm Optimization for optimal column grouping and tabulated scheduling. This will be uploaded in the future

