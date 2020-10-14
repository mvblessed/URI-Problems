while True:
    try:
        a = input().split(" ")
        h = int(a[0])
        m = int(a[1])
        print(f'{int((h % 360) / 30):02d}:{int((m % 360) / 6):02d}')
    except EOFError:
        break
