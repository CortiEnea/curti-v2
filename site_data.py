from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ProductCategory:
    slug: str
    title: str
    short: str
    highlights: list[str]
    usfa_summary: str | None = None
    usfa_bullets: list[str] | None = None


@dataclass(frozen=True)
class ProjectItem:
    title: str
    location: str
    goal: str
    solution: str
    materials: str


@dataclass(frozen=True)
class RealEstateListing:
    id: str
    listing_type: str  # "vendita" | "affitto"
    place: str
    title: str
    rooms: str
    floor: str
    price_chf: int  # monthly for rent, total for sale
    price_label: str  # e.g. "/mese" or "" (blank for sale)
    description: str
    bullets: list[str]
    images: list[str]  # URLs for carousel


USFA = {
    # Source: https://www.usfa.ch/it/prodotti
    "products_url": "https://www.usfa.ch/it/prodotti",
}


COMPANY = {
    # Source: https://fernandocurti.ch/
    "name": "Fernando Curti SA",
    "alt_name": "Falegnameria Curti SA",
    "tagline": "Falegnameria • Serramenti • Porte • Mobili su misura",
    "address": "Via Mastri Ligornettesi 32A, 6853 Ligornetto (TI) — Svizzera",
    "phone_joinery": "+41 91 647 24 35",
    "phone_real_estate": "+41 91 210 21 91",
    "email": "info@fernandocurti.ch",
    # Map coordinates for reliable embed
    "maps_lat": 45.8610357,
    "maps_lng": 8.9463414,
    "maps_link": "https://www.google.com/maps/place/Fernando+Curti+SA/@45.8610394,8.9437665,17z/data=!4m14!1m7!3m6!1s0x478429b92d4c7a8f:0xa5901147eb3842b1!2sFernando+Curti+SA!8m2!3d45.8610357!4d8.9463414!16s%2Fg%2F11h_3xksmb!3m5!1s0x478429b92d4c7a8f:0xa5901147eb3842b1!8m2!3d45.8610357!4d8.9463414!16s%2Fg%2F11h_3xksmb?entry=ttu",
}


ABOUT = {
    # Source: https://fernandocurti.ch/
    "title": "Una falegnameria di famiglia, un metodo contemporaneo.",
    "story": (
        "Nel 1974 Fernando Curti avvia la sua attività di falegname, curando ogni fase della lavorazione di porte, armadi, finestre e cucine. "
        "L’attuale officina in Via Mastri Ligornettesi viene costruita pochi anni dopo e nel 1988 nasce la Fernando Curti SA. "
        "Nel tempo l’azienda cresce rimanendo a conduzione famigliare, oggi portata avanti dalle figlie di Fernando: Paola e Valentina."
    ),
    "mission": (
        "Un unico interlocutore affidabile per un servizio completo: supporto in progettazione, produzione, posa, assistenza post‑vendita e — quando necessario — "
        "supporto per pratiche burocratiche."
    ),
    "pillars": [
        {
            "title": "Progetto e misure",
            "text": "Rilievi accurati, consulenza tecnica e scelte guidate: dal dettaglio di ferramenta alla stratigrafia.",
        },
        {
            "title": "Materiali e finiture",
            "text": "Essenza, verniciatura, trattamenti e manutenzione: estetica e durata devono convivere.",
        },
        {
            "title": "Produzione e posa",
            "text": "Organizzazione chiara: produzione in officina, posa pulita e regolazioni finali su cantiere.",
        },
        {
            "title": "Assistenza",
            "text": "Post‑vendita e interventi: un riferimento unico anche dopo la consegna.",
        },
    ],
    "people": [
        {
            "name": "Paola Curti",
            "role": "Direzione",
            "note": "Coordinamento, relazione con il cliente e gestione delle fasi progettuali.",
        },
        {
            "name": "Valentina Curti",
            "role": "Direzione",
            "note": "Gestione operativa, pianificazione e qualità del processo fino alla posa.",
        },
    ],
}


