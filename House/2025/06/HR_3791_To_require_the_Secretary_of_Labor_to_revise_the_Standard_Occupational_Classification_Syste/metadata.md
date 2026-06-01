# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3791?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3791
- Title: EMS Counts Act
- Congress: 119
- Bill type: HR
- Bill number: 3791
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2026-04-10T08:06:06Z
- Update date including text: 2026-04-10T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3791",
    "number": "3791",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "EMS Counts Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:06Z",
    "updateDateIncludingText": "2026-04-10T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "NC"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "WA"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "CO"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "GA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
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
      "sponsorshipDate": "2025-12-16",
      "state": "CO"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NH"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3791ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3791\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mr. Thompson of Pennsylvania (for himself and Mr. Mannion ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require the Secretary of Labor to revise the Standard Occupational Classification System to accurately count the number of emergency medical services practitioners in the United States.\n#### 1. Short title\nThis Act may be cited as the EMS Counts Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nEmergency Medical Services (in this Act referred to as EMS ) personnel provide a critical role in emergency response. EMS consists of a diverse group of health care practitioners, such as paramedics, emergency medical technicians (in this Act referred to as EMTs ), dual-role firefighter/EMTs, firefighter/paramedics, and volunteer personnel serving in each of such roles.\n**(2)**\nEMS is an integral component of the response capacity of the United States to disasters and public health crises, such as outbreaks of infectious diseases, bombings, mass shootings, earthquakes, tornadoes, and hurricanes. EMS personnel respond to more than 22,000,000 emergency calls each year including strokes, heart attacks, cardiac arrest, and trauma.\n**(3)**\nThe Bureau of Labor Statistics compiles information on the number of individuals working in roles across the entire United States workforce. The Bureau of Labor Statistics completes this work by maintaining the Standard Occupational Classification system which classifies workers and jobs into occupational categories for the purpose of collecting, calculating, analyzing, or disseminating data.\n**(4)**\nThe BLS fails to accurately count EMS practitioners because of its failure to include dual-role firefighter/EMTs and firefighter/paramedics in their count of EMS personnel.\n**(5)**\nAccurately counting the EMS workforce is critical for government agencies in determining the needs of EMS agencies and practitioners. These data are also crucial for informing many aspects of policy including preparedness for natural disasters, public health emergencies, and acts of terrorism.\n#### 3. Recognition of dual-role firefighters as EMS practitioners\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Labor shall revise the broad description under the occupational series 33\u20132011 Firefighters of the 2018 Standard Occupational Classification System of the Bureau of Labor Statistics to include the following detailed occupations:\n**(1)**\nFirefighters.\n**(2)**\nFirefighter/EMTs.\n**(3)**\nFirefighter/Paramedics.\n**(4)**\nFirefighters, All Other.\n#### 4. Reports to Congress\nNot later than 270 days after the enactment of this Act, the Secretary of Labor shall submit to Congress a report that details\u2014\n**(1)**\nthe actions taken in 2015 to expand the definition 29\u20132040 Emergency Medical Technicians and Paramedics to separately account for the numbers of EMTs and paramedics; and\n**(2)**\nthe implementation of the revisions under section 3.",
      "versionDate": "2025-06-05",
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
        "name": "Labor and Employment",
        "updateDate": "2025-06-26T14:24:47Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3791ih.xml"
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
      "title": "EMS Counts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EMS Counts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Labor to revise the Standard Occupational Classification System to accurately count the number of emergency medical services practitioners in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T06:18:25Z"
    }
  ]
}
```
