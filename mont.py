## streamlit version
import streamlit as st
import base64
from datetime import date

st.set_page_config(page_title="Montelliscious", layout="wide")

# ---------------- SESSION ----------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "selected_room" not in st.session_state:
    st.session_state.selected_room = None


def navigate(page):
    st.session_state.page = page


def select_room(room):
    st.session_state.selected_room = room
    st.session_state.page = "Room_Detail"


def reset_room():
    st.session_state.selected_room = None
    st.session_state.page = "Rooms"


# ---------------- ROOM DATA ----------------
rooms = {
    "Deluxe Room": {
        "price": 1500,
        "images": [
            "https://images.pexels.com/photos/164595/hotel-room-bed-bedroom-164595.jpeg",
            "https://images.pexels.com/photos/271624/pexels-photo-271624.jpeg",
            "https://images.pexels.com/photos/262048/pexels-photo-262048.jpeg"
        ]
    },
    "Premium Room": {
        "price": 1700,
        "images": [
            "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg",
            "https://images.pexels.com/photos/189296/pexels-photo-189296.jpeg",
            "https://images.pexels.com/photos/276724/pexels-photo-276724.jpeg"
        ]
    },
    "Standard Room": {
        "price": 1400,
        "images": [
            "https://images.pexels.com/photos/271618/pexels-photo-271618.jpeg",
            "https://images.pexels.com/photos/279746/pexels-photo-279746.jpeg",
            "https://images.pexels.com/photos/210604/pexels-photo-210604.jpeg"
        ]
    },
    "Family Room": {
        "price": 1600,
        "images": [
            "https://images.pexels.com/photos/261102/pexels-photo-261102.jpeg",
            "https://images.pexels.com/photos/237371/pexels-photo-237371.jpeg",
            "https://images.pexels.com/photos/1648776/pexels-photo-1648776.jpeg"
        ]
    }
}

