*BUILD MODELS*


  -  __MODEL__: *ACCOUNT*
      - ATRIBUTES:
          + *USER ID*
          + USERNAME:
                + max: 150 characters
                + Letters, digits and @ . + - _
          + PASSWORD:
                + min: 8 characters

      - ACTIONS:
          + Add Account (save account into database)
          + Is Valid Account (valid characters and symbols....)
          + Is Exist Account (exist in database)


  -  __FORM__ : *SIGN UP*: inheritance from ACCOUNT
      - ATRIBUTES: fields
          @USERNAME
          @PASSWORD
          + CONFIRM_PASSWORD: *don't save into database*
                + same as PASSWORD
          + BUTTON: SIGN UP - type 'submit'

      - ACTIONS:      
           + Is Same PASS and CONFIRM ?


  - __FORM__ : *LOGIN*: inheritance from ACCOUNT
      - ATRIBUTES: fields
          @USERNAME
          @PASSWORD
          + BUTTON: LOGIN - type 'submit'

      - ACTIONS:


  - __VIEW__ + __TEMPLATES__: *SIGN UP* and *LOGIN*
      (html + boostraps + css)
      - home.html (base page)
      - signup.html
      - login.html  


  - __MODEL__: *MOVIE*
      - ATTRIBUTES:
          + *MOVIE ID*
          + TITLE*: free
          + DESCRIPTIONS*: free
          + RELEASE DATE*: DD/MM/YYYY
          + CATEGORY*:
              + an available list(database): such as: action, fiction, horror, cartoon....
              + user drops down the list and chooses the CATEGORY
              + ONLY ONE CHOICE
          + *CAST* __many-many__
              + an available list(database): suck as: A,B,C,D.....
              + user checks list(by sticking) and chooses the ACTORS.
              + 0 UP TO several CHOICES
          + LOGO:
              + an absolute path to the image
              + upload image


      - ACTIONS:
          + Show list of movies sorted by RELEASE DATE (index_movie)
          + Add movie
          + Edit movie - *relative with actors/actress and award associated*
          + Delete movie - *relative with actors/actress and award associated*
          + ....


  - __FORM__ : *ADDING/UPDATE* MOVIE*: inheritance from MOVIE
      - ATRIBUTES: fields
          @TITLE
          @DESCRIPTIONS
          @RELEASE DATE
          @CATEGORY
          @ACTORS
          @LOGO
          + BUTTON: ADDING - type 'submit'

      - ACTIONS:


  - __VIEW__ + __TEMPLATES__: *MOVIE*
      (html + boostraps + css)
      - index_movie.html (list 10 films/page)
          + ONLY 1 buttons for adding movie
          + each film:
                - show tittle and release day
                - have buttons of view detail, edit and delete
      - add_movie.html (show the form for adding into database)
      - detail_movie.html (show detail of a movie)
      - delete_movie.html (announce a movie be deleted)


  - __MODEL__: *CAST*
      - ATTRIBUTES:
          + *CAST ID*
          + First name*
          + Last name*
          + Birthdate*: DD/MM/YYYY
          + Sex*: Male/Female
          + Nationality*
          + A checkbox to check if the actor/actress is alive
          + *MOVIE* __many-many__

      - ACTIONS:
          + Show list of cast sorted by RELEASE  (index_movie)
          + Add movie
          + Edit movie - *relative with actors/actress and award associated*
          + Delete movie - *relative with actors/actress and award associated*
          + ....
