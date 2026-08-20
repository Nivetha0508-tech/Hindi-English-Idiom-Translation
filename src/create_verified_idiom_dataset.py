import csv
import os

# Final verified Hindi → English idiom/proverb pairs
# Only cleaned and verified candidates are included.

data = [
    {
        "id": 1,
        "hindi_idiom": "हाथ जोड़ना",
        "hindi_sentence": "किसान सरकार से मदद के लिए हाथ जोड़कर गुहार लगा रहा था।",
        "english_translation": "The farmer was pleading with the government for help.",
        "idiom_meaning": "To plead or beg humbly."
    },
    {
        "id": 2,
        "hindi_idiom": "डूबते को तिनके का सहारा",
        "hindi_sentence": "डूबते को तिनके का सहारा समझकर उसने छोटी सी मदद भी स्वीकार कर ली।",
        "english_translation": "Desperate for help, he accepted even the smallest assistance.",
        "idiom_meaning": "A desperate person will accept even the slightest help."
    },
    {
        "id": 3,
        "hindi_idiom": "दो नावों की सवारी",
        "hindi_sentence": "दो नावों की सवारी करने वालों को अंत में दोनों ही नावों से पानी में गिरना पड़ता है।",
        "english_translation": "Those who try to ride two boats at once eventually lose both.",
        "idiom_meaning": "To pursue two conflicting goals at the same time."
    },
    {
        "id": 4,
        "hindi_idiom": "मुँहतोड़ जवाब",
        "hindi_sentence": "उसने मुँहतोड़ जवाब देकर अपने आलोचकों को चुप करा दिया।",
        "english_translation": "He gave his critics a fitting reply and silenced them.",
        "idiom_meaning": "A strong or decisive reply."
    },
    {
        "id": 5,
        "hindi_idiom": "सरकार का दामाद",
        "hindi_sentence": "ऐसे सरकार के दामादों की वजह से भ्रष्टाचार बढ़ता है।",
        "english_translation": "Corruption increases because such people receive excessive government favors.",
        "idiom_meaning": "A person who receives excessive benefits or special treatment from the government."
    },
    {
        "id": 6,
        "hindi_idiom": "दूध का दूध और पानी का पानी",
        "hindi_sentence": "उसने अपनी रिपोर्ट में दूध का दूध और पानी का पानी कर दिया।",
        "english_translation": "His report clearly separated the truth from the falsehood.",
        "idiom_meaning": "To make the truth and facts completely clear."
    },
    {
        "id": 7,
        "hindi_idiom": "अपना उल्लू सीधा करना",
        "hindi_sentence": "वह हमेशा अपना उल्लू सीधा करने की कोशिश करता है।",
        "english_translation": "He always tries to serve his own interests.",
        "idiom_meaning": "To serve one's own selfish interests."
    },
    {
        "id": 8,
        "hindi_idiom": "रामबाण",
        "hindi_sentence": "इस समस्या के लिए यह उपाय रामबाण साबित हुआ।",
        "english_translation": "This solution proved to be a sure remedy for the problem.",
        "idiom_meaning": "A highly effective remedy or solution."
    },
    {
        "id": 9,
        "hindi_idiom": "बकरे की माँ कब तक ख़ैर मनायेगी",
        "hindi_sentence": "अभी खतरा टला नहीं है; बकरे की माँ कब तक ख़ैर मनायेगी।",
        "english_translation": "The danger has not passed; sooner or later the inevitable may happen.",
        "idiom_meaning": "One cannot escape an inevitable danger forever."
    },
    {
        "id": 10,
        "hindi_idiom": "नाम बड़े और दर्शन छोटे",
        "hindi_sentence": "उस दुकान का बहुत नाम था, लेकिन वहाँ पहुँचकर पता चला कि नाम बड़े और दर्शन छोटे।",
        "english_translation": "The shop was famous, but its actual quality was disappointing.",
        "idiom_meaning": "A person or thing is famous by name but unimpressive in reality."
    },
    {
        "id": 11,
        "hindi_idiom": "साँच को आँच नहीं",
        "hindi_sentence": "उसे किसी झूठे आरोप का डर नहीं था, क्योंकि साँच को आँच नहीं।",
        "english_translation": "He was not afraid of the false accusation because truth needs no protection.",
        "idiom_meaning": "A truthful person has nothing to fear."
    },
    {
        "id": 12,
        "hindi_idiom": "सीधी उंगली से घी नहीं निकलता",
        "hindi_sentence": "इस काम के लिए थोड़ी सख्ती करनी पड़ेगी; सीधी उंगली से घी नहीं निकलता।",
        "english_translation": "We will have to be a little firm; gentle methods will not work here.",
        "idiom_meaning": "Sometimes firmness or cleverness is necessary to get something done."
    },
    {
        "id": 13,
        "hindi_idiom": "पल्ले नहीं पड़ना",
        "hindi_sentence": "शिक्षक ने कई बार समझाया, लेकिन बात उसके पल्ले नहीं पड़ी।",
        "english_translation": "The teacher explained it several times, but he could not understand it.",
        "idiom_meaning": "To fail to understand something."
    },
    {
        "id": 14,
        "hindi_idiom": "आस्तीन का सांप",
        "hindi_sentence": "जिस व्यक्ति पर हमने भरोसा किया, वही आस्तीन का सांप निकला।",
        "english_translation": "The person we trusted turned out to be a hidden enemy.",
        "idiom_meaning": "A trusted person who secretly betrays or harms you."
    },
    {
        "id": 15,
        "hindi_idiom": "बाल-बाल बचना",
        "hindi_sentence": "तेज रफ्तार कार की चपेट में आने से वह बाल-बाल बच गया।",
        "english_translation": "He narrowly escaped being hit by the speeding car.",
        "idiom_meaning": "To narrowly escape danger."
    },
    {
        "id": 16,
        "hindi_idiom": "खाली दिमाग शैतान का घर",
        "hindi_sentence": "बुजुर्ग हमेशा कहते हैं कि खाली दिमाग शैतान का घर होता है।",
        "english_translation": "Elders always say that an idle mind is the devil's workshop.",
        "idiom_meaning": "Idleness can lead to undesirable thoughts or actions."
    },
    {
        "id": 17,
        "hindi_idiom": "आम के आम गुठलियों के दाम",
        "hindi_sentence": "इस योजना से पैसे भी बचेंगे और समय भी; आम के आम गुठलियों के दाम।",
        "english_translation": "This plan will save both money and time; it gives us two benefits at once.",
        "idiom_meaning": "To get two benefits from one thing."
    },
    {
        "id": 18,
        "hindi_idiom": "पाँचों उंगलियाँ बराबर नहीं होती",
        "hindi_sentence": "सभी लोगों की क्षमता एक जैसी नहीं होती; पाँचों उंगलियाँ बराबर नहीं होतीं।",
        "english_translation": "Everyone has different abilities; all five fingers are not equal.",
        "idiom_meaning": "People are different from one another."
    },
    {
        "id": 19,
        "hindi_idiom": "काम का न काज का, दुश्मन अनाज का",
        "hindi_sentence": "वह न कोई काम करता है और न दूसरों को करने देता है; काम का न काज का, दुश्मन अनाज का।",
        "english_translation": "He does no useful work and only wastes resources.",
        "idiom_meaning": "A useless person who contributes nothing but consumes resources."
    },
    {
        "id": 20,
        "hindi_idiom": "अधजल गगरी छलकत जाय",
        "hindi_sentence": "उसे विषय की थोड़ी जानकारी है, फिर भी वह बहुत दिखावा करता है; अधजल गगरी छलकत जाय।",
        "english_translation": "He knows very little about the subject but boasts a lot; empty vessels make the most noise.",
        "idiom_meaning": "A person with little knowledge often shows it off."
    },
    {
        "id": 21,
        "hindi_idiom": "आँख मारना",
        "hindi_sentence": "राहुल ने दस्तावेज़ देते हुए आँख मारी, जो एक गुप्त संकेत था।",
        "english_translation": "Rahul winked while handing over the document as a secret signal.",
        "idiom_meaning": "To wink as a signal or hint."
    },
    {
        "id": 22,
        "hindi_idiom": "ऊँट के मुँह में जीरा",
        "hindi_sentence": "इतनी बड़ी समस्या के सामने यह छोटी-सी मदद ऊँट के मुँह में जीरा है।",
        "english_translation": "This small amount of help is far too little for such a huge problem.",
        "idiom_meaning": "An amount that is far too small for the need."
    },
    {
        "id": 23,
        "hindi_idiom": "नाच न जाने आँगन टेढ़ा",
        "hindi_sentence": "अपनी गलती मानने के बजाय वह दूसरों को दोष देता है; नाच न जाने आँगन टेढ़ा।",
        "english_translation": "Instead of admitting his mistake, he blames others; a bad dancer blames the floor.",
        "idiom_meaning": "To blame circumstances for one's own shortcomings."
    },
    {
        "id": 24,
        "hindi_idiom": "मन मारना",
        "hindi_sentence": "मैंने मन मारकर मिठाई नहीं खाई क्योंकि मैं डाइट पर था।",
        "english_translation": "I reluctantly gave up the sweets because I was on a diet.",
        "idiom_meaning": "To suppress one's desire or feelings."
    },
    {
        "id": 25,
        "hindi_idiom": "दूर के ढोल सुहावने लगते हैं",
        "hindi_sentence": "दूसरे शहर की नौकरी दूर से बहुत अच्छी लगती थी, लेकिन वहाँ जाकर कठिनाइयों का पता चला; दूर के ढोल सुहावने लगते हैं।",
        "english_translation": "The job in another city looked attractive from afar, but its difficulties became clear after moving there.",
        "idiom_meaning": "Things seem more attractive when viewed from a distance."
    },
    {
        "id": 26,
        "hindi_idiom": "मगरमच्छ के आँसू",
        "hindi_sentence": "अपनी गलती के बाद उसके मगरमच्छ के आँसू देखकर किसी को विश्वास नहीं हुआ।",
        "english_translation": "No one believed his crocodile tears after his mistake.",
        "idiom_meaning": "Insincere tears or false sympathy."
    },
    {
        "id": 27,
        "hindi_idiom": "मरता क्या न करता",
        "hindi_sentence": "मरता क्या न करता, उसने मजबूरी में वह कठिन काम स्वीकार कर लिया।",
        "english_translation": "He accepted the difficult task out of desperation because he had no other choice.",
        "idiom_meaning": "A desperate person will do whatever is necessary."
    },
    {
        "id": 28,
        "hindi_idiom": "कुएँ का मेंढक",
        "hindi_sentence": "जो व्यक्ति अपने छोटे से संसार से बाहर की दुनिया को नहीं जानता, वह कुएँ का मेंढक कहलाता है।",
        "english_translation": "A person who knows nothing beyond his small world is like a frog in a well.",
        "idiom_meaning": "A person with a very limited outlook or experience."
    },
    {
        "id": 29,
        "hindi_idiom": "मियाँ बीवी राज़ी तो क्या करेगा काज़ी",
        "hindi_sentence": "जब दोनों परिवारों की सहमति थी, तो किसी तीसरे व्यक्ति की जरूरत नहीं थी; मियाँ बीवी राज़ी तो क्या करेगा काज़ी।",
        "english_translation": "When the two people involved agree, outside interference is unnecessary.",
        "idiom_meaning": "When the concerned parties agree, outsiders cannot interfere."
    },
    {
        "id": 30,
        "hindi_idiom": "सर खाना",
        "hindi_sentence": "बार-बार एक ही बात पूछकर मेरा सर मत खाओ।",
        "english_translation": "Don't pester me by asking the same thing repeatedly.",
        "idiom_meaning": "To annoy or pester someone repeatedly."
    },
    {
        "id": 31,
        "hindi_idiom": "कमर तोड़ना",
        "hindi_sentence": "महँगाई ने आम लोगों की कमर तोड़ दी है।",
        "english_translation": "Inflation has severely burdened ordinary people.",
        "idiom_meaning": "To severely weaken or burden someone."
    },
    {
        "id": 32,
        "hindi_idiom": "मुल्ला की दौड़ मस्जिद तक",
        "hindi_sentence": "वह हर समस्या का समाधान अपनी पार्टी तक ही सीमित रखता है; मुल्ला की दौड़ मस्जिद तक।",
        "english_translation": "His thinking never goes beyond his own party; his outlook is very limited.",
        "idiom_meaning": "A person's efforts or thinking remain confined to a narrow limit."
    },
    {
        "id": 33,
        "hindi_idiom": "बूढ़ी घोड़ी लाल लगाम",
        "hindi_sentence": "बूढ़ी उम्र में वह बहुत भड़कीले कपड़े पहनकर घूमती है; बूढ़ी घोड़ी लाल लगाम।",
        "english_translation": "At an old age, she dresses in overly flashy clothes; an old mare with a red bridle.",
        "idiom_meaning": "An elderly person trying too hard to appear youthful or fashionable."
    },
    {
        "id": 34,
        "hindi_idiom": "उल्टा चोर कोतवाल को डांटे",
        "hindi_sentence": "अपनी गलती के लिए माफी माँगने के बजाय वह शिकायत करने वाले को ही डाँटने लगा; उल्टा चोर कोतवाल को डांटे।",
        "english_translation": "Instead of apologizing for his mistake, he scolded the person who complained; the guilty person is blaming the accuser.",
        "idiom_meaning": "A guilty person blaming or accusing the innocent."
    },
    {
        "id": 35,
        "hindi_idiom": "सीना चौड़ा होना",
        "hindi_sentence": "बेटी की सफलता पर पिता का सीना चौड़ा हो गया।",
        "english_translation": "The father felt extremely proud of his daughter's success.",
        "idiom_meaning": "To feel very proud."
    },
    {
        "id": 36,
        "hindi_idiom": "बोया पेड़ बबूल का तो आम कहाँ से होए",
        "hindi_sentence": "उसने गलत रास्ता चुना था, इसलिए उसे बुरा परिणाम मिला; बोया पेड़ बबूल का तो आम कहाँ से होए।",
        "english_translation": "He chose the wrong path and therefore got a bad result; you cannot expect mangoes from a babul tree.",
        "idiom_meaning": "You cannot expect good results from bad actions."
    },
    {
        "id": 37,
        "hindi_idiom": "चुल्लू भर पानी में डूब मरना",
        "hindi_sentence": "इतनी बड़ी गलती करने के बाद उसे चुल्लू भर पानी में डूब मरना चाहिए।",
        "english_translation": "After making such a shameful mistake, he should be extremely ashamed of himself.",
        "idiom_meaning": "To feel extremely ashamed."
    },
    {
        "id": 38,
        "hindi_idiom": "मीन-मेख निकालना",
        "hindi_sentence": "हर काम में मीन-मेख निकालने के बजाय समाधान पर ध्यान दो।",
        "english_translation": "Instead of finding fault with everything, focus on the solution.",
        "idiom_meaning": "To find unnecessary faults or flaws."
    },
    {
        "id": 39,
        "hindi_idiom": "सूप बोले तो बोले छलनी भी बोले जिसमें बहत्तर छेद",
        "hindi_sentence": "खुद बहुत गलतियाँ करने वाला व्यक्ति दूसरों की गलतियाँ गिनाने लगा; सूप बोले तो बोले छलनी भी बोले जिसमें बहत्तर छेद।",
        "english_translation": "Someone full of faults began criticizing others; the pot calling the kettle black.",
        "idiom_meaning": "A flawed person criticizing someone else for similar faults."
    },
    {
        "id": 40,
        "hindi_idiom": "जले पर नमक छिड़कना",
        "hindi_sentence": "मेरे नुकसान पर हँसकर उसने जले पर नमक छिड़क दिया।",
        "english_translation": "By laughing at my loss, he added insult to injury.",
        "idiom_meaning": "To make an already painful situation worse."
    },
    {
        "id": 41,
        "hindi_idiom": "घोड़ा घास से यारी करे तो खाए क्या?",
        "hindi_sentence": "अगर दुकानदार अपने सामान को मुफ्त में बाँटता रहेगा, तो घोड़ा घास से यारी करे तो खाए क्या?",
        "english_translation": "If a shopkeeper keeps giving away his goods for free, how will he make a living?",
        "idiom_meaning": "One cannot sacrifice one's own livelihood for others."
    },
    {
        "id": 42,
        "hindi_idiom": "खोदा पहाड़ निकली चुहिया",
        "hindi_sentence": "टीम ने एक महीने मेहनत की, लेकिन परिणाम बहुत छोटा निकला; खोदा पहाड़ निकली चुहिया।",
        "english_translation": "The team worked for a month, but the result was tiny; much effort produced very little.",
        "idiom_meaning": "A great deal of effort producing a very small result."
    },
    {
        "id": 43,
        "hindi_idiom": "थाली का बैगन होना",
        "hindi_sentence": "वह थाली का बैगन है, जो भी उसे दबाव में डालता है, वह उसी का साथ देने लगता है।",
        "english_translation": "He is easily influenced and sides with whoever puts pressure on him.",
        "idiom_meaning": "A person who frequently changes sides according to circumstances."
    },
    {
        "id": 44,
        "hindi_idiom": "मुँह में राम बगल में छुरी",
        "hindi_sentence": "उसकी मीठी बातों पर भरोसा मत करना; मुँह में राम बगल में छुरी वाले लोगों से सावधान रहना चाहिए।",
        "english_translation": "Do not trust his sweet words; beware of people who pretend to be good while secretly intending harm.",
        "idiom_meaning": "A person who appears virtuous but secretly intends harm."
    },
    {
        "id": 45,
        "hindi_idiom": "सोलह आने सच",
        "hindi_sentence": "उसकी बात सोलह आने सच निकली।",
        "english_translation": "What he said turned out to be completely true.",
        "idiom_meaning": "Completely true."
    },
    {
        "id": 46,
        "hindi_idiom": "मक्खन लगाना",
        "hindi_sentence": "वह बॉस को मक्खन लगाकर अपनी पसंद की छुट्टी लेना चाहता है।",
        "english_translation": "He wants to flatter the boss to get the leave he wants.",
        "idiom_meaning": "To flatter someone for personal gain."
    },
    {
        "id": 47,
        "hindi_idiom": "घड़ियाल के आँसू",
        "hindi_sentence": "अपनी गलती के बाद उसके घड़ियाल के आँसू देखकर किसी को उस पर विश्वास नहीं हुआ।",
        "english_translation": "No one believed his crocodile tears after his mistake.",
        "idiom_meaning": "False or insincere expressions of sorrow."
    },
    {
        "id": 48,
        "hindi_idiom": "चेहरा उतरना",
        "hindi_sentence": "परीक्षा का परिणाम सुनते ही उसका चेहरा उतर गया।",
        "english_translation": "His face fell as soon as he heard the exam result.",
        "idiom_meaning": "To become disappointed or worried."
    },
    {
        "id": 49,
        "hindi_idiom": "चार दिन की चाँदनी फिर अँधेरी रात",
        "hindi_sentence": "उसकी नई नौकरी की खुशी कुछ ही दिनों में खत्म हो गई; चार दिन की चाँदनी फिर अँधेरी रात।",
        "english_translation": "The happiness of his new job ended within a few days; temporary happiness does not last.",
        "idiom_meaning": "A short-lived period of happiness or success."
    },
    {
        "id": 50,
        "hindi_idiom": "लातों के भूत बातों से नहीं मानते",
        "hindi_sentence": "उसे समझाने की बहुत कोशिश की, लेकिन वह नहीं माना; लातों के भूत बातों से नहीं मानते।",
        "english_translation": "We tried hard to reason with him, but he would not listen; some people respond only to strict action.",
        "idiom_meaning": "Some stubborn people do not respond to words and require strict action."
    },
    {
        "id": 51,
        "hindi_idiom": "नाक कटना",
        "hindi_sentence": "बेटे की करतूत से पूरे परिवार की नाक कट गई।",
        "english_translation": "The son's actions brought shame to the entire family.",
        "idiom_meaning": "To suffer shame or disgrace."
    },
    {
        "id": 52,
        "hindi_idiom": "मक्खीचूस",
        "hindi_sentence": "वह इतना मक्खीचूस है कि जरूरत पड़ने पर भी पैसे खर्च नहीं करता।",
        "english_translation": "He is so miserly that he does not spend money even when necessary.",
        "idiom_meaning": "An extremely miserly person."
    },
    {
        "id": 53,
        "hindi_idiom": "दूध का जला छाछ भी फूँक फूँक कर पीता है",
        "hindi_sentence": "पहले धोखा खाने के बाद अब वह हर नए व्यक्ति पर बहुत सावधानी से भरोसा करता है; दूध का जला छाछ भी फूँक फूँक कर पीता है।",
        "english_translation": "After being deceived once, he is now very cautious about trusting new people.",
        "idiom_meaning": "A person who has suffered once becomes very cautious afterward."
    },
    {
        "id": 54,
        "hindi_idiom": "बात बनना",
        "hindi_sentence": "काफी बातचीत के बाद आखिरकार प्रस्ताव पर सहमति हो गई और बात बन गई।",
        "english_translation": "After much discussion, the proposal was finally accepted and the matter worked out.",
        "idiom_meaning": "For a matter to work out successfully."
    },
    {
        "id": 55,
        "hindi_idiom": "कंगाली में आटा गीला",
        "hindi_sentence": "नौकरी जाने के बाद घर का खर्च भी बढ़ गया; कंगाली में आटा गीला हो गया।",
        "english_translation": "After losing his job, his household expenses also increased, making a bad situation worse.",
        "idiom_meaning": "An additional problem making an already bad situation worse."
    },
    {
        "id": 56,
        "hindi_idiom": "उड़ती चिड़िया के पर पहचानना",
        "hindi_sentence": "वह इतना अनुभवी है कि उड़ती चिड़िया के पर पहचान लेता है और किसी की चालाकी से आसानी से धोखा नहीं खाता।",
        "english_translation": "He is so perceptive and experienced that he quickly recognizes people's tricks.",
        "idiom_meaning": "To be extremely perceptive and quick to understand things."
    },
    {
        "id": 57,
        "hindi_idiom": "अपनी गली में कुत्ता भी शेर होता है",
        "hindi_sentence": "वह अपने इलाके में बहुत दबंग है; अपनी गली में कुत्ता भी शेर होता है।",
        "english_translation": "He is very powerful in his own neighborhood; even a dog is a lion in its own street.",
        "idiom_meaning": "A person feels powerful in their own territory."
    },
    {
        "id": 58,
        "hindi_idiom": "नया नौ दिन, पुराना सौ दिन",
        "hindi_sentence": "नई चीज़ का आकर्षण कुछ ही दिनों में कम हो जाता है; नया नौ दिन, पुराना सौ दिन।",
        "english_translation": "The attraction of something new soon fades; old things often become more valued.",
        "idiom_meaning": "New things are attractive briefly, while familiar old things often become more valued."
    },
    {
        "id": 59,
        "hindi_idiom": "दाल में कुछ काला होना",
        "hindi_sentence": "पुलिस को शक था कि मामले में दाल में कुछ काला है, इसलिए उन्होंने जाँच शुरू की।",
        "english_translation": "The police suspected that something was suspicious in the matter, so they started an investigation.",
        "idiom_meaning": "To suspect that something is wrong or suspicious."
    },
    {
        "id": 60,
        "hindi_idiom": "न रहेगा बाँस न बजेगी बाँसुरी",
        "hindi_sentence": "समस्या की जड़ को ही खत्म कर दिया गया, इसलिए न रहेगा बाँस न बजेगी बाँसुरी।",
        "english_translation": "The root cause of the problem was removed, so the problem itself will disappear.",
        "idiom_meaning": "Remove the source of a problem and the problem disappears."
    },
    {
        "id": 61,
        "hindi_idiom": "घोड़े बेचकर सोना",
        "hindi_sentence": "परीक्षा की सारी तैयारी पूरी करने के बाद वह रात को घोड़े बेचकर सोया।",
        "english_translation": "After finishing all his exam preparation, he slept very soundly.",
        "idiom_meaning": "To sleep very soundly and carefree."
    },
    {
        "id": 62,
        "hindi_idiom": "सिट्टीपिट्टी गुम होना",
        "hindi_sentence": "अचानक तेज आवाज सुनकर उसकी सिट्टीपिट्टी गुम हो गई।",
        "english_translation": "The sudden loud noise left him completely frightened and confused.",
        "idiom_meaning": "To become extremely frightened or confused."
    },
    {
        "id": 63,
        "hindi_idiom": "हाँ में हाँ मिलाना",
        "hindi_sentence": "अजय हमेशा बॉस की हर बात में हाँ में हाँ मिलाता रहता है ताकि उसे पसंद किया जाए।",
        "english_translation": "Ajay always agrees with everything his boss says in order to be liked.",
        "idiom_meaning": "To agree with someone excessively, often to gain favor."
    }
]

# Save inside the data folder
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, "verified_hindi_english_idioms.csv")

with open(output_file, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=[
            "id",
            "hindi_idiom",
            "hindi_sentence",
            "english_translation",
            "idiom_meaning"
        ]
    )

    writer.writeheader()
    writer.writerows(data)

print("Verified idiom dataset created successfully!")
print(f"Total verified rows: {len(data)}")
print(f"Saved to: {output_file}")