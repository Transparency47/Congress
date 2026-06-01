# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/280?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/280
- Title: COAL Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 280
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-09-09T08:05:47Z
- Update date including text: 2025-09-09T08:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-02 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-09-03 - Committee: Subcommittee Hearings Held
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-07-02 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-09-03 - Committee: Subcommittee Hearings Held

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/280",
    "number": "280",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
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
    "title": "COAL Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-09T08:05:47Z",
    "updateDateIncludingText": "2025-09-09T08:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-02",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
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
        "item": {
          "date": "2025-01-09T14:30:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-09-03T13:13:32Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-07-02T13:01:04Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WV"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "MN"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr280ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 280\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Hageman (for herself, Mr. Meuser , and Mrs. Miller of West Virginia ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of the Interior to take certain actions with respect to certain qualified coal applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Combating Obstruction Against Leasing Act of 2025 or the COAL Act of 2025 .\n#### 2. Leasing for certain qualified coal applications\n##### (a) Definitions\nIn this section:\n**(1) Coal lease**\nThe term coal lease means a lease entered into by the United States as lessor, through the Bureau of Land Management, and the applicant on Bureau of Land Management Form 3400\u2013012.\n**(2) Qualified application**\nThe term qualified application means any application pending under the lease by application program administered by the Bureau of Land Management pursuant to the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ) and subpart 3425 of title 43, Code of Federal Regulations (as in effect on the date of the enactment of this Act), for which the environmental review process under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) has commenced.\n##### (b) Mandatory leasing and other required approvals\nAs soon as practicable after the date of the enactment of this Act, the Secretary shall promptly\u2014\n**(1)**\nwith respect to each qualified application\u2014\n**(A)**\nif not previously published for public comment, publish a draft environmental assessment, as required under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) and any applicable implementing regulations;\n**(B)**\nfinalize the fair market value of the coal tract for which a lease by application is pending;\n**(C)**\ntake all intermediate actions necessary to grant the qualified application; and\n**(D)**\ngrant the qualified application; and\n**(2)**\nwith respect to previously awarded coal leases, grant any additional approvals of the Department of the Interior or any bureau, agency, or division of the Department of the Interior required for mining activities to commence.\n#### 3. Future coal leasing\nNotwithstanding any judicial decision to the contrary or a departmental review of the Federal coal leasing program, Secretarial Order 3338, issued by the Secretary of the Interior on January 15, 2016, shall have no force or effect.",
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
            "name": "Coal",
            "updateDate": "2025-03-03T18:07:53Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-03-03T18:08:05Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-03-03T18:08:10Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-03-03T18:07:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-03T21:20:52Z"
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
          "measure-id": "id119hr280",
          "measure-number": "280",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr280v00",
            "update-date": "2025-04-08"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Combating Obstruction Against Leasing Act of 2025 or the COAL Act of 2025</strong></p><p>This bill requires the Bureau of Land Management (BLM)\u00a0to process certain applications to lease\u00a0coal mineral estates owned by the federal government\u00a0in order to develop coal.</p><p>If the environmental review process under the\u00a0National Environmental Policy Act of 1969 has commenced for an application, then the BLM must publish a draft environmental assessment and any applicable implementing regulations, finalize the fair market value of the coal tract for which a lease by application is pending, take all intermediate actions necessary to grant the application, and grant the application.</p><p>With respect to previously awarded coal leases, the BLM must grant any additional approvals required for mining activities to commence.</p><p>Finally, the bill nullifies the Department of the Interior's\u00a0Secretarial Order 3338, which placed a hold on most new federal coal leases\u00a0until the BLM completes a comprehensive review of\u00a0the federal coal program.</p>"
        },
        "title": "COAL Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr280.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Combating Obstruction Against Leasing Act of 2025 or the COAL Act of 2025</strong></p><p>This bill requires the Bureau of Land Management (BLM)\u00a0to process certain applications to lease\u00a0coal mineral estates owned by the federal government\u00a0in order to develop coal.</p><p>If the environmental review process under the\u00a0National Environmental Policy Act of 1969 has commenced for an application, then the BLM must publish a draft environmental assessment and any applicable implementing regulations, finalize the fair market value of the coal tract for which a lease by application is pending, take all intermediate actions necessary to grant the application, and grant the application.</p><p>With respect to previously awarded coal leases, the BLM must grant any additional approvals required for mining activities to commence.</p><p>Finally, the bill nullifies the Department of the Interior's\u00a0Secretarial Order 3338, which placed a hold on most new federal coal leases\u00a0until the BLM completes a comprehensive review of\u00a0the federal coal program.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr280"
    },
    "title": "COAL Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Combating Obstruction Against Leasing Act of 2025 or the COAL Act of 2025</strong></p><p>This bill requires the Bureau of Land Management (BLM)\u00a0to process certain applications to lease\u00a0coal mineral estates owned by the federal government\u00a0in order to develop coal.</p><p>If the environmental review process under the\u00a0National Environmental Policy Act of 1969 has commenced for an application, then the BLM must publish a draft environmental assessment and any applicable implementing regulations, finalize the fair market value of the coal tract for which a lease by application is pending, take all intermediate actions necessary to grant the application, and grant the application.</p><p>With respect to previously awarded coal leases, the BLM must grant any additional approvals required for mining activities to commence.</p><p>Finally, the bill nullifies the Department of the Interior's\u00a0Secretarial Order 3338, which placed a hold on most new federal coal leases\u00a0until the BLM completes a comprehensive review of\u00a0the federal coal program.</p>",
      "updateDate": "2025-04-08",
      "versionCode": "id119hr280"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr280ih.xml"
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
      "title": "COAL Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COAL Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combating Obstruction Against Leasing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Interior to take certain actions with respect to certain qualified coal applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T04:33:38Z"
    }
  ]
}
```
