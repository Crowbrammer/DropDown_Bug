#Create an example of the simplest version of the problem I*'m facing. So I can get help, or help myself more easily. 

'''

A'. Import the App, BoxLayout, Button, and DropDown class (X)
A. Instantiate an app (X)
B. Build an easy layout, consisting of a BoxLayout with 2 buttons in id (X)
B2-A. Make the buttons look more comfortable on the eyes (X)
B2-B. Create a list to store new instances of 'easy layouts' and dropdowns. (X)
C. Dynamically generate new instances of this BoxLayout with varying text (X)
D/2. Build the buttons within the DropDown (X)
D. Attach a dropdown to the right buttons (X)
E. Try to get it to change the widget beneath it, and nothing else. (X)

'''

# (A')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

kv = """
# File name: dropdownbug.py

EntireLayout:

<EntireLayout>:

	# B2-A
	orientation: 'vertical'
	padding: 20, 20

# (B)
<ItemLayout>:
	
	# B2-A
	padding: 20, 20
	# size_hint_y: None
	# height:'40dp'
	
	Button:
		id: Tom
		
	Button:
		id: Jerry
"""

class EntireLayout(BoxLayout):
	
	def __init__(self, **kwargs):
		super(EntireLayout, self).__init__(**kwargs)
		
		# (B2-B)
		dd_s = []
		easy_layouts = []
		
		# (C)
		for i in range(3):
		
			dd_s.append(DropDown())
			
			# D/2
			for each in range(3):
				
				btn = Button(text='{}'.format(str(each)), size_hint_y=None, height=44)
				
				btn.bind(on_release=lambda btn: dd_s[i].select(btn.text))

				dd_s[i].add_widget(btn)
			
			easy_layouts.append(ItemLayout())
			easy_layouts[i].ids.Jerry.text = 'VT: {}'.format(str(i))
			# D
			easy_layouts[i].ids.Jerry.bind(on_release=dd_s[i].open)				
			self.add_widget(easy_layouts[i])
			
			# The issue is with this line, I think.
			# E
			dd_s[i].bind(on_select=lambda instance, x: setattr(easy_layouts[i].ids.Jerry, 'text', x)) # lambda - get through Unit 1
			
class ItemLayout(BoxLayout):
	pass

class DropDownBugApp(App):
	def build(self):
		EntireLayout()

# A
if __name__ == '__main__':
	DropDownBugApp().run()