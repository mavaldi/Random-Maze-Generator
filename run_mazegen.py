from mazegen import maze,COLOR,agent

# default run = 10x10 maze
# jika ingin mengganti ukuran bisa dengan cara: maze(20,20)
m=maze()

# dalam CreateMaze bisa ditentukan goal cellnya ex: (2,3)
# bisa menentukan pattern maze 'v'/'V' untuk bentuk yang lebih vertikal dan 'h'/'H' untuk bentuk yang lebih horizontal ex: (pattern='h')
# bisa menentukan berapa banyak multiple path dengan cara (loopPercent=50)
# bisa menyimpan files maze hasil generate dalam file .csv dengan cara (saveMaze=True)
# apabila ingin melakukan load pada file maze yang sebelumnya tersimpan bisa menggunakan (loadMaze="filename")
# warna juga bisa diubah dengan cara (theme='light')
m.CreateMaze()

# inisiasi titik yang akan menjelajahi maze
# tempat spawn titik bisa ditentukan dengan cara (3,2)
# (filled=True) jika titik ingin memenuhi cell
# aktifkan footprint jika ingin melihat jejak pergerakan titik (footprints=True)
# ubah warna dengan cara (color='red')
a=agent(m, footprints=True, filled=True)

# menandai cell ini jika dilewati saat titik menuju goal cell, tambahkan (showMarked=True) pada m.tracePath
# m.markCells=[(1,1),(2,2),(1,2),(2,1),(5,5)]

# membuat titik untuk bergerak ke goal cell dengan jalan tercepat
# atur kecepatan berpindah titik dengan menambahkan ({}, delay=100)
m.tracePath({a:m.path}, delay=50)

print(m.path)

m.run()