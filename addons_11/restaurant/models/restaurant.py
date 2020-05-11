from odoo import models,fields

class commande (models.Model):
    _name = 'commande.commande'
    _description='commande.commande'
    
    nom = fields.Char(string='nom', required=True, readonly=False)
    
    produit_ids = fields.One2many('produit.produit','commande_id',string='produit')
    cuisinier_id = fields.Many2one('cuisinier.cuisinier',string='cuisinier')
    serveur_id = fields.Many2one('serveur.serveur',string='serveur')
    caissier_id = fields.Many2one('caissier.caissier',string='caissier')
    facture_id = fields.Many2one('facture.facture',string='facture')
    client_id = fields.Many2one('client.client',string='client')
    

class produit (models.Model):
    _name = 'produit.produit'
    _description='produit'
    
    nom = fields.Char(string='nom', required=True , readonly=False)
    type = fields.Char(string='type', required=True , readonly=False)
    quantite = fields.Float(string='quantite' , required=True , readonly=False)
    commande_id = fields.Many2one('commande.commande',string='commande')
    cuisinier_id = fields.Many2one('cuisinier.cuisinier',string='cuisinier')
    
class Cuisinier (models.Model):
    _name = 'cuisinier.cuisinier'
    _description='cuisinier'
    
    nom = fields.Char(string='nom', required=True , readonly=False)
    produit_ids = fields.One2many('produit.produit','cuisinier_id',string='produit') 
    commande_ids = fields.One2many('commande.commande','cuisinier_id',string='commande')
   

class Serveur (models.Model):
    _name = 'serveur.serveur'
    _description='serveur' 
    
    nom = fields.Char(string='nom', required=True , readonly=False)
    prenom = fields.Char(string='prenom', required=True , readonly=False)
    pos = fields.Char(string='pos', required=True , readonly=False)
    commande_ids = fields.One2many('commande.commande','serveur_id',string='commande')
    table_id = fields.Many2one('table.table',string='table')
   
class Table (models.Model): 
    _name = 'table.table'
    _description='table'
    
    numero = fields.Integer(string='numero' , required=True , readonly=False)
    occupe = fields.Boolean(string='occupe' , required=True , readonly=False)
    serveur_ids = fields.One2many('serveur.serveur','table_id',string='serveur')
    client_id = fields.Many2one('client.client',string='client')
       
class Client (models.Model):
    _name = 'client.client'
    _description='client'
    
    
    nom = fields.Char(string='nom', required=True , readonly=False)
    prenom = fields.Char(string='prenom', required=True , readonly=False)
    facture_ids = fields.One2many('facture.facture','client_id',string='facture')
    table_ids = fields.One2many('table.table','client_id',string='table')
    commande_ids = fields.One2many('commande.commande','client_id',string='commande')
    
class Facture (models.Model):
    _name = 'facture.facture'
    _description='facture' 
    
    code = fields.Integer(string='code' , required=True , readonly=False)
    payment= fields.Char(string='payment', required=True , readonly=False)
    commande_ids = fields.One2many('commande.commande','facture_id',string='commande')
    caissier_ids = fields.One2many('caissier.caissier','facture_id',string='caissier')
    client_id = fields.Many2one('client.client',string='client')
    
class Caissier (models.Model):
    _name = 'caissier.caissier'
    _description='caissier' 
    
    nom = fields.Char(string='nom', required=True , readonly=False)
    prenom = fields.Char(string='prenom', required=True , readonly=False)
    pos = fields.Char(string='pos', required=True , readonly=False)
    commande_ids = fields.One2many('commande.commande','caissier_id',string='commande')
    facture_id = fields.Many2one('facture.facture',string='facture')            
    
