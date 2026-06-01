# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5481?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5481
- Title: Wildfire Smoke Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 5481
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-12-05T21:49:01Z
- Update date including text: 2025-12-05T21:49:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5481",
    "number": "5481",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Wildfire Smoke Relief Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:49:01Z",
    "updateDateIncludingText": "2025-12-05T21:49:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "OR"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NM"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-21",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5481ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5481\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Neguse (for himself, Ms. Dexter , Ms. Stansbury , and Mr. Morelle ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo authorize transitional sheltering assistance for individuals who live in areas with unhealthy air quality caused by wildfires, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wildfire Smoke Relief Act .\n#### 2. Transitional sheltering assistance\n##### (a) Definitions\nIn this Act:\n**(1) Individual at risk of wildfire smoke related illness**\nThe term individual at risk of wildfire smoke related illness means an individual, living in an area where the air quality index is determined to be unhealthy for not less than 3 consecutive days as a result of a wildfire, who is\u2014\n**(A)**\na low-income individual;\n**(B)**\na parent or guardian with a child who has not attained 19 years of age;\n**(C)**\na pregnant woman;\n**(D)**\nan individual who is 65 years of age or older;\n**(E)**\nan individual with chronic respiratory or cardiovascular illness; or\n**(F)**\nan individual with a chronic disease that is exacerbated by smoke inhalation.\n**(2) Low-income individual**\nThe term low-income individual means an individual from a family whose taxable income (as defined in section 63 of the Internal Revenue Code of 1986) for the preceding year did not exceed 200 percent of an amount equal to the poverty level, as determined by using criteria of poverty established by the Bureau of Census.\n**(3) Qualified entity**\nThe term qualified entity means\u2014\n**(A)**\na State or unit of local government;\n**(B)**\na local public health authority; and\n**(C)**\na coordinated care organization.\n##### (b) Transitional sheltering assistance program\nIn carrying out the Transitional Sheltering Assistance Program of the Federal Emergency Management Agency under section 403 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170b ), the President shall\u2014\n**(1)**\nprovide assistance to a qualified entity to purchase and provide, to an individual at risk of wildfire smoke related illness, smoke-inhalation prevention equipment, including\u2014\n**(A)**\na portable air filtration unit;\n**(B)**\nan air filter;\n**(C)**\na face mask or respirator, such as\u2014\n**(i)**\nan N95 respirator;\n**(ii)**\na P100 respirator; or\n**(iii)**\nother equipment certified by the National Institute for Occupational Safety and Health to protect from airborne particle exposure;\n**(D)**\nlow-cost equipment to keep smoke out of a house, such as:\n**(i)**\na weather strip;\n**(ii)**\nnot more than 1 portable air-conditioning unit per household;\n**(iii)**\nventilation equipment;\n**(iv)**\na screening and shading device; or\n**(v)**\na window covering; or\n**(E)**\nother similarly effective devices; and\n**(2)**\nin any case in which smoke-inhalation prevention equipment is not sufficient to mitigate the risk of illness, provide cost-efficient transitional shelter assistance to an individual at risk of wildfire smoke related illness.",
      "versionDate": "2025-09-18",
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
        "actionDate": "2025-09-18",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "2856",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Wildfire Smoke Relief Act",
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
        "name": "Emergency Management",
        "updateDate": "2025-12-05T21:44:12Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5481ih.xml"
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
      "title": "Wildfire Smoke Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T04:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wildfire Smoke Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize transitional sheltering assistance for individuals who live in areas with unhealthy air quality caused by wildfires, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T04:48:19Z"
    }
  ]
}
```
