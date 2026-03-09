movies = {
    "action": ["Avengers", "Batman", "Spider-Man"],
    "comedy": ["Mr Bean", "The Mask", "Home Alone"],
    "romance": ["Titanic", "The Notebook", "La La Land"]
}

print("Movie Recommendation System")

choice = input("Enter genre (action/comedy/romance): ").lower()

if choice in movies:
    print("Recommended Movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Genre not available")