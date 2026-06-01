# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7704
- Title: VA Call Center Multi-Factor Authentication Act
- Congress: 119
- Bill type: HR
- Bill number: 7704
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-28T08:06:00Z
- Update date including text: 2026-04-28T08:06:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7704",
    "number": "7704",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "VA Call Center Multi-Factor Authentication Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:00Z",
    "updateDateIncludingText": "2026-04-28T08:06:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "TN"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "KS"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7704ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7704\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Moore of Alabama (for himself, Mr. Van Epps , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require call centers of the Department of Veterans Affairs to use multi-factor identification to verify the identity of callers in connection with high-impact veteran or beneficiary actions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Call Center Multi-Factor Authentication Act .\n#### 2. Multi-factor authentication required to verify the identity of callers to Veterans Affairs call centers in connection with high-impact veteran or beneficiary actions\nSection 5722(b)(3) of title 38, United States Code, is amended by adding at the end the following: Such controls shall include the use of multi-factor authentication by Department call centers in connection with high-impact veteran or beneficiary actions to verify the identity of the caller and confirm that the participation of the caller in connection with the action is in fact appropriate. As used in the preceding sentence, an action is high-impact if an impersonator could cause real, durable harm to the veteran or beneficiary, such as by diverting funds, manipulating access to accounts, or disclosing sensitive information. .",
      "versionDate": "2026-02-25",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-24T01:07:57Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7704ih.xml"
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
      "title": "VA Call Center Multi-Factor Authentication Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T07:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Call Center Multi-Factor Authentication Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T07:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require call centers of the Department of Veterans Affairs to use multi-factor identification to verify the identity of callers in connection with high-impact veteran or beneficiary actions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T07:18:20Z"
    }
  ]
}
```
