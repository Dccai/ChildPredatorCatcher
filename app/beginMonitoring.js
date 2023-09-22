import { View,Text, ScrollView, SafeAreaView,Button,TouchableOpacity,Image,Pressable} from "react-native";
import { Stack,useRouter,Link } from "expo-router";
import { useState } from "react";
import TesseractOcr, { LANG_ENGLISH } from 'react-native-tesseract-ocr';
import ViewShot from "react-native-view-shot";
const BeginMonitoring=()=>{
    return(
        <View>
            <Text>Hello My Boi</Text>
        </View>
    );
}
export default BeginMonitoring;