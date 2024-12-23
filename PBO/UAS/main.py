from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class ProductCard(BoxLayout):
    def __init__(self, product_name, price, image_path, add_to_cart_callback, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        self.padding = 10
        self.spacing = 5
        self.size_hint = (None, None)
        self.size = (200, 300)

        # Product Image
        self.add_widget(Image(source=image_path, size_hint=(1, 0.6)))

        # Product Name
        self.add_widget(Label(text=product_name, size_hint=(1, 0.2), color=(0.3, 0.2, 0.1, 1)))

        # Product Price
        self.add_widget(Label(text=f'Rp {price}', size_hint=(1, 0.1), color=(0.4, 0.3, 0.2, 1)))

        # Add to Cart Button
        add_button = Button(text="+ Add to Cart", size_hint=(1, 0.1), background_color=(0.6, 0.4, 0.3, 1))
        add_button.bind(on_press=lambda instance: add_to_cart_callback(product_name, price))
        self.add_widget(add_button)

class MainApp(App):
    def build(self):
        self.cart = []

        root = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Navigation Bar
        nav_bar = BoxLayout(size_hint=(1, 0.1), spacing=10)
        nav_bar.add_widget(Button(text="Home", background_color=(0.6, 0.4, 0.3, 1)))
        nav_bar.add_widget(Button(text="Products", background_color=(0.6, 0.4, 0.3, 1)))
        nav_bar.add_widget(Button(text="Cart", background_color=(0.6, 0.4, 0.3, 1), on_press=self.show_cart))
        root.add_widget(nav_bar)

        # Product List
        scroll_view = ScrollView(size_hint=(1, 0.8))
        product_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        product_layout.bind(minimum_height=product_layout.setter('height'))

        # Sample Products
        products = [
            {"name": "Casual Blouse", "price": 200000, "image": "blouse.jpg"},
            {"name": "Vintage Dress", "price": 350000, "image": "vintage_dress.jpg"},
            {"name": "Summer Skirt", "price": 150000, "image": "summer_skirt.jpg"},
            {"name": "Classic Jacket", "price": 400000, "image": "classic_jacket.jpg"},
        ]

        for product in products:
            product_card = ProductCard(
                product_name=product["name"],
                price=product["price"],
                image_path=product["image"],
                add_to_cart_callback=self.add_to_cart
            )
            product_layout.add_widget(product_card)

        scroll_view.add_widget(product_layout)
        root.add_widget(scroll_view)

        # Checkout Button
        checkout_button = Button(text="Checkout", size_hint=(1, 0.1), background_color=(0.5, 0.3, 0.2, 1))
        checkout_button.bind(on_press=self.show_cart)
        root.add_widget(checkout_button)

        return root

    def add_to_cart(self, product_name, price):
        self.cart.append((product_name, price))
        popup = Popup(title="Product Added",
                      content=Label(text=f"{product_name} has been added to your cart!"),
                      size_hint=(0.8, 0.4))
        popup.open()

    def show_cart(self, instance):
        if not self.cart:
            popup = Popup(title="Cart",
                          content=Label(text="Your cart is empty!"),
                          size_hint=(0.8, 0.4))
            popup.open()
            return

        cart_content = GridLayout(cols=1, spacing=10, size_hint_y=None)
        cart_content.bind(minimum_height=cart_content.setter('height'))

        total_price = 0
        for item in self.cart:
            cart_content.add_widget(Label(text=f"{item[0]} - Rp {item[1]}", size_hint_y=None, height=30, color=(0.3, 0.2, 0.1, 1)))
            total_price += item[1]

        cart_content.add_widget(Label(text=f"Total: Rp {total_price}", size_hint_y=None, height=30, color=(0.4, 0.3, 0.2, 1)))

        popup = Popup(title="Your Cart",
                      content=cart_content,
                      size_hint=(0.8, 0.8))
        popup.open()

if __name__ == '__main__':
    MainApp().run()
