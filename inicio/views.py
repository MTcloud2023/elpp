from django.shortcuts import redirect, render 
from django.http import HttpResponse
from .models import UserSurvey

def home(request):

    mostrar_formulario = request.session.get("acepto", False)

    if request.method == "POST":

        # Paso 1: aceptar disclaimer
        if "aceptar" in request.POST:
            request.session["acepto"] = True
            return redirect("home")

        # Paso 2: envío del formulario
        if request.session.get("acepto"):

            nombre = request.POST.get("nombre", "").strip()

            # Si marcó admin
            if "admin" in request.POST:
                request.session["nombre"] = ""
                return redirect("admin_view")

            # Si escribió nombre (usuario normal)
            elif nombre:
                request.session["user_nombre"] = nombre
                return redirect("user_view")

    return render(request, "home.html", {
        "mostrar_formulario": mostrar_formulario
    })

def admin_view(request):
    if request.method == "POST" and "enviar_admin" in request.POST:
        request.session["pregunta1"] = request.POST.get("pregunta1")
        request.session["fecha_inicio"] = request.POST.get("fecha_inicio")
        request.session["fecha_fin"] = request.POST.get("fecha_fin")
        request.session["pregunta3"] = request.POST.get("pregunta3")
        return render(request, "admin_step2.html")

    return render(request, "admin_view.html")

def why_view(request):
    if request.method == "POST":
        request.session["motivo"] = request.POST.get("motivo")
        return redirect("final")

    return render(request, "why.html")

def final_view(request):
    contexto = {
        "nombre": request.session.get("nombre"),
        "pregunta1": request.session.get("pregunta1"),
        "fecha_inicio": request.session.get("fecha_inicio"),
        "fecha_fin": request.session.get("fecha_fin"),
        "pregunta3": request.session.get("pregunta3"),
        "motivo": request.session.get("motivo"),
    }
    return render(request, "final.html", contexto)



def user_view(request):
    nombre = request.session.get("user_nombre")

    if not nombre:
        return redirect("home")

    if request.method == "POST":
        UserSurvey.objects.create(
            nombre=nombre,
            opcion_principal=request.POST.get("opcion_principal"),
            pregunta1=request.POST.get("pregunta1"),
            pregunta2=request.POST.get("pregunta2"),
            pregunta2_detalle=request.POST.get("pregunta2_detalle"),
            pregunta3=request.POST.get("pregunta3"),
            fecha_inicio=request.POST.get("fecha_inicio"),
            fecha_fin=request.POST.get("fecha_fin"),
            pregunta5=request.POST.get("pregunta5"),
            pregunta6=request.POST.get("pregunta6"),
            pregunta7=request.POST.get("pregunta7"),
            pregunta8=request.POST.get("pregunta8"),
            pregunta9=request.POST.get("pregunta9"),
            pregunta10=request.POST.get("pregunta10"),
            pregunta11=request.POST.get("pregunta11"),
            pregunta12=request.POST.get("pregunta12"),

            imagen=request.FILES.get("imagen"),
        )

        return render(request, "survey_success.html", {"nombre": nombre})

    return render(request, "user_view.html", {
    "nombre": nombre,
    "preguntas_check": {
        "7": "Oral",
        "8": "Anal",
        "9": "Condom?",
        "10": "Threesome",
        "11": "Cum in Face",
        "12": "Toys"
    }
})
