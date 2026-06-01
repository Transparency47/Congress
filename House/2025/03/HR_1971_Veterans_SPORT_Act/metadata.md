# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1971?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1971
- Title: Veterans SPORT Act
- Congress: 119
- Bill type: HR
- Bill number: 1971
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-04-16T08:07:10Z
- Update date including text: 2026-04-16T08:07:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Health.
- 2025-03-25 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-03-25 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-10 - Committee: Referred to the Subcommittee on Health.
- 2025-03-25 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-03-25 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1971",
    "number": "1971",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Veterans SPORT Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:07:10Z",
    "updateDateIncludingText": "2026-04-16T08:07:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
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
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-03-25T18:08:09Z",
                "name": "Reported by"
              },
              {
                "date": "2025-03-25T18:07:43Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-10T21:32:50Z",
                "name": "Referred to"
              }
            ]
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
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1971ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1971\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mrs. Miller-Meeks introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to include adaptive prostheses and terminal devices for sports and other recreational activities in the medical services furnished to eligible veterans by the Secretary of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act or the Veterans SPORT Act .\n#### 2. Inclusion of adaptive prostheses and terminal devices for sports and other recreational activities in medical services furnished to eligible veterans by the Secretary of Veterans Affairs\nSection 1701 of title 38, United States Code, is amended, in paragraph (6)(F)(i), by inserting (including adaptive prostheses and terminal devices for sports and other recreational activities) after artificial limbs .",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-18",
        "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably."
      },
      "number": "3138",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Veterans SPORT Act",
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
            "name": "Athletes",
            "updateDate": "2025-04-01T15:33:07Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-04-01T15:32:52Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2025-04-01T15:33:03Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-04-01T15:32:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-26T15:14:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hr1971",
          "measure-number": "1971",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1971v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act or the Veterans SPORT Act</strong></p><p>This bill includes adaptive prostheses and terminal devices for sports and other recreational activities within the definition of <em>medical services</em> under the laws administered by the Department of Veterans Affairs (VA). Under the bill, these artificial limbs must be furnished as medical services to eligible veterans.</p>"
        },
        "title": "Veterans SPORT Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1971.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act or the Veterans SPORT Act</strong></p><p>This bill includes adaptive prostheses and terminal devices for sports and other recreational activities within the definition of <em>medical services</em> under the laws administered by the Department of Veterans Affairs (VA). Under the bill, these artificial limbs must be furnished as medical services to eligible veterans.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hr1971"
    },
    "title": "Veterans SPORT Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act or the Veterans SPORT Act</strong></p><p>This bill includes adaptive prostheses and terminal devices for sports and other recreational activities within the definition of <em>medical services</em> under the laws administered by the Department of Veterans Affairs (VA). Under the bill, these artificial limbs must be furnished as medical services to eligible veterans.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hr1971"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1971ih.xml"
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
      "title": "Veterans SPORT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans SPORT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Supporting Prosthetics Opportunities and Recreational Therapy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to include adaptive prostheses and terminal devices for sports and other recreational activities in the medical services furnished to eligible veterans by the Secretary of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:20Z"
    }
  ]
}
```
