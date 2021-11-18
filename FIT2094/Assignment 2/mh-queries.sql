--****PLEASE ENTER YOUR DETAILS BELOW****
--mh-queries.sql

--Student ID: 30612616 
--Student Name: Ian WONG
--Tutorial No: 10

/* Comments for your marker:




*/


/*
    Q1
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
SELECT HT_NBR
    ,EMP_NBR
    ,EMP_LNAME
    ,EMP_FNAME
    ,END_LAST_ANNUAL_REVIEW AS REVIEW_DATE
FROM MH.ENDORSEMENT 
NATURAL JOIN MH.EMPLOYEE
WHERE END_LAST_ANNUAL_REVIEW > TO_DATE('31/03/2020','DD/MM/YYYY')
ORDER BY END_LAST_ANNUAL_REVIEW;

/*
    Q2
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
SELECT CHARTER_NBR
    ,CLIENT_NBR
    ,CLIENT_LNAME
    ,CLIENT_FNAME
    ,CHARTER_SPECIAL_REQS
FROM MH.CHARTER
NATURAL JOIN MH.CLIENT
WHERE CHARTER_SPECIAL_REQS IS NOT NULL
ORDER BY CHARTER_NBR;

/*
    Q3
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
SELECT CHARTER_NBR
    ,CLIENT_FNAME||' '||CLIENT_LNAME AS FULLNAME
    ,CHARTER_COST_PER_HOUR
FROM MH.CHARTER 
NATURAL JOIN MH.CLIENT
NATURAL JOIN MH.CHARTER_LEG CL
INNER JOIN MH.LOCATION L
    ON CL.LOCATION_NBR_DESTINATION = L.LOCATION_NBR
    AND L.LOCATION_NAME LIKE 'Mount Doom'
WHERE CHARTER_COST_PER_HOUR < 1000 
      OR CHARTER_SPECIAL_REQS IS NULL 
ORDER BY FULLNAME DESC;

/*
    Q4
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
SELECT HT_NBR
    ,HT_NAME
    ,COUNT(HT_NBR) AS COUNT
FROM MH.HELICOPTER
NATURAL JOIN MH.HELICOPTER_TYPE
GROUP BY HT_NBR, HT_NAME
HAVING COUNT(HT_NBR) >= 2
ORDER BY COUNT DESC;

/*
    Q5
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
SELECT LOCATION_NBR
    ,LOCATION_NAME
    ,COUNT(LOCATION_NBR_ORIGIN) AS COUNT
FROM MH.CHARTER_LEG CL
JOIN MH.LOCATION L
    ON CL.LOCATION_NBR_ORIGIN = L.LOCATION_NBR
GROUP BY LOCATION_NBR, LOCATION_NAME
ORDER BY COUNT;

/*
    Q6
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
SELECT HT.HT_NBR
    ,HT.HT_NAME
    ,CASE
        WHEN SUM(HELI_HRS_FLOWN) IS NULL 
            THEN 0
        ELSE SUM(HELI_HRS_FLOWN)
     END HRS_FLOWN
FROM MH.HELICOPTER H
RIGHT JOIN MH.HELICOPTER_TYPE HT
    ON H.HT_NBR = HT.HT_NBR
GROUP BY HT.HT_NBR, HT.HT_NAME
ORDER BY HRS_FLOWN;

/*
    Q7
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
SELECT CHARTER_NBR, TO_CHAR(CL_ATD,'DD/MON/YYYY HH12:MI PM') AS DEPARTURE
FROM MH.CHARTER C
INNER JOIN MH.EMPLOYEE E
    ON C.EMP_NBR = E.EMP_NBR
    AND E.EMP_LNAME LIKE 'Baggins'
    AND E.EMP_FNAME LIKE 'Frodo'
NATURAL JOIN MH.CHARTER_LEG CL
WHERE CL_LEG_NBR = 1 AND CL.CL_ATA IS NOT NULL
ORDER BY TO_DATE(DEPARTURE,'DD/MON/YYYY HH12:MI PM') DESC;

/*
    Q8
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
WITH TEMP AS (
SELECT CHARTER_NBR
    ,CLIENT_NBR
    ,CLIENT_LNAME
    ,CLIENT_FNAME
    ,SUM(24*(CL_ATA- CL_ATD)*CHARTER_COST_PER_HOUR) AS TOTALCHARTERCOST
FROM MH.CHARTER
NATURAL JOIN MH.CLIENT
NATURAL JOIN MH.CHARTER_LEG
GROUP BY CHARTER_NBR, CLIENT_NBR, CLIENT_LNAME, CLIENT_FNAME
HAVING SUM(24*(CL_ATA-CL_ATD)) IS NOT NULL
ORDER BY TOTALCHARTERCOST DESC
)

SELECT CHARTER_NBR
    ,CLIENT_NBR
    ,NVL(CLIENT_LNAME, '-') AS CLIENT_LNAME
    ,NVL(CLIENT_FNAME, '-') AS CLIENT_FNAME
    ,TO_CHAR(TOTALCHARTERCOST, '$9999.99') AS TOTALCHARTERCOST
FROM
    TEMP
WHERE TOTALCHARTERCOST < (SELECT AVG(TOTALCHARTERCOST) FROM TEMP);
/*
    Q9
*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE your query has a semicolon (;) at the end of this answer
SELECT CHARTER_NBR
    ,EMP_FNAME||' '||EMP_LNAME AS PILOTNAME
    ,CLIENT_FNAME||' '||CLIENT_LNAME AS CLIENTNAME
FROM
(
SELECT CHARTER_NBR
    ,EMP_FNAME
    ,EMP_LNAME
    ,CLIENT_FNAME
    ,CLIENT_LNAME
    ,SUM(24*(CL_ETD-CL_ATD)) AS DIFFERENCE
FROM MH.CHARTER
NATURAL JOIN MH.CLIENT
NATURAL JOIN MH.EMPLOYEE
NATURAL JOIN MH.CHARTER_LEG
GROUP BY CHARTER_NBR
    ,EMP_FNAME
    ,EMP_LNAME
    ,CLIENT_FNAME
    ,CLIENT_LNAME
HAVING SUM(24*(CL_ETD-CL_ATD)) IS NOT NULL
)
WHERE DIFFERENCE = 0
ORDER BY CHARTER_NBR;