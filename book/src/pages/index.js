import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';

export default function Home() {
    const { siteConfig } = useDocusaurusContext();
    return (
        <Layout
            title={siteConfig.title}
            description="Humanoid Robotics Course">
            <main style={{ padding: '40px 20px', textAlign: 'center' }}>
                <h1>{siteConfig.title}</h1>
                <h2>{siteConfig.tagline}</h2>
                <p style={{ fontSize: '18px', marginBottom: '30px' }}>
                    Learn everything about humanoid robotics, from basics to advanced control systems.
                </p>

                <Link
                    to="/docs/intro"
                    style={{
                        display: 'inline-block',
                        padding: '15px 40px',
                        backgroundColor: '#2563eb',
                        color: 'white',
                        textDecoration: 'none',
                        borderRadius: '8px',
                        fontSize: '18px',
                        fontWeight: 'bold',
                        marginRight: '20px'
                    }}
                >
                    📚 Start Learning
                </Link>

                <Link
                    to="/docs/intro"
                    style={{
                        display: 'inline-block',
                        padding: '15px 40px',
                        backgroundColor: '#10b981',
                        color: 'white',
                        textDecoration: 'none',
                        borderRadius: '8px',
                        fontSize: '18px',
                        fontWeight: 'bold'
                    }}
                >
                    🔧 API Docs
                </Link>

                <div style={{ marginTop: '60px', textAlign: 'left', maxWidth: '800px', margin: '60px auto' }}>
                    <h3>What's Inside?</h3>
                    <ul style={{ fontSize: '16px', lineHeight: '2' }}>
                        <li>Introduction to Robotics</li>
                        <li>Humanoid Robotics Basics</li>
                        <li>Physical Systems & Actuators</li>
                        <li>Core Programming for Humanoids</li>
                        <li>AI Integration & Control Systems</li>
                        <li>Movement, Balance & Dynamics</li>
                    </ul>
                </div>
            </main>
        </Layout>
    );
}
