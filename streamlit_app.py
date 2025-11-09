import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="🎬 Location de Films", page_icon="🎬")
st.title("🎬 Application de location de films")

def get_movies():
    r = requests.get(f"{API_URL}/movies")
    return r.json()

def get_movie(mid):
    r = requests.get(f"{API_URL}/movies/{mid}")
    return r.json()

def rent_movie(mid, renter_name):
    r = requests.put(f"{API_URL}/movies/{mid}/rent", json={"renter_name": renter_name})
    return r.json()

def return_movie(mid):
    r = requests.put(f"{API_URL}/movies/{mid}/return")
    return r.json()

def create_movie(data):
    r = requests.post(f"{API_URL}/movies", json=data)
    return r.json()

def delete_movie(mid):
    requests.delete(f"{API_URL}/movies/{mid}")


def trigger_refresh():
    rerun_fn = getattr(st, 'experimental_rerun', None) or getattr(st, 'rerun', None)
    if rerun_fn:
        rerun_fn()
    else:
        st.warning('Veuillez rafraichir la page pour voir les dernieres donnees.')


tab1, tab2, tab3 = st.tabs(["📜 Films", "🎥 Détails / Location", "🛠 Gestion"])

with tab1:
    st.subheader("Liste des films")
    if st.button("Rafraichir la liste"):
        trigger_refresh()
    movies = get_movies()
    for m in movies:
        st.write(f"**{m['title']}** ({m['year']}) — {m['genre']}")
        st.caption(f"ID: {m['id']} | {'✅ Disponible' if m['is_available'] else '❌ Loué'}")

with tab2:
    st.subheader("Details / Louer / Rendre")
    movies_for_select = get_movies()
    if not movies_for_select:
        st.info("Aucun film disponible pour le moment.")
    else:
        options = {
            f"{m['title']} ({m['year']}) - ID {m['id']}": m for m in movies_for_select
        }
        labels = list(options.keys())
        selection = st.selectbox("Choisissez un film", labels)
        movie_choice = options[selection]
        movie_id = movie_choice["id"]
        movie = get_movie(movie_id)
        st.write(f"### {movie['title']} ({movie['year']})")
        st.write(movie["description"])
        st.write(f"Realisateur : {movie['director']} | Note : {movie['rating']}")
        if movie["is_available"]:
            name = st.text_input("Nom du locataire", key=f"rent_name_{movie_id}")
            if st.button("Louer", key=f"rent_btn_{movie_id}"):
                rent_movie(movie_id, name)
                st.success("Film loue.")
                trigger_refresh()
        else:
            st.caption(f"Loue par : {movie.get('renter_name') or 'Inconnu'}")
            if st.button("Rendre", key=f"return_btn_{movie_id}"):
                return_movie(movie_id)
                st.success("Film rendu.")
                trigger_refresh()

with tab3:
    st.subheader("Ajouter ou supprimer un film")
    with st.form("ajout"):
        title = st.text_input("Titre")
        genre = st.text_input("Genre")
        year = st.number_input("Année", min_value=1888, max_value=3000, value=2000)
        description = st.text_area("Description")
        duration = st.number_input("Durée (min)", min_value=1, value=120)
        director = st.text_input("Réalisateur")
        rating = st.slider("Note", 0.0, 10.0, 8.0, 0.1)
        submitted = st.form_submit_button("Ajouter")
        if submitted:
            data = dict(title=title, genre=genre, year=int(year), description=description,
                        duration_min=int(duration), director=director, rating=float(rating))
            create_movie(data)
            trigger_refresh()
            st.success("Film ajouté ✅")

    del_id = st.number_input("ID à supprimer", min_value=1, step=1)
    if st.button("🗑 Supprimer"):
        delete_movie(del_id)
        st.warning("Film supprime.")
        trigger_refresh()
