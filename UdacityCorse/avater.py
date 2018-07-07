import media
import fresh_tomatoes

avater = media.Movie('Avatar', 'Avatar Final fight scene Jake vs Quaritch', 'https://www.google.com/search?hl=ar&tbm=isch&source=hp&biw=1280&bih=608&ei=O3cYW-K-EMbvUp-9ktAB&q=avarter&oq=avarter&gs_l=img.12...15200.15633.0.19363.2.2.0.0.0.0.0.0..0.0....0...1ac.1.64.img..2.0.0....0.jTESVsAOKaU#', 'https://www.youtube.com/watch?v=4lmrmx3cpWU')
#print (avater.storyline)
tango = media.Movie('Tango', 'تانغو - عامر لفرح بعدما شهدت على الجريمة التي نفذها: "أنا مني مجرم... ','https://www.google.com/search?hl=ar&tbm=isch&q=%D8%AA%D8%A7%D9%86%D8%AC%D9%88&chips=q:%D8%AA%D8%A7%D9%86%D8%AC%D9%88,online_chips:%D8%AA%D8%A7%D9%86%D8%BA%D9%88&sa=X&ved=0ahUKEwiV_M2uosDbAhUmLMAKHb0yDAIQ4lYIJSgB&biw=1280&bih=608&dpr=1.25#imgrc=naH4ljqKsJ7uIM:','https://www.youtube.com/watch?v=FZBhw91Pw74')
bmpt = media.Movie('BMPT', 'شاهد مركبة الدعم الناري الروسية| Terminator BMPT| اثناء اطلاق النيران|HD', 'https://www.google.com/search?hl=ar&biw=1280&bih=608&tbm=isch&sa=1&ei=u3cYW97ZMMXPgAbwrLuoBg&q=bmpt&oq=bmpt&gs_l=img.1.0.0l2j0i30k1l8.115407.130137.0.133001.14.10.1.0.0.0.271.1473.0j4j3.7.0....0...1c.1.64.img..6.8.1479.0..0i10k1j0i7i30k1j0i10i24k1j0i67k1.0.rfZ3vpmpGCE#imgrc=u_DKf_L1YHDiCM:', 'https://www.youtube.com/watch?v=1G3KIrJD3H4')
oman = media.Movie('Oman', 'Omane water', 'https://www.google.com/search?hl=ar&biw=1280&bih=608&tbm=isch&sa=1&ei=mXgYW-zpFsyTgAbL_qqwBA&q=%D8%B9%D9%8F%D9%85%D8%A7%D9%86&oq=%D8%B9%D9%8F&gs_l=img.1.0.0l10.33105.50002.0.53684.8.5.3.0.0.0.212.1021.0j2j3.5.0....0...1c..64.img..0.8.1073...35i39k1j0i5i30k1j0i24k1.0.0Wvt_P8qiXs#imgrc=-nCRdIcmULK9kM:','https://www.youtube.com/watch?v=4xtih8CCAK0')
h21 = media.Movie('Haeba21', 'مسلسل الهيبة - الحلقة 21 - محاولات سمية تبوء بالفشل', 'https://www.google.com/search?hl=ar&biw=1280&bih=608&tbm=isch&sa=1&ei=ZncYW6G2AorqgQa66qC4Bg&q=%D8%A7%D9%84%D9%87%D9%8A%D8%A8%D8%A9+2&oq=hgidf&gs_l=img.1.3.0i10i1k1j0i10i1i24k1l9.40162.41801.0.46285.5.5.0.0.0.0.579.1083.5-2.2.0....0...1c.1.64.img..3.2.1076...0j0i30k1.0.U5nN_FuUpc0#imgrc=_', 'https://www.youtube.com/watch?v=xzRpEOIaW7Q')
h20 = media.Movie('Haeba20', 'مسلسل الهيبة - الحلقة 20 - بعد زواج منى.. ابنة جديدة لناهد', 'https://www.google.com/search?hl=ar&biw=1280&bih=608&tbm=isch&sa=1&ei=ZncYW6G2AorqgQa66qC4Bg&q=%D8%A7%D9%84%D9%87%D9%8A%D8%A8%D8%A9+2&oq=hgidf&gs_l=img.1.3.0i10i1k1j0i10i1i24k1l9.40162.41801.0.46285.5.5.0.0.0.0.579.1083.5-2.2.0....0...1c.1.64.img..3.2.1076...0j0i30k1.0.U5nN_FuUpc0#imgrc=BG9ufdnWvqgMbM:', 'https://www.youtube.com/watch?v=PqnN3aLay2E')
# Movies list
'''
movies = [avater, tango, bmpt, oman, h21, h20]
fresh_tomatoes.open_movies_page(movies)
'''
print (media.Movie.__doc__)
print (media.Movie.__name__)
print (media.Movie.__module__)
