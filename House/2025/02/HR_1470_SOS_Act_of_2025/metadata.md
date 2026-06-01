# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1470?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1470
- Title: SOS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1470
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-12-19T09:07:50Z
- Update date including text: 2025-12-19T09:07:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1470",
    "number": "1470",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "SOS Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:50Z",
    "updateDateIncludingText": "2025-12-19T09:07:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:36:50Z",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1470ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1470\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Gottheimer (for himself, Mr. Moskowitz , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide funding for school resource officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Our Schools Act of 2025 or the SOS Act of 2025 .\n#### 2. Funding for school resource officers\nSection 1101(a)(11) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10261(a)(11) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking $1,047,119,000 for each of fiscal years 2006 through 2009 and inserting $1,097,119,000 for each of fiscal years 2026 through 2035 ; and\n**(2)**\nin subparagraph (B), by inserting after of the purposes of part Q the following: , and not less than $50,000,000 shall be allocated for grants pursuant to applications submitted by units of local government or law enforcement agencies for the purposes described in section 1701(b)(12) .",
      "versionDate": "2025-02-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Education programs funding",
            "updateDate": "2025-07-14T15:26:23Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-07-14T15:26:32Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-07-14T15:26:19Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-07-14T15:26:13Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-07-14T15:26:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-18T16:09:13Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1470ih.xml"
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
      "title": "SOS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-18T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SOS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Our Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to provide funding for school resource officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:20Z"
    }
  ]
}
```
