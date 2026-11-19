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
    "products_url": "https://www.usfa.ch/it/prodotti",
    "intro": (
        "Per rimanere al passo con i tempi, l’azienda ha cercato fornitori in grado di soddisfare "
        "le molteplici richieste di una clientela sempre più esigente. Una ricerca che ha portato "
        "alla collaborazione con la cooperativa USFA di Cadenazzo: un unico partner per la "
        "commercializzazione di una variegata gamma di prodotti di qualità, con cui lavoriamo dal 1992."
    ),
    "renovation": (
        "Tra le sfide di oggi, a farla da padrone è il risanamento degli edifici. Il panorama "
        "immobiliare svizzero è composto da molti edifici con un’importante vetustà tecnica e una "
        "scarsa qualità energetica. Per questo la Fernando Curti SA cerca soluzioni che rendano "
        "l’intervento di sostituzione di serramenti e porte il meno invasivo possibile, riducendo "
        "il dispendio energetico e migliorando qualità di vita ed economicità per il committente."
    ),
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
    "title": "Passione e professionalità: la storia della Fernando Curti SA.",
    "story": (
        "Sono ormai trascorsi 44 anni da quel lontano 1974, quando Fernando Curti iniziò la sua attività di falegname. Nella bottega ricavata al pianterreno della casa del papà Aldo curava ogni fase della lavorazione di porte, armadi, finestre e cucine. L’attuale officina in via Mastri Ligornettesi venne costruita solo qualche anno dopo e nel 1988 nacque la Fernando Curti SA. Una società che nel tempo è cresciuta, rimanendo però sempre a conduzione famigliare. Una conduzione la cui continuità è assicurata oggi dalle figlie di Fernando: Paola e Valentina."
        "Gli oltre trent’anni di esperienza nel settore hanno portato la Fernando Curti SA a essere un punto di riferimento per gli studi d’architettura e le imprese di costruzione, che sanno di poter contare su un unico interlocutore affidabile per un servizio completo, che li supporta dalla fase di progettazione alla messa in opera dei manufatti, fino al dopo vendita e alle pratiche burocratiche, come ad esempio l’eventuale richiesta di sussidi."
        "Per garantire l’alta qualità della consulenza tecnica, dei lavori di posa e dell’assistenza post vendita la Fernando Curti SA può contare su personale serio e qualificato, in grado di soddisfare al meglio il desiderio di ogni cliente, senza dover fare capo a collaboratori esterni. Questo permette di offrire un servizio puntuale e su misura molto apprezzato dalla clientela, la cui soddisfazione è da decenni il miglior biglietto da visita, che si tratti di grandi forniture per complessi residenziali o di una singola anta del piccolo cliente."
    ),
    "mission": (
        "Per rimanere al passo con i tempi, l’azienda ha cercato dei fornitori che potessero permettergli di soddisfare le molteplici richieste di una clientela sempre più esigente. Una ricerca che ha portato alla collaborazione con la cooperativa USFA di Cadenazzo: un unico partner per la commercializzazione di una variegata gamma di prodotti di qualità, con cui lavora dal 1992."
        "Molti prodotti diversi per far fronte alle molte sfide del mercato. Tra queste a farla da padrone oggi è il risanamento degli edifici. Il panorama immobiliare svizzero è composto da molti edifici caratterizzati da un’importante vetustà tecnica e una scarsa qualità energetica, per questi motivi la Fernando Curti SA è alla continua ricerca di soluzioni per rendere meno invasivo possibile l’intervento di sostituzione di serramenti e porte nelle abitazioni e per permettere la massima riduzione del dispendio energetico, con un conseguente maggior beneficio in termini di qualità di vita ed economicità per il committente." 
        "Oltre alla tradizionale sostituzione dei serramenti in legno con elementi di nuova generazione, senza drastici interventi edili è oggi possibile trasformare radicalmente lo stato di fatto, ad esempio sostituendo una poco isolante finestra con tapparella avvolgibile e cassonetto con una di nuova concezione, dotata di pannello superiore coibentato che migliora decisamente il grado di isolamento termico. Inoltre inserendo una più moderna lamella a pacco con guide incassate ne guadagnano pure sia l’estetica della costruzione sia la sua sicurezza."

    ),
    "quality": (
        "Un punto quest’ultimo che è un’altra delle sfide recenti che vale la pena citare: la ricerca di soluzioni anti effrazione per una clientela che richiede sistemi di sicurezza sempre più evoluti. Sicurezza per quanto riguarda le intrusioni, ma pure per quanto attiene alle misure anti incendio, a questo proposito la collaborazione con professionisti del settore ci permette di garantire una consulenza corretta al cliente nella scelta di porte omologate sia in legno, sia in metallo. "
        "Molte sfide diverse, che la Fernando Curti SA affronta ogni giorno forte dell’esperienza e la competenza maturate in oltre trent’anni di attività, con la stessa passione che animava la bottega sotto casa del nonno Aldo."
    ),
    "pillars": [
        {
            "title": "Posa in opera",
            "text": (
                "La messa in opera di tutti i prodotti trattati è effettuata da collaboratori interni: "
                "non affidiamo mai il montaggio in maniera esclusiva a squadre esterne."
            ),
        },
        {
            "title": "Conoscenza del prodotto",
            "text": (
                "Installatori che conoscono a fondo ciò che posano, senza le sorprese tipiche del subappalto: "
                "smaltimenti, pulizie e trasporto a piè d’opera restano sotto il nostro controllo."
            ),
        },
        {
            "title": "Supporto tecnico",
            "text": (
                "Oltre a consigliare il cliente in fase di scelta, forniamo i particolari costruttivi per i "
                "progetti esecutivi e collaboriamo alla realizzazione dei dettagli specifici."
            ),
        },
        {
            "title": "Post vendita",
            "text": (
                "Un servizio post vendita puntuale e preciso, con la stessa attenzione che riserviamo "
                "alla posa in cantiere."
            ),
        },
    ],
    "people": [
        {
            "name": "Paola Curti",
            "role": "Direzione",
        },
        {
            "name": "Valentina Curti",
            "role": "Direzione",
        },
    ],
}


