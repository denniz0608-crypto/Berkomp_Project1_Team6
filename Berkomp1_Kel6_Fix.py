kendaraan = int(input("Masukkan Jumlah Kendaraan:"))
data_plat = []
plat = []
jenis = []
kecepatan = []
handphone = []
statusk = [] #status kecepatan kendaraan
statusp = [] #status ada sealtbelt/helm
statushp = [] #status ada penggunaan handphone
statuspl = [] #status ada plat nomor 
denda=[]
#data timestamp
tanggal=[]
bulan=[]
tahun=[]
jam=[]
menit=[]

for i in range (kendaraan):
    database = input("Database Plat Nomor: ")
    data_plat.append(database)    
    print("--------------------")
    print("Timestamp kendaraan ke-" + str(i+1))
    tglkend = int(input("Tanggal: "))
    tanggal.append(tglkend)
    blnkend = int(input("Bulan: "))
    bulan.append(blnkend)
    thnkend = int(input("Tahun: "))
    tahun.append(thnkend)
    jamkend = int(input("Pukul: "))
    jam.append(jamkend)
    mntkend = int(input("Menit: "))
    menit.append(mntkend)


for i in range(kendaraan):
    print("--------------------")
    platkend = input("Plat Kendaraan " + str(i+1) + ":")
    plat.append(platkend)
    jenkend = input("Jenis Kendaraan " + str(i+1) + "(Motor/Mobil):")
    jenis.append(jenkend)
    keckend = int(input("Kecepatan Kendaraan " + str(i+1) + ":"))
    kecepatan.append(keckend)
    mainhp = input("Menggunakan Handphone (Ya/Tidak): ")
    if mainhp == "Ya":
        handphone.append(True)
    else:
        handphone.append(False)
    

# Pelanggaran umum
    if handphone[i]:
        statushp.append(True)
    else:
        statushp.append(False)
    #-----------------------------
    if plat[i] in data_plat:
        statuspl.append(True)
    else:
        statuspl.append(False)
    if kecepatan[i] > 50:
        statusk.append("Kecepatan Melebihi Batas")
    else:
        statusk.append("Aman")
    
# Untuk kendaraan motor
    if jenkend == "Motor":
        Pengkendmtr = input("Menggunakan Helm (Ya/Tidak): ")
        if Pengkendmtr == "Ya":
            statusp.append(True)
        else:
            statusp.append(False)
# Untuk kendaraan Mobil
    elif jenkend == "Mobil":
        Pengkendmbl = input("Menggunakan sabuk (Ya/Tidak): ")
        if Pengkendmbl == "Ya":
            statusp.append(True)
        else:
            statusp.append(False)
    totaldenda = 0
    if statusk[i] !="Aman":
        totaldenda = totaldenda + 500000
    if not statusp[i] :
        totaldenda = totaldenda + 250000
    if not statuspl[i]:
        totaldenda = totaldenda + 500000
    if statushp[i] :
        totaldenda = totaldenda + 750000
    denda.append(totaldenda)
    print("--------------------")

#Untuk plat belom
print("=== LAPORAN ETLE ===")
for i in range(kendaraan):
    print("Tanggal/Waktu:", tanggal[i], "/", bulan[i], "/", tahun[i], "  ", jam[i], ":", menit[i])
    print("Plat:", plat[i])
    print("Jenis:", jenis[i])
    print("Kecepatan:", kecepatan[i], "km/jam")
    #Tiga pelanggaran
    if statusk[i] != "Aman" and not statusp[i] and statushp[i]:
        if jenis[i]=="Motor":
            print("Status: Pelanggaran Kecepatan, Helm, dan Handphone")
        elif jenis[i]=="Mobil":
            print("Status: Pelanggaran Kecepatan, Seatbelt, dan Handphone")
    #dua pelanggaran
    elif statusk[i] != "Aman" and not statusp[i]:
        if jenis[i]=="Motor":
            print("Status: Pelanggaran Kecepatan dan Helm")
        elif jenis[i]=="Mobil":
            print("Status: Pelanggaran Kecepatan dan Seatbelt")
    elif statusk[i] != "Aman" and statushp[i]: 
        print("Status: Pelanggaran Kecepatan dan Handphone")
    elif not statusp[i] and statushp[i]:
        if jenis[i]=="Motor":
            print("Status: Pelanggaran Helm dan Handphone")
        elif jenis[i]=="Mobil":
            print("Status: Pelanggaran Seatbelt dan Handphone")
    #satu pelanggaran
    elif statusk[i] != "Aman": 
            print("Status: Pelanggaran Kecepatan")
    elif statushp[i]:
        print("Status: Pelanggaran Handphone")
    elif not statushp[i]:
        if jenis[i]=="Motor":
            print("Status: Pelanggaran Helm")
        elif jenis[i]=="Mobil":
            print("Status: Pelanggaran Seatbelt")
    else:
        print("Status: Aman")
    
    if not statuspl[i]:
        print("Peringatan: Plat Nomor tidak terdeteksi di Database") 
    print("Denda: Rp", denda[i])
    print("--------------------")
