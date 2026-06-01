# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4188?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4188
- Title: VA Flood Preparedness Act
- Congress: 119
- Bill type: HR
- Bill number: 4188
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-03-31T10:58:52Z
- Update date including text: 2026-03-31T10:58:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-28 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-28 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4188",
    "number": "4188",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "VA Flood Preparedness Act",
    "type": "HR",
    "updateDate": "2026-03-31T10:58:52Z",
    "updateDateIncludingText": "2026-03-31T10:58:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-28",
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
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:07:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-28T18:17:04Z",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4188ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4188\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Ms. Mace (for herself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to make certain contributions to local authorities to mitigate the risk of flooding on local property adjacent to medical facilities of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Flood Preparedness Act .\n#### 2. Contributions to local authorities to mitigate the risk of flooding on local property adjacent to medical facilities of the Department of Veterans Affairs\n##### (a) In general\nSection 8108 of title 38, United States Code, is amended by inserting , or to mitigate the risk of flooding, including the risk of flooding associated with rising sea levels before the period at the end.\n##### (b) Report\nNot later than two years after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate a report that includes an assessment of\u2014\n**(1)**\nthe extent to which each medical facility (as such term is defined in section 8101 of such title) is at risk of flooding, including the risk of flooding associated with rising sea levels; and\n**(2)**\nwhether additional resources are necessary to address the risk of flooding at each such facility.",
      "versionDate": "2025-06-26",
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
        "updateDate": "2025-07-09T15:33:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-26",
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
          "measure-id": "id119hr4188",
          "measure-number": "4188",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-26",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4188v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-06-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>VA Flood Preparedness Act</b></p> <p>This bill authorizes the Department of Veterans Affairs (VA) to make contributions to local authorities to mitigate the risk of flooding on local property adjacent to VA medical facilities.</p>"
        },
        "title": "VA Flood Preparedness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4188.xml",
    "summary": {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><b>VA Flood Preparedness Act</b></p> <p>This bill authorizes the Department of Veterans Affairs (VA) to make contributions to local authorities to mitigate the risk of flooding on local property adjacent to VA medical facilities.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4188"
    },
    "title": "VA Flood Preparedness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><b>VA Flood Preparedness Act</b></p> <p>This bill authorizes the Department of Veterans Affairs (VA) to make contributions to local authorities to mitigate the risk of flooding on local property adjacent to VA medical facilities.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4188"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4188ih.xml"
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
      "title": "VA Flood Preparedness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-04T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Flood Preparedness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-04T04:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to make certain contributions to local authorities to mitigate the risk of flooding on local property adjacent to medical facilities of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-04T04:03:43Z"
    }
  ]
}
```
