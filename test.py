from IAscrapped import JobDescriptionWriter

writer = JobDescriptionWriter()

# Jobs that actually fit Patrick's profile based on AI_CONTEXT.md
# Mix of: Tech (motion/3D), Operations (store/field mgmt), and Hybrid roles

job_descriptions = [
    # TECH TRACK: Motion/3D Focus
    """
Senior Frontend Engineer - Motion & 3D Systems
Company: Stripe (Design Systems)
Location: San Francisco, CA (Remote-friendly)

Stripe is building next-generation payment interfaces. We need someone who can architect 
motion systems and 3D web experiences that feel alive and performant at scale.

Requirements:
- 6+ years React/frontend experience
- Deep expertise in GSAP, Three.js, WebGL, or similar
- Proven shipped work (not just portfolio pieces)
- Can mentor engineers on animation/performance best practices
- Comfortable with fast shipping and iteration

What we're solving:
- High-performance animation systems for financial interfaces
- Real-time data visualization with WebGL
- Design system component architecture
- Complex interactive experiences that don't sacrifice performance

Why you'd fit: You've shipped GSAP/Three.js systems, understand quality at scale, 
can teach others, and refuse mediocre code.
""",

    # TECH TRACK: Full-Stack with Animation
    """
Full-Stack Engineer - Interactive Data Visualization
Company: Figma
Location: San Francisco, CA (Remote)

Figma is hiring for our multiplayer canvas rendering team. We need engineers who can 
build high-performance interactive systems with beautiful motion and real-time updates.

Requirements:
- 7+ years full-stack development
- Expert in React, WebGL/Canvas, or 3D graphics
- Experience with real-time systems and performance optimization
- Shipped production work with complex animations
- Can own projects end-to-end and mentor others

What you'll do:
- Build rendering pipeline for complex 3D scenes
- Optimize performance for real-time collaboration
- Design animation systems for UI/data visualization
- Lead technical decisions and architecture

Why you'd fit: ScrollStudio3D, AURELIAN, Singularity prove you can architect complex 
systems. You understand performance. You ship quality.
""",

    # OPS TRACK: Store/Retail Leadership
    """
Store Manager - Expansion & Scaling
Company: REI (Retail Leadership)
Location: San Diego, CA (Local - HQ nearby)

REI is opening new flagship stores in CA. We need an experienced Store Manager who can 
launch operations, build teams, and drive revenue while maintaining our quality culture.

Requirements:
- 5+ years store management experience
- Proven track record increasing revenue and reducing shrink
- Can build and lead 15-20 person teams
- Strong vendor relationships and operational excellence
- Local to San Diego area preferred

What you'll do:
- Launch new store from ground zero
- Hire, train, and develop management team
- Build customer loyalty programs
- Optimize operations for profitability and customer experience
- Drive revenue growth through strategic merchandising

Why you'd fit: Leslie's Pool proved you can increase revenue 15% YOY, manage teams, 
and deliver operational excellence. Pat's Pools shows you can scale from zero. 
You understand SOP, vendor management, and team training.
""",

    # OPS TRACK: Operations Manager (Field Service)
    """
Operations Manager - Field Service Scaling
Company: Yelp (Service Professionals Network)
Location: San Diego, CA (Hybrid)

We're scaling a field service network across CA. We need an experienced Ops Manager who 
can manage 50+ service professionals, optimize routing, and maintain quality standards.

Requirements:
- 5+ years operations/field service management
- Experience managing distributed teams
- Proven ability to scale operations
- Strong vendor/partner management
- Data-driven approach to optimization

What you'll do:
- Manage field service team (50+ technicians)
- Optimize routing, scheduling, and resource allocation
- Train and coach team on quality/safety standards
- Build SOPs and operational processes
- Drive customer satisfaction and retention

Why you'd fit: Pat's Pools scaled to 90+ weekly services—you know field ops. 
Leslie's proved you can manage teams and increase revenue. You're an operations person 
with proven scaling ability and obsession with quality.
""",

    # HYBRID TRACK: Tech Operations/Technical Leadership
    """
Technical Operations Manager - Growth Stage Startup
Company: Phantom (Solana Infrastructure)
Location: San Diego, CA (Hybrid)

Phantom is building developer tools for Solana. We need someone who can bridge 
engineering and operations—shipping fast while maintaining code quality and team health.

Requirements:
- 5+ years full-stack development
- 2+ years technical team leadership
- Experience with crypto/blockchain (Solana preferred)
- Obsessive about code quality and shipping
- Can manage both technical and operational challenges

What you'll do:
- Lead 5-person engineering team
- Architect technical infrastructure for developer tools
- Own product shipping and quality standards
- Build operational processes for a scaling startup
- Work directly with founders on strategy

Why you'd fit: Your background combines deep technical skills (React, Three.js, Node), 
operations expertise (Pat's Pools, Leslie's), and blockchain knowledge (trading systems, 
on-chain analytics). You understand both sides—can code AND manage operations.
""",

    # HYBRID TRACK: Freelance → Full-Time (Custom Systems)
    """
Lead Technical Architect - Custom Systems & Operations
Company: Private Growth Company (Series A)
Location: San Diego, CA (Local)

We're a scaling services company looking for someone who can build custom technical 
systems to streamline operations AND lead technical/operational teams.

Requirements:
- 6+ years full-stack development + 3+ years operations experience
- Can architect systems from scratch (not just code)
- Comfortable with both technical and people leadership
- Obsessed with quality and reliability
- Understands business metrics (revenue, costs, ROI)

What you'll do:
- Design and build internal tools for operations (dispatch, scheduling, invoicing)
- Lead 3-5 person technical team
- Optimize operations through automation and process improvement
- Own both technical and operational outcomes
- Guide company scaling decisions

Why you'd fit: This is literally your superpower. You've been freelance (building systems), 
scaled a business (Pat's Pools), and managed operations at scale (Leslie's). You're a 
rare combination of hardcore engineer + operations expert.
""",
]

print("=" * 100)
print("INDEED AI - TARGETED JOB SEARCH")
print("Based on: Patrick Dunn's AI_CONTEXT.md Profile")
print("=" * 100)
print()

for i, job_desc in enumerate(job_descriptions, 1):
    print(f"\n{'='*100}")
    print(f"OPPORTUNITY {i}")
    print(f"{'='*100}")
    print(job_desc)
    print()
    print("GENERATING TAILORED COVER LETTER...")
    print("-" * 100)
    
    try:
        letter = writer.compose_presentation_letter(job_desc)
        print(letter)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("-" * 100)
    print()

print("\n" + "=" * 100)
print("Job categories represented:")
print("1. Tech (Motion/3D) - Stripe Design Systems")
print("2. Tech (Full-Stack/Interactive) - Figma Rendering")
print("3. Operations (Retail) - REI Store Manager")
print("4. Operations (Field Service) - Yelp Service Network")
print("5. Hybrid (Tech + Ops) - Phantom Solana")
print("6. Hybrid (Custom Systems) - Private Growth Company")
print("=" * 100)
