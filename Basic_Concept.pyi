# Stationary
## Serinin istatiksel özelliklerinin zaman içerisinde zaman içerisinde değişmemesidir.
### Durağınlığı incelemek için bazı istatiki testler incelenmelidir.
## Bir zaman serisinin ortalaması, varyansı ve kovaryansı zaman boyunca
## sabit kalıyorsa, serinin durağan olduğu ifade edilir
#-- Buraya grafik ekle
## Aynı şekilde ilerleyen grafiğin bir sonraki adımı daha kolay tahmin edilebilir.
## Durağanlık sağlanmıyorsa bunu sağlamamız gerekmektedir.
##Bunu yapmak için farklı yöntemler kullanabiliriz.

# Trend

##Bir zaman serisinin  uzun vadedeki artış ya da azalışının gösterdiği yapıya trend denir.
#- Grafik koy
## Her yılın ortalaması alınırsa bu artış veya azalışda görülebilmektedir.

# Mevsimsellik (Seasonality)

## Mevsimsellik ise bir grafiğin belirli adımlarla artıp azalmasıdır ve bunu tekrarlamasıdır

# Döngü(Cycle)

##Belirli bir mevsimsellik var gibi gözüksede bazı anlık durumlar gerçekleşebilir
##Bunun sebebi ise yapısal bozukluklar siyasi ortam gibi farklı nedenler olabilmektedir.

# Hareketli Ortalama(Moving Average)

## Bir zaman serisinin gelecek değeri kendisinin k adet önceki değerinin ortalamasıdır.
## Hareketli ortalama bize trend hakkında bilgi verir.
## Bu sayede eğimin ne tarafa olduğu hakkında bilgi edinmiş oluruz
## Window Size kaç adımlı hareketli ortalama alınacağını ifade eder.
## window size arttırıldığında farkın açıldığını görebiliriz.
## Bunun sebebi ise alt ve üst limitlerde reaksiyonların geriden gelmesidir.
## Ayrıca önemli not olarak bir zaman serisi en çok kendinden bir adım önce gelen değerden etkilenir.


# Ağırlıklı Ortalama(Weighted Average)

## Ağırlıklı ortalama hareketli ortalamaya benzer.
##Fikir olarak tek fark ise 12 adımlık bir window size olduğunu düşünürsek
### Son 4 adıma %80 gibi bir ağırlık verirken 4-8. adımlara %15 8 ve üstüne %5 gibi ağırlık verilmesi denebilir.
## Bunun haricinde ise window size 4 olarak düşünürsek
### 1. ye %60 2.ye %20 3.ye %15 4.ye de %5 vererekte ağırlıklı ortalama hesaplaması yapabiliriz.

#Smoothing Yöntemleri

##Smoothing düzeltmek anlamına gelmektedir
##Singe Exponential Smoothing(Sadece durağan serilerde . Trend ve mevsimsellik olmamalı)
##Double Exponential Smoothing(Level + Trend . Mevsimsellik olmamalı)
##Triple Exponential Smoothing a.k.a. Holt Winters(Level + Trend + Mevsimsellik )

##Biz elimize veriler geldiğinde
### Bizim bu yöntemler arasında seçim yapmak için tek ilkemiz model başarısının en fazla olduğudur.
#### Optimizasyonla denemeleri yaparak en az hatası olan yöntem üzerinden ilerleyeceğiz.

#Singe Exponential Smoothing
##Üssel düzenleme yaparak tahminde bulunur.
##Gelecek yakın geçmişle daha fazla ilişkilidir varsayımı ile geçmişin ekilerini ağırlıklandırılır.
##Geçmiş gerçek değerler ve geçmiş tahmin edilen değerlerin üssel olarak ağırlandırılmasıyla tahmin yapılır.
##Geçmişten gelen bilgiyi taşıma zorunluluğu vardır fakat ağırlık değişirilebilir.
###Yani gerçek değerlere daha fazla kat sayı verilirken
#### Geçmiş tahminlerin kat sayısı otomatik olarak düşecektir.
##### Bu da yöntemin genel kuralından kaynaklanır.
