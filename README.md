# column_grouper

Bentley System's "RAM Structural Systems" is a commonly used modelling program for the design of steel buildings. In my experience, it is typically used for gravity design because of its superior tooling and ease of use. Here, gridlines are layed out, beamns/columns are added level by level along with the deck diaphragm and the imposed loads each story.

The script in this repository makes use of python to enable interoperability between modelling data, SQLite3, and Pandas. Story data is extracted from the model and iterated over to produce a dataframe that houses all gridline intersections and the column size that exists in each level. The trickiest part of this exercise was figuring out string synxtax issues to exchange variables between python and the SQL query.

The output of this script has been used for further post processing which will be uploaded in the future: Particle Swarm Optimization for optimal column grouping 

