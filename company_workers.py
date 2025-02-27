# 3rd program
# Company workers dictionary

company_workers={
    "Developers": {
        "Bob":{"age": 28, "role" : "Back_end Developer"},
        "Alice":{"age": 23, "role" : "Front_end Developer"},
        "John":{"age": 25, "role" : "Full_Stack Developer"}
    },
    "Designers":{
        "Jane":{"age": 24, "role" : "UI/UX Designer"},
        "Sam":{"age": 26, "role" : "Graphic Designer"}
    }
}
# Printing the current company workers
print("Current company workers: ", company_workers)

# Adding a worker to the company
company_workers["Developers"]["Ali"]={"age": 28, "role" : "Data Analyst"}

