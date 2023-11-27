def read_csv(name, value_types, delimiter=' '):
    with open(name, "r") as file:
        data = []
        lines = [line for line in file]
        row_0 = [el.strip() for el in lines[0].split(delimiter)]

        data.append(row_0)  # keep first row
        n_columns = len(row_0)  # number of values on a row
        if len(value_types) != n_columns:
            raise Exception(f"Wrong number of value types, expected {n_columns}, got {len(value_types)}")

        for i in range(1, len(lines)):
            row = [el.strip() for el in lines[i].split(delimiter)]
            # missing values
            if len(row) != n_columns:
                raise Exception(f"Wrong number of columns on row {i + 1}")
            new_row = []
            # check the value type of each element on a row
            for j in range(0, len(row)):
                try:
                    new_row.append(value_types[j](row[j]))
                except:
                    raise Exception(f"Expected value of type {value_types[j]} on row {i + 1}, column {j + 1}")
            data.append(new_row)
        return data
