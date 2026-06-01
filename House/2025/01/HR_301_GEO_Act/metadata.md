# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/301?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/301
- Title: GEO Act
- Congress: 119
- Bill type: HR
- Bill number: 301
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-05-22T02:38:25Z
- Update date including text: 2026-05-22T02:38:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-12-09 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-12-16 - Committee: Subcommittee Hearings Held
- 2026-03-05 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-05 - Committee: Ordered to be Reported by Unanimous Consent.
- 2026-03-05 - Committee: Subcommittee on Energy and Mineral Resources Discharged
- 2026-05-20 - Calendars: Placed on the Union Calendar, Calendar No. 568.
- 2026-05-20 - Committee: Reported by the Committee on Natural Resources. H. Rept. 119-654.
- 2026-05-20 - Committee: Reported by the Committee on Natural Resources. H. Rept. 119-654.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-12-09 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-12-16 - Committee: Subcommittee Hearings Held
- 2026-03-05 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-05 - Committee: Ordered to be Reported by Unanimous Consent.
- 2026-03-05 - Committee: Subcommittee on Energy and Mineral Resources Discharged
- 2026-05-20 - Calendars: Placed on the Union Calendar, Calendar No. 568.
- 2026-05-20 - Committee: Reported by the Committee on Natural Resources. H. Rept. 119-654.
- 2026-05-20 - Committee: Reported by the Committee on Natural Resources. H. Rept. 119-654.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/301",
    "number": "301",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001228",
        "district": "2",
        "firstName": "Celeste",
        "fullName": "Rep. Maloy, Celeste [R-UT-2]",
        "lastName": "Maloy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "GEO Act",
    "type": "HR",
    "updateDate": "2026-05-22T02:38:25Z",
    "updateDateIncludingText": "2026-05-22T02:38:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-05-20",
      "calendarNumber": {
        "calendar": "U00568"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 568.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-05-20",
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
      "text": "Reported by the Committee on Natural Resources. H. Rept. 119-654.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-05-20",
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
      "text": "Reported by the Committee on Natural Resources. H. Rept. 119-654.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-05",
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
      "text": "Ordered to be Reported by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-05",
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
      "actionDate": "2026-03-05",
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
      "text": "Subcommittee on Energy and Mineral Resources Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-09",
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
        "item": [
          {
            "date": "2026-05-20T17:50:59Z",
            "name": "Reported By"
          },
          {
            "date": "2026-03-05T17:45:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-09T14:32:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-05T15:00:00Z",
                "name": "Discharged from"
              },
              {
                "date": "2025-12-16T15:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-09T15:00:00Z",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NV"
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
      "sponsorshipDate": "2025-07-21",
      "state": "AK"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "MN"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "NC"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "ID"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr301ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 301\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Maloy introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Geothermal Steam Act of 1970 to establish a deadline for processing applications related to geothermal leasing.\n#### 1. Short title\nThis Act may be cited as the Geothermal Energy Opportunity Act or the GEO Act .\n#### 2. Effect of pending civil actions on processing applications related to geothermal leasing\nSection 4 of the Geothermal Steam Act of 1970 ( 30 U.S.C. 1003 ) is amended by adding at the end the following:\n(h) Effect of pending civil actions on processing applications related to geothermal leasing (1) Requirement to process applications Notwithstanding the existence of any pending civil action that affects an application for a geothermal drilling permit, sundry notice, notice to proceed, right-of-way, or any other authorization under a valid existing geothermal lease, the Secretary shall, unless a United States Federal court vacates or provides injunctive relief for the applicable geothermal lease, geothermal drilling permit, sundry notice, notice to proceed, right-of-way, or other authorization, approve and issue, or deny, each such application not later than 60 days after completing all requirements under applicable Federal laws and regulations, including the National Environmental Policy Act of 1969, the Endangered Species Act of 1973, and division A of subtitle III of title 54, United States Code. (2) No new authority for Federal courts Nothing in this subsection shall be construed as modifying any existing authority of a Federal court to vacate or provide injunctive relief for a geothermal lease, geothermal drilling permit, sundry notice, notice to proceed, right-of-way, or other authorization. (3) Definition of authorization In this subsection, the term authorization means any license, permit, approval, finding, determination, or other administrative decision issued by a Federal agency, or any interagency consultation, that is required or authorized under Federal law or regulations in order to site, construct, reconstruct, or commence operations of a geothermal project administered by a Federal agency. .",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr301rh.xml",
      "text": "IB\nUnion Calendar No. 568\n119th CONGRESS\n2d Session\nH. R. 301\n[Report No. 119\u2013654]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Maloy introduced the following bill; which was referred to the Committee on Natural Resources\nMay 20, 2026 Additional sponsors: Ms. Lee of Nevada , Mr. Begich , Mr. Harder of California , Mr. Stauber , Mr. McDowell , Mr. Fulcher , and Ms. Elfreth\nMay 20, 2026 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo amend the Geothermal Steam Act of 1970 to establish a deadline for processing applications related to geothermal leasing.\n#### 1. Short title\nThis Act may be cited as the Geothermal Energy Opportunity Act or the GEO Act .\n#### 2. Effect of pending civil actions on processing applications related to geothermal leasing\nSection 4 of the Geothermal Steam Act of 1970 ( 30 U.S.C. 1003 ) is amended by adding at the end the following:\n(h) Effect of pending civil actions on processing applications related to geothermal leasing (1) Requirement to process applications Notwithstanding the existence of any pending civil action that affects an application for a geothermal drilling permit, sundry notice, notice to proceed, right-of-way, or any other authorization under a valid existing geothermal lease, the Secretary shall, unless a United States Federal court vacates or provides injunctive relief for the applicable geothermal lease, geothermal drilling permit, sundry notice, notice to proceed, right-of-way, or other authorization, approve and issue, or deny, each such application not later than 60 days after completing all requirements under applicable Federal laws and regulations, including the National Environmental Policy Act of 1969, the Endangered Species Act of 1973, and division A of subtitle III of title 54, United States Code. (2) No new authority for Federal courts Nothing in this subsection shall be construed as modifying any existing authority of a Federal court to vacate or provide injunctive relief for a geothermal lease, geothermal drilling permit, sundry notice, notice to proceed, right-of-way, or other authorization. (3) Definition of authorization In this subsection, the term authorization means any license, permit, approval, finding, determination, or other administrative decision issued by a Federal agency, or any interagency consultation, that is required or authorized under Federal law or regulations in order to site, construct, reconstruct, or commence operations of a geothermal project administered by a Federal agency. .",
      "versionDate": "2026-05-20",
      "versionType": "Reported in House"
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
            "name": "Alternative and renewable resources",
            "updateDate": "2026-01-05T18:09:30Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-01-05T18:09:30Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-01-05T18:09:30Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-01-05T18:09:30Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-01-05T18:09:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-02-07T13:13:14Z"
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
          "measure-id": "id119hr301",
          "measure-number": "301",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr301v00",
            "update-date": "2025-03-12"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Geothermal Energy Opportunity Act or the GEO Act</strong></p><p>This bill expands the Geothermal Steam Act of 1970 to establish a deadline for the Department of the Interior to process applications related to geothermal leases. Specifically, Interior must process each application for a geothermal drilling permit or other authorization under a valid existing geothermal lease within 60 days after completing all requirements under applicable federal laws and regulations (including the National Environmental Policy Act of 1969, the Endangered Species Act of 1973, and the National Historic Preservation Act) unless a U.S. federal court vacates or provides injunctive relief for the underlying lease. \u00a0</p>"
        },
        "title": "GEO Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr301.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Geothermal Energy Opportunity Act or the GEO Act</strong></p><p>This bill expands the Geothermal Steam Act of 1970 to establish a deadline for the Department of the Interior to process applications related to geothermal leases. Specifically, Interior must process each application for a geothermal drilling permit or other authorization under a valid existing geothermal lease within 60 days after completing all requirements under applicable federal laws and regulations (including the National Environmental Policy Act of 1969, the Endangered Species Act of 1973, and the National Historic Preservation Act) unless a U.S. federal court vacates or provides injunctive relief for the underlying lease. \u00a0</p>",
      "updateDate": "2025-03-12",
      "versionCode": "id119hr301"
    },
    "title": "GEO Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Geothermal Energy Opportunity Act or the GEO Act</strong></p><p>This bill expands the Geothermal Steam Act of 1970 to establish a deadline for the Department of the Interior to process applications related to geothermal leases. Specifically, Interior must process each application for a geothermal drilling permit or other authorization under a valid existing geothermal lease within 60 days after completing all requirements under applicable federal laws and regulations (including the National Environmental Policy Act of 1969, the Endangered Species Act of 1973, and the National Historic Preservation Act) unless a U.S. federal court vacates or provides injunctive relief for the underlying lease. \u00a0</p>",
      "updateDate": "2025-03-12",
      "versionCode": "id119hr301"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr301ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr301rh.xml"
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
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "GEO Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-22T02:38:25Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Geothermal Energy Opportunity Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-22T02:38:25Z"
    },
    {
      "title": "GEO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:14:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GEO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-07T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Geothermal Energy Opportunity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-07T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Geothermal Steam Act of 1970 to establish a deadline for processing applications related to geothermal leasing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T04:18:17Z"
    }
  ]
}
```
