#Create an example of the simplest version of the problem I*'m facing. So I can get help, or help myself more easily. 

'''

A'. Import the App, BoxLayout, and DropDown class (X)
A. Instantiate an app (X)
B. Build an easy layout, consisting of a BoxLayout with 2 buttons in id (X)
B2. Create a list to store new instances of 'easy layouts' and dropdowns. (X)
C. Dynamically generate new instances of this BoxLayout with varying text (X)
D. Attach a dropdown to the right buttons 
E. Try to get it to change the widget beneath it, and nothing else. 

'''

# (A')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown

class EntireLayout(BoxLayout):
	
	def __init__(self, **kwargs):
		super(EntireLayout, self).__init__.(**kwargs)
		
		# (B2)
		dd_s = []
		easy_layouts = []
		
		# (C)
		for i in range(3):
		
			dd_s.append(DropDown())
			easy_layouts.append(ItemLayout())
			easy_layouts[i].ids.text = 'Varying text: {}'.format(str(i))
			
			self.add_widget(ItemLayout)
			
class ItemLayout(BoxLayout):
	pass

class DropDownBugApp(App):
	def build(self)
		EntireLayout()

if __name__ == '__main__':
	DropDownBugApp().run()