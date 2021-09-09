import React, { useState } from 'react'
import {  AppstoreOutlined, DatabaseOutlined } from '@ant-design/icons';
import {Menu} from 'antd'
import {Link} from 'react-router-dom'
import logo from './league2.jpg'



function MainPage(props) {
const [current, setcurrent] = useState('email')  
const handleClick = (e) => {
    setcurrent(e.key)
}
    return (
        <div>
            <div>
                <div style={{
                    position:"fixed",
                    left:0,
                    top:0,
                    width:"15vw",
                }}>
                    <img src={logo} alt="None" style={{
                        objectFit:"contain",
                        width:"80%"
                    }}/>
                </div>
            <Menu onClick={handleClick} selectedKeys={[current]} mode="horizontal" style={{
                justifyContent:"center",
                padding:"5px"
            }}>
               
                <Menu.Item key="mail" icon={<DatabaseOutlined />}>
                <Link to={'/'}>
                Predict
                </Link>
                </Menu.Item>
                <Menu.Item key="app"  icon={<AppstoreOutlined />} onClick={() => window.open('https://www.facebook.com/','_blank')}>
                Some Infos
                </Menu.Item>
            </Menu>
            </div>
        </div>
    )
}

export default MainPage
