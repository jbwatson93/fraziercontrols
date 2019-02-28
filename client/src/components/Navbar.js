import React, { Component } from 'react';
import { Link } from 'react-router-dom'

class Navbar extends Component {
    render() {
        return (
            <div className="navbar">
                <h1>Frazier Controls</h1>
                
                <Link to='/newproject' className='projectsLink'><h1>New</h1></Link>
                <Link to='/projects' className='projectsLink'><h1>Projects</h1></Link>
                <Link to='/items' className='projectsLink'><h1>Items</h1></Link>
               
            </div>
        );
    }
}

export default Navbar;