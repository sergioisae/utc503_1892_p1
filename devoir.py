class Etudiant:
    def __init__(self, id_etudiant, nom_etudiant, prenom_etudiant, level_etudiant):
        self.id_etudiant = id_etudiant
        self.nom_etudiant = nom_etudiant
        self.prenom_etudiant = prenom_etudiant
        self.level_etudiant = level_etudiant


class Cours:
    def __init__(self, id_cours, code_cours, level_cours):
        self.id_cours = id_cours
        self.code_cours = code_cours
        self.level_cours = level_cours


class Note:
    def __init__(self, id_etudiant, code_cours, note_etudiant):
        self.id_etudiant = id_etudiant
        self.code_cours = code_cours
        self.note_etudiant = note_etudiant


class DB:
    def __init__(self):
        self.list_etudiant = []
        self.list_cours = []
        self.list_note = []

    def AjouterEtudiant(self, Etudiant):
        self.list_etudiant.append(Etudiant)

    def SupprimerEtudiant(self, Etudiant):
        self.list_etudiant.remove(Etudiant)

    def ModifierEtudiant(self, Etudiant, nom_etudiant, prenom_etudiant, level_etudiant):
        self.list_etudiant.remove(Etudiant)
        Etudiant.nom_etudiant = nom_etudiant
        Etudiant.prenom_etudiant = prenom_etudiant
        Etudiant.level_etudiant = level_etudiant
        self.list_etudiant.append(Etudiant)

    def AjouterCours(self, Cours):
        self.list_cours.append(Cours)

    def SupprimerCours(self, Cours):
        self.list_cours.remove(Cours)

    def ModifierCours(self, code_cours, level_cours):
        self.list_cours.remove(Cours)
        Cours.code_cours = code_cours
        Cours.level_cours = level_cours
        self.list_cours.append(Cours)

    def AjouterNote(self, Cours):
        self.list_note.append(Note)

    def SupprimerNote(self, Cours):
        self.list_note.remove(Note)

    def ModifierNote(self, Note, note_etudiant):
        self.list_note.remove(Note)
        Note.note_etudiant = note_etudiant
        self.list_note.append(Note)


def CalculeMoyenneClasse(self, DB, Cours):
    list_moyenne = []
    for i in DB.list_note:
        if (DB.list_note[i].code_cours == Cours.code_cours):
            list_moyenne.append(DB.list_note.note_etudiant)
    MoyenneClasse = sum(list_moyenne) / len(list_moyenne)
    return MoyenneClasse


def CalculeMoyenneEtudiant(self, DB, Etudiant):
    list_moyenne = []
    for i in DB.list_note:
        if (DB.list_note[i].id_etudiant == Etudiant.id_etudiant):
            list_moyenne.append(DB.list_note.note_etudiant)
    moyenne_cours = sum(list_moyenne) / len(list_moyenne)
    return moyenne_cours


def ConsultationClasse(Cours,list_note):
    note_cours = list(filter(lambda GetNote: list_note.code_cours == Cours.code_cours, list_note))
    valeur_note = list(map(lambda valeur_note: Note.note_etudiant, note_cours))
    print(valeur_note)


def ConsultationEtudiant(Etudiant,list_note):
    note_cours = list(filter(lambda GetNote: Note.code_cours == Cours.code_cours,list_note))
    valeur_note = list(map(lambda valeur_note: Note.note_etudiant, note_cours))
    print(valeur_note)
    
