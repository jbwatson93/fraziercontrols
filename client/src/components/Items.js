import React, { Component } from 'react';
import axios from 'axios'
import { Link } from 'react-router-dom'
class Items extends Component {
    state={
        items: []
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



    render() {
        return (
            <div className='itemwrapper'>
                {this.state.items.map((item, i) => {
                    return(
                        <div className='singleitem' key={i}>
                            <Link to={`/items/${item.itemNo}`} ><h3 className=''>{item.description}</h3></Link>
                            
                            <p>{item.manufacturer}</p>
                        </div>
                    )
                })}
            </div>
        );
    }
}

export default Items;