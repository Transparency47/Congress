# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2520?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2520
- Title: All Aboard Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2520
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-01-15T07:03:32Z
- Update date including text: 2026-01-15T07:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2520",
    "number": "2520",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "All Aboard Act of 2025",
    "type": "S",
    "updateDate": "2026-01-15T07:03:32Z",
    "updateDateIncludingText": "2026-01-15T07:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-07-29T21:06:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-29",
      "state": "VT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "DE"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MD"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2520is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2520\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Markey (for himself, Mr. Sanders , Mr. Padilla , Mr. Murphy , Mr. Blumenthal , Ms. Warren , Ms. Blunt Rochester , Mr. Van Hollen , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish a State rail formula grant program, to direct the Federal Railroad Administration to create a Green Railroads Fund, to expand passenger rail programs, to address air quality concerns, to establish rail workforce training centers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the All Aboard Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administration**\nThe term Administration means the Federal Railroad Administration.\n**(2) Administrator**\nThe term Administrator means the Administrator of the Federal Railroad Administration.\n**(3) Amtrak**\nThe term Amtrak means the National Railroad Passenger Corporation.\n**(4) Electrification infrastructure**\nThe term electrification infrastructure \u2014\n**(A)**\nmeans overhead wire in-motion charging technology and any associated infrastructure necessary for the operation to propel a locomotive or train; and\n**(B)**\nincludes battery electric technology that propels a locomotive or train in railyards and other environments in which catenary infrastructure is difficult to deploy as determined by the Secretary.\n**(5) Environmental justice community**\nThe term environmental justice community means a community with significant representation of individuals of color, low-income individuals, or Tribal and Indigenous individuals, that experiences, or is at risk of experiencing, higher or more adverse human health or environmental effects.\n**(6) Federal-State Intercity Partnership program**\nThe term Federal-State Intercity Partnership program means the grant program developed and implemented by the Secretary pursuant to section 24911(b) of title 49, United States Code.\n**(7) High-performance rail service**\nThe term high-performance rail service means an intercity passenger rail service that is designed to meet the current and future market demand for the transportation of people and goods, in terms of capacity, travel times, reliability, and efficiency.\n**(8) Locomotive**\nThe term locomotive has the meaning given that term in section 1033.901 of title 40, Code of Federal Regulations.\n**(9) MU locomotive**\nThe term MU locomotive , with respect to electric multiple unit and battery-electric multiple unit trains, has the meaning given that term in section 229.5 of title 49, Code of Federal Regulations.\n**(10) Partnership applicant**\nThe term partnership applicant has the meaning given that term applicant in section 24911 of title 49, United States Code.\n**(11) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(12) State**\nThe term State means a State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, Guam, American Samoa, the Commonwealth of the Northern Mariana Islands, the United States Virgin Islands, the Federated States of Micronesia, the Republic of the Marshall Islands, or the Republic of Palau.\n**(13) Train**\nThe term train has the meaning given that term in section 221.5 of title 49, Code of Federal Regulations.\n**(14) Zero-emission locomotive**\nThe term zero-emission locomotive means a locomotive that does not emit any criteria pollutant, toxic pollutant, or greenhouse gas from any onboard source of power at any power setting, including any propulsion power that is connected to and moves with the locomotive when it is in motion.\n#### 3. State rail formula funding\n##### (a) In general\nThe Secretary shall establish a formula grant program under which the Secretary shall award grants to States for the development of State rail plans, operations of rail service, and maintenance and expansion of rail infrastructure.\n##### (b) Report required\nEach State that receives a grant under this section shall submit to the Secretary a report describing how the State rail plan and activities\u2014\n**(1)**\ninclude a strategy\u2014\n**(A)**\nto expand passenger rail service, particularly high-performance rail service, including new routes, existing routes identified by the department of transportation of the State, and routes selected under the Corridor Identification and Development Program established under section 25101 of title 49, United States Code; and\n**(B)**\nto electrify existing freight and passenger rail; and\n**(2)**\nwill demonstrate progress towards the goals described in subsection (c).\n##### (c) Goals\nThe goals described in this subsection are\u2014\n**(1)**\nto support the goal of achieving zero-emission locomotives by 2047;\n**(2)**\nto guarantee the national rail network has the capacity to serve a significant portion of freight and passenger movement along the current and projected highest trafficked intercity corridors by 2050;\n**(3)**\nto achieve zero emissions for\u2014\n**(A)**\n50 percent of all trains by 2030;\n**(B)**\nall new trains by 2035; and\n**(C)**\nall locomotives by 2047;\n**(4)**\nto reconnect communities divided by railroads through infrastructure improvements that expand freight and passenger rail capacity;\n**(5)**\nto protect the safety and health of rail workers and nearby communities;\n**(6)**\nto ensure current and future rail infrastructure is climate resilient;\n**(7)**\nto realize high-quality service that is trip-time competitive with other intercity travel options; and\n**(8)**\nto facilitate a viable mode shift from short-haul flights to passenger rail between targeted city pairs.\n##### (d) Use of funds\nA State awarded a grant under this section may use funds from such grant to advance rail planning and operations by\u2014\n**(1)**\nhiring and retaining staff;\n**(2)**\npooling funds with other States to advance interstate initiatives and projects;\n**(3)**\nmaking improvements to existing rail infrastructure;\n**(4)**\nconstructing new rail infrastructure;\n**(5)**\ncarrying out such other rail activities as the Secretary determines appropriate, including studying the impacts on freight rail operations and ridership and operations coordination;\n**(6)**\noperating intercity passenger rail service; and\n**(7)**\npreparing applications for competitive Federal grant programs.\n##### (e) Formula\nIn allocating grant funds among the States, the Administrator shall\u2014\n**(1)**\nensure that each State receives not less than $5,000,000, annually over a 5-year period; and\n**(2)**\ndetermine a method of apportionment that fairly distributes funds based on the existing and future demand for rail service in a State.\n##### (f) Technical assistance\nThe Administrator, in coordination with the Administrator of the Environmental Protection Agency, the Secretary of Energy, Amtrak, and the Administrator of the Federal Transit Administration, shall provide technical assistance to States and communities to assist with the development of State rail plans.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary $3,500,000,000 for the 5-year period beginning on October 1, 2025, to provide grants under this section.\n#### 4. Green Railroads Fund\n##### (a) In general\nThe Secretary, in consultation with the Administrator of the Environmental Protection Agency, may award competitive grants to eligible entities described in subsection (c) to enable or improve electrified rail operations.\n##### (b) Application\n**(1) In general**\nTo apply for a grant under this section an eligible entity shall submit an application to the Secretary in such manner as the Secretary may reasonably require.\n**(2) Requirements**\nEach application submitted in accordance with paragraph (1) shall include\u2014\n**(A)**\na plan for robust engagement that details a public notice process that requires\u2014\n**(i)**\nnotification online and in relevant print sources written in languages used within the area reasonably affected by the proposed grant;\n**(ii)**\nopportunities for public meetings and comment; and\n**(iii)**\nother information relevant to the project to be made publicly available;\n**(B)**\na plan that details how\u2014\n**(i)**\nthe project will safeguard or improve the local environment and public health; and\n**(ii)**\nenvironmental and public health stressors will be monitored and minimized during the project;\n**(C)**\na description of wage and apprenticeship requirements for individuals employed to construct, operate, and maintain rail electrification infrastructure; and\n**(D)**\na transition plan that examines the impact of the proposed project on the workforce of the eligible entity, including\u2014\n**(i)**\nidentifying skills gaps, training needs, and retraining needs of the workforce;\n**(ii)**\na plan to operate and maintain infrastructure of the project using existing insourced workforce;\n**(iii)**\na plan to avoid displacement of the workforce and to transition any displaced workers to new jobs created by the project;\n**(iv)**\nidentifying the steps the eligible entity will take to offset any identified negative impact or potential displacement of the workforce, including how the entity will use the funds from the grant and its own funding to implement the transition plan; and\n**(v)**\na description of how the eligible entity will work with any organizations representing the workforce to implement the transition plan.\n##### (c) Eligible entities\nAn eligible entity described in this subsection is any of the following:\n**(1)**\nA State.\n**(2)**\nA group of States.\n**(3)**\nAn interstate compact.\n**(4)**\nA public agency or a publicly chartered authority established by one or more States.\n**(5)**\nA political subdivision of a State.\n**(6)**\nAmtrak or any other rail carrier that provides intercity rail passenger transportation.\n**(7)**\nA class I railroad in partnership with at least 1 of the entities described in paragraphs (1) through (5).\n**(8)**\nA class II or III railroad.\n**(9)**\nA Federally recognized Indian Tribe.\n**(10)**\nA rail equipment manufacturer in partnership with at least 1 of the entities described in paragraphs (1) through (5).\n**(11)**\nA public utility.\n**(12)**\nA nonprofit labor organization representing a class or craft of employees of rail carriers or rail carrier contractors.\n##### (d) Use of funds\nAn eligible entity awarded a grant under this section may use funds from such grant\u2014\n**(1)**\nto purchase railroad lines and right of way from other railroads that host Amtrak or other intercity passenger rail transportation for new electrification infrastructure;\n**(2)**\nto rebuild or improve existing locomotives, trains, or MU locomotives to enable such trains and locomotives to use electrification infrastructure;\n**(3)**\nto install or improve existing rail electrification infrastructure;\n**(4)**\nto build new rail corridors with electrification infrastructure;\n**(5)**\nto update rail yards by adding electrification infrastructure;\n**(6)**\nto lease or acquire an easement along a right of way for electrification infrastructure;\n**(7)**\nto purchase or lease electric locomotives, MU locomotives, and trains or rolling stock;\n**(8)**\nto ensure new electrification infrastructure is climate resilient;\n**(9)**\nto engage in robust engagement with communities; and\n**(10)**\nfor workforce development and training to support the maintenance, deployment, and operation of electric locomotives, MU locomotives, and trains.\n##### (e) Labor requirements\n**(1) In general**\nA project funded by a grant awarded under this section shall\u2014\n**(A)**\nuse project labor agreements;\n**(B)**\nuse enforceable agreements to hire from local communities; and\n**(C)**\nfor any freight train or light engine used in connection with the movement of freight, require a crew consisting of at least 2 individuals, one of whom is certified under regulations promulgated by the Administration as a locomotive engineer pursuant to section 20135 of title 49, United States Code, and the other of whom is certified under regulations promulgated by the Administration as a conductor pursuant to section 20163 of title 49, United States Code.\n##### (f) Priority\nIn awarding grants under this section, the Secretary shall give priority to projects that will\u2014\n**(1)**\nreduce air pollution in environmental justice communities to yield measurable health benefits where air pollutants include particulate matter, nitrogen oxides, and other criteria air pollutants, hazardous air pollutants, and volatile organic compounds; and\n**(2)**\nexpand high performance passenger rail.\n##### (g) Benefits for other programs\nAn eligible entity that receives a grant under this section and is eligible for other rail grant programs described by this Act shall receive priority for additional funding under such programs for rail electrification infrastructure projects. Entities awarded grants under other programs in this Act may be awarded a grant under this section when applicable.\n##### (h) Study on transmission co-Location with rail electrification infrastructure\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary, in coordination with the Administrator, and in consultation with the Department of Energy, the Federal Energy Regulatory Commission, and any other agency deemed relevant by the Secretary and the Administrator, shall conduct a study to evaluate the feasibility, benefits, equity impacts, and challenges of co-locating electric transmission infrastructure within the same right-of-way or adjacent to rail corridors as part of efforts to minimize land use, streamline permitting processes, support rail electrification, expand renewable energy capacity, reduce community impacts of new infrastructure, improve safety, and ensure fair access to infrastructure benefits for all communities.\n**(2) Outcomes and recommendations**\n**(A) Interagency task force**\nIn carrying out the study required under paragraph (1), the Secretary may recommend the establishment of an interagency task force to facilitate ongoing coordination among Federal, state, and local, and private entities to advance projects involving transmission and rail electrification infrastructure.\n**(B) Designated priority corridors**\nIn carrying out the study required under paragraph (1), the Secretary may\u2014\n**(i)**\npropose a framework to designate priority corridors for co-located transmission and rail electrification projects; and\n**(ii)**\nrecommend how such projects should be incentivized.\n##### (i) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary $50,000,000,000 for the 5-year period beginning on October 1, 2025, to provide grants under this section.\n#### 5. Expansion of passenger rail and high-performance rail\n##### (a) Federal-State Intercity Partnership program\n**(1) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary for the Federal-State Intercity Partnership program $80,000,000,000 for the 5-year period beginning on October 1, 2025.\n**(2) Priority high-performance rail**\nSection 24911(d) of title 49, United States Code, is amended\u2014\n**(A)**\nby redesignating paragraphs (1) through (3) as paragraphs (2) through (4), respectively; and\n**(B)**\nby inserting before paragraph (2), as redesignated, the following:\n(1) the Secretary shall give priority to projects that install or upgrade infrastructure that will enable high-performance passenger rail along new or existing rail corridors regardless of the location of such projects within the United States; .\n**(3) Cost benefit analysis**\nSection 24911(d)(3)(B)(i) of title 49, United States Code, as redesignated, is amended\u2014\n**(A)**\nin subclause (IV), by striking ; and and inserting a semicolon;\n**(B)**\nin subclause (V), by inserting and after the semicolon at the end; and\n**(C)**\nby adding at the end the following:\n(VI) anticipated positive impacts of the project's efforts to electrify the corridor, or make improvements to allow for electrification infrastructure (as defined in the All Aboard Act of 2025 ) in the future; .\n##### (b) Consolidated Rail Infrastructure and Safety Improvement Program\n**(1) Authorization of appropriations**\nThere is authorized to be appropriated to the Secretary $30,000,000,000 for the 5-year period beginning on October 1, 2025, to provide grants authorized under section 22907 of title 49, United States Code.\n**(2) Expanded eligibility**\nSection 22907(b) of title 49, United States Code, is amended by adding at the end the following:\n(14) A Class I railroad company only if\u2014 (A) the entity uses the funds to install electrification infrastructure; (B) the project uses project labor agreements; (C) the project includes enforceable agreements to hire from local communities; (D) the entity complies with section 22404 of title 49, United States Code; and (E) the project is in partnership with at least 1 of the entities described in paragraphs (1) through (5). .\n**(3) Eligible activities**\nSection 22907(c) of title 49, United States Code, is amended by adding at the end the following:\n(17) Any project to facilitate zero-emission locomotive infrastructure, including projects\u2014 (A) to electrify publicly-owned or Amtrak-owned routes; (B) to rehabilitate or improve existing locomotives, MU locomotives, or trains (including engines) to reduce emissions; (C) to purchase railroad infrastructure and right of way from freight railroads\u2014 (i) to expand passenger rail or regional rail; or (ii) with the intent to electrify rail in the future; (D) to build electrified rail corridors; (E) to electrify rail yards; (F) to lease or acquire an easement along a right-of-way for electrification; (G) to purchase electrification equipment and rolling stock or other zero-emission locomotives, MU locomotives, and equipment; (H) to ensure new electrification infrastructure is climate-resilient; and (I) to engage in robust engagement with communities impacted by any new rail infrastructure. .\n**(4) Requirements**\nSection 22907(d) of title 49, United States Code, is amended to read as follows:\n(d) Application process (1) In general The Secretary shall prescribe the form and manner of filing an application under this section. (2) Workforce development requirements Each application for a grant under this section shall include a transition plan that examines the impact of the proposed project on the workforce of the eligible entity and includes\u2014 (A) an identification of skills gaps, training needs, and retraining needs of the workforce; (B) a plan to operate and maintain infrastructure of the project using existing insourced workforce; (C) a plan to avoid displacement of the workforce; (D) an identification of the steps the eligible entity will take to offset any identified negative impact or potential displacement of the workforce, including how the entity will use the funds from the grant and its own funding to implement the transition plan; and (E) a description of how the eligible entity will work with any organizations representing the workforce to implement the transition plan. (3) Requirements for rail electrification projects Each application for a grant for an eligible project described under subsection (c)(17) shall include\u2014 (A) plans for robust engagement, early in the project planning process, with communities impacted by any new rail electrification infrastructure; (B) plans for hiring from local communities, displaced rail workers, tribal and indigenous communities, and environmental justice communities; and (C) a description of wage and apprenticeship requirements for individuals employed to construct, operate, and maintain rail electrification infrastructure. .\n**(5) Priority for rail electrification**\nSection 22907(e) of title 49, United States Code, is amended\u2014\n**(A)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively; and\n**(B)**\nby inserting after paragraph (1) the following:\n(2) Priority for rail electrification In selecting a recipient of a grant for an eligible project, the Secretary shall give priority to a proposed project that includes electrification infrastructure (as defined in the All Aboard Act of 2025 )\u2014 (A) in freight railyards or corridors in environmental justice communities; and (B) along new or existing rail corridors. .\n##### (c) Amtrak\n**(1) In general**\nThere is authorized to be appropriated to the Secretary $30,000,000,000 for the 5-year period beginning on October 1, 2025, for the use of Amtrak.\n**(2) Climate resilience fund**\nOf the funds appropriated to the Secretary pursuant to paragraph (1), $5,000,000,000 shall be used for climate resiliency improvement projects to increase resiliency against climate-related changes in conditions, including flooding risk, sea level rise, extreme storms, coastal erosion, and extreme temperatures.\n##### (d) Railroad crossing elimination program\nThere is authorized to be appropriated to the Secretary $10,000,000,000 for the 5-year period beginning on October 1, 2025, to provide grants under section 22909 of title 49, United States Code.\n##### (e) Restoration and enhancement program\nThere is authorized to be appropriated to the Secretary $1,000,000,000 for the 5-year period beginning on October 1, 2025, to provide grants under section 22908 of title 49, United States Code.\n##### (f) Grant adjustment To support rail expansion\nSection 24305 of title 49, United States Code, is amended by adding at the end the following:\n(g) Use of Federal grant funds Unless specifically prohibited by law or inconsistent with a grant agreement pursuant to which the relevant funding was provided, Amtrak or States may use grant funding received from the Federal Government to cover any non-Federal share of costs required to be paid under grant programs authorized in title 23 or 49, United States Code, or in other Federal laws, to the extent necessary to advance critical intercity passenger rail investments. .\n##### (g) Railway-Highway crossings\nSection 130(e)(1) of title 23, United States Code, is amended\u2014\n**(1)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (C) and (D), respectively; and\n**(2)**\nby inserting after subparagraph (A) the following:\n(B) Installation of protective devices At least \u00bd of the funds set aside each fiscal year under subparagraph (A) shall be available for the installation of protective devices at railway-highway crossings. .\n#### 6. Rail air pollution grant program\n##### (a) In general\nThe Administrator of the Environmental Protection Agency shall establish a program to provide grants under sections 103 and 105 of the Clean Air Act (42 U.S.C. 7403 and 7405) to address the air pollution generated by railyards.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Administrator of the Environmental Protection Agency $500,000,000 for the 5-year period beginning on October 1, 2025, to provide grants under section 105 of the Clean Air Act ( 42 U.S.C. 7405 ) to carry out subsection (a).\n#### 7. Labor protections and workforce development\n##### (a) Grant conditions\nSubsections (a), (c), and (d) of section 22905 of title 49, United States Code, shall apply to any grant awarded pursuant to this Act, or funds provided under this Act, as if the grant or funds were awarded under chapter 229 of title 49, United States Code. The conditions of section 22404 of title 49, United States Code, shall apply to any grant awarded pursuant to this Act.\n##### (b) Operators and certain railroad transportation service providers deemed rail carriers and employers for certain purposes\n**(1)**\nA person that (A) conducts passenger rail operations over, or (B) that performs work for, or in support of, passenger rail operations that is work performed by employees in railroad industry crafts and classes recognized under paragraph Ninth of section 2 of the Railway Labor Act ( 45 U.S.C. 152 ) on rail infrastructure constructed or improved with funding provided in whole in or part in a grant made under this Act shall be considered a rail carrier, and an employer only for the purposes of making such person subject to the laws of the United States referred to in section 10501(c)(3)(A) of title 49, United States Code, including (i) the Railroad Retirement Act of 1974 ( 45 U.S.C. 231 et seq. ); (ii) the Railway Labor Act ( 45 U.S.C. 151 et seq. ); and (iii) the Railroad Unemployment Insurance Act ( 45 U.S.C. 351 et seq. ) but is not deemed to be a rail carrier for the purposes of, or subject to, any other law of the United States.\n**(2)**\nNotwithstanding paragraph (1)\u2014\n**(A)**\n**(i)**\nan employer engaged primarily in the building and construction industry, as that term is used in section 8(f) of the National Labor Relation Act ( 29 U.S.C. 158(f) ) which is performing construction work as a contractor for an eligible entity receiving funds provided under this Act, including a rail carrier, shall not itself be considered a rail carrier solely as a result of performance of that work, and shall be permitted to perform the work with employees who are not covered by (i) the Railroad Retirement Act of 1974 ( 45 U.S.C. 231 et seq. ); (ii) the Railway Labor Act ( 45 U.S.C. 151 et seq. ); and (iii) the Railroad Unemployment Insurance Act ( 45 U.S.C. 351 et seq. ); and\n**(ii)**\nthe exception described in clause (i) does not apply to the performance of railroad maintenance and repair work that is, and has been, historically and customarily performed by employees in railroad industry crafts and classes recognized under paragraph Ninth of section 2 of the Railway Labor Act ( 45 U.S.C. 152 );\n**(B)**\nan employer performing work as a contractor or subcontractor for\u2014\n**(i)**\na railroad that owns, uses, or is contracted to perform work on, rail infrastructure constructed or improved with funding provided in whole or in part in a grant made under this Act; or\n**(ii)**\nan operator that uses such infrastructure,\n45 U.S.C. 231 et seq.\n45 U.S.C. 151 et seq.\n45 U.S.C. 351 et seq.\n45 U.S.C. 152\n##### (c) Other requirements\n**(1) In general**\nAll laborers and mechanics employed by contractors or subcontractors in the performance of construction, alternation, or repair work carried out, in whole or in part, with assistance made available under this Act shall be paid wages at rates not less than those prevailing on projects of a character similar in the locality as determined by the Secretary of Labor in accordance with subchapter IV of chapter 31 of title 40, United States Code.\n**(2) Authority**\nWith respect to labor standards specified in paragraph (1), the Secretary of Labor shall have the authority and functions set forth in Reorganization Plan Numbered 14 of 1950 (64 Stat. 1267; 5 U.S.C. App.) and sections 3145 of title 40, United States Code.\n##### (d) Rail workforce training centers\n**(1) Passenger rail workforce training center**\n**(A) In general**\nThere is established within the consolidated workforce training program\u2014\n**(i)**\na center, which shall be known as the Passenger Rail Workforce Training Center , to meet the needs of the passenger rail systems workforce through standards-based training relating to relevant maintenance and operations occupations; and\n**(ii)**\nexpand workforce development efforts in partnership with organized labor including, apprenticeship training programs.\n**(B) Duties**\nThe Passenger Rail Workforce Training Center, in cooperation with nonprofit labor organizations and Amtrak, shall develop and carry out training and educational programs for rail employees serving in the passenger rail workforce.\n**(2) Freight rail workforce training center**\nThe Administrator, in partnership with rail carriers and nonprofit labor organizations, shall\u2014\n**(A)**\nestablish a consolidated workforce training program for freight railroad personnel;\n**(B)**\nestablish a center, which shall be known as the Freight Rail Workforce Training Center , to meet the needs of the freight rail systems workforce through standards-based training relating to relevant maintenance and operations occupations; and\n**(C)**\nexpand, in partnership with organized labor, workforce development efforts, including apprenticeship training programs.\n**(3) Training and educational program inclusions**\nThe training and educational programs developed pursuant to paragraphs (1) and (2) may include courses in recent developments, techniques, and procedures relating to\u2014\n**(A)**\ndeveloping consensus national training standards, in partnership with industry stakeholders, for key rail occupations with demonstrated skill gaps;\n**(B)**\nestablishing regional, State, and local rail training partnerships\u2014\n**(i)**\nto identify and address workforce skill gaps; and\n**(ii)**\nto develop skills needed for\u2014\n**(I)**\ndelivering quality rail service; and\n**(II)**\nsupporting employee career advancement;\n**(C)**\ndeveloping programs for the training of frontline workforce, instructors, mentors, and labor-management partnership representatives, in the form of classroom, hands-on, on-the-job, and internet web-based training, to be delivered\u2014\n**(i)**\nat a national center;\n**(ii)**\nregionally; or\n**(iii)**\nat an individual rail carrier;\n**(D)**\ndeveloping training programs for skills relating to existing and emerging rail technologies, such as zero-emission locomotives and trains and zero-emission locomotive infrastructure;\n**(E)**\ndeveloping improved capacity for safety, security, and emergency preparedness in rail systems and the industry as a whole through\u2014\n**(i)**\ndeveloping the role of the rail workforce in establishing and sustaining safety culture and safety systems in rail; and\n**(ii)**\ntraining to address rail workforce roles in promoting health and safety for rail workers, communities adjacent to railroad infrastructure and railyards; and\n**(F)**\ndeveloping rail carrier capacity for career pathway partnerships with schools and other community organizations for recruiting and training underrepresented populations as successful rail employees who can develop careers in the rail industry.\n**(4) Authorization of appropriations**\nThere is authorized to be appropriated to the Administrator $500,000,000 for the 5-year period beginning on October 1, 2025, to carry out the Rail Workforce Training Program authorized under this subsection.",
      "versionDate": "2025-07-29",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-30",
        "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials."
      },
      "number": "4790",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "All Aboard Act of 2025",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-17T17:15:13Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2520is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "All Aboard Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-05T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "All Aboard Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a State rail formula grant program, to direct Federal Railroad Administration to create a Green Railroads Fund, to expand passenger rail programs, to address air quality concerns, to establish rail workforce training centers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:21Z"
    }
  ]
}
```
