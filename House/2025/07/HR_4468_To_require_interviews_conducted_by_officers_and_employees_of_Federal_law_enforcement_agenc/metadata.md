# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4468?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4468
- Title: Federal Interviews Reform Act
- Congress: 119
- Bill type: HR
- Bill number: 4468
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2025-09-09T14:16:54Z
- Update date including text: 2025-09-09T14:16:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4468",
    "number": "4468",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "T000165",
        "district": "7",
        "firstName": "Thomas",
        "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
        "lastName": "Tiffany",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Federal Interviews Reform Act",
    "type": "HR",
    "updateDate": "2025-09-09T14:16:54Z",
    "updateDateIncludingText": "2025-09-09T14:16:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:04:15Z",
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
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4468ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4468\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Tiffany (for himself, Mr. Nehls , and Mr. Cline ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require interviews conducted by officers and employees of Federal law enforcement agencies to be recorded.\n#### 1. Short title\nThis Act may be cited as the Federal Interviews Reform Act .\n#### 2. Audio recording of interviews conducted by certain Federal law enforcement officers\n##### (a) In general\nThe Attorney General shall require the recording, using an electronic audio or video recording technology, of each interview of any person who is suspected of having committed a criminal offense conducted by an officer or employee of the Department of Justice in connection with an investigation of a Federal offense or an investigation with respect to which the Department is assisting a State, local, or tribal law enforcement agency.\n##### (b) Application\n**(1) Custodial and non-custodial interviews**\nThe requirements under this section apply with respect to any custodial and non-custodial interview, but do not apply with respect to communication with a confidential informant.\n**(2) Extraterritorial application**\nThe requirements under this section apply with respect to any interview of a United States citizen outside of the United States conducted by an officer or employee of the Department of Justice.\n##### (c) Notification, consent not required\nAn officer or employee of the Department of Justice may record an interview described in this section without providing notice to or obtaining consent from the interviewee.\n##### (d) Inadmissibility\nA statement or information obtained during an interview that is not recorded in accordance with this section may not be offered as evidence by the Government in Federal court.\n##### (e) Retention\n**(1) In general**\nExcept as provided in paragraph (2), a recording of an interview described in this section shall be retained for a period of 10 years beginning on the date on which the applicable investigation or any related judicial procedures is finally concluded, whichever is later.\n**(2) Exception**\nA recording of an interview described in this section shall be retained indefinitely if the content of the recording is related to a judicial proceeding that involves a Federal capital offense or a State capital offense with respect to which the Federal law enforcement officer was assisting the law enforcement agency of the jurisdiction in which the offense occurred.\n##### (f) Rules\nThe Attorney General shall finalize rules to carry out this section not later than 180 days after the date of enactment of this Act.",
      "versionDate": "2025-07-16",
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
        "updateDate": "2025-09-09T14:16:54Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4468ih.xml"
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
      "title": "Federal Interviews Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Interviews Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require interviews conducted by officers and employees of Federal law enforcement agencies to be recorded.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T05:48:17Z"
    }
  ]
}
```