# -------------------- CSS --------------------
st.markdown("""
<style>
/* ---------------- DARK THEME BACKGROUND ---------------- */
.stApp {
    background-color: #1f2937;   /* dark slate background */
}
h1 {
    color: #ffffff !important;
}
h2 {
    color: #ffffff !important;
}
div[data-testid="stMetricLabel"] {
    color: #ffffff !important;
}

div[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

div[data-testid="stMetricDelta"] {
    color: #ffffff !important;
}

/* ---------------- RADIO BUTTON TEXT ---------------- */
div[data-testid="stRadio"] label {
    color: #ffffff !important;
}

/* ---------------- SLIDER TEXT ---------------- */
div[data-testid="stSlider"] label {
    color: #ffffff !important;
}

/* ---------------- SELECTBOX TEXT ---------------- */
div[data-testid="stSelectbox"] label {
    color: #ffffff !important;
}

/* ---------------- INPUT LABELS ---------------- */
div[data-testid="stTextInput"] label {
    color: #ffffff !important;
}

/* ---------------- DATE INPUT LABELS ---------------- */
div[data-testid="stDateInput"] label {
    color: #ffffff !important;
}

/* ---------------- NUMBER INPUT LABELS ---------------- */
div[data-testid="stNumberInput"] label {
    color: #ffffff !important;
}
div[data-testid="stRadio"] div[role="radiogroup"] label {
    color: #ffffff !important;
}
div[data-testid="stMetric"] * {
    color: #ffffff !important;
}
div[data-testid="stSelectbox"] * {
    color: #ffffff !important;
}
.stMarkdown, .stMarkdown p, .stMarkdown li {
    color: #ffffff !important;
}
h3 {
    color: #ffffff !important;
}

/* HOME CARD ONLY: BLACK TEXT */
.card h3 {
    color: #000000 !important;
}

.card p {
    color: #000000 !important;
}
.main-title {
    font-size: 48px;
    font-weight: bold;
    color: white;
}
.sub-title {
    font-size: 20px;
    color: #f9fafb;
}
.section {
    padding: 40px 20px;
}
.card {
    padding: 25px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.1);
    text-align: center;
}
.highlight {
    font-size: 18px;
    font-weight: bold;
    color: #f9fafb;
}
.footer {
    text-align: center;
    padding: 20px;
    color: gray;
}
.stButton>button {
    background-color: #e67e22;
    color: white;
    border-radius: 8px;
    height: 45px;
    width: 100%;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)



# ---------------- NAVBAR ----------------
col1, col2, col3, col4, col5 = st.columns([2.5,1,1,1,1])

with col1:
    st.image(
        "assets/218245014_109376818090070_8985566675702664760_n.jpg",
        width=160
    )

with col2:
    st.button("Home", on_click=navigate, args=("Home",))

with col3:
    st.button("Rooms", on_click=navigate, args=("Rooms",))

with col4:
    st.button("Restaurant", on_click=navigate, args=("Restaurant",))

with col5:
    st.button("Banquet", on_click=navigate, args=("Banquet",))


# ================= HOME =================
if st.session_state.page == "Home":

    video_file = open(r"assets/AQOlAru5UeiElOzBD5uYR5Z0C2qhbFkuD2PlVgk2G91cE2HvI-gbUTl-uyvfmHQXFgV1vVOEhTqfJN32fPhw3Tw86fUcAZReStU.mp4", "rb")
    video_base64 = base64.b64encode(video_file.read()).decode()

    st.components.v1.html(f"""
    <div style="position:relative;height:450px;">
        <video style="width:100%;height:100%;object-fit:cover;" autoplay muted loop>
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);
        color:white;text-align:center;">
            <h1>Montelliscious</h1>
            <p>Stay • Dine • Celebrate</p>
        </div>
    </div>
    """, height=450)

    st.markdown("## Why Choose Us")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🛏️ Comfortable Rooms</h3>
            <p>Affordable stays under ₹1700 with premium comfort</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h3>🍽️ Great Food</h3>
            <p>Delicious meals at competitive prices</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <h3>🎉 Banquet Space</h3>
            <p>Perfect for small events & office gatherings</p>
        </div>
        """, unsafe_allow_html=True)

    # -------------------- BANNER SLIDER --------------------

    if "banner_index" not in st.session_state:
        st.session_state.banner_index = 0

    banners = [
        "https://images.pexels.com/photos/258154/pexels-photo-258154.jpeg",
        "https://images.pexels.com/photos/271624/pexels-photo-271624.jpeg",
        "https://images.pexels.com/photos/164595/hotel-room-bed-bedroom-164595.jpeg"
    ]

    st.markdown("## 🔥 Offers & Updates")

    # IMAGE (your HTML version - 80% centered)
    st.markdown(f"""
    <div style="width:80%; margin:auto;">
        <img src="{banners[st.session_state.banner_index]}" 
             style="width:100%; height:280px; object-fit:cover; border-radius:12px;">
    </div>
    """, unsafe_allow_html=True)

    # BUTTONS (aligned under image)
    b1, b2, b3 = st.columns([3, 2, 3])

    with b1:
        if st.button("⬅ Previous"):
            st.session_state.banner_index = (st.session_state.banner_index - 1) % len(banners)

    with b3:
        if st.button("Next ➡"):
            st.session_state.banner_index = (st.session_state.banner_index + 1) % len(banners)

    

          
        
        
    # -------------------- HIGHLIGHTS --------------------
    st.markdown("## Highlights")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rooms", "4")
    col2.metric("Restaurant Capacity", "50-70")
    col3.metric("Parking", "Available")
    col4.metric("Price Range", "₹1400-1700")

    # -------------------- GALLERY --------------------
    st.markdown("## Gallery")

    col1, col2, col3 = st.columns(3)
    col1.image(r"assets/2mont.jpg",width=250)
    col2.image(r"assets/3.Mont.jpg",width=250)
    col3.image(r"assets/1mont.jpg",width=250)


# ================= ROOMS =================

elif st.session_state.page == "Rooms":

    st.title("🛏️ Our Rooms")

    rooms = {
        "Deluxe Room": {
            "price": 1500,
            "images": [
                "https://images.pexels.com/photos/164595/hotel-room-bed-bedroom-164595.jpeg",
                "https://images.pexels.com/photos/271624/pexels-photo-271624.jpeg",
                "https://images.pexels.com/photos/262048/pexels-photo-262048.jpeg"
            ]
        },
        "Premium Room": {
            "price": 1700,
            "images": [
                "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg",
                "https://images.pexels.com/photos/189296/pexels-photo-189296.jpeg",
                "https://images.pexels.com/photos/276724/pexels-photo-276724.jpeg"
            ]
        },
        "Standard Room": {
            "price": 1400,
            "images": [
                "https://images.pexels.com/photos/271618/pexels-photo-271618.jpeg",
                "https://images.pexels.com/photos/279746/pexels-photo-279746.jpeg",
                "https://images.pexels.com/photos/210604/pexels-photo-210604.jpeg"
            ]
        },
        "Family Room": {
            "price": 1600,
            "images": [
                "https://images.pexels.com/photos/261102/pexels-photo-261102.jpeg",
                "https://images.pexels.com/photos/237371/pexels-photo-237371.jpeg",
                "https://images.pexels.com/photos/1648776/pexels-photo-1648776.jpeg"
            ]
        }
    }

    for room_name, details in rooms.items():
        st.markdown(f"### {room_name} - ₹{details['price']} / night")

        cols = st.columns(3)
        for col, img in zip(cols, details["images"]):
            with col:
                st.image(img, use_container_width=True)

        if st.button(f"Reserve {room_name}"):
            select_room(room_name)

        st.markdown("---")


