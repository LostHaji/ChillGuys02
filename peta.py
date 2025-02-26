import streamlit as stl
from streamlit_option_menu import option_menu

stl.set_page_config(page_title="Number Theory App", layout="wide")

stl.markdown(
    """
    <div style= "display: flex; justify-content: center ">
        <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdW5pbDFhMjl0dzNieDRycHpjOGRkZHEzOHI3bGU5ZmdhOHFnbTlycCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/dFpXc9idyowth1EiWd/giphy.gif" width="550">
    </div>
    """,
    unsafe_allow_html=True
)

selected_page = option_menu(
    menu_title=None,
    options=["Mathematics", "Chemistry", "Social Sciences"],
    icons=["calculator", "highlighter", "house-door-fill"],
    menu_icon=None,
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#fdb400"},
        "nav-link-selected": {"background-color": "#196b03"},
    }
)

if selected_page == "Mathematics":
    stl.markdown(
        """
        <style>
        body {
            font-family: sans-serif;
            color: #333;
            background-color: #EAE2B7; /* Beige background */
        }
        .big-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #F77F00; /* Red title */
            text-align: center;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 1.8em;
            font-weight: bold;
            color: #F77F00; /* Orange section titles */
            margin-top: 30px;
            margin-bottom: 15px;
            border-bottom: 2px solid #FCBF49; /* Golden Yellow border */
            padding-bottom: 5px;
        }
        .content-text {
            font-size: 1.1em;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .math-formula {
            font-size: 1.2em;
            background-color: #FCBF49; /* Golden Yellow formula background */
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            color: black; /* Text inside formula boxes is black */
        }
        .math-formula strong {
            color: black; /* Make the strong text also black */
        }
        table {
            width: 100%;
            text-align: center;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #F77F00; /* Orange table border */
            padding: 8px;
            color: black; /* Text in table cells is black */
            background-color: white; /* Table cell background is white */
        }
        th {
            background-color: #FCBF49; /* Golden Yellow header background */
            color: black; /* Text in table header is black */
        }
        .video-title {
            font-size: 1.3em;
            font-weight: bold;
            color: #F77F00;
            margin-bottom: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="big-title">Mathematical Field</div>', unsafe_allow_html=True)

    stl.markdown('<div class="section-title">INTRODUCTION</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            In the Philippines, more than 60% of people live in cities. The country’s growing urbanization makes efficient population modeling essential for sustainable development.
            <br><br>
            Population modeling allows urban planners to predict changes in the population and the requirements for allocating resources such as food, housing, and infrastructure. By doing this, the planners assure that resources are available without shortages and sustainable development is maintained. The analysis of the country's population helps in rational planning about the organization and development of the economy, and analyzes the labor supply and its placements.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">MATHEMATICAL FOUNDATION</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            There are many factors for which there may come instances where a community’s population changes. One of the most fundamental factors are the births and deaths of species. By analyzing these two fundamental factors, a simple measure for population change could be achieved:
            <div class="math-formula">
                dN/dt = Birth - Death
            </div>
            Where dN is the change in population and dt is the change in time.
            <br><br>
            This fundamental model lets us analyze the amount of change in population given two time frames as seen in the following example:
            <br><br>
            <table>
                <tr><th>Original Population</th><th>Births</th><th>Deaths</th><th>dN/dt</th></tr>
                <tr><td>1000</td><td>50</td><td>10</td><td>40</td></tr>
                <tr><td>50</td><td>25</td><td>5</td><td>20</td></tr>
            </table>
            <br><br>
            The table illustrates that population growth is influenced not only by births but also by the initial population size. Although the rate of change in population dN/dt doesn't directly predict future populations, it provides insight into how growth relates to the original population. Once dN/dt is determined, the maximum growth rate per capita r<sub>max</sub> can be analyzed through mathematical equations that account for different population growth patterns. By understanding r<sub>max</sub>, it becomes possible to make predictions about future population sizes.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">EXPONENTIAL GROWTH</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            For populations which grow exponentially without being under a restriction, the following formula may be used to find an approximation of r<sub>max</sub> through dN/dt between 2 time frames: (this determines how fast the population is growing)
            <div class="math-formula">
                dN/dt = r<sub>max</sub>N
            </div>
            Additionally, for prediction purposes, we may find the general formula of that model:
            <div class="math-formula">
                dN/N = r<sub>max</sub>dt
            </div>
            Since r<sub>max</sub> will be constant, we may continue integrating both sides. (this determines the population after a given time)
            <div class="math-formula">
                ln(N) = r<sub>max</sub>t
            </div>
            such that e<sup>ln(N)</sup> = e<sup>(C1)(t) + c</sup>, C1 = r<sub>max</sub>
            <br><br>
            And N = (e<sup>(C1)(t)</sup>)(e<sup>c</sup>)
            <br><br>
            Because e<sup>c</sup> is also N<sub>0</sub>, then
            <div class="math-formula">
                N(t) = N<sub>0</sub>e<sup>r<sub>max</sub>t</sup>
            </div>
            Through this new model, approximate predictions may now be calculated for future population sizes.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">LOGISTIC GROWTH</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            A population limited by a carrying capacity cannot continue to grow exponentially, it grows logistically. Only if the carrying capacity is given, use the following logistic growth formula to solve for r<sub>max</sub>:
            <div class="math-formula">
                dN/dt = r<sub>max</sub>N(K-N)/K
            </div>
            For example, a forest might have a carrying capacity that determines how many deer it can support before food and space become limited. If the deer population exceeds this number, competition for resources intensifies, and the population growth slows down or declines.
            <br><br>
            Similarly with the process for prediction in the Exponential Growth, the general formula of the given variable separable differential equations must be found.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Videos
    stl.markdown('<div class="section-title">Example Videos</div>', unsafe_allow_html=True)

    stl.markdown('<div class="video-title">1. Let P(t) be the population (In millions) of a certain city t years after 1995 and suppose that P(t) satisfies the differential equation: P\'(t) = .05 * P(t) P(0) = 2</div>', unsafe_allow_html=True)
    stl.video("https://youtu.be/SkpTQvWchYY")

    stl.markdown('<div class="video-title">2. A bacterial colony starts with 10 bacteria. Under ideal conditions, the population doubles every hour with maximum per capita growth rate of r max = 1.2 per hour. However the environment has limited resources, setting a carrying capacity of K = 1000 bacteria.</div>', unsafe_allow_html=True)
    stl.video("https://youtu.be/mG9arcDRFS8")
elif selected_page == "Chemistry":
    stl.markdown(
        """
        <style>
        body {
            font-family: sans-serif;
            color: #333;
            background-color: #EAE2B7; /* Beige background */
        }
        .big-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #F77F00; /* Red title */
            text-align: center;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 1.8em;
            font-weight: bold;
            color: #F77F00; /* Orange section titles */
            margin-top: 30px;
            margin-bottom: 15px;
            border-bottom: 2px solid #FCBF49; /* Golden Yellow border */
            padding-bottom: 5px;
        }
        .content-text {
            font-size: 1.1em;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .example-box {
            background-color: #FCBF49; /* Golden Yellow example box */
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
            color: black; /* Text inside the boxes is black */
        }
        .example-box strong {
            color: black; /* Make the strong text also black */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Content ---

    stl.markdown('<div class="big-title">Field of Chemsitry</div>', unsafe_allow_html=True)

    stl.markdown('<div class="section-title">Introduction</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            Chemical reactions are fundamental to numerous natural and industrial processes. Their rates are influenced by a variety of factors, including temperature, concentration of reactants, surface area, and the presence of catalysts or inhibitors. Understanding and controlling these factors is critical for optimizing processes across diverse fields, ranging from food preservation and material production to environmental management and industrial safety.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Factors</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            <ul>
                <li><strong>Temperature:</strong> Directly affects reaction rate, microbial growth, and enzyme activity.</li>
                <li><strong>Presence of Catalysts or Inhibitors:</strong> Catalysts speed up, inhibitors slow down reactions.</li>
                <li><strong>Surface Area:</strong> Affects reactions and microbial growth by exposing more to external factors.</li>
                <li><strong>Concentration of Reactants:</strong> Influences spoilage and chemical reaction rates.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Examples</div>', unsafe_allow_html=True)

    stl.markdown(
        '<div class="example-box"><strong>Food Preservation: Preserving Meat by Salting</strong><br>'
        'Temperature: Freezing halts microbial growth.<br>'
        'Inhibitors: Salt inhibits microbial growth.<br>'
        'Surface Area: Ground meat spoils faster.<br>'
        'Concentration: Smoking reduces water.<br>'
        'Result: Prolonged meat preservation.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown(
        '<div class="example-box"><strong>Materials Production: Steel Production</strong><br>'
        'Temperature: Higher temperatures speed up process.<br>'
        'Catalysts: Carbon speeds up process.<br>'
        'Surface Area: Finer ore reacts faster.<br>'
        'Concentration: More oxygen and carbon increase efficiency.<br>'
        'Result: Faster and more efficient steel production.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown(
        '<div class="example-box"><strong>Control of Fire: L.A. Forest Fires</strong><br>'
        'Temperature: Hot, dry climate increases intensity.<br>'
        'Catalysts/Inhibitors: Dry vegetation and winds fuel fires; water and retardants slow them.<br>'
        'Surface Area: Dry vegetation accelerates combustion.<br>'
        'Concentration: High oxygen and fuel sustain fires.<br>'
        'Result: Widespread destruction despite control efforts.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown(
        '<div class="example-box"><strong>Pollution: Sea Pollution</strong><br>'
        'Temperature: Warmer waters speed up pollutant breakdown.<br>'
        'Catalysts: Oil and chemicals worsen pollution.<br>'
        'Surface Area: Microplastics spread pollution faster.<br>'
        'Concentration: More pollutants lead to faster contamination.<br>'
        'Result: Worsening sea pollution.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown(
        '<div class="example-box"><strong>Corrosion: Metal Bar Rusting</strong><br>'
        'Temperature: Higher temperatures speed up rusting.<br>'
        'Catalysts: High humidity provides water.<br>'
        'Surface Area: Scratched metal rusts faster.<br>'
        'Concentration: More oxygen and moisture lead to faster rusting.<br>'
        'Result: Rapid rusting of the bar.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Advanced Chemistry: Overpopulation and Water Pollution</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            Overpopulation drives increased demand, leading to more waste and runoff contaminating water. Contaminants pose health and environmental risks. Solubility is affected by solute/solvent nature, temperature, pressure, and pH.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Examples of Contaminants</div>', unsafe_allow_html=True)

    stl.markdown(
        '<div class="example-box"><strong>Nitrate-Contaminated Water</strong><br>'
        'Source: Fertilizers, sewage.<br>'
        'Solution: Nitrates (NO₃⁻) in water.<br>'
        'Impact: Reduces oxygen transport in blood.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown(
        '<div class="example-box"><strong>Heavy Metal Solutions</strong><br>'
        'Source: Industrial waste, mining.<br>'
        'Solutions: Lead (Pb²⁺), Mercury (Hg²⁺), Cadmium (Cd²⁺) in water.<br>'
        'Impact: Neurological damage, kidney failure, cancer.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown(
        '<div class="example-box"><strong>Phosphate-Contaminated Water</strong><br>'
        'Source: Detergents, fertilizers, sewage.<br>'
        'Solution: Phosphates (PO₄³⁻) in water.<br>'
        'Impact: Eutrophication, oxygen depletion.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown(
        '<div class="example-box"><strong>Pesticides</strong><br>'
        'Source: Agricultural runoff.<br>'
        'Solutions: Organophosphates, Glyphosate in water.<br>'
        'Impact: Cancer, hormonal disruptions.</div>',
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Application to Contaminants</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            <ul>
                <li><strong>Nitrates:</strong> Highly soluble due to ionic nature.</li>
                <li><strong>Heavy Metals:</strong> Solubility varies with pH and complexing agents.</li>
                <li><strong>Phosphates:</strong> Affected by pH and cation presence.</li>
                <li><strong>Pesticides:</strong> Solubility varies with chemical structure and pH.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown(
        """
        <div class="content-text">
            <strong>Organophosphates:</strong> Pesticides, nerve agents. Example: Parathion (C₁₀H₁₄NO₅PS).<br><br>
            <strong>Glyphosate:</strong> Herbicide. Example: C₃H₈NO₅P.
        </div>
        """,
        unsafe_allow_html=True,
    )
elif selected_page == "Social Sciences":
    stl.markdown(
        """
        <style>
        body {
            font-family: sans-serif;
            color: #333;
            background-color: #EAE2B7; /* Beige background */
        }
        .big-title {
            font-size: 2.5em;
            font-weight: bold;
            color: #F77F00; /* Red title */
            text-align: center;
            margin-bottom: 20px;
        }
        .section-title {
            font-size: 1.8em;
            font-weight: bold;
            color: #F77F00; /* Orange section titles */
            margin-top: 30px;
            margin-bottom: 15px;
            border-bottom: 2px solid #FCBF49; /* Golden Yellow border */
            padding-bottom: 5px;
        }
        .content-text {
            font-size: 1.1em;
            line-height: 1.6;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # --- Content ---

    stl.markdown('<div class="big-title">Social Sciences</div>', unsafe_allow_html=True)

    stl.markdown('<div class="section-title">Informative</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            A community’s carrying capacity represents the maximum population size it can support, while overpopulation happens when a community’s population exceeds its carrying capacity. When Overpopulation occurs, it causes the deprivation of resources such as food, water, and shelter. It also causes the increased difficulty for women to access education, healthcare services, and opportunities leading to issues within gender roles.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Argumentative</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            Though, Some argue that Overpopulation doesn't cause issues within gender roles and also claim that it doesn't specifically affect women. Others deny resource scarcity, suggesting it's not a real problem and that technology will always provide solutions, minimizing the effect of overpopulation on women, downplaying the rise of social inequality and portraying poverty and resource management as the only “real” issues. Finally, some confuse concerns about overpopulation with coercive population control, dismissing any discussions about it as anti-women, even when the focus is on empowering women. However, these arguments fail to understand how Overpopulation does affect women, how it exacerbates existing inequalities by straining women from their ability to access basic necessities including reproductive health services, education and limiting their opportunities, hindering them from making informed choices about family planning, creating a loop of poverty and overpopulation placing a heavier burden for women and impacting their health, well-being, and overall quality of life.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Persuasive</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            Furthermore, The arguments caused a series of misunderstandings, disregarding women and their rights. The Reproductive Health Law in the Philippines, while not explicitly addressing the issues overpopulation cause, helps control population growth by encouraging individuals to make better reproductive choices, learn about family planning, reproductive health education, and maternal care, aiming to decrease the issues caused by overpopulation and helping women along the way.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --- Filipino (AP) Content ---

    stl.markdown('<div class="section-title">Impormasyong Pahayag</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            Sa pagdami ng populasyon ng isang pamayanan, nasusubok ang kapasidad nito sa paghawak. Ito ay humahantong sa pag-ubos ng mapagkukunan, labis na pagpuno, at maaaring makaapekto sa iba't ibang aspeto ng buhay, kabilang ang mga tungkulin ng kasarian. Sa mga lugar na napakarami ng tao, ang tradisyunal na mga tungkulin ng kasarian ay maaaring mapalawak habang ang mga tao ay nakikipaglaban para sa limitadong mga mapagkukunan. Halimbawa, ang kakulangan ng mga pasilidad at serbisyo tulad ng pangangalagang pangkalusugan at edukasyon ay nangangahulugan na ang mga kababaihan ang pinakakararanas sa abot ng kanilang maibibigay na kontribusyon sa lipunan. Ang lahat ng mga isyung ito na nakabatay sa kasarian ay mahalaga sa pagtukoy sa mga epekto ng labis na populasyon sa buong mundo.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Mapanghikayat na Pahayag</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            Ang mga suliranin ng sobrang populasyon ay humihiling na tingnan ang balanse ng kasarian tungkol sa kontrol sa populasyon. Sa lumalagong mga pamayanan, ang mga tungkulin ng kasarian ay madaling nasisira, at ang mga kababaihan ay madalas na nahaharap sa mas makabuluhang mga kawalan sa mga labis na crowded na kapaligiran. Ang pagkakapantay-pantay ng kasarian ay maaaring itaguyod sa pamamagitan ng mga diskarte sa napapanatiling paglago ng populasyon, na magsisiguro na ang lahat ng kasarian ay tumatanggap ng pantay na mga mapagkukunan at sa gayon ay makakatulong upang mapanatili ang isang balanseng lipunan. Upang mapagtagumpayan ang gayong paglago, dapat na magkaroon ng pangangailangan para sa pantay na pagpapalakas ng kapangyarihan ng mga kababaihan at kalalakihan upang sila rin ay makapagpapatakbo ng kanilang nagbabago na mga tungkulin nang naaayon.
        </div>
        """,
        unsafe_allow_html=True,
    )

    stl.markdown('<div class="section-title">Argumentatibong Pahayag</div>', unsafe_allow_html=True)
    stl.markdown(
        """
        <div class="content-text">
            Habang ang paglago ng populasyon ay maaaring mapalakas ang pag-unlad ng ekonomiya sa pamamagitan ng paglikha ng isang mas malaking lakas ng trabaho, ang pangangatuwiran na ito ay karaniwang hindi pinapansin ang mapagkukunan at istraktura na strain na maaaring maging sanhi nito. Ang labis na populasyon ay nagpapalakas ng mga isyu na nauugnay sa hindi pagkakapantay-pantay ng kasarian, yamang karaniwan na ang mga grupo na walang pribilehiyo, tulad ng mga kababaihan, ang pinakakaramdam ng pinsala sa mga tuntunin ng mapagkukunan. Bagaman mahalaga ang pag-unlad sa ekonomiya, ang tunay na pag-unlad ay dapat magsimula sa pagsasaalang-alang sa pagkakapantay-pantay ng mga lalaki at babae, pantay na pag-aari ng mga mapagkukunan, at iba pa, na magiging kapaki-pakinabang sa pangmatagalan
        </div>
        """,
        unsafe_allow_html=True,
    )
