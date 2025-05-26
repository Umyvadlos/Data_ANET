from datetime import date, timedelta
import unittest


#konstanty pro navraceni kodu
MISS = -1 #nejake obdobi chybi
OK = 0
OVER = 1 #nejake obdobi je fakturovano navic


#testovani, vola se napr pomoci: python3 -m unittest pondeli.py
#manual viz https://docs.python.org/3/library/unittest.html
class TestKontrolaPausaly(unittest.TestCase):
  def test_porovnani_terminu(self):
    """Test porovnani terminu.
    """
    termin_pripojen = (
      #od                 do
      (date(2025, 4,  3), date(2025, 4, 12)),
      (date(2025, 4, 28), date(2025, 5, 18))
    )
    termin_fakturovano = (
      #od                 do
      (date(2025, 4, 17), date(2025, 5, 16)),
    )

    self.assertEqual(
      porovnej_terminy(termin_pripojen, termin_fakturovano),
      (MISS,
        ( #od                 do
          (date(2025, 4,  3), date(2025, 4, 12)),
          (date(2025, 5, 17), date(2025, 5, 18))
        )
      )
    )

  def test_vytvor_terminy(self):
    """Test vytvoreni terminu z datumu.
    """
    datumy = (
      date(2025, 4,  3),
      date(2025, 4,  4),
      date(2025, 4,  5),
      date(2025, 4,  6),
      date(2025, 4,  7),
      date(2025, 4,  8),
      date(2025, 4,  9),
      date(2025, 4, 10),
      date(2025, 4, 11),
      date(2025, 4, 12),
      date(2025, 5, 17),
      date(2025, 5, 18),
    )

    self.assertEqual(
      vytvor_terminy(datumy),
        ( #od                 do
          (date(2025, 4,  3), date(2025, 4, 12)),
          (date(2025, 5, 17), date(2025, 5, 18))
        )
    )


def vytvor_terminy(datumy, max_mezera=1):
    """Ze zadaných dat vytvoří spojité termíny (intervaly).
    @param datumy (tuple of date): Jednotlivé datumy.
    @param max_mezera (int): Největší povolená mezera (ve dnech) mezi daty, která se ještě spojují.
    @return (tuple of (date, date)): Souvislé termíny.
    """

    terminy = []

    start = datumy[0]
    end = datumy[0]

    for d in datumy[1:]:
        if d <= end + timedelta(days=max_mezera):
            end = d
        else:
            terminy.append((start, end))
            start = end = d

    terminy.append((start, end))
    return tuple(terminy)


  
  #TODO naprogramovat
#  return (
    #od                 do
 #   (date(2025, 4,  3), date(2025, 4, 12)),
  #  (date(2025, 5, 17), date(2025, 5, 18))
  #)


from datetime import date, timedelta

MISS = -1
OK = 0
OVER = 1

def porovnej_terminy(termin_pripojen, termin_fakturovano):
    """
    Porovna zadane terminy. Vychazi z termin_pripojen, zjistuje jestli v termin_fakturovano neco chybi, pripadne prebyva.
    Nejdriv kontroluje jestli neco chybi, pak az prebyva.

    @param termin_pripojen (tuple of (date, date)): Terminy pripojeni.
    @param termin_fakturovano (tuple of (date, date)): Vyfakturovane terminy.
    @return (tuple): (stav, (terminy))
        stav (int): MISS | OK | OVER
        terminy (tuple of (date,date)): Terminy od-do, s timto stavem.
    """


def generuj_dny(intervaly):
    dny = set()
    for od, do in intervaly:
        aktualni = od
        while aktualni <= do:
            dny.add(aktualni)
            aktualni += timedelta(days=1)
    return dny

def spoj_dny_do_intervalu(seznam_dnu):
    """Spojí sousední dny do intervalů (od, do)."""
    if not seznam_dnu:
        return []

    seznam_dnu = sorted(seznam_dnu)
    intervaly = []
    start = seznam_dnu[0]
    konec = start

    for d in seznam_dnu[1:]:
        if d == konec + timedelta(days=1):
            konec = d
        else:
            intervaly.append((start, konec))
            start = konec = d
    intervaly.append((start, konec))
    return intervaly

def porovnej_terminy(termin_pripojen, termin_fakturovano):
    dny_pripojeni = generuj_dny(termin_pripojen)
    dny_fakturovane = generuj_dny(termin_fakturovano)

    chybne = sorted(dny_pripojeni - dny_fakturovane)

    if chybne:
        return spoj_dny_do_intervalu(chybne)

    return () 







#  #TODO naprogramovat
#  return MISS, (
#    #od                 do
#    (date(2025, 4,  3), date(2025, 4, 12)),
#    (date(2025, 5, 17), date(2025, 5, 18))
#  )


if __name__ == "__main__":
  # vytvor_terminy
  datumy = (
    date(2025, 4,  3),
    date(2025, 4,  4),
    date(2025, 4,  5),
    date(2025, 4,  6),
    date(2025, 4,  7),
    date(2025, 4,  8),
    date(2025, 4,  9),
    date(2025, 4, 10),
    date(2025, 4, 11),
    date(2025, 4, 12),
    date(2025, 5, 17),
    date(2025, 5, 18),
  )

  vysl = vytvor_terminy(datumy)
  print(vysl)

  # porovnej_terminy
  termin_pripojen = (
    #od                 do
    (date(2025, 4,  3), date(2025, 4, 12)),
    (date(2025, 4, 28), date(2025, 5, 18))
  )
  termin_fakturovano = (
    #od                 do
    (date(2025, 4, 17), date(2025, 5, 16)),
  )

  vysl = porovnej_terminy(termin_pripojen, termin_fakturovano)
  print(vysl)
