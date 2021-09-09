import React, {useState,useEffect} from 'react'
import axios from 'axios'
import styled from 'styled-components'
import {Divider, Row, Col, Button,Typography,Input,Select} from 'antd'
import { SkinOutlined,StarOutlined,CalendarOutlined, PoundCircleOutlined, ReloadOutlined } from '@ant-design/icons'

const {Title,Text} = Typography
const { Option} = Select

const MainContainer = styled.div`
   display : flex;
   justify-content : space-around;
   padding : 10px;
   flex-direction: column;
   &>div{
    padding:5px
   }
`
const SecondaryContainer = styled.div`
display : flex;
   justify-content : space-around;
   padding : 10px;
   padding:10px
`

function DataLabels(props) {
      const [PlayerName, setPlayerName] = useState("")
      const [predicted, setpredicted] = useState(null)
      const [infosToPredict, setinfosToPredict] = useState({
        age:null,
        page_views:null,
        fpl_value:null,
        fpl_points:null,
        region:null,
        new_foreign:null,
        big_club:null,
        new_signing:null,
        nat:null,
        club:null,
        pos:null
      })
    //   useEffect(() => {
    //      console.log(infosToPredict)
    //   }, [infosToPredict])
      const [data, setdata] = useState(null)
      const get_loaded_data = () => {
          axios.get('/get_data').then(res => {
               setdata(res.data)
               console.log(res.data.club)
          }).catch(err => {
              alert("Ooops something went wrong")
          })
      }
      useEffect(() => {
           get_loaded_data()
      }, [])
      function get_predicted_value(){
          const config = {
            headers : {'Content-Type': 'application/json'}
          }
          axios.post('/predict_market_value',JSON.stringify(infosToPredict),config).then(res => {
              setpredicted(res.data)
          }).catch(err => {
              alert("Ooops Something Went wrong")
          })
        console.log(infosToPredict)
      }
  return (
        <MainContainer>
      
            <Title level={3}>{PlayerName}</Title>
            <div style={{
                display:"flex",
                padding:"10px",
                justifyContent:"center"
            }}>
                <div style={{
                    display :"inline-block"
                }}> 
            <Input required placeholder="Enter Players Name" prefix={<SkinOutlined />} value={PlayerName} onChange={(e,v) => setPlayerName(e.target.value)}/>
               </div>
            </div>
             <div>
             <Row justify="space-around" style={{
                 margin:"20px"
             }}>
                 {/**age,page_views,fpl_value,fpl_points,region,new_foreign,big_club,new_signing,nat,club,pos */}
                 <Col span={11}> 
                    <div>
                        <div>
                        <Input required placeholder="Enter Players Age" prefix={<CalendarOutlined />} value={infosToPredict.age} 
                        onChange={(e,v) => setinfosToPredict({...infosToPredict,age:!isNaN(+e.target.value)?+e.target.value:alert("Numbers Only")})}/>
                        <br />
                        <br />
                        <Select  style={{ width: '100%' }} placeholder="Nationality" value={infosToPredict.nat} 
                         onChange={(e,v) => setinfosToPredict({...infosToPredict,nat:v.value})}
                        >
                            {data?.nationality.map((e,i) => {
                                return <Option value={e} key={i}>{e}</Option>
                            })}
                            <Option value={'Other'} key={50}>{'Other'}</Option>
                        </Select>
                        <br />
                        <br />
                        <Select  style={{ width: '100%' }} placeholder="Club" value={infosToPredict.club} 
                         onChange={(e,v) => setinfosToPredict({...infosToPredict,club:v.value})}
                        >
                            {data?.club.map((e,i) => {
                                return <Option value={e} key={i}>{e}</Option>
                            })}
                        </Select>
                        <br />
                        <br />
                        <Select prefix={<StarOutlined />}  style={{ width: '100%' }} placeholder="Big Club?" value={infosToPredict.big_club} 
                         onChange={(e,v) => setinfosToPredict({...infosToPredict,big_club:v.value})}
                        >
                                 <Option  value={0} key={0}>No</Option>
                                 <Option value={1} key={1}>Yes</Option>
                        </Select>
                        </div>
                    </div>
                 </Col>
                 <Divider type="vertical" />
                 <Col span={11}>  
                    <div style={{
                 
                    }}>
                        <Select prefix={<StarOutlined />}  style={{ width: '100%' }} placeholder="position" value={infosToPredict.pos} 
                         onChange={(e,v) => setinfosToPredict({...infosToPredict,pos:v.value})}
                        >
                                {data?.position.map((e,i) => {
                                return <Option value={e} key={i}>{e}</Option>
                            })}
                        </Select>
                        <br />
                        <br />
                        <Select prefix={<StarOutlined />}  style={{ width: '100%' }} placeholder="Region" value={infosToPredict.region} 
                         onChange={(e,v) => setinfosToPredict({...infosToPredict,region:v.value})}
                        >
                                  {[1,2,3,4].map((e,i) => (
                                      <Option value={e} key={i}>{e}</Option>
                                  ))}
                        </Select>
                        <br />
                        <br />
                        <Select prefix={<StarOutlined />}  style={{ width: '100%' }} placeholder="new signing" value={infosToPredict.new_signing} 
                         onChange={(e,v) => setinfosToPredict({...infosToPredict,new_signing:v.value})}
                        >
                                 <Option  value={0} key={0}>No</Option>
                                 <Option value={1} key={1}>Yes</Option>
                        </Select>
                        <br />
                        <br />
                        <Select  prefix={<StarOutlined />}  style={{ width: '100%' }} placeholder="new foreign?" value={infosToPredict.new_foreign} 
                         onChange={(e,v) => setinfosToPredict({...infosToPredict,new_foreign:v.value})}
                        >
                                 <Option  value={0} key={0}>No</Option>
                                 <Option value={1} key={1}>Yes</Option>
                        </Select>
                       </div>
                 </Col>
                 <Divider orientation="center">FPL INFOS</Divider>
                 <Col span={24}>
                     <SecondaryContainer>
                          <div style={{
                              width:"20vw"
                          }}>
                          <Input required placeholder="Page views"  value={infosToPredict.page_views} 
                        onChange={(e,v) => setinfosToPredict({...infosToPredict,page_views:!isNaN(+e.target.value)?+e.target.value:alert("Numbers Only")})}/>
                         </div>
                         <div style={{
                              width:"20vw"
                          }}>
                        <Input required placeholder="Fpl value 1 ~ 14" prefix={<CalendarOutlined />} value={infosToPredict.fpl_value} 
                        onChange={(e,v) => setinfosToPredict({...infosToPredict,fpl_value:e.target.value})}/>
                         </div>
                         <div style={{
                              width:"20vw"
                          }}>
                          <Input required placeholder="Enter FPL points"  value={infosToPredict.fpl_points} 
                        onChange={(e,v) => setinfosToPredict({...infosToPredict,fpl_points:e.target.value})}/>
                          </div>
                     </SecondaryContainer>
                 </Col>
            </Row>
             </div>
             <SecondaryContainer>
             <Button type="primary"  icon={<PoundCircleOutlined size="large"/>} size="large" onClick={get_predicted_value}>Predict Value</Button>
             <Title level={2} type="success">{`${predicted?.estimated_price?predicted.estimated_price:"..."}m `}&#163;</Title>
             <Button type="primary" shape="circle" icon={<ReloadOutlined />}  size="large" onClick={() => window.location.reload()}/>
             </SecondaryContainer>
   
        </MainContainer>
    )
}   

export default DataLabels
