const Person=
{
    firstName:'Pavitra',
    lastName:'Nagaral',
    get fullName()
    {
        return `${Person.firstName} ${Person.lastName}`;
    },
    set fullName(value)
    {
        const parts = value.split('');
        this.firstName=parts[0];
        this.lastName=parts[1];
    }

};

//console.log(Person.fullName());
Person.fullName='John Smith';
console.log(Person);