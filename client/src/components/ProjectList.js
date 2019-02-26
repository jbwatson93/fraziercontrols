import React, { Component } from 'react';
import axios from 'axios'
import Project from './Project';

class ProjectList extends Component {
    state={
        projects: []
    }
    componentDidMount(){
        this.getProjects()
    }
    getProjects = () => {
        axios.get('/api/v1/projects')
            .then((res) => {
                 this.setState({ projects: res.data })
            })
    }
    render() {
        return (
            <div>
                <h1>Projects</h1>
                {this.state.projects.map((project,i)=>(
                    <Project 
                    key={i}
                    name={project.projectname}
                    description={project.description}
                    company={project.company}
                    projectid={project.projectid}/>
                ))}
            </div>
        );
    }
}

export default ProjectList;