SERVICES: list[dict] = [
    # Source: https://fernandocurti.ch/ (Cosa facciamo)
    {
        "title": "Porte interne e portoncini",
        "intro": "Porte su misura con dettagli curati e posa pulita.",
        "bullets": ["Su misura", "Ferramenta e dettagli tecnici", "Posa e assistenza post‑vendita"],
    },
    {
        "title": "Serramenti e gelosie",
        "intro": "Sistemi in legno con focus su risanamento e interventi energetici.",
        "bullets": ["Risanamento energetico", "Riduzione dispersioni", "Interventi il meno invasivi possibile"],
    },
    {
        "title": "Cucine",
        "intro": "Cucine su misura progettate sullo spazio reale e sull’uso quotidiano.",
        "bullets": ["Progettazione e rilievi", "Materiali e finiture", "Produzione e posa"],
    },
    {
        "title": "Armadi e mobili su misura",
        "intro": "Armadi, contenitori e arredi su misura per privati e professionisti.",
        "bullets": ["Per nicchie e fuori squadro", "Accessori e allestimenti interni", "Durabilità e manutenzione semplice"],
    },
]


# Categories inspired by USFA product families (without inventing numeric performance values)
# Source: https://www.usfa.ch/it/prodotti
PRODUCTS: list[ProductCategory] = [
    ProductCategory(
        slug="windows",
        title="Finestre (legno)",
        short="Finestre in legno con posa curata: comfort, prestazioni e dettaglio costruttivo.",
        highlights=["Configurazione su progetto", "Vetri e guarnizioni su specifica", "Posa e sigillature curate"],
        usfa_summary="Famiglia prodotto certificabile con configurazione su specifica (materiali, vetri, ferramenta).",
        usfa_bullets=["Profili e materiali su progetto", "Vetraggi e guarnizioni su specifica", "Posa e regolazioni"],
    ),
    ProductCategory(
        slug="shutters",
        title="Gelosie / persiane",
        short="Elementi esterni in legno per protezione e identità architettonica.",
        highlights=["Geometrie su misura", "Trattamenti protettivi", "Manutenzione e ripristini"],
    ),
    ProductCategory(
        slug="entrance-doors",
        title="Portoncini d’entrata",
        short="Ingressi su misura con dettagli tecnici curati.",
        highlights=["Ferramenta e chiusure", "Soglie e battute", "Posa accurata"],
        usfa_summary="Portoncini configurabili (sicurezza, isolamento, finiture) con posa coordinata.",
        usfa_bullets=["Pannelli e strutture su specifica", "Soglie e ferramenta su progetto", "Assistenza e manutenzione"],
    ),
    ProductCategory(
        slug="interior-doors",
        title="Porte interne",
        short="Porte interne con linee pulite, chiusure precise e finiture durevoli.",
        highlights=["A battente o scorrevoli", "Finiture coordinate", "Posa e messa a punto"],
        usfa_summary="Famiglia porte interne su misura (tipologie, finiture e accessori).",
        usfa_bullets=["Tipologia e apertura su specifica", "Maniglie e finiture", "Posa e regolazioni finali"],
    ),
    ProductCategory(
        slug="wardrobes",
        title="Armadi su misura",
        short="Spazi ottimizzati e fruibilità reale: composizioni su misura per nicchie e pareti attrezzate.",
        highlights=["Interni modulari", "Accessori su richiesta", "Ante battenti o scorrevoli"],
    ),
    ProductCategory(
        slug="usfa-stock",
        title="Prodotti a stock (USFA)",
        short="Prodotti a stock e disponibilità veloce dal circuito USFA (quando possibile).",
        highlights=["Disponibilità variabile", "Soluzioni pronte", "Supporto scelta e posa"],
    ),
]


PROJECTS: list[ProjectItem] = [
    ProjectItem(
        title="Cucina su misura con isola e boiserie",
        location="Lugano",
        goal="Ottimizzare lo spazio con linee pulite e una luce calda.",
        solution="Composizione con isola centrale e dettagli integrati; boiserie coordinata e organizzazione interna pensata per gesti quotidiani.",
        materials="Rovere selezionato, finitura oliata, ferramenta soft‑close.",
    ),
    ProjectItem(
        title="Portoncino d’entrata con dettaglio tecnico",
        location="Mendrisio",
        goal="Un ingresso contemporaneo con robustezza e isolamento.",
        solution="Portoncino in legno con stratigrafie e ferramenta su specifica; posa con cura di battute e sigillature.",
        materials="Legno lamellare, finitura protettiva, ferramenta di sicurezza.",
    ),
    ProjectItem(
        title="Armadio a muro con ante complanari",
        location="Locarno",
        goal="Massima capienza senza “peso” visivo.",
        solution="Ante complanari e interni modulari; integrazione in nicchia con fuori squadro.",
        materials="Pannellature impiallacciate, laccatura opaca, accessori interni.",
    ),
]


