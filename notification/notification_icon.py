from notifypy import Notify #notification için hazır kütüphane çağırımı

notification = Notify()
notification.title = "Nice job"  #gelecek bildirimin üst başlığı
notification.message = "Hello user" #gelecek bildirimin alt mesajı
notification.icon = "icon.png" #gelecek bildirimin yanında çıkacak iconun adres bilgisi (iconu çalıştığımız dosya konumunun içerisine gönderdiğimiz için sadece adını kullandık)

notification.send()