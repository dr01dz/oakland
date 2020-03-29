from django.db import models


class Order(models.Model):

    rcode = models.CharField(max_length=4, null=True)
    scode = models.CharField(max_length=4, null=True)
    ponum = models.CharField(max_length=20, null=True)

    def __str__(self):

        return f'{self.scode} - {self.rcode} - {self.ponum}'

# ----------------------------------------------------------


class Retailer(models.Model):

    rcode = models.CharField(max_length=4)
    rname = models.CharField(max_length=100)
    slist = models.ManyToManyField('Supplier')

    def __str__(self):

        return f'{self.rcode} - {self.rname}'


class Supplier(models.Model):

    scode = models.CharField(max_length=4)
    sname = models.CharField(max_length=100)

    def __str__(self):

        return f'{self.scode} - {self.sname}'


class Concession(models.Model):

    rcode = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    scode = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    pcode = models.CharField(max_length=20)
    pdesc = models.CharField(max_length=100)
    prbbd = models.DateField(null=True)
    cstart = models.DateField(null=True)
    cend = models.DateField(null=True)

    def __str__(self):

        return f'{self.rcode}, {self.scode}, {self.pcode}, {self.pdesc}, {self.prbbd}, {self.cstart}, {self.cend}'


class ConcessionNote(models.Model):

    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField(null=True)
    note = models.TextField()

    def __str__(self):

        return f'{self.retailer}, {self.supplier}, {self.end}'


class SmallOrder(models.Model):

    retailer = models.ForeignKey(Retailer, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    despatch = models.DateField()
    details = models.TextField()
    attachments = models.FileField()

    def __str__(self):

        return f'{self.retailer}, {self.supplier}, {self.despatch}'
