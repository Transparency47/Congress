# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6954?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6954
- Title: January 6th Truth and Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 6954
- Origin chamber: House
- Introduced date: 2026-01-06
- Update date: 2026-01-22T15:30:51Z
- Update date including text: 2026-01-22T15:30:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-06: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-06: Introduced in House

## Actions

- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Introduced in House
- 2026-01-06 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-06",
    "latestAction": {
      "actionDate": "2026-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6954",
    "number": "6954",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "January 6th Truth and Transparency Act",
    "type": "HR",
    "updateDate": "2026-01-22T15:30:51Z",
    "updateDateIncludingText": "2026-01-22T15:30:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-06",
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
      "actionDate": "2026-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-06",
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
          "date": "2026-01-06T23:30:35Z",
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
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "CA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "IL"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6954ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6954\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2026 Mrs. Torres of California (for herself, Ms. Friedman , Ms. Kelly of Illinois , and Mrs. Fletcher ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo direct the Director of the Congressional Research Service to prepare a report extent of recidivism by individuals pardoned by the President under Presidential Proclamation 10887, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the January 6th Truth and Transparency Act .\n#### 2. Report on recidivism by 1/6 insurrectionists\n##### (a) Report\nNot later than 60 days after the date of enactment of this Act, and every 180 days thereafter, the Director of the Congressional Research Service shall submit to the appropriate congressional committees and make publicly available on the website of the Library of Congress, a report on the extent of recidivism by individuals pardoned by the President under Presidential Proclamation 10887 entitled Granting Pardons and Commutation of Sentences for Certain Offenses Relating to the Events at or Near the United States Capitol on January 6, 2021 (January 20, 2025).\n##### (b) Contents\nThe report under subsection (a) shall contain\u2014\n**(1)**\na list of each individual who was pardoned by, had their sentence commuted by, or with respect to whom a pending indictment was dismissed pursuant to the Presidential Proclamation referred to in subsection (a);\n**(2)**\na list of each individual described in paragraph (1) who has been arrested for, charged with, or convicted of a criminal offense under Federal, State, or local law, during the period beginning on January 20, 2025, and ending on the date of the report, including a description of each such criminal offense;\n**(3)**\na list of each individual described in paragraph (1) who has been involved in an encounter with Federal, State, or local law enforcement, that involved the use of force by a law enforcement officer against the individual; and\n**(4)**\nany other information the Director of the Congressional Research Service determines appropriate.\n##### (c) Appropriate congressional committees\nIn this section, the term appropriate congressional committees means\n**(1)**\nthe Committee on House Administration of the House of Representatives;\n**(2)**\nthe Committee on Rules and Administration of the Senate; and\n**(3)**\nthe Committees on Appropriations of the House of Representatives and of the Senate.",
      "versionDate": "2026-01-06",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-22T15:30:51Z"
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
      "date": "2026-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6954ih.xml"
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
      "title": "January 6th Truth and Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T11:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "January 6th Truth and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the Congressional Research Service to prepare a report extent of recidivism by individuals pardoned by the President under Presidential Proclamation 10887, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T11:18:34Z"
    }
  ]
}
```