# ================= ROOM DETAIL =================
elif st.session_state.page == "Room_Detail":

    rooms = {
        "Deluxe Room": {"price": 1500, "images": [
            "https://images.pexels.com/photos/164595/hotel-room-bed-bedroom-164595.jpeg",
            "https://images.pexels.com/photos/271624/pexels-photo-271624.jpeg",
            "https://images.pexels.com/photos/262048/pexels-photo-262048.jpeg"
        ]},
        "Premium Room": {"price": 1700, "images": [
            "https://images.pexels.com/photos/1457842/pexels-photo-1457842.jpeg",
            "https://images.pexels.com/photos/189296/pexels-photo-189296.jpeg",
            "https://images.pexels.com/photos/276724/pexels-photo-276724.jpeg"
        ]},
        "Standard Room": {"price": 1400, "images": [
            "https://images.pexels.com/photos/271618/pexels-photo-271618.jpeg",
            "https://images.pexels.com/photos/279746/pexels-photo-279746.jpeg",
            "https://images.pexels.com/photos/210604/pexels-photo-210604.jpeg"
        ]},
        "Family Room": {"price": 1600, "images": [
            "https://images.pexels.com/photos/261102/pexels-photo-261102.jpeg",
            "https://images.pexels.com/photos/237371/pexels-photo-237371.jpeg",
            "https://images.pexels.com/photos/1648776/pexels-photo-1648776.jpeg"
        ]}
    }

    room = st.session_state.selected_room
    details = rooms[room]

    st.button("⬅ Back", on_click=reset_room)

    st.title(f"{room} - ₹{details['price']} / night")

    # Gallery
    cols = st.columns(3)
    for col, img in zip(cols, details["images"]):
        with col:
            st.image(img, use_container_width=True)

    # Booking
    st.markdown("## Book Now")

    col1, col2 = st.columns(2)
    with col1:
        checkin = st.date_input("Check-in")
    with col2:
        checkout = st.date_input("Check-out")

    nights = (checkout - checkin).days if checkin and checkout else 0
    nights = max(nights, 1)

    total_price = nights * details["price"]

    st.markdown(f"### 💰 Total Price: ₹{total_price}")

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")

    if st.button("Confirm Booking"):
        st.success(f"✅ Booking Confirmed for {room}")
        st.write(f"Booking Amount: ₹{total_price}")



# -------------------- RESTAURANT --------------------
elif st.session_state.page == "Restaurant":

    # Back button
    #st.button("⬅ Back to Home", on_click=navigate, args=("Home",))

    st.title("🍽️ Restaurant")

    # ---------------- HERO / AMBIENCE ----------------
    st.markdown("### Experience Fine Dining")

    cols = st.columns(9)
    cols[0].image(r"assets/restpic1.jpg", width=250)
    cols[1].image(r"assets/Food.jpg", width=250)
    cols[2].image(r"assets/food2.jpg",width=250)