# Real estate listings from official website (no edits to meaning)
# Source: https://fernandocurti.ch/ (Oggetti immobiliari)
REAL_ESTATE: list[RealEstateListing] = [
    # ─── IN AFFITTO ───────────────────────────────────────────────────────────────
    RealEstateListing(
        id="mendrisio-4-5",
        listing_type="affitto",
        place="Mendrisio",
        title="Affittasi 4.5 locali al 3° piano",
        rooms="4.5 locali",
        floor="3° piano",
        price_chf=1550,
        price_label="/mese",
        description=(
            "Luminoso appartamento di 4.5 locali: ingresso con ampio atrio e armadio a muro; soggiorno con accesso al balcone; cucina abitabile completa di elettrodomestici con balcone; "
            "bagno padronale con vasca e secondo bagno con box doccia. Recentemente ristrutturato."
        ),
        bullets=[
            "Pigione mensile Fr. 1'300.–",
            "Acconto spese mensile Fr. 250.–",
            "Posteggio esterno Fr. 60.–/mese (opz.)",
            "Box auto Fr. 130.–/mese (opz.)",
            "Ascensore • lavanderia in comune • zona centrale e tranquilla",
        ],
        images=[
            "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1560185893-a55cbc8c57e8?auto=format&fit=crop&w=1200&q=80",
        ],
    ),
    RealEstateListing(
        id="stabio-3-5",
        listing_type="affitto",
        place="San Pietro di Stabio",
        title="Affittasi 3.5 locali al 3° piano",
        rooms="3.5 locali",
        floor="3° e ultimo piano",
        price_chf=1300,
        price_label="/mese",
        description=(
            "Appartamento di 3.5 locali completamente ristrutturato: ingresso con armadio a muro, due camere, bagno con finestra e vasca, cucina completa di elettrodomestici con balcone e ampio soggiorno con balcone. "
            "Lavanderia in comune. Posizione ben soleggiata, scuole e fermata bus nelle immediate vicinanze. Disponibile da subito."
        ),
        bullets=["Pigione mensile Fr. 1'100.–", "Acconto spese accessorie Fr. 200.–", "Posteggio esterno Fr. 50.–"],
        images=[
            "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1560185007-cde436f6a4d0?auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1484154218962-a197022b25ba?auto=format&fit=crop&w=1200&q=80",
        ],
    ),
    # ─── IN VENDITA ───────────────────────────────────────────────────────────────
    RealEstateListing(
        id="ligornetto-5-5",
        listing_type="vendita",
        place="Ligornetto",
        title="Vendesi 5.5 locali – stabile di nuova costruzione",
        rooms="5.5 locali",
        floor="2° piano",
        price_chf=780000,
        price_label="",
        description=(
            "Appartamento di 5.5 locali di nuova costruzione con finiture di pregio. Ampio soggiorno con cucina a vista, tre camere, doppi servizi, balcone coperto. "
            "Riscaldamento a pavimento, domotica base, cantina e due posteggi inclusi."
        ),
        bullets=[
            "Superficie ca. 145 m²",
            "Cucina moderna con elettrodomestici Miele",
            "Due bagni (uno en suite)",
            "Balcone coperto 18 m²",
            "Due posteggi in autorimessa",
            "Libero subito",
        ],
        images=[
            "https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1200&q=80",
            "https://images.unsplash.com/photo-1560440021-33f9b867899d?auto=format&fit=crop&w=1200&q=80",
        ],
    ),
]


# Immagini “come prima” (Unsplash) per hero/servizi/progetti
IMAGES = {
    "hero": "https://images.unsplash.com/photo-1505798577917-a65157d3320a?auto=format&fit=crop&w=2400&q=80",
    "services": {
        "arredi": "https://images.unsplash.com/photo-1615876234886-fd9a39fda97f?auto=format&fit=crop&w=1600&q=80",
        "serramenti": "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6?auto=format&fit=crop&w=1600&q=80",
        "porte": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1600&q=80",
    },
    "projects": {
        "cucina": "https://images.unsplash.com/photo-1556912172-45b7abe8b7e1?auto=format&fit=crop&w=1600&q=80",
        "portoncino": "https://images.unsplash.com/photo-1520607162513-77705c0f0d4a?auto=format&fit=crop&w=1600&q=80",
        "armadio": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1600&q=80",
    },
}

