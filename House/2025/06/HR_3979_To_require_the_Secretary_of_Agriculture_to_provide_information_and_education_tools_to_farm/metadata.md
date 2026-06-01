# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3979?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3979
- Title: LEAPS Act
- Congress: 119
- Bill type: HR
- Bill number: 3979
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-12-19T09:07:30Z
- Update date including text: 2025-12-19T09:07:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3979",
    "number": "3979",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "LEAPS Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:30Z",
    "updateDateIncludingText": "2025-12-19T09:07:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "MD"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3979ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3979\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Lawler (for himself and Mr. Riley of New York ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Secretary of Agriculture to provide information and education tools to farmers on the cost savings, energy savings, water conservation, and carbon emissions reductions that can be realized through the use of energy-efficient pumping systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Leveraging Efficiency Awareness for Pumping Systems Act or the LEAPS Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThere are over 600,000 pumping systems used for irrigation on agricultural land in the United States, many of which still rely on fossil fuels.\n**(2)**\nImproving the efficiency of agricultural irrigation pumping systems can save up to 22 billion kilowatt hours of energy per year and eliminate 8.3 million metric tons of carbon emissions annually.\n**(3)**\nEnergy savings from electrifying agricultural irrigation pumping systems can save farmers and ranchers more than $1.8 billion annually in energy costs.\n**(4)**\nPumping systems play a central role in the watering of livestock and the management of animal waste in every State.\n**(5)**\nPumping systems are a critical component of the Nation\u2019s $2,300,000,000 aquaculture industry.\n**(6)**\nImproving the efficiency of pumping systems used in raising livestock and fish can significantly reduce energy use, save producers millions of dollars annually, and provide meaningful reductions in carbon emissions.\n**(7)**\nAgricultural irrigation pumping systems utilizing plastic piping can provide significant drought relief benefits, dramatically reducing water losses from evaporation and seepage; agriculture uses 37 percent of the Nation\u2019s surface and ground water, 30 percent of which is lost to seepage and evaporation.\n**(8)**\nReducing the friction in piping used for agricultural irrigation and livestock watering can provide meaningful energy and cost savings; there are potentially 2,500 kWh of energy savings for every 10 miles of plastic piping utilized in delivering water for crops and livestock.\n**(9)**\nSolar pumping systems can play an important role in protecting riparian habitat and improving water quality in streams, rivers, lakes, and estuaries through providing alternative watering options for livestock.\n#### 3. Information on energy-efficient pumping systems\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary, in consultation with pumping system experts, in order to educate farmers on the benefits of energy-efficient pumping systems, shall develop and make publicly available on the website of the Department of Agriculture easily accessible information on cost savings, energy savings, water conservation, and carbon emissions reductions that can be realized through the use of energy-efficient pumping systems.\n##### (b) Contents\nIn carrying out subsection (a), the Secretary shall include information on\u2014\n**(1)**\npumps, pipes, motors, drives, and controls that can provide energy savings and cost savings, conserve water, and reduce carbon emissions; and\n**(2)**\nDepartment of Agriculture programs that provide farmers resources for acquiring energy-efficient pumping systems and drought management infrastructure, including the environmental quality incentives program, the Rural Energy for America Program, and the conservation stewardship program.\n#### 4. Energy efficiency pre-assessment tool\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary, in consultation with pumping system experts, in order to raise awareness of the benefits of energy-efficient pumping systems and increase participation in Department of Agriculture programs that promote energy efficiency, shall develop and make publicly available on the website of the Department of Agriculture a user-friendly tool to\u2014\n**(1)**\nassist farmers in making a preliminary assessment of the energy efficiency of existing pumping systems; and\n**(2)**\nprovide an estimate of potential energy savings, cost savings, and carbon emissions reductions that may be realized through pumping system improvements.\n##### (b) Requirements\n**(1) Ease of use**\nThe Secretary shall ensure that the tool made available under subsection (a) provides a user with projected energy savings, projected cost savings, and projected carbon emissions reductions through the input by the user of the following data relating to an existing pumping system:\n**(A)**\nPump type.\n**(B)**\nFlow rating and actual flow.\n**(C)**\nPressure rating and actual pressure.\n**(D)**\nSpeed rating and actual speed.\n**(2) Considerations**\nThe Secretary shall ensure that the tool made available under subsection (a)\u2014\n**(A)**\nin assessing the energy efficiency of a pumping system, takes into consideration pumps, pipes, motors, drives, and controls associated with the pumping system; and\n**(B)**\nin projecting the energy savings, cost savings, and carbon emissions reductions that may be realized through pumping system improvements, takes into consideration the cost of electricity and the profile of the existing pumping system.\n#### 5. Energy auditor education\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary, in consultation with pumping system experts, in order to increase the effectiveness of Department of Agriculture energy efficiency programs, shall establish a process to educate persons performing energy efficiency audits for the Department of Agriculture on energy use and energy efficiency in pumping systems.\n##### (b) Implementation\nIn carrying out subsection (a), the Secretary shall consider the use of existing education and training programs focused on energy use and energy efficiency in pumping systems.\n#### 6. Conservation stewardship program activities\nSection 1240I(2)(B)(i) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201321(2)(B)(i) ) is amended by inserting and energy-efficient pumping systems before , as determined .\n#### 7. Definitions\nIn this Act:\n**(1) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n**(2) Pumping system**\nThe term pumping system means any pumps, pipes, motors, drives, and controls used to move water and other fluids on farms, ranches, and aquaculture operations.",
      "versionDate": "2025-06-12",
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
        "updateDate": "2025-07-07T13:42:15Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3979ih.xml"
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
      "title": "LEAPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LEAPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Leveraging Efficiency Awareness for Pumping Systems Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to provide information and education tools to farmers on the cost savings, energy savings, water conservation, and carbon emissions reductions that can be realized through the use of energy-efficient pumping systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T03:03:17Z"
    }
  ]
}
```
