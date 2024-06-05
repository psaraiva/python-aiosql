import asyncio
import time
import aiosql
import aiosqlite

async def main():
    querie = aiosql.from_path("sql/earthquakes.sql", "aiosqlite")
    async with aiosqlite.connect("db/disaster.db") as conn:
        start_time = time.time()
        earthquakes, deaths, count_earthquakes = await asyncio.gather(
            querie.get_all_earthquake(conn),
            querie.sum_deaths(conn),
            querie.count_earthquakes(conn)
        )
        execution_time = time.time() - start_time
        print(f"Execution Query Time: {format(execution_time, '.4f')} seconds")

        print("+-------- Statistic --------+")
        print(f"Total earthquakes: {count_earthquakes}")
        print(f"Total deaths: {deaths}")
        print("+---------------------------+")

        for item in earthquakes:
            print(f"Date: {item[0]}, Deaths {item[5]}")

        print(f"Execution Query Time: {format(execution_time, '.4f')} seconds")

asyncio.run(main())
