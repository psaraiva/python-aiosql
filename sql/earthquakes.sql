-- name: get_all_earthquake
-- Get all earthquakes
  SELECT date,
         country,
         region,
         depth,
         magnitude,
         deaths
    FROM earthquakes
ORDER BY 1;

-- name: sum_deaths$
-- Get the sum of deaths
SELECT sum(deaths)
  FROM earthquakes;

-- name: count_earthquakes$
-- Get the count of earthquakes
SELECT count(deaths)
  FROM earthquakes;
