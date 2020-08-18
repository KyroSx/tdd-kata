def read_input_data() -> (str, float):
    str_input = input("Enter the name of client: ")
    float_input = float(input("Enter the value of purchase: $ "))

    return (str_input, float_input)


def read_many_inputs_times(times: int = 1
                           ) -> [(str, float)]:
    input_list = [
        read_input_data()
        for time in range(times)
    ]

    return input_list
