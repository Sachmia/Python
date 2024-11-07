# Plan

import json

# Klass för artist

# Klass för band plus medlemmar

# Klass för album


# VG: Funktion spara JSON-fil: (save_data())

# VG: Funktion ladda data från JSON: (load_data())

# Funktion lägga till artist: add_artist()
# Användare: Lägga till en artist, inklusive namn och (valfritt) instrument
# VG: Undvika duplicering av artister

# Funktion lägga till band: add_band()
# Användare: Skapa ett band genom att ange ett bandnamn
# Dictionary som innehåller bandnamnet som nyckel och en lista med medlemmar (artister och deras instrument) som värde
# VG: Undvika duplicering av band

# Funktion lägga till album: add_album()
# Användare: Lägg till ett album med namn och eventuellt ett släppår.
# Om albumet är ett soloalbum ska det kopplas till en artist, och om det är ett bandalbum ska det kopplas till ett band.
# Dictionary håller reda på albumets namn som nyckel och dess tillhörande artist eller band
# VG: Undvika duplicering av album

# Funktion för att koppla artist till band: add_artist_to_band()
# Användare: koppla en artist till ett band, och även specificera vilket instrument artisten spelar i bandet
# Info om koppling lyckas eller misslyckas

# Funktion för att söka data: search()
# Sök efter band: Visa en lista med bandens namn och deras medlemmar
# Sök efter artist: Visa en lista med artister och eventuella band de är med i
# Sök efter album: Visa en lista med album och tillhörande artist eller band
# VG: Informera användaren om felaktig inmatning (t.ex., om band eller artist inte finns vid sökning)

# VG: Funktion ta bort artister, band och album

# VG: Allmänt att lägga till: Användarvänlig felhantering

# VG: I mån av tid
Användarvänlig Meny: Programmet ska ha under-menyer och minst kunna göra filtrerade sökningar såsom: Alla Band, Specifik Band, Alla Artister, Specifik Artist, Alla Album, Specifikt Album
