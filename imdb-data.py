from statistics import mean
def reader(filename):
    file = open(filename, "r", encoding="utf-8")
    while True:
        yield file.readline()
def main():
    generator = reader("data.tsv")
    genres = {}
    while True:
        value = next(generator)
        if value == "":
            break
        id, title_type, primary_title, secondary_title, a, start_year, end_year,runtime, genre_string = value.strip("\n").split("\t")
        for genre in genre_string.split(","):
            if genre in genres.keys():
                genres[genre] += 1
            else:
                genres[genre] = 1
    with open("imdb-data-output.txt", "w") as file:
        file.write("\n".join(map(str, genres.items())))
main()







        # masses = []
        # for line in data.splitlines():
        #     name, id, type, reclass, mass, fall, year, lat, long, geo = line.split(",")
        #     masses.append(int(mass))
        # print("smallest meteorite weighed: {}".format(min(masses)))
#         # print("Greatest meteorite weighed: {}".format(max(masses)))
#         # print("Avreage of mass of metiorites: {}".format(mean(masses)))
# reader("Big(small)Data.csv")