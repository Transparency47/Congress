# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3646?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3646
- Title: Guam Temporary Workforce Act
- Congress: 119
- Bill type: HR
- Bill number: 3646
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-10-01T08:05:50Z
- Update date including text: 2025-10-01T08:05:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3646",
    "number": "3646",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "Guam Temporary Workforce Act",
    "type": "HR",
    "updateDate": "2025-10-01T08:05:50Z",
    "updateDateIncludingText": "2025-10-01T08:05:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3646ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3646\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Moylan introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo allow the Governor of Guam to determine temporary need of nonimmigrant workers on Guam, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guam Temporary Workforce Act .\n#### 2. Nonimmigrant workers in the Territory of Guam\n##### (a) In general\nThe following shall apply in the case of an alien who seeks admission to Guam under section 101(a)(15)(H)(ii)(b) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(H)(ii)(b) ):\n**(1)**\nAn employer must file a petition with the Secretary for endorsement of the alien's eligibility for classification as a H\u20132B temporary employee before the alien may apply for a visa or seek admission to the United States.\n**(2)**\nIn the Territory of Guam, an employer petitioning for H\u20132B temporary employees shall apply for a temporary labor certification with the Governor of Guam (as described in 8 CFR 214.2 unless otherwise contradicted by this Act) prior to filing a petition.\n**(3)**\nThe Secretary will conclude the following when presented with an employer petition containing an approved temporary labor certification issued by the Governor of Guam:\n**(A)**\nUnited States workers capable of performing the temporary services or labor as described in the temporary labor certification are not available.\n**(B)**\nThe alien's employment will not adversely affect the wages and working conditions of similarly employed United States workers.\n**(C)**\nThe employer has a one-time occurrence, seasonal need, peakload need, intermittent need, or other qualified need for temporary employees.\nA completed employer petition for H\u20132B temporary employees on Guam shall be approved by the Secretary so long as the petition includes an approved temporary labor certification issued by the Governor of Guam within the last 365 days.\n**(4)**\nAn approved temporary labor certification issued by the Governor of Guam may only be invalidated if it is determined by a court of law that the temporary labor certification request involved fraud, willful misrepresentation, or gross misconduct.\n#### 3. Definitions\n##### (a) In general\nUnless otherwise contradicted in this Act, all terms, including H\u20132B, intermittent need, one-time occurrence, peakload need, petition, seasonal need, temporary employees, and temporary labor certification, are as described or defined in the Regulations promulgated by the Department of Homeland Security (8 CFR 1.2 and 214.2) as in effect on July 24, 2018.\n##### (b) Other definitions\nThe following terms are defined as below:\n**(1) Secretary**\nSecretary means the Secretary of the Department of Homeland Security or any official to which the Secretary of the Department of Homeland Security has delegated his or her authority.\n**(2) Qualified need**\nThe Governor of Guam shall establish procedures for determining what constitutes a qualified need under this Act.",
      "versionDate": "2025-05-29",
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
        "name": "Immigration",
        "updateDate": "2025-06-12T14:05:27Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3646ih.xml"
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
      "title": "Guam Temporary Workforce Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guam Temporary Workforce Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow the Governor of Guam to determine temporary need of nonimmigrant workers on Guam, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:26Z"
    }
  ]
}
```
