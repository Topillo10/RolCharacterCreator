/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                                   TABLA DATOS BASICOS                                                   //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if(window.location.href.endsWith('/pjcreation04')){

    var profesionSelect = document.getElementById("id_profesion");
    var dominioSelect = document.getElementById("id_dominio_magico");

    // función que se ejecuta al cambiar la selección de "Profesión"
    function actualizarDominio() {
        var profesionSeleccionada = profesionSelect.options[profesionSelect.selectedIndex].value;
        dominioSelect.innerHTML = "";
        if (profesionSeleccionada == "Guerrero" || profesionSeleccionada == "Explorador" || profesionSeleccionada == "Mago" || profesionSeleccionada == "Bardo") {
            var opcionEsencia = document.createElement("option");
            opcionEsencia.value = "Esencia";
            opcionEsencia.text = "Esencia";
            dominioSelect.add(opcionEsencia);
        }
        if (profesionSeleccionada == "Guerrero" || profesionSeleccionada == "Explorador" || profesionSeleccionada == "Montaraz" || profesionSeleccionada == "Animista") {
            var opcionCanalizacion = document.createElement("option");
            opcionCanalizacion.value = "Canalizacion";
            opcionCanalizacion.text = "Canalización";
            dominioSelect.add(opcionCanalizacion);
        }
    }

    profesionSelect.addEventListener("change", actualizarDominio);
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                     TABLA CARACTERISTICAS - DUPLICIDAD DE OPCIONES                                      //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if(window.location.href.endsWith('/asignar_caract_t1') || window.location.href.endsWith('/asignar_caract_t2') || window.location.href.endsWith('/asignar_caract_t3')){

  let opciones = [  { valor: "---", texto: "---" },  { valor: "FUE", texto: "FUE" },  { valor: "AGI", texto: "AGI" },  { valor: "CON", texto: "CON" },  { valor: "INT", texto: "INT" },  { valor: "I", texto: "I" },  { valor: "PRE", texto: "PRE" },  { valor: "APA", texto: "APA" },];

  const caract1 = document.getElementById("caract1");
  const caract2 = document.getElementById("caract2");
  const caract3 = document.getElementById("caract3");
  const caract4 = document.getElementById("caract4");
  const caract5 = document.getElementById("caract5");
  const caract6 = document.getElementById("caract6");
  const caract7 = document.getElementById("caract7");

  function agregarOpciones(select) {
    opciones.forEach((opcion) => {
      const option = document.createElement("option");
      option.value = opcion.valor;
      option.text = opcion.texto;
      select.appendChild(option);
    });
    console.log("Opciones agregadas al select");
  }

  function eliminarOpcionSeleccionada(valorSeleccionado) {
    opciones = opciones.filter((opcion) => opcion.valor !== valorSeleccionado);
  }

  window.addEventListener("load", () => {
    agregarOpciones(caract1);
    agregarOpciones(caract2);
    agregarOpciones(caract3);
    agregarOpciones(caract4);
    agregarOpciones(caract5);
    agregarOpciones(caract6);
    agregarOpciones(caract7);
  });

  caract1.addEventListener("change", (event) => {
    const valorSeleccionado = event.target.value;
    eliminarOpcionSeleccionada(valorSeleccionado);
    caract2.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract3.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract4.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract5.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract6.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract7.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
  });

  caract2.addEventListener("change", (event) => {
    const valorSeleccionado = event.target.value;
    eliminarOpcionSeleccionada(valorSeleccionado);
    caract1.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract3.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract4.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract5.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract6.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract7.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
  });

  caract3.addEventListener("change", (event) => {
    const valorSeleccionado = event.target.value;
    eliminarOpcionSeleccionada(valorSeleccionado);
    caract1.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract2.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract4.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract5.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract6.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract7.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
  });

  caract4.addEventListener("change", (event) => {
    const valorSeleccionado = event.target.value;
    eliminarOpcionSeleccionada(valorSeleccionado);
    caract1.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract2.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract3.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract5.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract6.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract7.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
  });

  caract5.addEventListener("change", (event) => {
    const valorSeleccionado = event.target.value;
    eliminarOpcionSeleccionada(valorSeleccionado);
    caract1.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract2.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract3.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract4.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract6.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract7.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
  });

  caract6.addEventListener("change", (event) => {
    const valorSeleccionado = event.target.value;
    eliminarOpcionSeleccionada(valorSeleccionado);
    caract1.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract2.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract3.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract4.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract5.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract7.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
  });

  caract7.addEventListener("change", (event) => {
    const valorSeleccionado = event.target.value;
    eliminarOpcionSeleccionada(valorSeleccionado);
    caract1.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract2.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract3.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract4.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract5.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
    caract6.querySelectorAll("option").forEach((option) => {
      if (option.value === valorSeleccionado) {
        option.remove();
      }
    });
  });


/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//                                     TABLA CARACTERISTICAS - DESHABILITAR BOTON ELEGIR                                   //
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
  
    // Obtén todos los selectores por su id y recorre cada uno
    for (var i = 1; i <= 7; i++) {
      var selector = document.getElementById('caract' + i);
      var opcionSeleccionada = selector.value;

      // Incrementa el contador de la opción seleccionada
      opciones[opcionSeleccionada]++;
    }
      
  function contarOpcionesSeleccionadas(){
      
    var opciones = {
        '---': 0,
        'FUE': 0,
        'AGI': 0,
        'CON': 0,
        'INT': 0,
        'I': 0,
        'PRE': 0,
        'APA': 0
      };
    
    // Imprime los resultados en la consola
    console.log('---: ' + opciones['---']);
    console.log('FUE: ' + opciones['FUE']);
    console.log('AGI: ' + opciones['AGI']);
    console.log('CON: ' + opciones['CON']);
    console.log('INT: ' + opciones['INT']);
    console.log('I: ' + opciones['I']);
    console.log('PRE: ' + opciones['PRE']);
    console.log('APA: ' + opciones['APA']);
    
    // Obtén los botones por su id
    var botonsiguiente = document.getElementById('next');

    // Desactiva los botones si opciones['---'] es distinta de 0
    if (opciones['---'] !== 0) {
        botonsiguiente.disabled = true;
      } else {
        botonsiguiente.disabled = false;
        }
  }

  selector.addEventListener("change", contarOpcionesSeleccionadas);

}
