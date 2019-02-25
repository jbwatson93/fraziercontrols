import React, { Component } from 'react';
import axios from 'axios'
import { Link } from 'react-router-dom'
class SingleProject extends Component {
    state={
        project: {
            Exhibits:[]
        },
        displayForm:false,
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
        }
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
        return Promise.resolve(newexhibit)
    }


    render() {
        return (
            <div>
                <div className='projectHeader'>
                <h1>{this.state.project.projectname}</h1>
                <button onClick={this.toggleForm}>New Exhibit</button>
                </div>
                {this.state.displayForm?<div> 
                    <input  onChange={this.handleChange} type="text" name='exhibitName' placeholder="Exhibit Name" /> <br />
                <input  onChange={this.handleChange} type="text" maxLength="5" name='exhibitID' placeholder="Exhibit ID" /> <br />
                <textarea   onChange={this.handleChange} rows='5' name='description' placeholder="Description" /> <br />
                <input  onChange={this.handleChange} type="number" name='desiredTurnover' placeholder="Desired Turnover" /> <br />
                <input  onChange={this.handleChange} type="number" name='estimatedGal' placeholder="Estimated Gallon" /> <br />
                <input  onChange={this.handleChange} type="number" name='systemFlow' placeholder="System Flow" /> <br />
                 Creation Date: <br/>
                 <input  onChange={this.handleChange} type="datetime-local" name='creationDate'  /> <br />
                 <input  onChange={this.handleChange} type="text" name='type' placeholder="Type" /> <br />
                 <button  onClick={this.submitForm}> Create Exhibit </button>
                     </div>: null}
                <div className='exhibitwrapper'> 
                {this.state.project.Exhibits.map((exhibit, i) => {
                    return(
                        <div className='singleExhibit'>
                            <Link to={`/exhibits/${exhibit.exhibitID}`} ><h3 className='exhibitHeader'>{exhibit.exhibitName}</h3></Link>
                            
                            <p>{exhibit.description}</p>
                        </div>
                    )
                })}
                </div>
            </div>
        );
    }
}

export default SingleProject;