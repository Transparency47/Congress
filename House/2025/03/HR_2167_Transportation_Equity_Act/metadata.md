# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2167
- Title: Transportation Equity Act
- Congress: 119
- Bill type: HR
- Bill number: 2167
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-06-26T13:12:15Z
- Update date including text: 2025-06-26T13:12:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-14 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-03-14 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2167",
    "number": "2167",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "W000808",
        "district": "24",
        "firstName": "Frederica",
        "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
        "lastName": "Wilson",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Transportation Equity Act",
    "type": "HR",
    "updateDate": "2025-06-26T13:12:15Z",
    "updateDateIncludingText": "2025-06-26T13:12:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:05:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T20:43:17Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "IN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2167ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2167\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Ms. Wilson of Florida (for herself, Mr. Johnson of Georgia , Mr. Carson , Ms. Tlaib , and Mrs. McIver ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo re-establish an advisory committee to provide independent advice and recommendations to the Secretary of Transportation regarding comprehensive, interdisciplinary issues related to transportation from a variety of stakeholders in transportation planning, design, research, policy, and advocacy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Transportation Equity Act .\n#### 2. Establishment of transportation equity advisory committee\n##### (a) Establishment\nNot later than 120 days after the date of enactment of this Act, the Secretary of Transportation shall establish an advisory committee, to be known as the Transportation Equity Committee (referred to in this Act as the Committee ), regarding comprehensive and interdisciplinary issues related to transportation equity from a variety of stakeholders in transportation planning, design, research, policy, and advocacy.\n##### (b) Purpose of the advisory committee\nThe Committee established under subsection (a) shall provide independent advice and recommendations to the Secretary on transportation equity, including developing a strategic plan with recommendations to the Secretary on national transportation metrics and the effect on such factors as economic development, connectivity, and public engagement.\n##### (c) Duties\nThe Committee shall evaluate the Department's work in connecting people to economic and related forms of opportunity and revitalize communities in carrying out its strategic, research, technological, regulatory, community engagement, and economic policy activities related to transportation and opportunity. Decisions directly affecting implementation of transportation policy remain with the Secretary.\n##### (d) Membership\n**(1) In general**\nThe Secretary shall appoint an odd number of members of not less than 9 but not more than 15 members (with a quorum consisting of a majority of members rounded up to the nearest odd number), to include balanced representation from academia, community groups, industry and business, non-governmental organizations, State and local governments, federally recognized Tribal Governments, advocacy organizations, and indigenous groups with varying points of view.\n**(2) Broad representation**\nTo the extent practicable, members of the Committee shall reflect a variety of backgrounds and experiences, geographic diversity, including urban, rural, tribal, territories, and underserved and marginalized communities throughout the country, and individuals with expertise in related areas such as housing, health care, and the environment.\n**(3) Replacement for non-active members**\nThe Secretary may remove a non-active member who misses 3 consecutive meetings and appoint a replacement to service for the period of time set forth in subsection (f).\n##### (e) Meetings\nThe Committee shall meet not less than 2 times each year with not more than 9 months between meetings at a reasonable time, in a place accessible to the public, and in a room large enough to accommodate the Committee members, staff, and a reasonable number of interested members of the public. The room in which the Committee meets shall be large enough to accommodate at least 100 and shall be compliant with the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ).\n##### (f) Term\nEach member of the Committee shall serve a 2-year term with not more than 2 consecutive term reappointments, but may continue service until a replacement is appointed.\n##### (g) Support\nThe Office of the Under Secretary for Policy of the Department of Transportation shall provide necessary funding, logistics, and administrative support for the Committee.\n##### (h) Application of FACA\nThe Federal Advisory Committee Act (5 U.S.C. app.) shall apply, except section 14, to the Committee established under this section.\n#### 3. Designated federal officer\n##### (a) In general\nThe Secretary of Transportation shall appoint a full-time Federal employee to serve as the coordinator of the Committee on Transportation Equity and act as the Designated Federal Officer for the Transportation Equity Committee. The designated Federal officer shall ensure that administrative support is provided for the Committee.\n##### (b) Responsibilities\nThe Designated Federal Officer shall\u2014\n**(1)**\ncall meetings of the Committee, and any subcommittees that the Committee designates, after consultation with the Chair;\n**(2)**\nformulate and approve an agenda, in consultation with the Chair, for each meeting;\n**(3)**\nnotify all Committee members of the time, place, and agenda for any meeting;\n**(4)**\nprovide administrative support for all meetings of the Committee;\n**(5)**\nattend each Committee and subcommittee meeting;\n**(6)**\nmaintain all Advisory Committee on Transportation Equity files and records, including minutes from each meeting;\n**(7)**\nadjourn any meeting when it is determined to be in the public interest and chair meetings when directed to do so by the Secretary;\n**(8)**\nmake available to the public meeting notes and information; and\n**(9)**\npublish notice of any meeting of the Committee in the Federal Register at least 15 days before such meeting.",
      "versionDate": "2025-03-14",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-04-04T13:43:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2167",
          "measure-number": "2167",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-06-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2167v00",
            "update-date": "2025-06-26"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Transportation Equity Act</strong></p><p>This bill directs the Department of Transportation (DOT) to reestablish an advisory committee to provide independent advice and recommendations to DOT on transportation equity issues.</p><p>The bill designates the committee as the Transportation Equity Committee and requires the committee to also evaluate the work of DOT in connecting people to economic and related forms of opportunity and\u00a0carrying out its strategic, research, technological, regulatory, community engagement, and economic policy activities related to transportation and opportunity.</p><p>In addition, DOT must appoint a full-time federal employee to serve as coordinator and act as the designated federal officer for the committee.\u00a0</p>"
        },
        "title": "Transportation Equity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2167.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Transportation Equity Act</strong></p><p>This bill directs the Department of Transportation (DOT) to reestablish an advisory committee to provide independent advice and recommendations to DOT on transportation equity issues.</p><p>The bill designates the committee as the Transportation Equity Committee and requires the committee to also evaluate the work of DOT in connecting people to economic and related forms of opportunity and\u00a0carrying out its strategic, research, technological, regulatory, community engagement, and economic policy activities related to transportation and opportunity.</p><p>In addition, DOT must appoint a full-time federal employee to serve as coordinator and act as the designated federal officer for the committee.\u00a0</p>",
      "updateDate": "2025-06-26",
      "versionCode": "id119hr2167"
    },
    "title": "Transportation Equity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Transportation Equity Act</strong></p><p>This bill directs the Department of Transportation (DOT) to reestablish an advisory committee to provide independent advice and recommendations to DOT on transportation equity issues.</p><p>The bill designates the committee as the Transportation Equity Committee and requires the committee to also evaluate the work of DOT in connecting people to economic and related forms of opportunity and\u00a0carrying out its strategic, research, technological, regulatory, community engagement, and economic policy activities related to transportation and opportunity.</p><p>In addition, DOT must appoint a full-time federal employee to serve as coordinator and act as the designated federal officer for the committee.\u00a0</p>",
      "updateDate": "2025-06-26",
      "versionCode": "id119hr2167"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2167ih.xml"
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
      "title": "Transportation Equity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Transportation Equity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To re-establish an advisory committee to provide independent advice and recommendations to the Secretary of Transportation regarding comprehensive, interdisciplinary issues related to transportation from a variety of stakeholders in transportation planning, design, research, policy, and advocacy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:21Z"
    }
  ]
}
```
