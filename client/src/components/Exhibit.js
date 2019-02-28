import React, { Component } from 'react';
import axios from 'axios'
import { Link } from 'react-router-dom'

class Exhibit extends Component {
    state={
        exhibit: {
           description: ''
             },
        displayForm: false,
        
    }
    componentDidMount(){
        this.getExhibit()
       
    }
    getExhibit = () => {
        axios.get(`/api/v1/exhibits/${this.props.match.params.id}`)
            .then((res) => {
                 this.setState({ exhibit: res.data })
            })
    }
    deleteExhibit = () => {
        axios.delete(`/api/v1/exhibits/${this.props.match.params.id}`)
            
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
        axios.patch(`/api/v1/exhibits/${this.props.match.params.id}/`, newexhibit)
        this.toggleForm()
    }
    render() {
        return (
            <div>
                <div className='projectHeader'>
                <h1>{this.state.exhibit.exhibitName}</h1>
                <button onClick={this.toggleForm}>Update Exhibit</button>
                </div>
                <p>{this.state.exhibit.description}</p>
                <p>Creation Date: {this.state.exhibit.creationDate} </p>
                <p>Desired Turn Over: {this.state.exhibit.desiredTurnover} </p>
                <p>Estimated Gallon Size: {this.state.exhibit.estimatedGal} </p>
                <p>System Flow: {this.state.exhibit.systemFlow} </p>
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
                 <button  onClick={this.submitForm}> Update</button>
                 </div>
                     </div>: null}
             <Link to='/projects'> <button onClick={this.deleteExhibit}>Delete</button></Link>  
            </div>
        );
    }
}

export default Exhibit;