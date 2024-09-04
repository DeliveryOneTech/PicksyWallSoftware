from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from app.styles import Styles
from app.ui.utils import ui_utils


class ApproveWithCheckboxInputComponent(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.is_approved = False
        self.setupUi(self)

    def setupUi(self, approve_with_checkbox_input):
        approve_with_checkbox_input.setObjectName("approve_with_checkbox_input")
        self.layout = QtWidgets.QHBoxLayout(approve_with_checkbox_input)
        self.layout.setObjectName("layout")

        # Checkbox & Label
        self.condition_checkbox = QtWidgets.QCheckBox(approve_with_checkbox_input)
        self.condition_checkbox.setObjectName("condition_checkbox")
        self.layout.addWidget(self.condition_checkbox)

        self.condition_label = QtWidgets.QLabel(approve_with_checkbox_input)
        self.condition_label.setObjectName("condition_label")
        self.layout.addWidget(self.condition_label)

        self.retranslateUi()

    def retranslateUi(self):
        self.condition_label.setText(
            "<html><head/><body><p>Bu sistemde girdiğiniz T.C. kimlik numarası ve diğer kişisel verileriniz, kargo gönderim ve teslimat işlemlerinin gerçekleştirilmesi amacıyla işlenmektedir. Verileriniz, 6698 sayılı Kişisel Verilerin Korunması Kanunu'na uygun olarak saklanmakta ve korunmaktadır. Kişisel verilerinizle ilgili haklarınızı ve detaylı bilgiyi <a href='kvkk'>buraya tıklayarak</a> öğrenebilirsiniz.</p></body></html>")
        self.condition_label.setStyleSheet(Styles.label())
        self.condition_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.condition_label.setWordWrap(True)

        self.condition_checkbox.setStyleSheet(Styles.lg_checkbox())
        self.condition_checkbox.setChecked(False)
        self.condition_checkbox.stateChanged.connect(self.on_checkbox_state_changed)

        self.condition_label.linkActivated.connect(self.on_privacy_policy_link_clicked)

    def on_checkbox_state_changed(self, state):
        self.is_approved = state == 2

    def on_privacy_policy_link_clicked(self, url):
        if url == 'kvkk':
            dialog = QDialog()
            dialog.setWindowTitle("KVKK Aydınlatma Metni")
            dialog.setWindowFlag(Qt.FramelessWindowHint)
            dialog.setWindowModality(Qt.ApplicationModal)
            dialog_layout = QVBoxLayout(dialog)
            dialog_layout.setContentsMargins(20, 20, 20, 20)
            dialog.setFixedSize(600, 700)

            icon_label = QLabel()
            icon_label.setPixmap(ui_utils.get_pixmap(':/icons/assets/spellcheck.svg'))
            icon_label.setAlignment(Qt.AlignCenter)
            dialog_layout.addWidget(icon_label)

            # add space
            dialog_layout.addSpacing(10)

            scroll_area = QtWidgets.QScrollArea()
            scroll_area.setWidgetResizable(True)
            dialog_layout.addWidget(scroll_area)
            scroll_area.setStyleSheet("QScrollArea {border: 0px;}")

            label = QLabel()
            label.setText(
                '<html><head/><body>\n'
                '<div style="padding: 0cm 0cm 1pt; border-top: none; border-right: none; border-bottom: 1pt solid #4a66ac; border-left: none; text-align: justify;"><p><strong>1.GİRİŞ</strong></p><p>İşbu aydınlatma metni, 6698 sayılı Kişisel Verilerin Korunması Kanununun (“Kanun”) 10. maddesi uyarınca, T.C. KÜLTÜR VE TURİZM BAKANLIĞI (“VERİ SORUMLUSU”) tüzel kişiliği, ilgili müdürlük ve birimleri ve hizmet merkezlerinde toplanan kişisel verilerin işlenmesine ilişkin ilgili kişilerin aydınlatılması amacı ile hazırlanmıştır.&nbsp;</p><p>VERİ SORUMLUSU, kişisel verilerin işlenmesi, korunması ve güvenliği hususuna azami hassasiyet ve gayret göstermektedir.</p><p>Kişisel veriler VERİ SORUMLUSU tarafından her türlü işitsel, yazılı, görsel ya da elektronik yöntemlerle toplanabilecektir. </p><p>Bu kapsamda ve Kanun gereğince ilgili kişilerin kişisel verileri VERİ SORUMLUSU tarafından Kanunda sayılan genel ilkeler doğrultusunda gerçekleştirilmesi gereken iş ve işlemler için Veri Sorumlusu sıfatıyla işlenebilecektir.</p><p><strong>2.KİŞİSEL VERİLERİN İŞLENME AMACI</strong></p><p>Kişisel veriler, Kanun’un 5. ve 6. maddelerinde belirtilen kişisel veri işleme şartları ile Kanun’da belirtilen amaçlar çerçevesinde ve sınırlı olmamak kaydıyla aşağıda belirtilen amaçlarla işlenmektedir. Buna göre kişisel verilerin işlenme amacı;</p><ol><li>VERİ SORUMLUSU ‘un ilgili mevzuatlar çerçevesinde yükümlü olduğu iş ve işlemleri yürütebilmesi, vazife ve sorumlulukları çerçevesinde kamu hizmetini ifa etmesi,</li><li>VERİ SORUMLUSU tarafından sunulan hizmetlerden maksimum faydanın sağlanması için gerekli çalışmaların yapılması,</li><li>VERİ SORUMLUSU ‘un ve paydaşların hukuki yükümlülüklerinin ve hizmet güvenliğinin sağlanması, </li><li>VERİ SORUMLUSU ’un hizmetlerinin ve stratejilerinin sürdürülmesi,</li><li>VERİ SORUMLUSU’na haklar, vazifeler, iş ve işlemler yükleyen kanunlar ve ilgili mevzuatlar uyarınca sorumluluklarını ifa etme, </li><li>VERİ SORUMLUSU’nun insan kaynakları ve istihdam politikalarının yönetilmesi</li><li>Kültür Varlıklarının korunması işlemlerinin yürütülmesi</li><li>Kütüphanecilik faaliyetlerinin yürütülmesi</li><li>Destek, hibe, teşvik vb. işlemlerin gerçekleştirilmesi</li><li>Müzelere ilişkin işlemlerin gerçekleştirilmesi</li><li>Avrupa ve dış ilişkilerin yönetilmesi</li><li>Basın ve yayın faaliyetlerinin yürütülmesi</li><li>Sanatsal etkinlik, faaliyet vb. hususlarda çalışmaların yapılması</li><li>Hizmet ve yönetim kalitesinin arttırılması ve bu kapsamda çalışmaların yapılması</li></ol><p>VERİ SORUMLUSU, kişisel verilerin hukuka aykırı olarak işlenmesinin ve verilere hukuka aykırı olarak erişilmesinin önlenmesi ve kişisel verilerin güvenli bir şekilde muhafaza edilmesi amacıyla gerekli hukuki, teknik ve idari tedbirleri en üst seviyede, kanunda belirtilen ilkeler doğrultusunda işlemeye gayret göstermektedir.</p><p><strong>3.KİŞİSEL VERİLEN PAYLAŞILMASI VE AKTARILMASI</strong></p><p>Çalışanlar, çalışan adayları, stajyer, habere konu kişi, potansiyel ürün veya hizmet alıcısı, ürün veya hizmet alıcısı, tedarikçi çalışanı, tedarikçi yetkilisi, veli/vasi/temsilci, ziyaretçi ve diğer vatandaşlardan toplanan kişisel veriler, Kanun’un 8. ve 9. maddelerinde belirtilen şartlar çerçevesinde VERİ SORUMLUSU’nun tedarikçileri, hizmet sağlayıcıları, veri işleyenleri ve yasal olarak yetkili kurum ve kuruluşlar ile, ilgili mevzuatlar çerçevesinde, kişisel veri işleme şartları ve amaçları doğrultusunda paylaşılabilecektir. </p><p>VERİ SORUMLUSU, kişisel verilerin paylaşılması halinde gerekli idari ve teknik tedbirleri, tüm güvenlik önlemlerini almaya özen göstermektedir. Ayrıca VERİ SORUMLUSU ISO 27001 Bilgi Güvenliği Yönetim Sistemi ve diğer bilgi ve veri güvenliğine ilişkin çalışmalar gerçekleştirmektedir. VERİ SORUMLUSU verilerinizin aktarılması ve paylaşılması hususunda dikkat ve özen yükümlülüğüne uymakta, verilerinize ve güvenliğine değer vermektedir.</p><p><strong>4.KİŞİSEL VERİ TOPLAMA YÖNTEMİ VE HUKUKİ SEBEBİ</strong></p><p>VERİ SORUMLUSU kişisel verileri, her türlü işitsel, yazılı, görsel ve elektronik ortamda ve işbu aydınlatma metninde belirtilen amaçlar çerçevesinde, VERİ SORUMLUSU’nun sunmuş olduğu hizmetlerin yasalara ve ilgili mevzuata uygun olarak sunulabilmesi ve yine VERİ SORUMLUSU’nun sözleşme ve yasalardan doğan yükümlülüklerini eksiksiz olarak yerine getirebilmesi, iş faaliyetlerinin yürütülmesi gibi birçok hukuki sebebe dayalı olarak toplamakta, Kanun’da belirtilen şartlara uygun olarak işlemektedir. Hukuki sebepler şu şekildedir;</p><ul style="list-style-type: disc;"><li>İlgili kişinin açık rızasının varlığı,</li><li>Kanunlarda açıkça öngörülmesi,</li><li>Fiili imkânsızlık nedeniyle rızasını açıklayamayacak durumda bulunan veya rızasına hukuki geçerlilik tanınmayan kişinin kendisinin ya da bir başkasının hayatı veya beden bütünlüğünün korunması için zorunlu olması,</li><li>Bir sözleşmenin kurulması veya ifasıyla doğudan doğruya ilgili olması kaydıyla sözleşmenin taraflarına ait kişisel verilerin işlenmesinin gerekli olması,</li><li>Veri sorumlusunun hukuki yükümlülüğünü yerine getirebilmesi için zorunlu olması,</li><li>İlgili kişinin kendisi tarafından alenileştirilmiş olması,</li><li>Bir hakkın tesisi, kullanılması veya korunması için veri işlemenin zorunlu olması,</li><li>İlgili kişinin temek hak ve özgürlüklerine zarar vermemek kaydıyla, veri sorumlusunun meşru menfaatleri için veri işlenmesinin zorunlu olması</li></ul><p><strong>5.KİŞİSEL VERİ SAHİPLERİNİN HAKLARI VE HAKLARIN KORUNMASI</strong></p><p>Kişisel veri sahipleri Kanun’un 11. maddesi uyarınca;</p><ol><li>Kişisel veri işlenip işlenmediğini öğrenme,</li><li>Kişisel verileri işlenmişse buna ilişkin bilgi talep etme,</li><li>Kişisel verilerin işlenme amacını ve bunların amacına uygun kullanılıp kullanılmadığını öğrenme,</li><li>Yurt içinde veya yurt dışında kişisel verilerin aktarıldığı üçüncü kişileri bilme,</li><li>Kişisel verilerin eksik veya yanlış işlenmiş olması hâlinde bunların düzeltilmesini isteme,</li><li>Kanun’un 7. maddesinde öngörülen şartlar çerçevesinde kişisel verilerin silinmesini veya yok edilmesini isteme,</li><li>5. ve 6. maddeler uyarınca yapılan işlemlerin, kişisel verilerin aktarıldığı üçüncü kişilere bildirilmesini isteme,</li><li>İşlenen verilerin münhasıran otomatik sistemler vasıtasıyla analiz edilmesi suretiyle kişinin kendisi aleyhine bir sonucun ortaya çıkmasına itiraz etme,</li><li>Kişisel verilerin kanuna aykırı olarak işlenmesi sebebiyle zarara uğraması hâlinde zararın giderilmesini talep etme, </li></ol><p>haklarına sahiptir.&nbsp;</p><p>Söz konusu hakların kullanılması için, kişisel veri sahipleri tarafından VERİ SORUMLUSU’na, yazılı olarak veya Kişisel Verileri Koruma Kurulu tarafından belirlenecek diğer yöntemlerle başvurulması halinde, başvurular talebin niteliğine göre en kısa zamanda ancak her halükârda en geç 30 gün içerisinde sonuçlandırılır. VERİ SORUMLUSU’na başvuru için adres ve iletişim bilgileri aşağıda belirtilmiştir.</p><p><strong>6.İLETİŞİM</strong></p><p>İşbu aydınlatma metni kapsamında yer alan hususlara ilişkin detaylı bilgilere T.C. KÜLTÜR VE TURİZM BAKANLIĞI Kişisel Verilerin Korunması ve İşlenmesi Politikasından ulaşılabilmektedir.</p><p>Kanun’dan doğan haklarınızı kullanmak için, kimlik bilgilerinizi, kullanmak istediğiniz hakkı ve talebinizin konusunu anlatan detaylı açıklamanızı aşağıdaki linkteki formu doldurarak imzalı şekilde İSMET İNÖNÜ BULVARI NO:32 06100 EMEK ANKARA/TÜRKİYE adresine başvuru formunda belirtilen yollardan birini kullanarak gönderebilirsiniz. Ayrıntılı bilgiye başvuru formu ve +90 (312) 470 8000 iletişim hattı ile ulaşabilirsiniz.</p></div>\n'
                '</body></html>')
            label.setStyleSheet(Styles.label())
            label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            label.setWordWrap(True)
            dialog_layout.addWidget(label)

            scroll_area.setWidget(label)

            # add space
            dialog_layout.addSpacing(20)

            h_box = QtWidgets.QHBoxLayout()

            close_button = QPushButton("Kapat")
            close_button_font = close_button.font()
            close_button_font.setPointSize(11)
            close_button.setFont(close_button_font)
            close_button.clicked.connect(dialog.close)
            close_button.setStyleSheet(Styles.btn_danger())

            accept_button = QPushButton("Okudum, Anladım ve Kabul Ediyorum")
            accept_button_font = accept_button.font()
            accept_button_font.setPointSize(11)
            accept_button.setFont(accept_button_font)
            accept_button.clicked.connect(lambda: self.condition_checkbox.setChecked(True) or dialog.close())
            accept_button.setStyleSheet(Styles.btn_success())

            h_box.addWidget(close_button)
            h_box.addWidget(accept_button)

            dialog_layout.addLayout(h_box)

            dialog.exec_()
