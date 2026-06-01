# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4079?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4079
- Title: PEARL Act
- Congress: 119
- Bill type: S
- Bill number: 4079
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-04-08T15:21:58Z
- Update date including text: 2026-04-08T15:21:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4079",
    "number": "4079",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "PEARL Act",
    "type": "S",
    "updateDate": "2026-04-08T15:21:58Z",
    "updateDateIncludingText": "2026-04-08T15:21:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-03-12T16:28:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "AZ"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4079is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4079\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Gallego (for himself, Mr. Cornyn , Mr. Kelly , and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo establish in U.S. Customs and Border Protection a pilot program to adopt dogs from local animal shelters to be trained as support dogs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Emotional Assistance with Relief and Love Act or the PEARL Act .\n#### 2. CBP support dog pilot program\n##### (a) In general\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Homeland Security, acting through the Commissioner of U.S. Customs and Border Protection (CBP), shall establish in CBP a pilot program to adopt dogs from local animal shelters to be trained as support dogs for CBP\u2019s Support Canine Program.\n##### (b) Duration\nThe pilot program under subsection (a) shall terminate three years after the date of its establishment.",
      "versionDate": "2026-03-12",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-11-20",
        "text": "Received in the Senate and Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3965",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PEARL Act",
      "type": "HR"
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
        "updateDate": "2026-04-01T16:57:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-12",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s4079",
          "measure-number": "4079",
          "measure-type": "s",
          "orig-publish-date": "2026-03-12",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4079v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2026-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Providing Emotional Assistance with Relief and Love Act or the PEARL Act</strong></p><p>This bill requires U.S. Customs and Border Protection (CBP) to establish\u00a0a pilot program to adopt dogs from local animal shelters to be trained as support dogs for CBP\u2019s Support Canine Program. Support dogs are used for grief assistance, trauma mitigation, and morale.</p>"
        },
        "title": "PEARL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4079.xml",
    "summary": {
      "actionDate": "2026-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Providing Emotional Assistance with Relief and Love Act or the PEARL Act</strong></p><p>This bill requires U.S. Customs and Border Protection (CBP) to establish\u00a0a pilot program to adopt dogs from local animal shelters to be trained as support dogs for CBP\u2019s Support Canine Program. Support dogs are used for grief assistance, trauma mitigation, and morale.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s4079"
    },
    "title": "PEARL Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Providing Emotional Assistance with Relief and Love Act or the PEARL Act</strong></p><p>This bill requires U.S. Customs and Border Protection (CBP) to establish\u00a0a pilot program to adopt dogs from local animal shelters to be trained as support dogs for CBP\u2019s Support Canine Program. Support dogs are used for grief assistance, trauma mitigation, and morale.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s4079"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4079is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "PEARL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PEARL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Providing Emotional Assistance with Relief and Love Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish in U.S. Customs and Border Protection a pilot program to adopt dogs from local animal shelters to be trained as support dogs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:23Z"
    }
  ]
}
```
