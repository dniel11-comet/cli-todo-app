def tampilan_menu():
    print("\n========================================")
    print("           APLIKASI CATATAN TUGAS         ")
    print("==========================================")
    print("1. Lihat Daftar Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")
 
 
def main():
      
     daftar_tugas = []
     
     while True:
         tampilan_menu()
         pilihan = input("\nPilih menu (1-4): ")
         
         if pilihan == "1":
             print("\n--- DAFTAR TUGAS ---")
             if not daftar_tugas:
                 print("Belum ada tugas yang dicatat.")
             else:
                 for indeks, tugas in enumerate(daftar_tugas, start=1):
                    print(f"{indeks}. {tugas}")
                    
         elif pilihan == "2":
              tugas_baru = input("\nMasukkan tugas baru: ").strip()
              if tugas_baru:
                daftar_tugas.append(tugas_baru)
                print(f"✅ '{tugas_baru}' berhasil ditambahkan!")
              else:
                  print("⚠️ Tugas tidak boleh kosong.")
        
         elif pilihan == "3":
            print("\n--- HAPUS TUGAS ---")
            if not daftar_tugas:
                print(f"Tidak ada tugas yang bisa dihapus.")
            else:
                for indeks, tugas in enumerate(daftar_tugas, start=1):
                    print(f"{indeks}. {tugas}")
                    
                try:
                    nomor = int(input("\nMasukkan nomor tugas yang ingin dihapus: "))
                    if 1 <= nomor <= len(daftar_tugas):
                        tugas_dihapus = daftar_tugas.pop(nomor - 1)
                        print(f"🗑️ '{tugas_dihapus}' berhasil dihapus.")
                    else:
                        print("⚠️ Nomor tugas tidak ditemukan.")
                except ValueError:
                    print("⚠️ Masukkan angka yang valid!")
                    
         elif pilihan == "4":
            print("\nTerima kasih! Sampai jumpa lagi.")
            break
        
         else:
            print("⚠️ Pilihan tidak valid, silakan pilih 1-4.")


if __name__ == "__main__":
    main()     