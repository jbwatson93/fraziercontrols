import React, { Component } from 'react';
import axios from 'axios'
import { Link } from 'react-router-dom'
import ProjectEdit from './ProjectEdit';
class SingleProject extends Component {
    state={
        project: {
            Exhibits:[],
            projectid:null,
            startdate:null,
            estimatedcompdate:null,
            projectname:null,
            description:null,
            creationdate:null,
            updatedate:null,
            company:null,
            customerid:null,
        },
        displayForm:false,
        displayedit: false,
        exhibit:{
            projectid: this.props.match.params.id,
            exhibitName:"",
            exhibitID:"",
            description:"",
            creationDate:Date,
            desiredTurnover:null,
            estimatedGal:null,
            systemFlow: null,
            type:"",
        },
       
    }
    componentDidMount(){
        this.getProjects()
       
    }
    
    getProjects = () => {
        axios.get(`/api/v1/projects/${this.props.match.params.id}`)
            .then((res) => {
                 this.setState({ project: res.data })
            })
    }
    toggleForm = () =>{
        this.setState({displayForm: !this.state.displayForm})
    }
    handleChange = (event) => {
        let newexhibit = { ...this.state.exhibit }
        newexhibit[event.target.name] = event.target.value
        this.setState({ exhibit: newexhibit });
    }
    submitForm = (event) =>{
        event.preventDefault()
        let newexhibit = {...this.state.exhibit}
        axios.post('/api/v1/exhibits/', newexhibit)
        this.toggleForm()
        this.getProjects()
        return Promise.resolve(newexhibit)
        
        
    }
    deleteProject = () => {
        axios.delete(`/api/v1/projects/${this.props.match.params.id}`)
            
    }
    toggleEdit = () =>{
        this.setState({displayedit: !this.state.displayedit})
    }
    

    render() {
        return (
            <div>
                <div className='projectHeader'>
                <h1>{this.state.project.projectname}</h1>
                <p>{this.state.project.description}</p>
                <div>
                <button onClick={this.toggleForm}>New Exhibit</button>
                <button onClick={this.toggleEdit}>Edit Description</button>
                </div>
                </div>
                
                {this.state.displayedit? <ProjectEdit
                toggleEdit= {this.toggleEdit}
                projectid ={this.props.match.params.id}
                startdate= {this.state.project.startdate}
                estimatedcompdate= {this.state.project.estimatedcompdate}
                projectname= {this.state.project.projectname}
                description= {this.state.project.description}
                creationdate= {this.state.project.creationDate}
                updatedate= {this.state.project.updatedate}
                company= {this.state.project.company}
                customerid= {this.state.project.customerid}
                /> :null }
                
                {this.state.displayForm?<div className='formwrap'>
                <div className='formlayout'> 
                    <input  onChange={this.handleChange} type="text" name='exhibitName' placeholder="Exhibit Name" /> 
                <input  onChange={this.handleChange} type="text" maxLength="5" name='exhibitID' placeholder="Exhibit ID" /> 
                <textarea   onChange={this.handleChange} rows='5' name='description' placeholder="Description" /> 
                <div> 
                <input  onChange={this.handleChange} type="number" name='desiredTurnover' placeholder="Desired Turnover" /> 
                <input  onChange={this.handleChange} type="number" name='estimatedGal' placeholder="Estimated Gallon" /> 
                </div>
                <input  onChange={this.handleChange} type="number" name='systemFlow' placeholder="System Flow" /> 
                <div>
                 Creation Date: <br/>
                 <input  onChange={this.handleChange} type="datetime-local" name='creationDate'  /> <br />
                 </div>
                 <input  onChange={this.handleChange} type="text" name='type' placeholder="Type" /> 
                 <button  onClick={this.submitForm}> Create Exhibit </button>
                 </div>
                     </div>: null}
                <div className='exhibitwrapper'> 
                {this.state.project.Exhibits.map((exhibit, i) => {
                    return(
                        <div className='singleExhibit' key={i}>
                            <Link to={`/exhibits/${exhibit.exhibitID}`} ><h3 className='exhibitHeader'>{exhibit.exhibitName}</h3></Link>
                            
                            <p>{exhibit.description}</p>
                        </div>
                    )
                })}
                </div>
                <Link to='/projects'>  <button onClick={this.deleteProject}>  Delete  </button></Link> 
            </div>
        );
    }
}

export default SingleProject;