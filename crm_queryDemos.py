# 1. Return all customers from customers table
customers = Customer.objects.all()

# 2. Returns first customer in table
first_customer = Customer.objects.first()

# 3. Returns last customer in table
last_customer =  Customer.objects.last()

# 4. Returns single customer by name
customer_by_name = Customer.objects.get(name="John Doe")

# 5. Returns single customer by id
customer_by_id = Customer.objects.get(id=1)

# 6. Returns all orders related to customer
firstCustomer = Customer.objects.first()
firstCustomer.order_set.all() # order = Order in order_set

# 7. Returns orders customer name
oder = Order.objects.first()
name = oder.customer.name

# 8. Returns products from products table with value of 'Out Door'
products = Product.objects.filter(category="Out Door")

# 9. Order / Sort Objects by id
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')

# 10. Returns all products with tag of 'Sport' (Query Many to Many)
productsFiltered = Product.objects.filter(tag__name='Sport')

# 11. Returns the total count of item ordered
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

# 12. Returns the total count of each item ordered
allOrder = {}

for order in firstCustomer.order_set.all():
    if order.product.name in allOrders:
        allOrders[order.product.name] += 1
    else:
        allOrders[order.product.name] = 1

# example returns: allOrders: {'Ball': 2, 'BBQ Grill':1}


# RELATED EXAMPLES
class ParentModel(models.Model):
    name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
    parent = models.ForeignKey(ParentModel)
    name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
# Returns all child models related to parent
parent.childmodel_set.all()