SERVICES: list[dict] = [
    {
        "title": "Gelosie",
        "intro": (
            "Che siano intese come protezioni solari o come primo elemento per la sicurezza dell’abitazione, "
            "disponiamo di un’ampia gamma di gelosie, dalle tradizionali in legno alle più moderne in alluminio."
        ),
        "bullets": [
            "Lamelle fisse, orientabili o a doppia spiovenza",
            "Scuretti dogati o bungati",
            "Adattabili ai cardini esistenti, senza ponteggi",
        ],
    },
    {
        "title": "Portoncini d’ingresso",
        "intro": (
            "Concepito come porta di sicurezza ma non solo, il portoncino d’ingresso deve caratterizzare "
            "un’abitazione, sia esso in legno o in alluminio."
        ),
        "bullets": [
            "Personalizzazione estetica su catalogo",
            "Sicurezza statica e anti-effrazione",
            "Coibentazione senza compromessi",
        ],
    },
    {
        "title": "Porte interne",
        "intro": (
            "Proponiamo una vasta gamma di porte interne: dalle pratiche e robuste porte in laminato "
            "alle classiche porte impiallacciate in essenza o laccate."
        ),
        "bullets": [
            "Semipesanti con anima in truciolare",
            "Stipiti in legno o in metallo",
            "Porte tecniche EI30 VKF e sicurezza EN 1627",
        ],
    },
]


