import React, { Component } from 'react';
import { Link } from 'react-router-dom'

class Project extends Component {
    render() {
        return (
           
            <div className='singleproject'>
                <Link to={`/projects/${this.props.projectid}`} ><h2>{this.props.name}</h2></Link>
                <p>{this.props.description}</p>
            </div>
           
        );
    }
}

export default Project;