class MyClass:
    
    shared_property = "same_value_for_all_instances"

    def __init__(self, instance_property):
       
        self.instance_property = instance_property


instance1 = MyClass("instance1_value")
instance2 = MyClass("instance2_value")


print("instance1 shared property:", instance1.shared_property)
print("instance1 instance property:", instance1.instance_property)
print("instance2 shared property:", instance2.shared_property)
print("instance2 instance property:", instance2.instance_property)
