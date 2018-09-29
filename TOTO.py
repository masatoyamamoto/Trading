from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import os


# a code to get Jleague Result from the Official site of J-league, using BeautifulSoup
def get_result(year_of_league):
    result_url = "https://data.j-league.or.jp/SFMS01/search?competition_years=" \
                 + str(year_of_league) \
                 + "&competition_frame_ids=1&tv_relay_station_name="

    # Get HTML from the J-league official site
    f = urlopen(result_url)
    html = f.read()

    # Parse by BeatufulSoup
    soup = BeautifulSoup(html, "lxml")

    # Results of game is included in the table whose class is "table-base00 search-table"
    # A header is written with "th" tag
    table = soup.find_all("table", {"class": "table-base00 search-table"})[0]
    rows = table.findAll(["th", "tr"])

    # Write out to a csv file
    with open(str(year_of_league) + ".csv", "wt", newline='', encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile)

        for row in rows:
            csvRow = []
            for cell in row.findAll(['th', 'td']):
                csvRow.append(cell.get_text(strip=True))

            if csvRow:  # if there is any data. It writes out empty rows without this.
                writer.writerow(csvRow)

    print("year " + str(year_of_league) + " is done!")


if __name__ == "__main__":
    # makedir
    os.makedirs("./JleagueResult", exist_ok=True)
    os.chdir("./JleagueResult")
    for i in range(1993, 2018, 1):
        get_result(i)

    print("all done!")
