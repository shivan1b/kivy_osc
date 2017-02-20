This is a sample program to implement OSC communication between an activity and a service in kivy.


Brief overview

==============


---------------------------------------------------------------------------------
|																				|
|																				|
|																				|
|			-------------------                 --------------------			|
|           |                 |					|				   | 			|
|           |     main.py     |---------------->|	  main.py      |			|
|			|				  |<----------------|				   |			|
|           -------------------					--------------------			|
|			|		UI  	  |					|	  service	   |			|
|			-------------------					--------------------			|
|																				|
|																				|
|								  Application									|
---------------------------------------------------------------------------------


Application comprises of UI and service so there should be two main.py bundled together.


In order for application to run, service should communicate with the UI. There are many ways to do this
but kivy uses OSC [see here](./activity_service_comm/service/main.py) because of its light weight nature.


API guidelines

--------------

- https://kivy.org/docs/api-kivy.lib.osc.oscAPI.html


UI is the root of the project and hence can start services on start, therefore running the main.py of UI
is enough to launch the entire project.


Note

----

* This code implements half-duplex messaging.

* In order to do a full-duplex messaging, two separate threads would be required.

* Default buildozer dependencies are provided