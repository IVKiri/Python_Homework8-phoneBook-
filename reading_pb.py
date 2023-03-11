

def print_pb(book):
    for k, v in book.items():
        print(k, end=' - ')
        for i, j in v.items():
            print(i, end=': ')
            print(*j, end=' | ')
        print()
