import { useState, useEffect } from 'react'
import ContactList from './ContactList'
import ContactForm from './ContactForm'
import './App.css'

function App() {

  // We need to fetch the contacts from the server
  // We will use the useState hook to store the contacts in an empty list
  const [contacts, setContacts] = useState([]) 
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentContact, setCurrentContact] = useState({})


  // As soon as the component is rendered we will call the fetchContacts function

  useEffect(() => {

    fetchContacts()

  }, [])

  const fetchContacts = async () => {
    // Fetch API to make request to server
    const response = await fetch("http://127.0.0.1:5001/contacts")

    // Once a response is received we need to convert it to JSON
    const data = await response.json()

    setContacts(data.contacts)
    console.log(data.contacts)
  }

  const closeModal = () => {

    setIsModalOpen(false)
    setCurrentContact({})

  }

  const openCreateModal = () => {
    if(!isModalOpen) {
      
      setIsModalOpen(true)

    }
  }

  const openEditModal = (contact) => {
    if(isModalOpen) return

    setCurrentContact(contact)
    setIsModalOpen(true)

  }

  const onUpdate = () => {
    closeModal()
    fetchContacts()
  }

  return (
   <>
    <ContactList contacts={contacts} updateContact={openEditModal} updateCallback={onUpdate}/>
    <button onClick={openCreateModal}> Create New Contact </button>
    {
      isModalOpen && <div className="modal"> 
        <div className="modal-content"> 
          <span className="close" onClick={closeModal}>&times;</span> 
          <ContactForm existingContact={currentContact} updateCallback={onUpdate}/>
        </div>  
      </div>
    }
  </>)  

}

export default App
