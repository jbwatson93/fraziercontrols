import React, { Component } from 'react';
import axios from 'axios'
import { Link } from 'react-router-dom'

class Item extends Component {
    state = {
        displayForm:false,
        item:{
            itemNo: '',
            manufacturer: '',
            manufactPartNo:'',
            description: '',
            pipeSize:'',
            HP: '',
            diameter: '',
            length:'',
            width: '',
            height:'',
            voltage:'',
            voltageType:'',
            creationdate:'',
        }
    }

    componentDidMount(){
        this.getItem()
    }
    getItem = () => {
        axios.get(`/api/v1/items/${this.props.match.params.id}`)
            .then((res) => {
                 this.setState({ item: res.data })
                 
            })
    }
    toggleForm = () =>{
        this.setState({displayForm: !this.state.displayForm})
    }
    submitForm = (event) =>{
        event.preventDefault()
        let newitem = {...this.state.item}
        axios.patch(`/api/v1/items/${this.props.match.params.id}/`, newitem)
        this.toggleForm()
        
        
        
    }
    handleChange = (event) => {
        let newitem = { ...this.state.item }
        newitem[event.target.name] = event.target.value
        this.setState({ item: newitem });
    }
    deleteItem = () => {
        axios.delete(`/api/v1/items/${this.props.match.params.id}/`)
            
    }
    
    render() {
        return (
            <div>
                <div className='projectHeader'>
                <h1>{this.state.item.description}</h1>
                <button onClick={this.toggleForm}>Edit Item</button>
                </div>
                <p>Creation Date: {this.state.item.creationdate}</p>
                <p>Item Number: {this.state.item.itemNo}</p>
                <p>Manufacturer: {this.state.item.manufacturer}</p>
                <p>Manufacturer Part Number: {this.state.item.manufactPartNo}</p>
                <p>Pipe Size: {this.state.item.pipeSize}</p>
                <p>HP: {this.state.item.HP}</p>
                <p>Diameter: {this.state.item.diameter}</p>
                <p>Width: {this.state.item.width}</p>
                <p>Heignt: {this.state.item.heignt}</p>
                <p>Voltage: {this.state.item.voltage}</p>
                <p>Voltage Type: {this.state.item.voltageType}</p>
                {this.state.displayForm?<div className='formwrap'>
                <div className='formlayout'> 
                    <input  onChange={this.handleChange} type="text" name='description' placeholder="Description" /> 
                <input  onChange={this.handleChange} type="number" maxLength="5" name='itemNo' placeholder="Item Number" /> 
                <div>
                <input  onChange={this.handleChange}  name='manufacturer' placeholder="Manufacturer" /> 
                <input  onChange={this.handleChange} type="text" name='manufactPartNo' placeholder="Manufact Part Number" /> 
                </div>
                <div>
                <input  onChange={this.handleChange} type="number" name='pipeSize' placeholder="Pipe Size" /> 
                <input  onChange={this.handleChange} type="number" name='HP' placeholder="HP" /> 
                </div>
                <input  onChange={this.handleChange} type="number" name='diameter' placeholder="Diameter" /> 
                <input  onChange={this.handleChange} type="number" name='length' placeholder="Length" /> 
                <input  onChange={this.handleChange} type="number" name='width' placeholder="Width" /> 
                <input  onChange={this.handleChange} type="number" name='height' placeholder="Height" /> 
                <input  onChange={this.handleChange} type="number" name='voltage' placeholder="Voltage" /> 
                <input  onChange={this.handleChange} type="text" maxLength="2" name='voltageType' placeholder="Voltage Type" /> 
                <div>
                 Creation Date: <br/>
                 <input  onChange={this.handleChange} type="datetime-local" name='creationdate'  /> <br />
                 </div>
                
                 <button  onClick={this.submitForm}> Update Item </button>
                 </div>
                     </div>: null}
                     <Link to='/items'>  <button onClick={this.deleteItem}>  Delete  </button></Link> 
            </div>
        );
    }
}

export default Item;