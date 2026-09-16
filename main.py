
# Använder en class för att skapa objekt för böckerna.
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self.borrowed = False


# Böcker som redan finns i biblioteket.
book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("Pippi Långstrump", "Astrid Lindgren")
book3 = Book("Röda rummet", "August Strindberg")
book4 = Book("Nils Holgerssons underbara resa", "Selma Lagerlöf")

# Lista som håller alla böcker.
books = [book1, book2, book3, book4]

# Funktion som ber om 2 inputs och med hjälp av Book classen skapar ett objekt som läggs till i book listan.
def add_book():
  title = input("Titel: ")

  # Kontrollerar ifall input är tomt
  while not title.strip():
    print("Titeln får inte vara tom.")
    title = input("Titel: ")

  author = input("Författare: ")

  # Kontrollerar ifall input är tomt
  while not author.strip():
    print("Författare får inte vara tom.")
    author = input("Författare: ")

  book = Book(title, author)
  books.append(book)

  print("Boken har lagts till.")

 
# Funktion som visar alla böcker i books listan (biblioteket).
def show_books():

  # Om inga böcker i listan finns körs denna.
  if len(books) == 0:
      print("Det finns inga böcker i biblioteket.")

  else:
    print("\n--- BÖCKER ---")

    for book in books:
      if book.borrowed:
        status = "Utlånad"
      else:
        status = "Tillgänglig"

      print(f"{book.title} - {book.author} ({status})")


# Funktion för att söka efter böker.
def search_book():
  search = input("Sök efter titel eller författare: ")

  found = False ## Sätter false innan loopen körs, ifall vi inte hittar nån bok.

  for book in books:
    if search.lower() in book.title.lower() or search.lower() in book.author.lower():
      if book.borrowed:
        status = "Utlånad"
      else:
        status = "Tillgänglig"

      print(f"{book.title} - {book.author} ({status})")
      found = True # Hittar vi en eller fler böcker sätt den till true

  # Om ingen bok hittas körs
  if not found:
    print("Ingen bok hittades.")


# Funktion för att låna en bok
def borrow_book():
  title = input("Vilken bok vill du låna (title)? ")

  for book in books:
    if book.title.lower() == title.lower():

      # Kontrollerar om boken redan är utlånad
      if book.borrowed:
        print("Boken är redan utlånad.")
      else:
        book.borrowed = True # Markerar boken som utlånad
        print("Du har lånat boken.")
      return

  print("Boken hittades inte.")


# Funktion för att returnera en bok
def return_book():
  title = input("Vilken bok vill du lämna tillbaka? ")

  for book in books:
    if book.title.lower() == title.lower():
      if book.borrowed:
        book.borrowed = False
        print("Boken har lämnats tillbaka.")
      else:
        print("Boken är inte utlånad.")

      return

  print("Boken hittades inte.")


# while loop som driver programmet så länge den är True.
while True:

  # Skriver ut programmets meny.
  print("""
    --- BIBLIOTEK ---
    1. Visa alla böcker
    2. Lägg till bok
    3. Sök efter bok
    4. Låna bok
    5. Lämna tillbaka bok
    6. Avsluta
    """)

  # Användaren input sparas.
  choice = input("Välj ett alternativ: ")

  # IF statements beroende på val.
  if choice == "1":
    show_books()

  elif choice == "2":
    add_book()

  elif choice == "3":
    search_book()

  elif choice == "4":
    borrow_book()

  elif choice == "5":
    return_book()

  elif choice == "6":
    print("Programmet avslutas.")
    break

  # Fångar upp ogiltigt val.
  else:
    print("Ogiltigt val. Försök igen.")

