import aiosql
import sqlite3
import time

def main():
    query = aiosql.from_path("sql/earthquakes.sql", "sqlite3")
    with sqlite3.connect("db/disaster.db") as conn:
        start_time = time.time()
        count_earthquakes = query.count_earthquakes(conn)
        deaths = query.sum_deaths(conn)
        earthquakes = query.get_all_earthquake(conn)
        execution_time = time.time() - start_time
        print(f"Execution Query Time: {format(execution_time, '.4f')} seconds")

        print("+-------- Statistic --------+")
        print(f"Total earthquakes: {count_earthquakes}")
        print(f"Total deaths: {deaths}")
        print("+---------------------------+")

        for item in earthquakes:
            print(f"Date: {item[0]}, Deaths {item[4]}")

    print(f"Execution Query Time: {format(execution_time, '.4f')} seconds")

main()
