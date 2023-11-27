import CsvReader as Csv
import MathModule as m
import MergeFiles as me
import PasswordGenerator as pg

if __name__ == '__main__':
    # ex1
    data = Csv.read_csv("trafic.csv", value_types=[float, float], delimiter=',')
    print(data)

    # ex2
    x = 2
    y = 10.0
    print(m.sum(x, y))
    print(m.diff(x, y))
    print(m.mult(x, y))
    print(m.div(x, y))

    # ex3
    me.merge("final_file.txt", "\n", "file1.txt", "file2.txt")
    with open("final_file.txt", "r") as file:
        for line in file:
            print(line.strip())

    # ex4
    print(pg.generate_password(10, mixed_case=False))
