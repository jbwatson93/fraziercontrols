import React, { Component } from 'react';
import Navbar from './Navbar';
import { Link } from 'react-router-dom'

class Homepage extends Component {
    render() {
        return (
            <div>
                <Navbar/>
                <div className='homeWrapper'>
                    <div className='viewProjects'>
               <h3 > View all - </h3 > <Link to='/projects' ><h3>  Projects</h3></Link>
                </div> 
                </div>
                <div className='homeWrapper' >
               <div className='viewProjects'>
               <h3 > Create new - </h3 > <Link to='/newprojects' ><h3>  Projects</h3></Link>
                </div>
                </div>
               
              
            </div>
        );
    }
}

export default Homepage;