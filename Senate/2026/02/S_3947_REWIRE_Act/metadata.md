# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3947?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3947
- Title: REWIRE Act
- Congress: 119
- Bill type: S
- Bill number: 3947
- Origin chamber: Senate
- Introduced date: 2026-02-26
- Update date: 2026-04-16T14:53:17Z
- Update date including text: 2026-04-16T14:53:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-26: Introduced in Senate
- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.
- Latest action: 2026-02-26: Introduced in Senate

## Actions

- 2026-02-26 - IntroReferral: Introduced in Senate
- 2026-02-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-26",
    "latestAction": {
      "actionDate": "2026-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3947",
    "number": "3947",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "REWIRE Act",
    "type": "S",
    "updateDate": "2026-04-16T14:53:17Z",
    "updateDateIncludingText": "2026-04-16T14:53:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-26",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-26",
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
          "date": "2026-02-26T18:51:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-15T19:37:30Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3947is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3947\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2026 Mr. McCormick (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Federal Power Act to establish a categorical exclusion for reconductoring within existing rights-of-way, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reconductoring Existing Wires for Infrastructure Reliability and Expansion Act or the REWIRE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Advanced transmission conductor**\nThe term advanced transmission conductor means a conductor, including a carbon fiber conductor, a composite core conductor, a superconductor, and any other conductor, that\u2014\n**(A)**\nhas a direct current electrical resistance at least 10 percent lower than a traditional ACSR conductor of a similar diameter and weight;\n**(B)**\nhas a potential energy carrying capacity at least 70 percent greater than a traditional ACSR conductor of a similar diameter and weight; and\n**(C)**\nhas a coefficient of thermal expansion at least 50 percent lower than a traditional ACSR conductor of a similar diameter and weight.\n**(2) ASCR conductor**\nThe term ASCR conductor means an aluminum conductor steel-reinforced cable.\n**(3) Bulk-power system**\nThe term bulk-power system has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(4) Commission**\nThe term Commission means the Federal Energy Regulatory Commission.\n**(5) Effective load carrying capability; ELCC**\n**(A) In general**\nThe term effective load carrying capability or ELCC means the ability of a generating resource to produce electricity when the grid needs it, measured as the additional load (or perfect replacement capacity) that the system can supply with a particular generator of interest with no net change in reliability.\n**(B) Clarification**\nThe additional load (or perfect replacement capacity) referred to in subparagraph (A)\u2014\n**(i)**\nmay be measured using LOLE, EUE, or other metrics; and\n**(ii)**\nmay be divided by the nameplate capacity of the generating resource to yield a percentage.\n**(6) Electric Reliability Organization**\nThe term Electric Reliability Organization has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(7) Electric utility**\nThe term electric utility has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(8) Expected unserved energy; EUE**\nThe term expected unserved energy or EUE means the cumulative amount of energy (in megawatt-hours) per year that is not provided to customers due to outages.\n**(9) Grid-enhancing technology**\nThe term grid-enhancing technology means any hardware or software that\u2014\n**(A)**\nincreases the capacity, efficiency, reliability, resilience, or safety of transmission facilities and transmission technologies; and\n**(B)**\nis installed in addition to transmission facilities and transmission technologies\u2014\n**(i)**\nto give operators of the transmission facilities and transmission technologies more situational awareness and control over the electric grid;\n**(ii)**\nto make the transmission facilities and transmission technologies more efficient; or\n**(iii)**\nto increase the transfer capacity of the transmission facilities and transmission technologies.\n**(10) Independent System Operator**\nThe term Independent System Operator has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(11) Integrated resource planning**\nThe term integrated resource planning means modeling and evaluating how projected long-term electricity demands (such as electricity demands over periods of 5, 10, 20, or more years) within a service area can be met with a combination of electric generation resources that best achieve desired metrics, such as metrics relating to reliability, resilience, and cost.\n**(12) Loss of load expectation; LOLE**\n**(A) In general**\nThe term loss of load expectation or LOLE means the expected number of days per year that the available generation capacity is less than the system load for the applicable power grid region or service area.\n**(B) Clarification**\nAs of November 2023, a commonly acceptable value for loss of load expectation is 0.1 days per year, as described in the standard of the North American Electric Reliability Corporation entitled Planning Resource Adequacy Analysis, Assessment and Documentation and numbered BAL\u2013502\u2013RF\u201303.\n**(13) National Laboratory**\nThe term National Laboratory has the meaning given the term in section 2 of the Energy Policy Act of 2005 ( 42 U.S.C. 15801 ).\n**(14) Planning reserve margin**\n**(A) In general**\nThe term planning reserve margin means the quotient, expressed as a percentage, obtained by dividing\u2014\n**(i)**\nthe difference between\u2014\n**(I)**\ndeliverable electric system supply capacity for a power grid region or service area; and\n**(II)**\nnet demand in that power grid region or service area; by\n**(ii)**\nnet demand in that power grid region or service area.\n**(B) Clarification**\nAs of November 2023, a reserve margin falling within the range from 15 percent to 25 percent is typical for a power grid region or service area.\n**(15) Power grid**\nThe term power grid means that portion of an Interconnection (as defined in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) )) that is located within the United States, including the relevant portion of each of the following:\n**(A)**\nThe Eastern Interconnection.\n**(B)**\nThe Western Interconnection.\n**(C)**\nThe Texas Interconnection.\n**(16) Power grid region**\nThe term power grid region means a geographic area\u2014\n**(A)**\nlocated within a power grid; and\n**(B)**\nfor which a regional entity (as defined in subsection (a) of section 215 of the Federal Power Act ( 16 U.S.C. 824o )) has enforcement authority under that section.\n**(17) Probabilistic modeling**\n**(A) In general**\nThe term probabilistic modeling means a modeling approach that uses statistics to simulate and quantify the likelihood of achieving desired metrics, taking into consideration all modeled uncertainties, for determination of the optimal resource portfolio, such as a modeling approach consistent with the document of the North American Electric Reliability Corporation entitled Probabilistic Assessment Technical Guideline Document and dated August 2016, including the recommendations described in that document.\n**(B) Inclusion**\nThe term probabilistic modeling includes modeling that can identify the most important parameters that impact a simulated metric for further characterization or optimization.\n**(18) Regional Transmission Organization**\nThe term Regional Transmission Organization has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n**(19) Reliability standard**\nThe term reliability standard has the meaning given the term in section 215(a) of the Federal Power Act ( 16 U.S.C. 824o(a) ).\n**(20) Resource adequacy**\nThe term resource adequacy means the adequate supply and provision of electricity from various electric generation resources to meet projected electricity demands in a particular power grid region or service area.\n**(21) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(22) Service area**\nThe term service area means the area or region served by\u2014\n**(A)**\nan electric utility;\n**(B)**\na Regional Transmission Organization; or\n**(C)**\nan Independent System Operator.\n**(23) State regulatory authority**\nThe term State regulatory authority has the meaning given the term in section 3 of the Federal Power Act ( 16 U.S.C. 796 ).\n#### 3. Categorical exclusion for reconductoring\nPart II of the Federal Power Act ( 16 U.S.C. 824 et seq. ) is amended by inserting after section 216 the following:\n216A. Grid capacity expansion in existing rights-of-way (a) Definition of previously disturbed or developed In this section, the term previously disturbed or developed has the meaning given the term in section 1021.102(g)(1) of title 10, Code of Federal Regulations (or a successor regulation). (b) Establishment of categorical exclusion Activities to increase the capacity of the electric grid within existing rights-of-way or on previously disturbed or developed land are a category of actions designated as being categorically excluded from the preparation of an environmental assessment or an environmental impact statement under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ). (c) Inclusions The activities to which the categorical exclusion established by subsection (b) shall apply include any repair, maintenance, replacement, upgrade, modification, optimization, or minor relocation of, addition to, or addition of energy storage at or near, an existing electric transmission or distribution facility or associated infrastructure, including electrical substations, within an existing right-of-way or on otherwise previously disturbed or developed land, including reconductoring and installation of grid-enhancing technologies. .\n#### 4. Return on equity for advanced transmission conductors\nSection 219 of the Federal Power Act ( 16 U.S.C. 824s ) is amended\u2014\n**(1)**\nin subsection (a), by striking Not later than 1 year after the date of enactment of this section, the and inserting The ;\n**(2)**\nin subsection (b), in the matter preceding paragraph (1), by inserting issued under subsection (a) after rule ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin the second sentence, by striking The Commission and inserting the following:\n(2) Recoverable costs The Commission ; and\n**(B)**\nin the first sentence, by striking In the rule issued under this section and inserting the following:\n(1) In general In the rule issued under subsection (a) ;\n**(4)**\nin subsection (d), by striking All rates approved under the rules adopted pursuant to this section, including any revisions to the rules, are and inserting Any rate approved under a rule issued pursuant to this section (including a revision to a rule) shall be ; and\n**(5)**\nby adding at the end the following:\n(e) Advanced transmission conductors (1) Return on equity Not later than 1 year after the date of enactment of the REWIRE Act , the Commission shall promulgate new, or revise existing, rules under this section to improve the return on equity for investments in advanced transmission conductors (as defined in section 2 of that Act). (2) Consumer protections The Commission shall ensure that all rates approved under the rules promulgated or revised under this subsection (including any subsequent revisions to those rules) are just and reasonable and not unduly discriminatory or preferential, as required by subsection (d). .\n#### 5. State energy programs\nSection 362(c)(7)(B) of the Energy Policy and Conservation Act ( 42 U.S.C. 6322(c)(7)(B) ) is amended by inserting , including reconductoring with advanced transmission conductors (as defined in section 2 of the REWIRE Act ) and the installation of grid-enhancing technologies (as defined in that section) before the semicolon at the end.\n#### 6. National Laboratory modeling and evaluation program\n##### (a) In general\nThe Secretary, acting through 1 or more National Laboratories, in consultation with the Commission and the Electric Reliability Organization, shall establish a program to model and evaluate the performance of the electric grid.\n##### (b) Requirements\nIn carrying out the program established under subsection (a), the Secretary shall develop 1 or more probabilistic models for transmission planning, resource adequacy modeling, and integrated resource planning that\u2014\n**(1)**\nreflect the specific needs, resources, and attributes of a given power grid region or service area;\n**(2)**\nensure consistent methods based on best practices;\n**(3)**\ninclude consideration of uncertainties relating to\u2014\n**(A)**\ntransmission systems and infrastructure;\n**(B)**\nthe impact of weather (such as the impact of temperature on transmission facilities, including line ratings);\n**(C)**\ncongestion and thermal overload; and\n**(D)**\nthe costs of new or modified transmission infrastructure, including reconductoring with advanced transmission conductors and the deployment of grid-enhancing technologies; and\n**(4)**\ninclude consideration of other relevant transmission uncertainties, including those which may be unique to a given power grid region or service area, as determined by the Secretary in consultation with the Commission.\n##### (c) Use of modeling\nThe Secretary shall ensure that the models developed pursuant to the program established under subsection (a) may be used, at a minimum\u2014\n**(1)**\nto simulate and quantify desired metrics, taking into consideration the relevant uncertainties described in paragraphs (3) and (4) of subsection (b), which may be used to assist in transmission planning and the determination of the optimal resource portfolio for the applicable power grid region or service area, including\u2014\n**(A)**\nloss of load expectation;\n**(B)**\nexpected unserved energy;\n**(C)**\neffective load carrying capability (also known as capacity value );\n**(D)**\nplanning reserve margin;\n**(E)**\nelectricity transmission losses;\n**(F)**\ncongestion; and\n**(G)**\ncost;\n**(2)**\nto identify the parameters and processes considered under subsection (b) that\u2014\n**(A)**\nhave the most impact on the magnitude or uncertainty of the applicable simulated metrics; and\n**(B)**\ncan be further characterized or optimized to improve the modeling and determination of the optimal resource portfolio and transmission system for the applicable power grid region or service area; and\n**(3)**\nto identify areas where the deployment of advanced transmission technologies, such as advanced transmission conductors or grid-enhancing technologies, may improve electric grid performance.\n##### (d) Regional collaboratives\n**(1) In general**\nIn carrying out the program under subsection (a), the Secretary shall establish regional collaboratives between the National Laboratories and institutions of higher education.\n**(2) Considerations**\nThe Secretary shall, to the maximum extent practicable, prioritize establishing regional collaboratives under paragraph (1) that\u2014\n**(A)**\nare between regional institutions of higher education and National Laboratories that are owned and operated by the Federal Government;\n**(B)**\ninclude institutions of higher education with existing demonstration capability, such as field-scale systems of not less than 100 kilovolt-amperes or laboratory capabilities of not less than 10 kilovolt-amperes, to support technology validation, utility adoption, industry engagement, and workforce development;\n**(C)**\ndemonstrate rural grid planning models (including transmission and distribution co-simulation and digital twin capabilities); or\n**(D)**\nutilize existing active data sharing and joint modeling programs between institutions of higher education and participating utilities at a statewide scale.\n#### 7. Technical assistance relating to the use of advanced transmission conductors\n##### (a) Definitions\nIn this section:\n**(1) Developer**\nThe term developer means a developer of electric transmission facilities or technologies that pays to install a high-voltage transmission conductor.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na developer;\n**(B)**\nan electric utility;\n**(C)**\na State;\n**(D)**\na Regional Transmission Organization or Independent System Operator; or\n**(E)**\nany other relevant entity, as determined by the Secretary.\n##### (b) Technical assistance and application guide\n**(1) Application guide**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall establish an application guide for eligible entities seeking to implement\u2014\n**(A)**\nadvanced transmission conductors, including through reconductoring with advanced transmission conductors; and\n**(B)**\ngrid-enhancing technologies.\n**(2) Updates**\nThe guide established under paragraph (1) shall be reviewed and updated annually.\n**(3) Technical assistance**\n**(A) In general**\nOn request of an eligible entity using the guide established under paragraph (1), the Secretary shall provide technical assistance to that eligible entity with respect to the use of advanced transmission conductors and grid-enhancing technologies for particular applications.\n**(B) Clearinghouse**\nIn carrying out subparagraph (A), the Secretary shall establish a clearinghouse of previously completed projects that the Secretary and eligible entities may use to identify issues and solutions relating to\u2014\n**(i)**\nthe use of advanced transmission conductors;\n**(ii)**\nreconductoring with advanced transmission conductors; and\n**(iii)**\nthe use of grid-enhancing technologies.",
      "versionDate": "2026-02-26",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-04-16T14:52:22Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-04-16T14:35:28Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2026-04-16T14:35:59Z"
          },
          {
            "name": "Energy prices",
            "updateDate": "2026-04-16T14:41:08Z"
          },
          {
            "name": "Energy research",
            "updateDate": "2026-04-16T14:40:58Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-04-16T14:36:11Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-04-16T14:53:17Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2026-04-16T14:37:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-03-19T14:45:52Z"
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
      "date": "2026-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3947is.xml"
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
      "title": "REWIRE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REWIRE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reconductoring Existing Wires for Infrastructure Reliability and Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Power Act to establish a categorical exclusion for reconductoring within existing rights-of-way, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-17T04:18:28Z"
    }
  ]
}
```
