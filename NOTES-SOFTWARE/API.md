## API-Application Presentation Interface:<br>
It is basically a messenger that helps in transportation of data from one location to another OR a script written by an organization to provide its principle working as a service.
### WORKING:<br>
<li> The client sends the request
<li>The server reads the request, validates the authentication.
<li>The server sends the response in the JSON or XML form.
<li>The app or the system displays the recieved data.

## Types of APIs
### 1. Open APIs (Public APIs):<BR>
These APIs are available to **anyone** — developers, businesses, or users — without restrictions (or with minimal signup).<br>
** Key Features:**
- Open access, often with a free or freemium model.
- Used to encourage external innovation and integrations.

### 2. Partner APIs:

These APIs are accessible only to **authorized partners** or third-party developers, often under a legal agreement or contract.

** Key Features:**
- Not public; requires approval or partnership.
- Used to share data with selected collaborators.

** Examples:**
- Zomato Partner API (for restaurants)
- Uber API (for affiliate integrations)

---

### 3. **Internal APIs (Private APIs)**

These APIs are used **within a company or organization**. They are not exposed to external users.

**Key Features:**
- Improves internal software modularity.
- Used for connecting internal tools, microservices, or systems.

**Examples:**
- HR system API connecting to payroll
- Inventory API connecting with internal ERP system

### 4. **Composite APIs**

Composite APIs combine **multiple APIs or services** into a **single call**. Useful for complex operations that need data from several sources.

**Key Features:**
- Reduces number of API calls.
- Improves performance and efficiency.

- # Client-Side APIs vs Server-Side APIs

| Feature                     | Client-Side APIs                                     | Server-Side APIs                                      |
|----------------------------|------------------------------------------------------|--------------------------------------------------------|
| **Definition**             | APIs accessed and run in the user's browser          | APIs built and hosted on a server                     |
| **Executed On**            | Client (browser or frontend)                         | Server (backend)                                      |
| **Languages Used**         | Mostly JavaScript (JS APIs)                          | Node.js, Python, PHP, Java, etc.                      |
| **Examples**               | DOM API, Fetch API, Geolocation API, Canvas API      | REST API, GraphQL API, internal business logic APIs   |
| **Accessed By**            | JavaScript running in browser                        | Frontend apps, mobile apps, third-party systems       |
| **Purpose**                | Interact with browser environment or call servers    | Expose data/services to clients                       |
| **Use of JavaScript APIs** | Yes (e.g., DOM, Fetch, Storage APIs)              | ❌ No (server doesn't use JS APIs like DOM, etc.)     |
| **Use of RESTful APIs**    | Does not define REST APIs, but **calls** them     | ✅ Yes, often implemented as REST APIs                |
| **Data Handling**          | Consumes data from server                            | Provides/serves data to clients                       |
| **Security Scope**         | Limited, runs in browser sandbox                     | Handles authentication, authorization, database access |

