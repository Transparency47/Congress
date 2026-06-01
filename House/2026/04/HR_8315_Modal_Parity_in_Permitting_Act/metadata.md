# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8315?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8315
- Title: Modal Parity in Permitting Act
- Congress: 119
- Bill type: HR
- Bill number: 8315
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-04-24T18:03:52Z
- Update date including text: 2026-04-24T18:03:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8315",
    "number": "8315",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Modal Parity in Permitting Act",
    "type": "HR",
    "updateDate": "2026-04-24T18:03:52Z",
    "updateDateIncludingText": "2026-04-24T18:03:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
          "date": "2026-04-15T14:03:10Z",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "PA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8315ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8315\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Ms. Titus (for herself, Mr. Bresnahan , and Ms. Friedman ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to clarify the assistance available for recipients of assistance under chapter 53 of such title for acquisition of real property interests, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Modal Parity in Permitting Act .\n#### 2. Acquisition of real property interests\n##### (a) In general\nSection 5323(q) of title 49, United States Code, is amended\u2014\n**(1)**\nin the heading by striking Corridor preservation and inserting Real property interests ;\n**(2)**\nin paragraph (1) by striking right-of-way each time it appears and inserting real property interests ;\n**(3)**\nby inserting acquired after may use the ; and\n**(4)**\nin paragraph (2) by striking Right-of-way and inserting Real property interests .\n##### (b) Updates required\nNot later than 6 months after the date of enactment of this Act the Administrator of the Federal Transit Administration shall update FTA Circular 5010.1F, or any successor circular or regulations, and any other necessary guidance necessary to implement the amendments made by subsection (a).\n#### 3. Passenger rail project transactions\n##### (a) In general\nChapter 242 of title 49, United States Code, is amended by adding at the end the following:\n24203. Passenger rail project transactions (a) Real property interests A recipient of financial assistance under chapter 229, 249, or 243 may use such assistance to acquire through purchase, lease, or otherwise secure or control real property interests before or during the completion of the environmental reviews for a project that may use such property interests if the acquisition or related transaction is otherwise permitted by Federal law. (b) Timing of development A real property interest acquired, leased, or otherwise secured or controlled under subsection (a) may not be physically developed or improved in anticipation of the proposed project until all required environmental reviews for the project have been completed. .\n##### (b) Clerical amendment\nThe analysis for chapter 242 of title 49, United States Code, is amended by adding at the end the following:\n24203. Passenger rail project transactions. .",
      "versionDate": "2026-04-15",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-04-24T18:03:51Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8315ih.xml"
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
      "title": "Modal Parity in Permitting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Modal Parity in Permitting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to clarify the assistance available for recipients of assistance under chapter 53 of such title for acquisition of real property interests, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T05:48:33Z"
    }
  ]
}
```
