import React, { Component } from 'react';
import axios from 'axios'
import { Link } from 'react-router-dom'
class Items extends Component {
    state={
        items: [],
        displayForm: false,
        searched: false,
        search: '',
        item: {
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
        this.getItems()
    }
    getItems = () => {
        axios.get('/api/v1/items')
            .then((res) => {
                 this.setState({ items: res.data })
            })
    }
    toggleForm = () =>{
        this.setState({displayForm: !this.state.displayForm})
    }
    submitForm = (event) =>{
        event.preventDefault()
        let newitem = {...this.state.item}
        axios.post('/api/v1/items/', newitem)
        this.toggleForm()
        
        
        
    }
    // searchLogic =(search) =>{
    //     if(search === ''){
    //         this.getItems()}
    //     else{
            
    //             return(search)
            
            
    //     }
        
    // }
    handleChange = (event) => {
        let newitem = { ...this.state.item }
        newitem[event.target.name] = event.target.value
        this.setState({ item: newitem });
    }
    searchItems= () => {
        const sorted = this.state.items.filter(item => item.description.includes( this.state.search ))
        
          this.setState({items: sorted, searched:true})
        
      }
      sortAgain = () => {
          this.getItems()
          this.setState({searched: false})
      }
      handleChange2 = (event) => {
         const newsearch = event.target.value
        this.setState({ search: newsearch })
        
        
    }

    render() {
        return (
            <div>
                <div className='projectHeader'>
                <h1>Items</h1>
                <div>
                <button onClick={this.toggleForm}>New Item</button>
                </div>
               
                </div>
                <div>
                <div className='searchbar'> {this.state.searched? <button onClick={this.sortAgain}>Search Again</button>:<div >
                    <input onChange={this.handleChange2} type='text' name='search' placeholder='Search'/>
                    <button onClick={this.searchItems}>Search</button>
                    </div> 
                    }</div>
                </div>
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
                
                 <button  onClick={this.submitForm}> Create Item </button>
                 </div>
                     </div>: null}
            <div className='itemwrapper'>
                {this.state.items.map((item, i) => {
                    return(
                        <div className='singleitem' key={i}>
                            <Link to={`/items/${item.itemNo}`} ><h3 className=''>{item.description}</h3></Link>
                            
        
                        </div>
                    )
                })}
            </div>
            </div>
        );
    }
}

export default Items;