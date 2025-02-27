import {useState} from 'react'

const ContactForm = ({ existingContact = {}, updateCallback}) => {

    const [firstName, setFirstName] = useState(existingContact.firstName || "")
    const [lastName, setLastName] = useState(existingContact.lastName || "")
    const [email, setEmail] = useState(existingContact.email || "")

    // Update or Create Contact
    const updating = Object.entries(existingContact).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            firstName,
            lastName,
            email
        }

        // Convert data to JSON

        const url = "http://127.0.0.1:5001/" + (updating ? `update_contact/${existingContact.id}` : "create_contact")
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }

        const response = await fetch(url, options)

        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        }
        else {
            updateCallback()
        }
    }

    // Return the form jsx
    return <form onSubmit={onSubmit}>
        <div>
            <div> 
                <label htmlFor="firstName"> First Name: </label>
                <input 
                    type="text" 
                    id="firstName" 
                    value={firstName} 
                    onChange={(e) => setFirstName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="lastName"> Last Name: </label>
                <input 
                    type="text" 
                    id="lastName" 
                    value={lastName} 
                    onChange={(e) => setLastName(e.target.value)}
                />
                <label htmlFor="email"> Email: </label>
            </div>
            <div>
                <input 
                    type="text" 
                    id="email" 
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)}
                />
                <button type="submit"> { updating ? "Update" : "Create" } </button>
            </div>
        </div>
    </form> 
}

export default ContactForm