# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/241?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/241
- Title: Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 241
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-07-15T08:05:52Z
- Update date including text: 2025-07-15T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-11 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-11 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/241",
    "number": "241",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "Y000067",
        "district": "2",
        "firstName": "Rudy",
        "fullName": "Rep. Yakym, Rudy [R-IN-2]",
        "lastName": "Yakym",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act",
    "type": "HR",
    "updateDate": "2025-07-15T08:05:52Z",
    "updateDateIncludingText": "2025-07-15T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:39:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-11T22:37:12Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr241ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 241\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Yakym introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for access standards with respect to the provision by the Department of Veterans Affairs of hospital care, medical services, or extended care services that are applicable to certain veterans with mental disorders.\n#### 1. Short title\nThis Act may be cited as the Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act .\n#### 2. Department of Veterans Affairs community care access standards for certain veterans with mental disorders\nSection 1703B(a) of title 38, United States Code, is amended by adding at the end the following new paragraph:\n(3) The access standards required under this subsection shall provide that in the case of a covered veteran with a service-connected mental disorder rated at 50 percent or more, the Department shall furnish hospital care, medical services, or extended care services for such mental disorder by not later than five days after the date on which the covered veteran requests such care or services. .",
      "versionDate": "2025-01-09",
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
            "name": "Health care coverage and access",
            "updateDate": "2025-03-05T16:09:08Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-03-05T16:09:04Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-05T16:08:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-12T15:42:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr241",
          "measure-number": "241",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr241v00",
            "update-date": "2025-02-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish care or services under the Veterans Community Care Program (VCCP) to an eligible veteran with a service-connected mental disorder not later than five days after the veteran seeks care for such disorder. Current law requires the VA to establish access standards for furnishing hospital care, medical services, or extended care services under the VCCP to veterans who are (1) enrolled in the VA health care system, or (2) not enrolled but are in the 12-month period following their discharge from service and meet other requirements (e.g., having a service-connected disability).</p><p>Under the bill, the VA must modify its access standards for furnishing such care and services under the VCCP to require the provision of care or services not later than five days after an eligible veteran with a service-connected mental disorder rated at 50% or more seeks treatment for such disorder.</p>"
        },
        "title": "Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr241.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish care or services under the Veterans Community Care Program (VCCP) to an eligible veteran with a service-connected mental disorder not later than five days after the veteran seeks care for such disorder. Current law requires the VA to establish access standards for furnishing hospital care, medical services, or extended care services under the VCCP to veterans who are (1) enrolled in the VA health care system, or (2) not enrolled but are in the 12-month period following their discharge from service and meet other requirements (e.g., having a service-connected disability).</p><p>Under the bill, the VA must modify its access standards for furnishing such care and services under the VCCP to require the provision of care or services not later than five days after an eligible veteran with a service-connected mental disorder rated at 50% or more seeks treatment for such disorder.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr241"
    },
    "title": "Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to furnish care or services under the Veterans Community Care Program (VCCP) to an eligible veteran with a service-connected mental disorder not later than five days after the veteran seeks care for such disorder. Current law requires the VA to establish access standards for furnishing hospital care, medical services, or extended care services under the VCCP to veterans who are (1) enrolled in the VA health care system, or (2) not enrolled but are in the 12-month period following their discharge from service and meet other requirements (e.g., having a service-connected disability).</p><p>Under the bill, the VA must modify its access standards for furnishing such care and services under the VCCP to require the provision of care or services not later than five days after an eligible veteran with a service-connected mental disorder rated at 50% or more seeks treatment for such disorder.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr241"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr241ih.xml"
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
      "title": "Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sergeant Ted Grubbs Mental Healthcare for Disabled Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for access standards with respect to the provision by the Department of Veterans Affairs of hospital care, medical services, or extended care services that are applicable to certain veterans with mental disorders.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:18Z"
    }
  ]
}
```
