from farm.cow import Cow
from farm.chicken import Chicken

print("\n\n📝 Üçüncü Gün: Hayvanlar Konuşuyor")

# 1. Kodu okuyun ve sınıfları kodlamak için bazı ipuçları toplayın.
cow = Cow()
female_chicken = Chicken('female')
male_chicken = Chicken('male')

print(f"İnek {cow.talk()} diyor.")
print(f"Dişi tavuk {female_chicken.talk()} diyor.")
print(f"Erkek tavuk {male_chicken.talk()} diyor")

print("\n\n📝 Dördüncü Gün: Hayvanları Besle")

# 1. Tüm hayvanlarını `animals` listesinde sakla
pass  # BURAYA KODUNU YAZ
animals =[]
animals.append(cow)
animals.append(female_chicken)
animals.append(male_chicken)
# 2. Her hayvan için `feed` yöntemini çağır (liste üzerinde bir döngü kullan)
pass  # BURAYA KODUNU YAZ
for animal in animals:
    animal.feed()
# 3. TODO'ları değiştirin

# 4. Aşağıdaki 3 satırı yazdırın:
# "The cow produced ## liters of milk"
# "The female chicken produced ## eggs"
# "The male chicken produced ## eggs"
pass  # KODUNUZ BURAYA
print(f"The cow produced {cow.milk} liters of milk")
print(f"The female chicken produced {female_chicken.eggs} eggs")
print(f"The male chicken produced {male_chicken.eggs} eggs")