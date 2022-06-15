with open('filterwithcount.csv', 'w') as ff:
    with open('filter.csv') as f:
        count = 0
        for line in f.readlines():
            if not line.startswith('1022,'):
                print(str(count)+','+line+'\r')
                ff.write(str(count)+','+line)
                count += 1
