# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8241?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8241
- Title: Power for the People Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8241
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-05-01T08:08:50Z
- Update date including text: 2026-05-01T08:08:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-09: Introduced in House

## Actions

- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8241",
    "number": "8241",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "T000469",
        "district": "20",
        "firstName": "Paul",
        "fullName": "Rep. Tonko, Paul [D-NY-20]",
        "lastName": "Tonko",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Power for the People Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:50Z",
    "updateDateIncludingText": "2026-05-01T08:08:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2026-04-09T15:34:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "TN"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "OR"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NC"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "DC"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "VA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MN"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "TX"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "VT"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8241ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8241\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Tonko (for himself, Ms. Castor of Florida , Mr. Cohen , Ms. Elfreth , Ms. Dexter , Mrs. Foushee , Mr. Garamendi , Mr. Goldman of New York , Mr. Lynch , Ms. Norton , Mr. Ivey , Mrs. McClain Delaney , Ms. McClellan , Mr. Mfume , Mr. Olszewski , Ms. Schakowsky , and Mr. Quigley ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo promote the creation of data center load queues and data center-specific rate classes to mitigate the impact of data centers on other electricity consumers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Power for the People Act of 2026 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nbecause of current energy policies and electricity market structures, households and businesses are subsidizing data center development, paying the way for data centers through rising energy bills;\n**(2)**\nrecent analysis indicates that data centers are set to more than double their electricity consumption, accounting for 6.7 percent to 12 percent of all energy demand by 2028, which is causing electricity prices to increase for ratepayers;\n**(3)**\nratepayers should not be forced to take on the financial risks and costs of new infrastructure investments needed to support projected data center energy demands;\n**(4)**\ndata center owners and operators should be held accountable for the increased energy costs that data centers are causing;\n**(5)**\n**(A)**\nthe uniquely large size, rapidly increasing pace, and uncertain nature of projected energy demand from data centers are impacting both grid reliability and the affordability of electricity;\n**(B)**\nenergy demand from data centers is also significantly impacting interstate commerce by putting a strain on the electric grid and causing reliability issues and energy costs to rise across State lines; and\n**(C)**\ntherefore, increased Federal oversight is necessary to ensure that the interconnection of data centers to the electric grid does not create reliability or affordability risks;\n**(6)**\ndata centers directly affect the transmission system and can increase transmission costs, regardless of whether they are connected directly to transmission facilities;\n**(7)**\nany policy solutions seeking to hold data center owners and operators accountable as described in paragraph (4) should also seek to minimize the climate and environmental impacts of data center development while creating good-paying jobs;\n**(8)**\nthe Commission has authority, pursuant to the mandates to ensure just and reasonable and not unduly discriminatory rates (as established under sections 205 and 206 of the Federal Power Act ( 16 U.S.C. 824d , 824e) (including the standards developed under those sections)) and grid reliability (as established under section 215 of that Act ( 16 U.S.C. 824o ) (including the standards developed under that section)), to require grid operators to create load queues for data centers that incentivize certain practices, including payment for required system upgrades and voluntary load flexibility;\n**(9)**\ngrid operators, as part of their mandate to provide reliable transmission service, have the authority to create load queues specific to data centers that delay or deny interconnection in order to ensure reliability, and it is not unduly discriminatory to do so under the Federal Power Act ( 16 U.S.C. 791a et seq. ) because data centers, as a single customer class, constitute enough new load to overwhelm the electric grid if their interconnection to the electric grid is left unchecked; and\n**(10)**\n**(A)**\nsome States are implementing processes to create rate classes specific to data centers, which are necessary to protect ratepayers from unfair costs and unnecessary risk, given the uncertain nature of data center energy demand projections and the high costs associated with the energy demands of data centers; and\n**(B)**\nrate classes specific to data centers should be adopted more broadly across all States to help ensure that, across the United States, energy system cost increases caused by data centers are paid for by data center owners and operators.\n#### 3. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(2) Covered interconnection entity**\nThe term covered interconnection entity means\u2014\n**(A)**\nan Independent System Operator (as defined in section 3 of the Federal Power Act ( 16 U.S.C. 796 ));\n**(B)**\na Regional Transmission Organization (as defined in that section); and\n**(C)**\na transmitting utility (as defined in that section) that is responsible for managing data center load interconnection requests (or the appropriate regional grid planning entity for the transmitting utility (as determined by the Commission)).\n**(3) Data center**\nThe term data center means any facility, or group of facilities with the same owner located in the same utility area, that\u2014\n**(A)**\nprimarily contains electronic equipment used to host information and information systems accessed by other systems or by users on other devices both in and outside of the State in which the facility or group of facilities is located;\n**(B)**\nmay be\u2014\n**(i)**\na free-standing structure; or\n**(ii)**\na facility that\u2014\n**(I)**\nis within a larger structure; and\n**(II)**\nuses environmental control equipment to maintain the proper conditions for the operation of electronic equipment;\n**(C)**\nhas an energy demand greater than 50 megawatts;\n**(D)**\nmeets such other criteria as the Commission determines to be appropriate for purposes of this Act, including anticircumvention provisions; and\n**(E)**\nis not owned by the Federal Government.\n**(4) Data center load queue**\nThe term data center load queue means a load queue that\u2014\n**(A)**\nrelates specifically to data center load interconnection requests; or\n**(B)**\nrelates to requests made by distribution utilities or load-serving entities (as those terms are defined in section 217(a) of the Federal Power Act ( 16 U.S.C. 824q(a) )) to study impacts on the transmission system caused by the interconnection of data centers.\n**(5) Data center owner or operator**\nThe term data center owner or operator means any person, including a corporation, that owns, builds, or operates a data center.\n**(6) Facility used to mine cryptocurrency**\nThe term facility used to mine cryptocurrency means any facility, or group of facilities with the same owner located in the same utility area, that\u2014\n**(A)**\nis used to mine or create cryptocurrencies or other blockchain-based digital assets;\n**(B)**\nmay be\u2014\n**(i)**\na free-standing structure; or\n**(ii)**\na facility that\u2014\n**(I)**\nis within a larger structure; and\n**(II)**\nuses environmental control equipment to maintain the proper conditions for the operation of electronic equipment; and\n**(C)**\nmeets such other criteria, such as a minimum peak electricity demand, as the Commission determines to be appropriate for purposes of this Act.\n**(7) Labor organization**\nThe term labor organization means a labor organization (as defined in section 2 of the National Labor Relations Act ( 29 U.S.C. 152 )) of which building and construction employees are members.\n**(8) Labor peace agreement**\nThe term labor peace agreement means a written agreement between an employer and a labor union through which the employer guarantees that\u2014\n**(A)**\nthe employer will be neutral regarding any of the employees of the employer seeking to be represented by the labor union; and\n**(B)**\nif employees seek to be represented by a labor union, the employer shall recognize the labor union as the exclusive bargaining representative on a showing that a majority of the employees choose to be represented by the labor organization.\n**(9) Load growth**\nThe term load growth means increasing demand for electricity.\n**(10) Load interconnection request**\nThe term load interconnection request means the request of a data center owner or operator to connect, or study the feasibility of connecting, a data center to the electric grid, whether at the transmission or distribution level.\n**(11) Organic load growth**\n**(A) In general**\nThe term organic load growth means load growth that is attributable to increases in demand associated with economic or population growth, including with respect to hospitals, educational institutions, advanced manufacturing facilities, residential homes, electric vehicles, and other facilities, as determined by the Commission.\n**(B) Exclusion**\nThe term organic load growth does not include load growth that is attributable to\u2014\n**(i)**\ndata centers; or\n**(ii)**\nfacilities used to mine cryptocurrency.\n**(12) Project labor agreement**\nThe term project labor agreement means a pre-hire collective bargaining agreement with 2 or more labor organizations that\u2014\n**(A)**\nestablishes the terms and conditions of employment for a specific construction project; and\n**(B)**\nis an agreement described in subsections (e) and (f) of section 8 of the National Labor Relations Act ( 29 U.S.C. 158 ).\n**(13) Qualifying battery energy storage system**\nThe term qualifying battery energy storage system means a utility-scale battery energy storage system that is connected to the electric grid and paid for by a data center owner or operator, including through a power purchase agreement or other bilateral contract, regardless of whether the battery energy storage system is onsite or offsite with respect to the data center.\n**(14) Qualifying load flexibility agreement**\nThe term qualifying load flexibility agreement means an agreement between a covered interconnection entity and 1 or more data center owners or operators\u2014\n**(A)**\nthat\u2014\n**(i)**\nis implemented by the covered interconnection entity; and\n**(ii)**\ncomplies with the minimum standards and guidelines established by the Commission under section 4(c); and\n**(B)**\npursuant to which\u2014\n**(i)**\ndata centers may be interrupted by the covered interconnection entity; and\n**(ii)**\nto the extent that the covered interconnection entity determines that load shedding, curtailments, or other grid protection is needed, data center service interruptions shall occur\u2014\n**(I)**\nbefore service interruptions for other grid users; and\n**(II)**\nbefore emergency conditions occur, as defined in the emergency procedures established by the interconnection entity.\n**(15) Registered apprenticeship program**\nThe term registered apprenticeship program means an apprenticeship program registered under the Act of August 16, 1937 (commonly known as the National Apprenticeship Act ) (50 Stat. 664, chapter 663; 29 U.S.C. 50 et seq. ), that meets the standards of parts 29 and 30 of title 29, Code of Federal Regulations (as in effect on the date of enactment of this Act).\n**(16) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 4. Data center load queues\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Commission shall issue a rule requiring all covered interconnection entities to create, for the purpose of addressing reliability and affordability concerns from new data center loads, regardless of whether those loads are connecting directly to the transmission system or through a distribution utility, a data center load queue system\u2014\n**(1)**\nthat gives priority for interconnection to data centers (including data center owners and operators) that, by implementing each of the strategies described in subsection (b), offset their electricity demand on the electric grid, reducing costs for all ratepayers, while also mitigating local air and noise pollution and providing good-paying job opportunities; and\n**(2)**\npursuant to which data centers are connected to the electric grid in a manner that does not interfere with serving organic load growth, which may include delaying or denying interconnection for a data center if the applicable covered interconnection entity determines that such interconnection is likely to adversely affect\u2014\n**(A)**\nthe reliability or resource adequacy of the electric grid; or\n**(B)**\nthe affordability of electricity or electric capacity for users of the electric grid that are not data centers.\n##### (b) Strategies described\nThe strategies referred to in subsection (a)(1) are the following:\n**(1)**\nBringing new, additional supply resources to the electric grid that\u2014\n**(A)**\nare designated for the service of, and paid for by, the data center owner or operator, including through a power purchase agreement or another bilateral contract;\n**(B)**\nare deliverable to the location where the new data center is interconnecting;\n**(C)**\nare maintained for the lifetime of the data center;\n**(D)**\nhave at least enough capacity\u2014\n**(i)**\nto fully serve the new data center; or\n**(ii)**\nto serve that portion of the capacity need of the new data center that is not offset by 1 or more qualifying battery energy storage systems, virtual power plants, or qualifying load flexibility agreements;\n**(E)**\nhave a generation output that\u2014\n**(i)**\nis substantially similar to the temporal load profile of the data center during peak demand; or\n**(ii)**\nis sufficient to fill any gaps in the temporal load profile of the data center during peak demand that are not offset by 1 or more qualifying battery energy storage systems, virtual power plants, or qualifying load flexibility agreements; and\n**(F)**\nare low- or no-carbon forms of generation.\n**(2)**\nIncorporating low- or no-carbon backup generation, which excludes diesel generation and may include behind-the-meter battery energy storage systems.\n**(3)**\nEnsuring that, in the construction of the data center and any new energy supply resource that the data center brings to the electric grid pursuant to paragraphs (1) and (2)\u2014\n**(A)**\nall laborers and mechanics employed by the data center owner or operator and contractors and subcontractors of the data center owner or operator, in the performance of construction, shall be paid wages at rates not less than those prevailing on projects of a character similar in the locality in which the construction project is located, as most recently determined by the Secretary of Labor in accordance with subchapter IV of chapter 31 of title 40, United States Code; and\n**(B)**\nall contractors and subcontractors of the data center owner or operator use registered apprentices participating in registered apprenticeship programs.\n**(4)**\nEnsuring that the operator of any new energy supply resource that the data center brings to the electric grid pursuant to paragraphs (1) and (2) agrees that the operator will use a labor peace agreement for the operation and maintenance of the energy supply resource.\n##### (c) Qualifying load flexibility agreements\n**(1) In general**\nThe Commission shall establish minimum standards and guidelines for qualifying load flexibility agreements.\n**(2) Requirements**\nThe standards and guidelines established under paragraph (1) shall\u2014\n**(A)**\nreduce costs for ratepayers by minimizing the need for the build out of new generation and transmission; and\n**(B)**\nensure that qualifying load flexibility agreements can be effectively implemented by the covered interconnection entity.\n##### (d) Priority\nFor purposes of priority in a data center load queue under subsection (a)(1), with respect to forms of generation described in paragraphs (1)(F) and (2) of subsection (b), priority shall be determined using a sliding scale pursuant to which additional priority is given for forms of generation having lower carbon intensity, such that the lower the carbon intensity of the applicable form of generation, the higher the priority given to the applicable data center in the data center load queue.\n##### (e) Effect of certain agreements\n**(1) Contractor or subcontractor**\nAny individual contractor or subcontractor of the data center owner or operator that is a signatory to a pre-hire collective bargaining agreement described in subsections (e) and (f) of section 8 of the National Labor Relations Act ( 29 U.S.C. 158 ) that covers construction work on the data center and any new energy supply resource that the data center brings to the electric grid shall be deemed to be in compliance with subsection (b)(3).\n**(2) Project labor agreement**\nIf a project labor agreement is used to construct a data center and any new energy supply resource that the data center brings to the electric grid, the data center (including the data center owner and operator) shall be deemed to be in compliance with the requirements of subsection (b)(3).\n##### (f) Labor standards\nWith respect to the labor standards specified in subsection (b)(3)(A), the Secretary of Labor shall have the authority and functions set forth in Reorganization Plan Numbered 14 of 1950 (64 Stat. 1267; 5 U.S.C. App.) and section 3145 of title 40, United States Code.\n##### (g) Deadline for compliance\nThe Commission shall ensure compliance with the rule issued under subsection (a) by the date that is 1 year after the date on which the rule is issued.\n##### (h) Prohibition\nOn and after the effective date of the final rule issued under subsection (a), a data center that is not already interconnected with the electric grid may not interconnect with the electric grid unless the data center has fully advanced through the applicable data center load queue system created under that subsection.\n#### 5. Local transmission cost allocation\nNot later than 120 days after the date of enactment of this Act, the Commission shall direct each public utility (as defined in section 201(e) of the Federal Power Act ( 16 U.S.C. 824(e) )) to file 1 or more tariff amendments pursuant to section 205 of that Act ( 16 U.S.C. 824d ) that\u2014\n**(1)**\nallocate to each interconnecting data center local transmission upgrade costs that, but for the existence of the data center, would not be needed; and\n**(2)**\nrequire data centers to pay transmission rates applicable to their rate class that reflect the embedded cost of the integrated grid, not including those local transmission upgrade costs that are required to be allocated to specific data centers under paragraph (1).\n#### 6. Data center-specific rate classes\n##### (a) In general\nSection 111(d) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2621(d) ) is amended by adding at the end the following:\n(22) Data centers (A) Definitions In this paragraph, the terms data center , data center owner or operator , and load interconnection request have the meanings given those terms in section 3 of the Power for the People Act of 2026 . (B) Standard Each State in which at least 1 data center is located or has been proposed via load interconnection request, legal filing, or public announcement shall consider\u2014 (i) establishing a rate class specific to data centers to ensure that data center owners and operators are covering the full cost of the generation, transmission, and distribution upgrades necessary to serve data centers; and (ii) including as requirements for the data center rate class, in addition to any other potential requirements the State chooses to examine\u2014 (I) minimum demand charges for data center owners and operators based on requested peak electricity demand if the monthly usage of a data center is less than its requested demand to ensure that ratepayers are not paying increased costs for generation and transmission built to serve data centers; (II) an extension of minimum utility contract lengths for data center customers to ensure that data center load does not leave utilities and ratepayers with stranded costs; (III) an increase in up-front interconnection study costs, deposit amounts, or collateral requirements for data center projects to ensure that the interconnection queue is not slowed down by projects that are unlikely to come to fruition; (IV) permissible load ramp periods for data centers that allow data center customers to start service with a lower-than-requested capacity and gradually increase their power demand over a period of multiple years to reach their full requested capacity, subject to the condition that flexible load interconnection pursuant to this subclause does not undermine grid reliability; (V) a clean transition tariff that allows data center customers to financially support novel zero-emissions energy technologies to meet their electricity demand in cooperation with intermediaries, such as a utility company; and (VI) the use of contribution in aid of construction (commonly referred to as CIAC ) as a tool to have the data center customer pay upfront for the utility investment determined to be the responsibility of that data center. .\n##### (b) Compliance\n**(1) Time limitation**\nSection 112(b) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622(b) ) is amended\u2014\n**(A)**\nin paragraph (8), by indenting subparagraph (B) appropriately; and\n**(B)**\nby adding at the end the following:\n(9) (A) Not later than 1 year after the date of enactment of this paragraph, each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority) and each nonregulated electric utility shall commence consideration under section 111, or set a hearing date for consideration, with respect to the standard established by paragraph (22) of section 111(d). (B) Not later than 2 years after the date of enactment of this paragraph, each State regulatory authority (with respect to each electric utility for which the State has ratemaking authority), and each nonregulated electric utility shall complete the consideration and make the determination under section 111 with respect to the standard established by paragraph (22) of section 111(d). .\n**(2) Failure to comply**\nSection 112(c) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622(c) ) is amended by adding at the end the following: In the case of the standard established by paragraph (22) of section 111(d), the reference contained in this subsection to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of that paragraph (22). .\n**(3) Prior state actions**\n**(A) In general**\nSection 112 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2622 ) is amended\u2014\n**(i)**\nin subsection (h), in the subsection heading, by striking Other ; and\n**(ii)**\nby adding at the end the following:\n(i) Prior State actions Subsections (b) and (c) shall not apply to the standard established by paragraph (22) of section 111(d) in the case of any electric utility in a State if, before the date of enactment of this subsection\u2014 (1) the State has implemented the standard (or a comparable standard) for the electric utility; (2) the State regulatory authority for the State or the relevant nonregulated electric utility has conducted a proceeding to consider implementation of the standard (or a comparable standard) for the electric utility; or (3) the State legislature has voted on the implementation of the standard (or a comparable standard) for the electric utility. .\n**(B) Cross reference**\nSection 124 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2634 ) is amended by adding at the end the following: In the case of the standard established by paragraph (22) of section 111(d), the reference contained in this section to the date of enactment of this Act shall be deemed to be a reference to the date of enactment of that paragraph (22). .\n#### 7. Creation of appropriate rate classes\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a program to provide grants and technical assistance to State regulatory authorities (as defined in section 3 of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2602 )) and nonregulated electric utilities (as defined in that section) considering the standard established by paragraph (22) of section 111(d) of that Act ( 16 U.S.C. 2621(d) ) to assist in the creation of appropriate rate classes to ensure that costs relating to the energy demands of data centers, including costs of generation, transmission, and distribution network upgrades, are not borne or subsidized by customers that are not data centers.\n##### (b) Authorization of appropriations\nThere are authorized to be appropriated such sums as are necessary to carry out this section.\n#### 8. Load and interconnection forecasting\n##### (a) Technical assistance\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a program to provide technical assistance to support the forecasting by covered interconnection entities of long-term load projections, particularly with respect to improving forecasting associated with data center load interconnection requests.\n**(2) Authorization of appropriations**\nThere are authorized to be appropriated such sums as are necessary to carry out this subsection.\n##### (b) Transparency and disclosure\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, to improve the forecasting of electricity demand and data center load interconnection requests by covered interconnection entities across the United States, the Commission shall establish transparency and disclosure requirements for data center load interconnection requests, including load interconnection requests occurring at the transmission level and load interconnection requests occurring at the distribution level.\n**(2) Requirement**\nThe requirements established under paragraph (1) shall seek to reduce duplicative, speculative, and other requests that impede accurate forecasting, including by imposing new transparency and information-sharing requirements for utilities and covered interconnection entities to implement with respect to data center load interconnection requests, as the Commission determines to be appropriate.",
      "versionDate": "2026-04-09",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-01-15",
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "3682",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Power for the People Act of 2026",
      "type": "S"
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
        "name": "Energy",
        "updateDate": "2026-04-21T18:07:29Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8241ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Power for the People Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Power for the People Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote the creation of data center load queues and data center-specific rate classes to mitigate the impact of data centers on other electricity consumers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T05:33:37Z"
    }
  ]
}
```
