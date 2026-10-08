import streamlit as st
from transformers import MarianMTModel, MarianTokenizer

MODEL_NAME = "NivethaT/hindi-english-idiom-translation"


@st.cache_resource
def load_model():
    tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
    model = MarianMTModel.from_pretrained(MODEL_NAME)
    return tokenizer, model


st.set_page_config(
    page_title="Hindi to English Idiom Translator",
    page_icon="🌐"
)

st.title("🌐 Hindi to English Idiom Translator")
st.write(
    "Translate Hindi idioms into English using a fine-tuned "
    "MarianMT model."
)

tokenizer, model = load_model()

hindi_text = st.text_area(
    "Enter a Hindi idiom",
    placeholder="उदाहरण: नाक कटना"
)

if st.button("Translate"):
    if hindi_text.strip():

        inputs = tokenizer(
            hindi_text,
            return_tensors="pt",
            padding=True,
            truncation=True
        )

        translated = model.generate(
            **inputs,
            max_length=128
        )

        english_text = tokenizer.decode(
            translated[0],
            skip_special_tokens=True
        )

        st.success("English Translation")
        st.write(english_text)

    else:
        st.warning("Please enter a Hindi idiom.")
