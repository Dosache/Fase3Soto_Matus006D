/*funcion para botones proximamente de autocultivo.html*/
function proximamente() {
    alert('Esta extensión estará disponible proximamente, ¡Suscríbete para más actualizaciones! 😎');
}

//validar registro
$(function () {
    $("#mi-formulario").validate({
        rules: {
            email: {
                required: true,
                email: true
            },
            email2: {
                required: true,
                email: true
            },
            password: "required",
            fono: "required",
            fecha: "required",
            password2: {
                required: true,
                equalTo: "#password"
            }

        }, //rules
        messages: {

            email: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido, intente nuevamente'
            },
            email2: {
                required: 'Ingresa tu correo electrónico',
                email: 'Formato de correo no válido, intente nuevamente'
            },
            password: {
                required: 'Ingresa una contraseña',
                minlength: 'Caracteres insuficiente'
            },
            fono: {
                required: 'Ingrese un número de celular',
                minlength: 'Cantidad de digitos insuficiente'
            },
            fecha: {
                required: 'Seleccione una fecha válida',
                min: 'Fecha no corresponde'
            },
            password2: {
                required: 'Reingresa la contraseña por favor',
                equalTo: 'Las contraseñas ingresadas no coinciden, intente nuevamente',
                minlength: 'Caracteres insuficiente'

            }

        }//messages
    }); //$('#mi-formulario').validate
}); //function

//Validar correo suscripción
function validacion()
{
    cor=document.getElementById('correo').value;
    if(cor.length>10 && cor!=null)
        {
            alert('¡Suscripción realizada correctamente!😎');
            
        }
    else{
        alert('Error: debe ingresar un correo válido, más de 10 caracteres!');
            document.getElementById('correo').value="";
            document.suscripcion.cor.focus();
            return false;
    }
    return true;
        
    
}