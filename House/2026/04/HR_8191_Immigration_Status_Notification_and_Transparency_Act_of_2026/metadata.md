# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8191
- Title: Immigration Status Notification and Transparency Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8191
- Origin chamber: House
- Introduced date: 2026-04-02
- Update date: 2026-04-13T14:42:07Z
- Update date including text: 2026-04-13T14:42:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-02: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-02: Introduced in House

## Actions

- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Introduced in House
- 2026-04-02 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-02",
    "latestAction": {
      "actionDate": "2026-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8191",
    "number": "8191",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Immigration Status Notification and Transparency Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-13T14:42:07Z",
    "updateDateIncludingText": "2026-04-13T14:42:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-02",
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
      "actionDate": "2026-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-02",
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
          "date": "2026-04-02T12:31:30Z",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "MA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8191ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8191\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2026 Mr. Subramanyam (for himself and Mr. Moulton ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to provide for electronic notification regarding change in status of immigration petitions or applications.\n#### 1. Short title\nThis Act may be cited as the Immigration Status Notification and Transparency Act of 2026 .\n#### 2. Electronic notification regarding change in status of immigration petitions or applications\n##### (a) In general\nChapter 9 of title II of the Immigration and Nationality Act is amended by adding at the end the following:\n295. Electronic notification regarding change of status for any filing Not later than 24 hours after a change in status with regard to a petition or application under the immigration laws, electronic notification shall be provided of such change to the applicant or petitioner, to any legal representative of such applicant or petitioner, and to each alien to whom the petition or application pertains. The electronic notification shall include at least two of the following: (1) Email. (2) Phone call (including an automated message). (3) Text message. .\n##### (b) Clerical amendment\nThe table of contents for such Act is amended by inserting after the item pertaining to section 294 the following:\n295. Electronic notification regarding change of status for any filing. .",
      "versionDate": "2026-04-02",
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
        "updateDate": "2026-04-13T14:42:07Z"
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
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8191ih.xml"
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
      "title": "Immigration Status Notification and Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Immigration Status Notification and Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to provide for electronic notification regarding change in status of immigration petitions or applications.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:27Z"
    }
  ]
}
```
