# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5855?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5855
- Title: Measuring the Cost of Disasters Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5855
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2025-12-09T22:33:35Z
- Update date including text: 2025-12-09T22:33:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5855",
    "number": "5855",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
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
    "title": "Measuring the Cost of Disasters Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-09T22:33:35Z",
    "updateDateIncludingText": "2025-12-09T22:33:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "OR"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5855ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5855\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Mr. Neguse (for himself, Ms. Lofgren , Ms. Hoyle of Oregon , and Ms. Elfreth ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo require the Administrator of the National Oceanic and Atmospheric Administration to establish and maintain a database and webpage that is available to the public and contains information on the billion-dollar disasters that occur each year in the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Measuring the Cost of Disasters Act of 2025 .\n#### 2. Database and webpage for information on billion-dollar disasters\n##### (a) In general\nThe Administrator of the National Oceanic and Atmospheric Administration (in this section referred to as the Administrator ) shall establish and maintain a database and webpage that is available to the public and contains information on each billion-dollar disaster that occurs each year in the United States.\n##### (b) Update\nNot less frequently than biannually, the Administrator shall update the database and webpage required under subsection (a) as new information is available.\n##### (c) Matters To Be included\nThe database and webpage required under subsection (a) shall include the following:\n**(1)**\nWith respect to each billion-dollar disaster included in the database and webpage\u2014\n**(A)**\nthe estimated cost of the disaster;\n**(B)**\nthe type of disaster;\n**(C)**\nthe location of the disaster;\n**(D)**\nthe date or dates of the disaster; and\n**(E)**\nsuch other information regarding the disaster as the Administrator considers appropriate.\n**(2)**\nVisual graphs and mapping features showing the trajectory of disasters over time and the distribution of types of disasters across the United States that are similar, if not identical, to those features produced by the National Centers for Environmental Information from 1980 through 2024 and that were available and updated online at www.ncei.noaa.gov/access/billions/ until May 9, 2025.\n##### (d) Data To Be used\nIn establishing and maintaining the database required under subsection (a), the Administrator shall use data available to the Administrator and may collaborate with Federal and non-Federal partners as necessary, such as those partners with which the Administrator collaborated previously while the database specified under subsection (c)(2) was active from 1980 through 2024.\n##### (e) Inclusion of other disasters\nThe Administrator may include in the database required under subsection (a) a disaster that is not a billion-dollar disaster if the Administrator determines that the inclusion of the disaster in the database would be appropriate.\n##### (f) Maintenance of existing database\nThe Administrator shall maintain and update information contained in the previously existing disaster database specified under subsection (c)(2) on the webpage for the National Centers for Environmental Information for archiving and research purposes.\n##### (g) Billion-Dollar disaster defined\nIn this section, the term billion-dollar disaster means a storm or severe weather event that results in $1,000,000,000 or more in combined direct costs and market costs as determined by the National Centers for Environmental Information.",
      "versionDate": "2025-10-28",
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
        "actionDate": "2025-09-11",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2775",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Measuring the Cost of Disasters Act of 2025",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-09T22:33:35Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5855ih.xml"
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
      "title": "Measuring the Cost of Disasters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T08:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Measuring the Cost of Disasters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-29T08:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the National Oceanic and Atmospheric Administration to establish and maintain a database and webpage that is available to the public and contains information on the billion-dollar disasters that occur each year in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-29T08:48:50Z"
    }
  ]
}
```
