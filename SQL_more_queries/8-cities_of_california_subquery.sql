-- Write a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.name FROM states, cities WHERE states.name="California";
