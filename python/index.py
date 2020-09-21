from browser import document, html

def action():
    html.H1('Brython Hello', style={'height':100, 'width':200, 'position': relative})  

      <script type="text/python" id="script0">
          from browser import document, console, alert
  
          def show(e):
              console.log(e)
              alert('Hello World')
              document['hello'] <= 'Hello World'
  
          document['alert-btn'].bind('click', show)
      </script>
  
      <script type="text/python" id="script1">
          from browser import document
  
          def show_text(e):
              document['output'].textContent = e.target.value;
  
          document['text'].bind('input', show_text)
      </script>
  
      <script type="text/python" id="script2">
          from browser import document
          from browser.template import Template
  
          Template(document['greet']).render(name='Brad')
      </script>

      <script type="text/python" id="script4">
          from browser import document, window
  
          def file_read(e):
              def onload(e):
                  document['file-text'].value = e.target.result 
              
              file = document['file-upload'].files[0]
              reader = window.FileReader.new()
              reader.readAsText(file)
              reader.bind('load', onload)
          
          document['file-upload'].bind('input', file_read)
      </script>
  
      <script type="text/python" id="script5">
          from browser import document, html
  
          box = document['rotate-box']
          angle = 10
  
          def change(e):
              global angle
              box.style.transform = f"rotate({angle}deg)"
              angle += 10
  
          document['rotate-btn'].bind('click', change)
      </script>
  
      <script type="text/python" id="script6">
          from browser import document, html, window, console
  
          storage = window.localStorage
  
          if storage.getItem('item'):
              document['item'] <= storage.getItem('item')
  
          def add_item(e):
              item = document['item-input'].value
              storage.setItem('item', item)
              document['item'].textContent = item
  
          def remove_item(e):
              storage.removeItem('item')
              document['item'].textContent = ''
  
          document['add-btn'].bind('click', add_item)

          document['remove-btn'].bind('click', remove_item)

      </script>