#     cols[3].image("https://images.pexels.com/photos/67468/pexels-photo-67468.jpeg", use_container_width=True)

    # ---------------- MENU SLIDER ----------------
    
    st.markdown("### 📜 Our Menu")

    menu_images = [
        
    r"assets/WhatsApp Image 2026-04-19 at 12.31.34 PM.jpeg"
    r"assets/WhatsApp Image 2026-04-19 at 12.31.30 PM.jpeg"
    r"assets/WhatsApp Image 2026-04-19 at 12.31.31 PM.jpeg"
    
    r"assets/WhatsApp Image 2026-04-19 at 12.31.31 PM (1).jpeg"
    r"assets/WhatsApp Image 2026-04-19 at 12.31.31 PM (2).jpeg"
    r"assets/WhatsApp Image 2026-04-19 at 12.31.32 PM.jpeg"
    r"assets/WhatsApp Image 2026-04-19 at 12.31.32 PM (1).jpeg"
    r"assets/WhatsApp Image 2026-04-19 at 12.31.33 PM.jpeg"
    r"assets/WhatsApp Image 2026-04-19 at 12.31.32 PM (2).jpeg"
    ]

    # selection (acts like clickable thumbnails)
    selected_index = st.radio(
        "Menu",
        options=list(range(len(menu_images))),
        format_func=lambda x: f"Menu {x+1}",
        horizontal=True,
        label_visibility="collapsed"
    )

    # Layout
    col1, col2 = st.columns([1,2])

    # ---- LEFT (THUMBNAILS) ----
    with col1:
        for i, img in enumerate(menu_images):
            st.image(img, width=100)

    # ---- RIGHT (MAIN IMAGE - CONTROLLED SIZE) ----
    with col2:
        st.image(menu_images[selected_index], width=350)  # 👈 controlled size

    # ---------------- BOOK TABLE ----------------
    st.markdown("## 🪑 Book Your Table")

    col1, col2 = st.columns(2)
    with col1:
        date_sel = st.date_input("Select Date")
    with col2:
        guests = st.slider("Guests", 1, 10)

    time_slot = st.selectbox("Select Time", ["7:00 PM", "8:00 PM", "9:00 PM"])

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")

    # ---------------- PAYMENT OPTION ----------------
    st.markdown("### 💳 Payment Option")
    payment = st.radio("Choose Payment", ["Pay at Restaurant", "Advance ₹200"])

    if st.button("Confirm Reservation"):
        if name and phone:
            st.success("✅ Table Reserved Successfully!")
            st.write(f"📅 {date_sel} | ⏰ {time_slot} | 👥 {guests} Guests")
            st.write(f"Payment Mode: {payment}")
        else:
            st.warning("Please enter Name & Phone")


# ================= BANQUET =================

elif st.session_state.page == "Banquet":

   # st.button("⬅ Back to Home", on_click=navigate, args=("Home",))

    st.title("🎉 Banquet Hall")

    # ---------------- HERO / IMAGES ----------------
    st.markdown("### Perfect for Small Events & Gatherings")

    col1, col2 = st.columns(2)
    col1.image(r"assets/banqmont.jpg", width=250)
    col2.image(r"assets/banqmon2.jpg", width=250)

    st.markdown("---")

    # ---------------- HIGHLIGHTS ----------------
    st.markdown("## ⭐ Highlights")

    c1, c2, c3 = st.columns(3)
    c1.metric("Capacity", "50–70 Guests")
    c2.metric("Parking", "Available")
    c3.metric("Setup", "Custom Decor")

    st.markdown("---")

    # ---------------- FIXED MENU ----------------
    st.markdown("## 🍽️ Fixed Banquet Menu")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### 🥗 Veg Menu
        - ₹300 / plate (Basic)
        - ₹500 / plate (Standard)
        - ₹700 / plate (Premium)
        """)

    with col2:
        st.markdown("""
        ### 🍗 Non-Veg Menu
        - ₹500 / plate (Basic)
        - ₹700 / plate (Standard)
        - ₹900 / plate (Premium)
        """)

    st.info("📞 Custom menu available. Contact for more details.")

    st.markdown("---")

    # ---------------- BOOKING FORM ----------------
    st.markdown("## 📅 Event Booking")

    col1, col2 = st.columns(2)
    with col1:
        event_type = st.selectbox("Event Type", ["Birthday", "Office Gathering", "Family Function", "Engagement"])
        event_date = st.date_input("Event Date")

    with col2:
        guests = st.number_input("Number of Guests", 10, 200)

    name = st.text_input("Name")
    phone = st.text_input("Phone Number")

    st.markdown("### 💳 Booking Type")
    payment = st.radio("Choose Option", ["Enquiry Only", "Advance Booking (₹2000)"])

    # ---------------- SUBMIT ----------------
    if st.button("Request Banquet Booking"):
        if name and phone:
            st.success("🎉 Request Submitted Successfully!")
            st.write(f"Event: {event_type}")
            st.write(f"Date: {event_date}")
            st.write(f"Guests: {guests}")
            st.write(f"Mode: {payment}")
        else:
            st.warning("Please enter Name and Phone Number")


# ---------------- FOOTER ----------------
# -------------------- FOOTER --------------------
st.markdown("""
<div class="footer">
📍 Your Location | 📞 Contact: 9XXXXXXXXX <br>
© 2026 Montelliscious. All rights reserved.
</div>
""", unsafe_allow_html=True)