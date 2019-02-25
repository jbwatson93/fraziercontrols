import React, { Component } from 'react';
import { Link } from 'react-router-dom'

class Project extends Component {
    render() {
        return (
            <div>
                <Link to={`/projects/${this.props.projectid}`} ><h1>{this.props.name}</h1></Link>
                <p>{this.props.description}</p>
            </div>
        );
    }
}

export default Project;