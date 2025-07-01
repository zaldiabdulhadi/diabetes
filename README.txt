Langkah - Langkah Mengerjakan Projek ini

1 . Menentukan Library yang akan digunakan
2. Melakukan Load Dataset 
3. Pemisahan Data Training dan Data Testing
4. Membuat Data Latih Menggunakan Algoritma SVM
5. Membuat Model Evaluasi untuk mengukur tingkat akurasi
6. Membuat Model Prediksi

Noted on this project :

Library Yang digunakan : numpy, pandas, sklearn.model_selection train_test_split(), sklearn SVM, sklearn.metrics accuracy_score

Di Project Ini harusnya dilakukan StandarisasiData, namun entah kenapa ketika telah dilakukan StandarisasiData, Hasil Prediksi malah tidak sesuai, jadi pada project ini dilewati Proses StandarisasiData

Data Training -> Data yang berasal dari dataset, di mana data tersebut dilatih supaya dapat melakukan prediksi (Mesin Mengetahui Outcomenya Dluan)
Data Testing -> Data yang berasal dari sebagian dataset (biasanya hanya 20%), di mana data tersebut dicoba untuk melakukan prediksi setelah data di training (Mesin Tidak Mengetahui Outcomenya dan ia akan menebak outcome)


Saat Mencoba Model Prediksi Dengan Input dari kita, Reshape data menggunakan numpy, Langkahnya Sebagai Berikut :
1. Ubah Tuple/List menjadi numpy array
2. Lakukan Reshape Menjadi Array 2d dengan melakukan reshape(1, -1) (1 baris, sesuai_jumlah_kolom)

Menyimpan Model Prediksi dengan library picke