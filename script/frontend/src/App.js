import React, { useEffect, useState } from 'react';
import { Bar } from 'react-chartjs-2';
import axios from 'axios';
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from 'chart.js';

// Register the necessary Chart.js components
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

const Analytics = () => {
  const [analyticsData, setAnalyticsData] = useState(null);

  useEffect(() => {
    axios.get('https://approval-ananlytics.onrender.com/api/analytics')
      .then((response) => {
        setAnalyticsData(response.data);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  if (!analyticsData) return <div>Loading...</div>;

  // Data for approval charts
  const extensionistData = {
    labels: ['Approved', 'Not Approved'],
    datasets: [{
      label: 'Extensionist Approval',
      data: [analyticsData.extensionist_approval.approved, analyticsData.extensionist_approval.not_approved],
      backgroundColor: ['green', 'red'],
    }],
  };

  const chairpersonData = {
    labels: ['Approved', 'Not Approved'],
    datasets: [{
      label: 'Chairperson Approval',
      data: [analyticsData.chairperson_approval.approved, analyticsData.chairperson_approval.not_approved],
      backgroundColor: ['green', 'red'],
    }],
  };

  const deanData = {
    labels: ['Approved', 'Not Approved'],
    datasets: [{
      label: 'Dean Approval',
      data: [analyticsData.dean_approval.approved, analyticsData.dean_approval.not_approved],
      backgroundColor: ['green', 'red'],
    }],
  };

  const userData = {
    labels: analyticsData.users.map(user => user.user_name),
    datasets: [{
      label: 'User Reports',
      data: analyticsData.users.map(user => user.total_reports),
      backgroundColor: 'blue',
    }],
  };

  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h2>Approval Analytics</h2>
      <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '20px' }}>
        <div style={{ width: '30%', height: '250px', marginBottom: '20px' }}>
          <h3>Extensionist Approval</h3>
          <Bar 
            data={extensionistData} 
            options={{ 
              responsive: true, 
              maintainAspectRatio: false, 
              height: 300 
            }} 
          />
        </div>

        <div style={{ width: '30%', height: '250px', marginBottom: '20px' }}>
          <h3>Chairperson Approval</h3>
          <Bar 
            data={chairpersonData} 
            options={{ 
              responsive: true, 
              maintainAspectRatio: false, 
              height: 300 
            }} 
          />
        </div>

        <div style={{ width: '30%', height: '250px', marginBottom: '20px' }}>
          <h3>Dean Approval</h3>
          <Bar 
            data={deanData} 
            options={{ 
              responsive: true, 
              maintainAspectRatio: false, 
              height: 300 
            }} 
          />
        </div>
        
        <div style={{ width: '30%', height: '250px', marginBottom: '20px' }}>
          <h3>User Reports</h3>
          <Bar 
            data={userData} 
            options={{ 
              responsive: true, 
              maintainAspectRatio: false, 
              height: 300 
            }} 
          />
        </div>
      </div>
    </div>
  );
};

export default Analytics;
