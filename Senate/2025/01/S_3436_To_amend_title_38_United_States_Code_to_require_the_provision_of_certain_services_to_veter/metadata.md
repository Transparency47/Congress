# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3436?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3436
- Title: Caring for Veterans and Strengthening National Security Act
- Congress: 119
- Bill type: S
- Bill number: 3436
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2025-12-19T17:32:05Z
- Update date including text: 2025-12-19T17:32:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-17 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8874; text: CR S8874)
- 2025-12-17 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-17 - Discharge: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-17 - Committee: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-18 - Floor: Message on Senate action sent to the House.
- 2025-12-18 09:57:08 - Floor: Received in the House.
- 2025-12-18 10:04:33 - Floor: Held at the desk.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-17 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8874; text: CR S8874)
- 2025-12-17 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-17 - Discharge: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-17 - Committee: Senate Committee on Veterans' Affairs discharged by Unanimous Consent.
- 2025-12-18 - Floor: Message on Senate action sent to the House.
- 2025-12-18 09:57:08 - Floor: Received in the House.
- 2025-12-18 10:04:33 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3436",
    "number": "3436",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Caring for Veterans and Strengthening National Security Act",
    "type": "S",
    "updateDate": "2025-12-19T17:32:05Z",
    "updateDateIncludingText": "2025-12-19T17:32:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-18",
      "actionTime": "10:04:33",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-18",
      "actionTime": "09:57:08",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S8874; text: CR S8874)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Veterans' Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Veterans' Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
        "item": [
          {
            "date": "2025-12-18T01:01:40Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-12-11T16:52:42Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "HI"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "MS"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "HI"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "ID"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AK"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NM"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3436is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3436\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Moran (for himself, Mr. Schatz , Mr. Wicker , Ms. Hirono , Mr. Boozman , Mr. Blumenthal , Mr. Risch , Ms. Murkowski , Mr. Heinrich , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the provision of certain services to veterans in the Freely Associated States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Caring for Veterans and Strengthening National Security Act .\n#### 2. Requirement to provide certain services to veterans in the Freely Associated States\n##### (a) Telehealth and mail order pharmacy benefits\nSection 1724(f)(1) of title 38, United States Code, is amended by adding at the end the following:\n(C) Not later than one year after the date of the enactment of the Caring for Veterans and Strengthening National Security Act , the Secretary shall furnish to veterans described in subparagraph (A), subject to agreements described in such subparagraph, telehealth benefits and mail order pharmacy benefits. .\n##### (b) Beneficiary travel\nSection 111(h)(1) of such title is amended by striking the Secretary may make payments and inserting beginning not later than one year after the date of the enactment of the Caring for Veterans and Strengthening National Security Act , the Secretary shall make payments .\n##### (c) Quarterly report\n**(1) In general**\nNot less frequently than quarterly, the Secretary of Veterans Affairs shall submit to the appropriate committees of Congress a report on the status of implementation of the amendments made by this section and the cost of such implementation.\n**(2) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the House of Representatives.\n#### 3. Extension of certain limits on payments of pension\nSection 5503(d)(7) of title 38, United States Code, is amended by striking January 31, 2033 and inserting March 31, 2033 .",
      "versionDate": "2025-12-11",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3436es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 3436\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend title 38, United States Code, to require the provision of certain services to veterans in the Freely Associated States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Caring for Veterans and Strengthening National Security Act .\n#### 2. Requirement to provide certain services to veterans in the Freely Associated States\n##### (a) Telehealth and mail order pharmacy benefits\nSection 1724(f)(1) of title 38, United States Code, is amended by adding at the end the following:\n(C) Not later than one year after the date of the enactment of the Caring for Veterans and Strengthening National Security Act , the Secretary shall furnish to veterans described in subparagraph (A), subject to agreements described in such subparagraph, telehealth benefits and mail order pharmacy benefits. .\n##### (b) Beneficiary travel\nSection 111(h)(1) of such title is amended by striking the Secretary may make payments and inserting beginning not later than one year after the date of the enactment of the Caring for Veterans and Strengthening National Security Act , the Secretary shall make payments .\n##### (c) Quarterly report\n**(1) In general**\nNot less frequently than quarterly, the Secretary of Veterans Affairs shall submit to the appropriate committees of Congress a report on the status of implementation of the amendments made by this section and the cost of such implementation.\n**(2) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Veterans\u2019 Affairs and the Committee on Appropriations of the House of Representatives.\n#### 3. Extension of certain limits on payments of pension\nSection 5503(d)(7) of title 38, United States Code, is amended by striking January 31, 2033 and inserting March 31, 2033 .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-19T17:31:45Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-12-19T17:32:05Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-12-19T17:31:14Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-12-19T17:31:20Z"
          },
          {
            "name": "Marshall Islands",
            "updateDate": "2025-12-19T17:31:50Z"
          },
          {
            "name": "Micronesia",
            "updateDate": "2025-12-19T17:31:54Z"
          },
          {
            "name": "Palau",
            "updateDate": "2025-12-19T17:31:58Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-12-19T17:31:36Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-12-19T17:31:32Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-12-19T17:31:40Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-12-19T17:31:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-16T17:03:39Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3436is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3436es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Caring for Veterans and Strengthening National Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:03:17Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Caring for Veterans and Strengthening National Security Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-18T06:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to require the provision of certain services to veterans in the Freely Associated States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-16T15:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Caring for Veterans and Strengthening National Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-16T14:53:17Z"
    }
  ]
}
```
