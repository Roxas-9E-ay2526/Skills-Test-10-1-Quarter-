from pyscript import document, display

def create_order(event):
    Hotdog1 = document.getElementById("Hotdog1")
    Hotdog2 = document.getElementById("Hotdog2")
    Hotdog3 = document.getElementById("Hotdog3")
    Hotdog4 = document.getElementById("Hotdog4")
    Hotdog5 = document.getElementById("Hotdog5")
    
    subtotal = (
        (float(Hotdog1.value) if Hotdog1.checked else 0.0) +
        (float(Hotdog2.value) if Hotdog2.checked else 0.0) +
        (float(Hotdog3.value) if Hotdog3.checked else 0.0) +
        (float(Hotdog4.value) if Hotdog4.checked else 0.0) +
        (float(Hotdog5.value) if Hotdog5.checked else 0.0) 
    )
    
    vat = subtotal * 0.12
    total = subtotal + vat

    receipt_html = f"""
    <div class="receipt">
        <p>===== <b>Receipt</b> =====</p>
        <p>Subtotal: ₱{subtotal:.2f}</p>
        <p>Tax: ₱{vat:.2f}</p>
        <p><b>Total: ₱{total:.2f}</b></p>
    </div>
    """

    document.getElementById("show").innerHTML = receipt_html