# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/962?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/962
- Title: Defending Veterans’ Second Amendment Rights Act
- Congress: 119
- Bill type: HR
- Bill number: 962
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-07-11T08:05:53Z
- Update date including text: 2025-07-11T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-06 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-06 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/962",
    "number": "962",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000614",
        "district": "21",
        "firstName": "Chip",
        "fullName": "Rep. Roy, Chip [R-TX-21]",
        "lastName": "Roy",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Defending Veterans\u2019 Second Amendment Rights Act",
    "type": "HR",
    "updateDate": "2025-07-11T08:05:53Z",
    "updateDateIncludingText": "2025-07-11T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-06T22:43:48Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr962ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 962\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Roy introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo prohibit the Secretary of Veterans Affairs from transmitting certain information to the Department of Justice for use by the national instant criminal background check system.\n#### 1. Short title\nThis Act may be cited as the Defending Veterans\u2019 Second Amendment Rights Act .\n#### 2. Prohibition on Secretary of Veterans Affairs transmittal of certain information to the Department of Justice for use by the national instant criminal background check system\nThe Secretary of Veterans Affairs may not transmit to any entity in the Department of Justice, for use by the national instant criminal background check system established under section 103 of the Brady Handgun Violence Prevention Act, personally identifiable information on veterans and other beneficiaries, solely on the basis of a determination by the Secretary under chapter 11 of title 38, United States Code, that a person has a service-connected disability.",
      "versionDate": "2025-02-04",
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
            "name": "Criminal justice information and records",
            "updateDate": "2025-04-11T18:14:28Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2025-04-11T18:14:28Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-04-11T18:14:28Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-11T18:14:28Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-04-11T18:14:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-18T18:47:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
    "originChamber": "House",
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
          "measure-id": "id119hr962",
          "measure-number": "962",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-03-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr962v00",
            "update-date": "2025-03-19"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Defending Veterans' Second Amendment Rights Act</strong></p> <p>This bill prohibits the Department of Veterans Affairs from transmitting personally identifiable information of veterans or their beneficiaries to the national instant criminal background check system utilized by licensed importers or dealers of firearms solely on the basis that a veteran has a service-connected disability. </p>"
        },
        "title": "Defending Veterans\u2019 Second Amendment Rights Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr962.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defending Veterans' Second Amendment Rights Act</strong></p> <p>This bill prohibits the Department of Veterans Affairs from transmitting personally identifiable information of veterans or their beneficiaries to the national instant criminal background check system utilized by licensed importers or dealers of firearms solely on the basis that a veteran has a service-connected disability. </p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr962"
    },
    "title": "Defending Veterans\u2019 Second Amendment Rights Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defending Veterans' Second Amendment Rights Act</strong></p> <p>This bill prohibits the Department of Veterans Affairs from transmitting personally identifiable information of veterans or their beneficiaries to the national instant criminal background check system utilized by licensed importers or dealers of firearms solely on the basis that a veteran has a service-connected disability. </p>",
      "updateDate": "2025-03-19",
      "versionCode": "id119hr962"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr962ih.xml"
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
      "title": "Defending Veterans\u2019 Second Amendment Rights Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defending Veterans\u2019 Second Amendment Rights Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of Veterans Affairs from transmitting certain information to the Department of Justice for use by the national instant criminal background check system.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:32Z"
    }
  ]
}
```
