
while True:
   
    print("Versione 1.0.0 - 'Calcolo Sconto' di TechCraft03 (Michele Paladini)\nCopyright 2019-2020 Michele Paladini\n\nThis program is free software: you can redistribute it and/or modify\nit under the terms of the GNU General Public License as published by\nthe Free Software Foundation, either version 3 of the License, or\n(at your option) any later version.\n\nThis program is distributed in the hope that it will be useful,\nbut WITHOUT ANY WARRANTY; without even the implied warranty of\nMERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\nGNU General Public License for more details.\n\nYou should have received a copy of the GNU General Public License\nalong with this program.  If not, see <http://www.gnu.org/licenses/>.")
    prz_in=float(input('\nInserisci il prezzo di partenza-> '))
    sconto=float(input('Inserisci la percentuale di sconto-> '))
    percfinale=(100-sconto)
    perzzofianle=(prz_in/100)
    final=(perzzofianle*percfinale)
    arro1=round(final,2)
    risp=(prz_in - final)
    arro2=round(risp,2)
    print('\nIl prezzo scontato è di '+str(arro1)+' euro')
    print('Hai risparmiato ' + str(arro2) +' euro')
    

    stop = input('\nDesideri continuare ad utilizzare la calcolatrice? S/N ')
    if stop == "S" or stop == "s":
        continue
    else:
        print('Grazie per aver utilizzato Il nostro calcolatore\nArrivederci!')
        break