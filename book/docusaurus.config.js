module.exports = {
  title: 'Physical AI: Humanoid Robotics',
  tagline: 'Learn humanoid robotics from scratch',
  url: 'https://yourusername.github.io',
baseUrl: '/',
  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
 presets: [
  [
    'classic',
    {
      docs: {
        sidebarPath: require.resolve('./sidebars.js'),
        routeBasePath: '/',
      },
      blog: false,
      theme: {
        customCss: require.resolve('./src/css/custom.css'),
      },
    },
  ],
],
  themeConfig: {
    navbar: {
      title: 'Physical AI Robotics',
      logo: {alt: 'Logo', src: 'img/logo.svg'},
      items: [{href: 'http://localhost:8000/docs', label: 'API', position: 'right'}],
    },
    footer: {
      style: 'dark',
      copyright: 'Built for GIAIC Hackathon',
    },
  },
  
};

