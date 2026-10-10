# BCHEIKH — Vitrine publique

Vitrine mobile-first pour présenter les tee-shirts, polos et caleçons de **BCHEIKH**.

## Offres affichées

- Tee-shirt / polo : **7 000 FCFA l’unité**
- Pack de 3 pièces : **20 000 FCFA**
- Poche de 3 caleçons : **7 000 FCFA**

## Contacts

- WhatsApp principal : **+221 78 652 31 29**
- WhatsApp secondaire : **+221 77 174 27 49**

## Fichiers à placer à la racine du dépôt

```text
index.html
README.md
BCHEIKH_TIKTOK_CORRIGE_9x16.mp4
a_vertical_product_advertisement_flyer_on_a_blac.png
```

Le fichier image sert d’affiche d’attente avant la lecture de la vidéo.

## Mise en ligne avec GitHub Pages

1. Créer un dépôt GitHub public.
2. Ajouter les quatre fichiers à la racine.
3. Ouvrir **Settings**.
4. Aller dans **Pages**.
5. Dans **Build and deployment**, choisir :
   - Source : `Deploy from a branch`
   - Branch : `main`
   - Folder : `/ (root)`
6. Enregistrer.
7. Attendre quelques minutes puis ouvrir l’adresse GitHub Pages fournie.

## Modification des prix

Dans `index.html`, rechercher les blocs suivants :

```html
<div class="price">7 000</div>
<div class="price">20 000</div>
<div class="price">7 000</div>
```

Modifier seulement les montants et les textes associés.

## Modification des numéros

Rechercher dans `index.html` :

```text
221786523129
221771742749
```

Les liens WhatsApp utilisent le format international sans espace ni signe `+`.

## Structure technique

- HTML, CSS et JavaScript dans un seul fichier
- Aucun framework
- Aucun abonnement externe
- Compatible mobile
- Boutons WhatsApp et téléphone
- Vidéo verticale 9/16
- Référencement social Open Graph

## Vérifications avant publication

- Tester la vidéo sur iPhone et Android
- Tester les deux liens WhatsApp
- Vérifier les prix affichés
- Vérifier les tailles et couleurs disponibles
- Contrôler que la vidéo et l’image utilisent exactement les noms de fichiers indiqués

---

BCHEIKH — Vente directe, prix clairs, commande simple.

## 🔐 Accès propriétaire — vitrine et carte vivante

Le bouton **Accès propriétaire**, présent sur `index.html` et `carte/index.html`, renvoie au portail existant de DIGIYLYFE :

`https://digiylyfe.com/acces-proprietaire.html?fiche=bcheikh`

**État au 10 octobre 2026 : lien public installé, activation personnelle non encore établie.** La fiche `bcheikh` n'est pas enregistrée dans `public.professionals` avec un email propriétaire autorisé, ni dans `digiy_commerce_sites`. Le simple bouton ne crée ni session, ni fiche CORE, ni droit d'édition et ne donne accès à aucune commande ou donnée personnelle.

Pour livrer la gestion au véritable professionnel : vérifier humainement son email, confirmer le compte Supabase Auth, enregistrer une association propriétaire sûre via le processus OPS, contrôler le magic link et un refus d'accès depuis un autre compte. Ne jamais utiliser le numéro WhatsApp ou le nom comme preuve de propriété, ni mettre un lien MASTER/administrateur dans la vitrine.

Ce correctif conserve les commandes WhatsApp, les paiements Wave directs, la boutique, les prix, les traductions WORLD8 et la PWA.
