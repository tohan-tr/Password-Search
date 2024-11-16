
Password Search projesi, internete sızdırılmış 20 milyon şifreyi kayıtlı olduğu dosyada bulunup bulunmadığını kontrol eden ve bulunmayan şifreleri otomatik olarak bir dosyaya kaydeden bir web uygulamasıdır. Flask tabanlı bu araç, kullanıcı dostu HTML/CSS/JS arayüzü ile hızlı ve kolay kullanım sunar.

Özellikler

    Şifre Sorgulama: Girilen şifre, password/password.txt dosyasında aranır ve bulunduğunda kullanıcıya bilgi verilir.
    Yeni Şifre Kaydetme: Şifre password.txt dosyasında yoksa, password klasöründeki new.txt dosyasına eklenir.
    Toplam Şifre Sayısı Görüntüleme: Bilgi simgesine tıklanarak toplam kayıtlı şifre sayısı görülebilir.
    Kopyalama Engeli: Güvenliği artırmak amacıyla sağ tıklama ve kopyalama gibi işlemler devre dışı bırakılmıştır.

Proje Yapısı

    start.py: Flask tabanlı web uygulamasını çalıştıran Python dosyası.
    password/password.txt: Kayıtlı şifrelerin saklandığı ana dosya.
    templates/index.html: Kullanıcı arayüzü için HTML dosyası.

Kurulum

    Projeyi klonlayın:

git clone https://github.com/tohan-tr/Password-Search/edit/main/

Gerekli bağımlılıkları yükleyin:

pip install -r requirements.txt

Uygulamayı başlatın:

    python start.py

    Tarayıcınızda http://127.0.0.1:5005 adresine giderek uygulamayı kullanabilirsiniz.

Kullanım

    Şifre Sorgulama: Şifreyi arama çubuğuna girin ve "Enter" tuşuna basarak şifre sorgulamasını başlatın.
    Sonuçlar: Şifre password.txt içinde bulunursa "Şifre bulundu!" mesajı, yoksa "Şifre bulunamadı." mesajı görünür.
    GitHub Profili: Sağ üst köşedeki GitHub düğmesine tıklayarak projenin GitHub sayfasına erişin.
