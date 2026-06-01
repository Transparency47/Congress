# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8556?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8556
- Title: Homegrown Defense Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8556
- Origin chamber: House
- Introduced date: 2026-04-28
- Update date: 2026-05-12T22:58:51Z
- Update date including text: 2026-05-12T22:58:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-28: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-04-28: Introduced in House

## Actions

- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Introduced in House
- 2026-04-28 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-28",
    "latestAction": {
      "actionDate": "2026-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8556",
    "number": "8556",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Homegrown Defense Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-12T22:58:51Z",
    "updateDateIncludingText": "2026-05-12T22:58:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-28",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-28",
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
          "date": "2026-04-28T13:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8556ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8556\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2026 Mr. Ruiz introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo improve oversight of Department of Defense compliance with certain requirements for domestic food supply chains, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Homegrown Defense Act of 2026 .\n#### 2. Oversight of Department of Defense compliance with certain requirements for domestic food supply chains\n##### (a) Audits\nNot later than 90 days after the date of the enactment of this Act, and on a quarterly basis thereafter, the Inspector General of the Department of Defense shall conduct an audit to determine the extent of compliance with the requirements of section 4862 of title 10, United States Code, with respect to the procurement of items described in subsection (b)(1)(A) of such section.\n##### (b) Reports to Congress\nNot later than 60 days after the conclusion of each audit under subsection (a), the Inspector General shall submit to the Committees on Armed Services of the House of Representatives and the Senate a report containing the results of such audit.",
      "versionDate": "2026-04-28",
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
        "updateDate": "2026-05-12T22:58:51Z"
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
      "date": "2026-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8556ih.xml"
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
      "title": "Homegrown Defense Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T09:23:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Homegrown Defense Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T09:23:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve oversight of Department of Defense compliance with certain requirements for domestic food supply chains, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T09:18:31Z"
    }
  ]
}
```
