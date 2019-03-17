
def escribir_archivo(nombres, links, dia):
	with open(f"./Trailers/{dia}.txt", "w", encoding="utf-8") as arch:
		for nombre, link in zip(nombres, links):
				arch.write(f"{nombre}\n\t{link}\n\n")
