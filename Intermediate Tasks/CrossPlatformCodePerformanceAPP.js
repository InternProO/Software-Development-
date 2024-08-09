import { DeviceEventEmitter } from 'react-native';

DeviceEventEmitter.addListener('codePerformance', (metrics) => {
    // Handle real-time code performance metrics
    console.log('Metrics received:', metrics);
});
