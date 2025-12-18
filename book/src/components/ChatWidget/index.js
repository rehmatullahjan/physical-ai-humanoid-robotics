import React, { useState, useRef, useEffect } from 'react';
import clsx from 'clsx';
import { useHistory } from '@docusaurus/router';
import '../../css/chat.css';

// Simple icons as SVG components
const MessageSquare = () => (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
    </svg>
);

const X = () => (
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <line x1="18" y1="6" x2="6" y2="18"></line>
        <line x1="6" y1="6" x2="18" y2="18"></line>
    </svg>
);

const Send = () => (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <line x1="22" y1="2" x2="11" y2="13"></line>
        <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
    </svg>
);

const API_URL = `http://${typeof window !== 'undefined' ? window.location.hostname : 'localhost'}:8000`;

const SUGGESTIONS = [
    { label: 'Introduction', path: '/docs/intro' },
    { label: 'Humanoid Basics', path: '/docs/humanoid-basics' },
    { label: 'Physical Systems', path: '/docs/physical-systems' },
    { label: 'Programming Core', path: '/docs/programming-core' },
    { label: 'AI Integration', path: '/docs/robot-ai-integration' },
    { label: 'Movement Dynamics', path: '/docs/movement-dynamics' },
];

export default function ChatWidget() {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState([
        {
            role: 'bot',
            content: (
                <div>
                    <p><strong>Hi there! 👋</strong></p>
                    <p>I'm your Physical AI Assistant. I can help you find exact information from the book.</p>
                    <p>You can ask me a question, or jump directly to a chapter below:</p>
                </div>
            )
        }
    ]);
    const [inputValue, setInputValue] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef(null);
    const history = useHistory();

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isOpen]);

    const handleSend = async () => {
        if (!inputValue.trim()) return;

        const userMessage = { role: 'user', content: inputValue };
        setMessages(prev => [...prev, userMessage]);
        setInputValue('');
        setIsLoading(true);

        try {
            const response = await fetch(`${API_URL}/search`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ query: userMessage.content, limit: 3 }),
            });

            const data = await response.json();

            let botContent;
            if (data.results && data.results.length > 0) {
                botContent = (
                    <div>
                        <p>Here is the exact content I found for you:</p>
                        {data.results.map((result, idx) => (
                            <div key={idx} className="source-card">
                                <div className="source-title">📄 {result.title} <span style={{ opacity: 0.6, fontSize: '0.8em' }}>({(result.score * 100).toFixed(0)}% Match)</span></div>
                                <div style={{ whiteSpace: 'pre-line', borderLeft: '2px solid #ddd', paddingLeft: '8px', margin: '4px 0' }}>
                                    {result.content}
                                </div>
                            </div>
                        ))}
                    </div>
                );
            } else {
                botContent = "I couldn't find any relevant sections in the book matching your query.";
            }

            setMessages(prev => [...prev, { role: 'bot', content: botContent }]);
        } catch (error) {
            console.error("Chat error:", error);
            setMessages(prev => [...prev, { role: 'bot', content: "Sorry, I'm having trouble connecting to the book brain right now. Please check if the backend is running." }]);
        } finally {
            setIsLoading(false);
        }
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter') handleSend();
    };

    const handleNavigate = (path) => {
        history.push(path);
        // Optionally close chat on mobile or keep open? Let's keep it open for now but maybe minimize checks
    };

    return (
        <div className="chat-widget-container">
            {isOpen && (
                <div className="chat-window">
                    <div className="chat-header">
                        <h3>Physical AI Assistant</h3>
                        <button className="close-button" onClick={() => setIsOpen(false)} style={{ background: 'none', border: 'none', color: 'white', cursor: 'pointer' }}>
                            <X />
                        </button>
                    </div>
                    <div className="chat-messages">
                        {messages.map((msg, idx) => (
                            <div key={idx} className={clsx('message', msg.role)}>
                                {msg.content}
                            </div>
                        ))}

                        {/* Show suggestions only if it's the start of conversation or requested */}
                        {messages.length === 1 && (
                            <div className="suggestions-grid" style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px', marginTop: '10px' }}>
                                {SUGGESTIONS.map((s) => (
                                    <button
                                        key={s.path}
                                        onClick={() => handleNavigate(s.path)}
                                        style={{
                                            padding: '8px',
                                            borderRadius: '8px',
                                            border: '1px solid #e2e8f0',
                                            background: 'white',
                                            cursor: 'pointer',
                                            fontSize: '0.85rem',
                                            textAlign: 'left',
                                            color: '#475569'
                                        }}
                                        onMouseOver={(e) => e.target.style.background = '#f1f5f9'}
                                        onMouseOut={(e) => e.target.style.background = 'white'}
                                    >
                                        {s.label} →
                                    </button>
                                ))}
                            </div>
                        )}

                        {isLoading && <div className="message bot">Thinking...</div>}
                        <div ref={messagesEndRef} />
                    </div>
                    <div className="input-area">
                        <input
                            type="text"
                            className="chat-input"
                            placeholder="Ask a question..."
                            value={inputValue}
                            onChange={(e) => setInputValue(e.target.value)}
                            onKeyPress={handleKeyPress}
                        />
                        <button className="send-button" onClick={handleSend} disabled={isLoading}>
                            <Send />
                        </button>
                    </div>
                </div>
            )}

            <button className="chat-button" onClick={() => setIsOpen(!isOpen)}>
                {isOpen ? <X color="white" /> : <MessageSquare color="white" />}
            </button>
        </div>
    );
}
