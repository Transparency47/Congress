# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/281?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/281
- Title: Grizzly Bear State Management Act
- Congress: 119
- Bill type: HR
- Bill number: 281
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-02-04T05:06:17Z
- Update date including text: 2026-02-04T05:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-15 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-15 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 20 - 19.
- 2025-10-03 - Calendars: Placed on the Union Calendar, Calendar No. 281.
- 2025-10-03 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-328.
- 2025-10-03 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-328.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-15 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-15 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 20 - 19.
- 2025-10-03 - Calendars: Placed on the Union Calendar, Calendar No. 281.
- 2025-10-03 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-328.
- 2025-10-03 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-328.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/281",
    "number": "281",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Grizzly Bear State Management Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:17Z",
    "updateDateIncludingText": "2026-02-04T05:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-10-03",
      "calendarNumber": {
        "calendar": "U00281"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 281.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-328.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-328.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 20 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
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
        "item": [
          {
            "date": "2025-10-03T20:19:09Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-15T21:15:40Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-09T14:31:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MT"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "ID"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MN"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr281ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 281\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Hageman (for herself, Mr. Zinke , Mr. Fulcher , Mr. Stauber , and Mr. Downing ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to reissue a final rule relating to removing the Greater Yellowstone Ecosystem population of grizzly bears from the Federal list of endangered and threatened wildlife, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Grizzly Bear State Management Act of 2025 .\n#### 2. Reissuance of final rule relating to Greater Yellowstone Ecosystem population of grizzly bears\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Interior shall reissue the final rule entitled Endangered and Threatened Wildlife and Plants; Removing the Greater Yellowstone Ecosystem Population of Grizzly Bears From the Federal List of Endangered and Threatened Wildlife (82 Fed. Reg. 30502 (June 30, 2017)) without regard to any other provision of law that applies to the issuance of that final rule.\n##### (b) No judicial review\nThe reissuance of the final rule described in subsection (a) (including this section) shall not be subject to judicial review.",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr281rh.xml",
      "text": "IB\nUnion Calendar No. 281\n119th CONGRESS\n1st Session\nH. R. 281\n[Report No. 119\u2013328]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Hageman (for herself, Mr. Zinke , Mr. Fulcher , Mr. Stauber , and Mr. Downing ) introduced the following bill; which was referred to the Committee on Natural Resources\nOctober 3, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on January 9, 2025\nA BILL\nTo direct the Secretary of the Interior to reissue a final rule relating to removing the Greater Yellowstone Ecosystem population of grizzly bears from the Federal list of endangered and threatened wildlife, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Grizzly Bear State Management Act .\n#### 2. Reissuance of final rule relating to Greater Yellowstone Ecosystem population of grizzly bears\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Interior shall reissue the final rule entitled Endangered and Threatened Wildlife and Plants; Removing the Greater Yellowstone Ecosystem Population of Grizzly Bears From the Federal List of Endangered and Threatened Wildlife (82 Fed. Reg. 30502 (June 30, 2017)) without regard to any other provision of law that applies to the issuance of that final rule.\n##### (b) No judicial review\nThe reissuance of the final rule described in subsection (a) (including this section) shall not be subject to judicial review.",
      "versionDate": "2025-10-03",
      "versionType": "Reported in House"
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
        "actionDate": "2025-01-29",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "316",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Grizzly Bear State Management Act of 2025",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-07-28T20:00:20Z"
          },
          {
            "name": "Department of the Interior",
            "updateDate": "2025-07-28T20:00:20Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2025-07-28T20:00:20Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2025-07-28T20:00:20Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-07-28T20:00:20Z"
          },
          {
            "name": "Mammals",
            "updateDate": "2025-07-28T20:00:20Z"
          },
          {
            "name": "Montana",
            "updateDate": "2025-07-28T20:00:20Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2025-07-28T20:00:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-02-08T13:31:23Z"
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
          "measure-id": "id119hr281",
          "measure-number": "281",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr281v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Grizzly Bear State Management Act of 2025</strong></p><p>This bill requires the\u00a0U.S. Fish and Wildlife Service\u00a0to\u00a0reissue the final rule\u00a0titled\u00a0<em>Endangered and Threatened Wildlife and Plants; Removing the Greater Yellowstone Ecosystem Population of Grizzly Bears From the Federal List of Endangered and Threatened Wildlife\u00a0</em>and published on\u00a0June 30, 2017.</p><p>In addition, the bill exempts the rule from judicial review.</p>"
        },
        "title": "Grizzly Bear State Management Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr281.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Grizzly Bear State Management Act of 2025</strong></p><p>This bill requires the\u00a0U.S. Fish and Wildlife Service\u00a0to\u00a0reissue the final rule\u00a0titled\u00a0<em>Endangered and Threatened Wildlife and Plants; Removing the Greater Yellowstone Ecosystem Population of Grizzly Bears From the Federal List of Endangered and Threatened Wildlife\u00a0</em>and published on\u00a0June 30, 2017.</p><p>In addition, the bill exempts the rule from judicial review.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr281"
    },
    "title": "Grizzly Bear State Management Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Grizzly Bear State Management Act of 2025</strong></p><p>This bill requires the\u00a0U.S. Fish and Wildlife Service\u00a0to\u00a0reissue the final rule\u00a0titled\u00a0<em>Endangered and Threatened Wildlife and Plants; Removing the Greater Yellowstone Ecosystem Population of Grizzly Bears From the Federal List of Endangered and Threatened Wildlife\u00a0</em>and published on\u00a0June 30, 2017.</p><p>In addition, the bill exempts the rule from judicial review.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr281"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr281ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr281rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Grizzly Bear State Management Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Grizzly Bear State Management Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Grizzly Bear State Management Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to reissue a final rule relating to removing the Greater Yellowstone Ecosystem population of grizzly bears from the Federal list of endangered and threatened wildlife, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:31Z"
    }
  ]
}
```
