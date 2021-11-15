def fizz_buzz(number):
    list = []

    def fizzy(n):
        fizz = (n % 3) == 0
        buzz = (n % 5) == 0

        if fizz and buzz:
            return 'fizzbuzz'
        elif fizz:
            return 'fizz'
        elif buzz:
            return 'buzz'
        else:
            return str(n+1)

    for i in range(number):
            list.append(fizzy(i))

            return list



if __name__ == "__main__":
    # Le Wagon locati
    nine = fizz_buzz(9)
    print(nine)
