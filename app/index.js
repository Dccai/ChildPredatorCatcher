import { View,Text, ScrollView, SafeAreaView,Button,TouchableOpacity,Image,Pressable} from "react-native";
import { Stack,useRouter,Link } from "expo-router";
import { useState } from "react";
import "expo-router/entry";
function HeadButton(props){

return (
<Button onPress={()=>{console.log('hi')}} title={props.name}></Button>
);
}
const Home=()=>{
    let [score,increaseScore]=useState(0);
    const router=useRouter();
 
    return( <SafeAreaView style={{flex:1,backgroundColor:"aliceblue"}}>
        <Stack.Screen options={{headerStyle:{backgroundColor:'red'},headerShadowVisible:true,
        headerLeft:()=>(<HeadButton name="Login"/>), headerRight:()=>(<HeadButton name="Home"/>),headerTitle:""
    }}>
        </Stack.Screen>
        <ScrollView showsVerticalScrollIndicator={false}>
        <View style={{flex:1,padding:"20px"}}>
            <TouchableOpacity style={{width:"100%",height:"100%"}}>
                <Image source={{uri:"https://bgchv.com/wp-content/uploads/2019/08/Safety.jpg"}}  style={{ resizeMode: 'cover', width: '100%', height: '100%' }}/>
            </TouchableOpacity>
            <Text>Your Score: {score}</Text>
            <Button onPress={()=>{increaseScore(a=>a+1)}} title="Click Here"></Button>
            <Link href={{pathname: "/about"}} asChild>
      <Pressable>
        <Text>Home</Text>
      </Pressable>
    </Link>
    <Link href={{pathname: "/reportPotentialThreats"}} asChild>
        <Pressable>
            <Text>Report Suspicious Behaviour</Text>
        </Pressable>
    </Link>
        </View>
        </ScrollView>
    </SafeAreaView>);
}
export default Home;