PRODUCTS: list[ProductCategory] = [
    ProductCategory(
        slug="shutters",
        title="Gelosie",
        short=(
            "Che siano intese come protezioni solari o come primo elemento per la sicurezza dell’abitazione, "
            "disponiamo di un’ampia gamma di gelosie, dalle tradizionali in legno alle più moderne in alluminio."
        ),
        highlights=[
            "Lamelle fisse, orientabili, a doppia spiovenza",
            "Scuretti dogati o bungati",
            "Meccanismi di chiusura e adattamento ai cardini esistenti, senza ponteggi",
        ],
    ),
    ProductCategory(
        slug="entrance-doors",
        title="Portoncini d’ingresso",
        short=(
            "Concepito come porta di sicurezza ma non solo, il portoncino d’ingresso deve caratterizzare "
            "un’abitazione, sia esso in legno o in alluminio."
        ),
        highlights=[
            "Personalizzazione estetica dei modelli a catalogo",
            "Criteri di sicurezza statica e contro l’effrazione",
            "Proprietà di coibentazione mantenute",
        ],
        usfa_summary="Collaborazione con produttori flessibili per configurare il portoncino nel rispetto di sicurezza e isolamento.",
        usfa_bullets=["Legno o alluminio", "Configurazione su catalogo", "Posa e post vendita interni"],
    ),
    ProductCategory(
        slug="interior-doors",
        title="Porte interne",
        short=(
            "Proponiamo una vasta gamma di porte interne: dalle pratiche e robuste porte in laminato "
            "alle classiche porte impiallacciate in essenza o laccate."
        ),
        highlights=[
            "Semipesanti con anima interna in truciolare",
            "Stipiti in legno o in metallo, finiture e accessori a scelta",
            "Porte tecniche anticendio EI30 VKF e di sicurezza (EN 1627)",
        ],
        usfa_summary="A disposizione in pronta consegna anche porte laccate bianco dal circuito USFA.",
        usfa_bullets=["Laminato, essenza, laccato", "Porte tecniche certificate", "Pronta consegna laccato bianco"],
    ),
    ProductCategory(
        slug="windows",
        title="Serramenti e risanamento",
        short=(
            "Oltre alla tradizionale sostituzione dei serramenti in legno con elementi di nuova generazione, "
            "è possibile trasformare lo stato di fatto senza drastici interventi edili, migliorando isolamento, "
            "estetica e sicurezza."
        ),
        highlights=[
            "Interventi il meno invasivi possibile",
            "Pannello superiore coibentato al posto del cassonetto poco isolante",
            "Lamella a pacco con guide incassate: estetica e sicurezza",
        ],
        usfa_summary="Soluzioni USFA per il risanamento energetico di edifici esistenti.",
        usfa_bullets=["Sostituzione serramenti", "Riduzione dispersioni", "Sistemi anti-effrazione"],
    ),
    ProductCategory(
        slug="installation",
        title="Posa in opera",
        short=(
            "Quello che ci differenzia è che la messa in opera di tutti i prodotti trattati è effettuata "
            "da collaboratori interni: non affidiamo mai il montaggio in maniera esclusiva a squadre esterne."
        ),
        highlights=[
            "Piena conoscenza dei prodotti da parte degli installatori",
            "Niente sorprese da subappalto (smaltimenti, pulizie, trasporto a piè d’opera)",
            "Sistemi di fissaggio in linea con la normativa termica, fonica e di tenuta",
        ],
    ),
    ProductCategory(
        slug="technical-support",
        title="Supporto tecnico",
        short=(
            "Oltre a seguire e consigliare il cliente in fase di scelta, offriamo un supporto tecnico completo "
            "sia ai progettisti che al cliente privato."
        ),
        highlights=[
            "Particolari costruttivi per i progetti esecutivi",
            "Collaborazione sui dettagli specifici",
            "Consulenza su porte omologate in legno e in metallo, anche anti-incendio",
        ],
    ),
]


PROJECTS: list[ProjectItem] = [
    ProjectItem(
        title="Finestra su misura a Ligornetto",
        location="Ligornetto",
        goal="Integrare una finestra particolare nello spessore del muro, con davanzale in legno e un sopraluce di geometria irregolare.",
        solution=(
            "Serramento in legno con inferriata, nicchia e davanzale a tutta profondità; "
            "sopraluce trapezoidale verso il tetto per portare luce nella zona giorno senza appesantire la parete."
        ),
        materials="Legno, vetro, ferramenta e inferriata su misura.",
    ),
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


IMAGES = {
    "logo": "images/logo-lockup.png",
    "workshop": "images/hero-custom.png",
    "ligornetto": "images/ligornetto-finestra.jpg",
    "hero": [
        "images/ligornetto-finestra.jpg",
        "images/hero-custom.png",
        "images/logo-lockup.png",
    ],
    "projects": {
        "ligornetto": "images/ligornetto-finestra.jpg",
        "cucina": "images/hero-custom.png",
        "portoncino": "images/logo-lockup.png",
        "armadio": "images/hero-custom.png",
    },
}

