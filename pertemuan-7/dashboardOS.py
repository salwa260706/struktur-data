from gtts import gtts 
impport streamlit as st
st.title(" Sistem Antrian Pasien di Rs Suka Sehat")
def generate_tts(text, filename="antrian.mp3"):
    tts = gtts(text, lang"id", slow.)
    tts.save(filename)
    return filename

if "queue" not in st.session_state:
    st.session_state.queue= []
if "current" not in st.session.state:
    st.session_state.current = 0
with st.form(form):
    nomor = st.text_input("masukan nomor antrian")
    submit = st.form_submit_button("tambah")
    if submit and nomor:
        st.session_state.Queue.append(nomor)
        st.success(f"nomor antrian [nomor] sudah ditambahkan")
st.subheader("daftar antrian")