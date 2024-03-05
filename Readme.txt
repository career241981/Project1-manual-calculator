Project Overview: 
To Create a Simple Manual Calculator Using Python GUI tkinter library in Visual Studio Basic.

Project Requirements:
> Manual Calculator with Clikabel buttons as in simple calculator.
> The buttons are placed equally spaced and digits printed on it.
> To provide Calculator background colour, font colours, Calculator Logo.
> Create the Entry Field where diplay of numbers and calculations are visible.
> Whenever any number button is pressed it is displayed at the entry field. 
> Buttons to be used 1,2,3,4,5,6,7,8,9,0, +, -, *, /, C,=
> Calculator not resizable.
> Calculator to evaluate the results of addition, subtraction, multiplication and division.
> Calculatorto Print Invalid Entry for Syntax Errors pressed by operator.
> For Division by Zero it should show Error message.
> Finally to push the Project to GitHub as Repository.

Goal Of the Project:
> Learn about Visual Studio Basic
> Learn about Tkinter and other libraries
> Learn about creating GUI applications
> Learn about 

Some Details and definations:
Tkinter is the inbuilt python module that is used to create GUI applications. 
It is one of the most commonly used modules for creating GUI applications in 
Python as it is simple and easy to work with. It gives an object-oriented 
interface to the Tk GUI toolkit. 
What are Widgets?
Widgets in Tkinter are the elements of GUI application which provides various 
controls (such as Labels, Buttons, ComboBoxes, CheckBoxes, MenuBars, RadioButtons and many more) 
to users to interact with the application. Fundamental structure of tkinter

Import Tkinter Libraties ---->>Creating Main Window for GUI application-->>Add Widgets totheApp-->>Enter the 
main event Loop.
Basic Tkinter Widgets: 

Widgets	Description:

Label	        It is used to display text or image on the screen
Button	        It is used to add buttons to your application
Canvas	        It is used to draw pictures and others layouts like texts, graphics etc.
ComboBox	It contains a down arrow to select from list of available options
CheckButton	It displays a number of options to the user as toggle buttons from which user can select any number of options.
RadioButton	It is used to implement one-of-many selection as it allows only one option to be selected
Entry	        It is used to input single line text entry from user
Frame	        It is used as container to hold and organize the widgets
Message	        It works same as that of label and refers to multi-line and non-editable text
Scale	        It is used to provide a graphical slider which allows to select any value from that scale
Scrollbar	It is used to scroll down the contents. It provides a slide controller.
SpinBox	        It is allows user to select from given set of values
Text	        It allows user to edit multiline text and format the way it has to be displayed
Menu	        It is used to create all kinds of menu used by an application

Geometry Management
Creating a new widget doesn’t mean that it will appear on the screen. To display it, we need to call a 
special method: either grid, pack(example above), or place. 

Method	Description
pack()	       The Pack geometry manager packs widgets in rows or columns.
grid()	       The Grid geometry manager puts the widgets in a 2-dimensional table. 

               The master widget is split into a number of rows and columns, and each “cell”
               in the resulting table can hold a widget.
place()	       The Place geometry manager is the simplest of the three general geometry managers 
               provided in Tkinter. It allows you explicitly set the position and size of a window,
               either in absolute terms, or relative to another window.


