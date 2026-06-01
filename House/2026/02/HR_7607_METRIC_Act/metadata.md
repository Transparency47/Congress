# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7607
- Title: METRIC Act
- Congress: 119
- Bill type: HR
- Bill number: 7607
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-02-27T18:01:34Z
- Update date including text: 2026-02-27T18:01:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7607",
    "number": "7607",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "METRIC Act",
    "type": "HR",
    "updateDate": "2026-02-27T18:01:34Z",
    "updateDateIncludingText": "2026-02-27T18:01:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:34:20Z",
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
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7607ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7607\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Casten (for himself, Ms. Castor of Florida , and Mr. Cleaver ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo study and modernize the measurement and reporting of United States energy use, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modernizing EIA Tracking and Reporting to Increase Consistency Act or the METRIC Act .\n#### 2. Purpose and findings\n##### (a) Purpose\nThe purpose of this Act is to improve the energy performance, transparency, and decision-making of the United States by modernizing how the United States measures and accounts for gross amount of energy input into the national energy system.\n##### (b) Findings\nCongress finds that\u2014\n**(1)**\nhistorical measures of primary energy were developed for economies dominated by combustion-based fuels and do not accurately capture the efficiency or system value of noncombustion energy sources;\n**(2)**\ndifferences in how primary energy are measured across fuel and renewable systems obscure trends in electrification, decarbonization, and energy productivity, hindering effective policymaking and misinforming researchers, market participants, and the public; and\n**(3)**\nenhancing national energy accounting through improved data collection, modeling, and transparency will strengthen evidence-based policymaking, support market efficiency, and better align United States statistics with the energy transition.\n#### 3. Modernizing energy metrics\n##### (a) Study on primary energy indicators\n**(1) Required study**\nThe Secretary of Energy, with support from the Administrator of the Energy Information Administration and relevant offices within the Department of Energy, shall conduct a comprehensive study on the validity, limitations, and potential alternatives to the use of the indicators for primary energy in national energy accounting.\n**(2) Scope of study**\nThe study shall include\u2014\n**(A)**\nan evaluation of the conceptual basis and historical rationale for the current indicator for primary energy calculated and reported by the Energy Information Administration;\n**(B)**\nan assessment of the limitations of primary energy accounting in accurately reflecting energy efficiency, energy transitions, and the value and comparability of combustible and noncombustible energy sources;\n**(C)**\nan analysis of alternative indicators and their suitability for integration into national energy statistics;\n**(D)**\na review of international best practices for energy accounting, including methodologies used by the International Energy Agency and peer nations; and\n**(E)**\nrecommendations for improvements or replacements to the primary energy indicator that better align with national goals for energy efficiency, electrification, decarbonization, and economic productivity.\n**(3) Report to Congress**\nNot later than 18 months after the date of enactment of this Act, the Secretary of Energy shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Energy and Natural Resources of the Senate a report containing the findings and recommendations of the study required under paragraph (1).\n##### (b) Complementary incident energy statistics\nSection 205 of the Department of Energy Organization Act ( 42 U.S.C. 7135 ) is amended by adding at the end the following:\n(n) Incident energy statistics (1) Requirement The Administrator shall develop, collect, analyze, and report on incident energy. (2) Measurement and estimation (A) Data derived from surveys To the extent feasible, under paragraph (1), the Administrator shall collect, through surveys, reporting requirements, or other data-collection mechanisms, data representing the amount of incident energy, consistent with the approaches used to evaluate primary energy for thermal energy sources. (B) Derived estimates With respect to energy sources for which it is not feasible to collect data under subparagraph (A), the Administrator shall develop and publish model-based estimates or analytical approximations of the amount of incident energy, updated on an annual basis, based on\u2014 (i) data collected through new or existing surveys of manufacturers, operators, or users of energy conversion technologies; (ii) physical models or statistical analyses developed or adopted by the Energy Information Administration; and (iii) information derived from Federal research institutions, National Laboratories, the National Aeronautics and Space Administration, the National Oceanic and Atmospheric Administration, or other appropriate entities using remote sensing, satellite imagery, or comparable observational techniques, as may be necessary. (3) Integration and publication (A) In general The Administrator shall include the data on the amount of incident energy included in each report required by paragraph (1) in the existing reports or other products published by the Energy Information Administration that include primary energy and final energy statistics in a manner that enables side-by-side comparison of energy-conversion efficiency and system performance. (B) Public availability The Administrator shall make all data, assumptions, and methods used under this subsection for purposes of developing, collecting, analyzing, and reporting on incident energy publicly available in machine-readable formats and shall describe the degree of uncertainty or approximation associated with the estimates and analytical approximations developed and published under paragraph (2)(B). (4) Relationship to existing statistics This subsection shall not be construed to affect how the Energy Information Administration defines or reports primary energy as of the date of enactment of this subsection. (5) Definitions In this subsection: (A) Energy conversion The term energy conversion means any physical, chemical, or mechanical process by which energy is transformed from one form to another for the purpose of producing electricity, heat, mechanical work, chemical energy, or another usable or storable form of energy. (B) Final energy The term final energy \u2014 (i) means energy in the form delivered to end users for consumption in buildings, transportation, industrial processes, or other sectors; and (ii) includes electricity, pipeline gas, gasoline, diesel, hydrogen, and district heat. (C) Incident energy The term incident energy \u2014 (i) means the total energy entering an energy conversion technology or system from natural or environmental sources, including both thermal and nonthermal forms, before any transformation or conversion losses occur; and (ii) includes energy from combustible fuels, biomass, nuclear materials, solar radiation, wind, geothermal heat, hydroelectric potential, and other renewable or nonrenewable resources. .",
      "versionDate": "2026-02-20",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-02-27T18:01:34Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7607ih.xml"
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
      "title": "METRIC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "METRIC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modernizing EIA Tracking and Reporting to Increase Consistency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To study and modernize the measurement and reporting of United States energy use, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T05:48:35Z"
    }
  ]
}
```
