# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8796?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8796
- Title: Federal Halo Act
- Congress: 119
- Bill type: HR
- Bill number: 8796
- Origin chamber: House
- Introduced date: 2026-05-13
- Update date: 2026-05-22T13:39:00Z
- Update date including text: 2026-05-22T13:39:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-13: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-13: Introduced in House

## Actions

- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Introduced in House
- 2026-05-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-13",
    "latestAction": {
      "actionDate": "2026-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8796",
    "number": "8796",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Federal Halo Act",
    "type": "HR",
    "updateDate": "2026-05-22T13:39:00Z",
    "updateDateIncludingText": "2026-05-22T13:39:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-13",
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
      "actionDate": "2026-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-13",
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
          "date": "2026-05-13T14:04:20Z",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "MS"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8796ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8796\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2026 Ms. Malliotakis (for herself, Mr. Ezell , and Mr. McGuire ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish a safety buffer zone to protect certain Federal law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Halo Act .\n#### 2. Criminal penalty for obstructing Federal law enforcement officer activities\n##### (a) In general\nChapter 73 of title 18, United States Code, is amended by adding at the end the following:\n1522. Obstructing law enforcement activities (a) Definitions In this section: (1) Federal law enforcement officer The term Federal law enforcement officer means any Federal law enforcement officer or agent who is engaged in the lawful performance of duties. (2) Harass The term harass means to knowingly engage in a course of conduct directed at a Federal law enforcement officer that intentionally causes substantial emotional distress in that Federal law enforcement officer and serves no legitimate purpose. (b) Offense It shall be unlawful for a person, after receiving a verbal warning not to approach from an individual whom the person knows or reasonably should know is a Federal law enforcement officer, and who is engaged in the lawful performance of a legal duty, to knowingly violate the warning and approach or remain within 15 feet of the Federal law enforcement officer with the intent to\u2014 (1) impede or interfere with the ability of the Federal Law Enforcement Officer to perform that legal duty; (2) threaten the Federal Law Enforcement Officer with physical harm; or (3) harass the Federal Law Enforcement Officer. (c) Penalty Any person who violates subsection (b) shall be fined under this title, imprisoned for not more than 5 years, or both. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 73 of title 18, United States Code, is amended by adding at the end the following:\n1522. Obstructing law enforcement activities. .",
      "versionDate": "2026-05-13",
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
        "updateDate": "2026-05-22T13:39:00Z"
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
      "date": "2026-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8796ih.xml"
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
      "title": "Federal Halo Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Halo Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to establish a safety buffer zone to protect certain Federal law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T08:18:26Z"
    }
  ]
}
```
