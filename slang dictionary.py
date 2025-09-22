slang = {"CRINGE":"sesuatu yg aneh", "LOL": "Ketawa banyak", "OTW": "On The Way"}

while True:
    word = input("kata (gunakan all caps) :")
    if word in slang.keys():
        print(slang[word])
    else:
        print("tidak ada")
