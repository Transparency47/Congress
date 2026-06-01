# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1687?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1687
- Title: CLEAN Act
- Congress: 119
- Bill type: HR
- Bill number: 1687
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-05-29T21:26:24Z
- Update date including text: 2026-05-29T21:26:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-12-09 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-12-16 - Committee: Subcommittee Hearings Held
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported in the Nature of a Substitute by Unanimous Consent.
- 2026-04-21 - Committee: Subcommittee on Energy and Mineral Resources Discharged
- 2026-05-20 - Calendars: Placed on the Union Calendar, Calendar No. 571.
- 2026-05-20 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-657.
- 2026-05-20 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-657.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2025-12-09 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2025-12-16 - Committee: Subcommittee Hearings Held
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported in the Nature of a Substitute by Unanimous Consent.
- 2026-04-21 - Committee: Subcommittee on Energy and Mineral Resources Discharged
- 2026-05-20 - Calendars: Placed on the Union Calendar, Calendar No. 571.
- 2026-05-20 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-657.
- 2026-05-20 - Committee: Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-657.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1687",
    "number": "1687",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "F000469",
        "district": "1",
        "firstName": "Russ",
        "fullName": "Rep. Fulcher, Russ [R-ID-1]",
        "lastName": "Fulcher",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "CLEAN Act",
    "type": "HR",
    "updateDate": "2026-05-29T21:26:24Z",
    "updateDateIncludingText": "2026-05-29T21:26:24Z"
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
        "calendar": "U00571"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 571.",
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
      "text": "Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-657.",
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
      "text": "Reported (Amended) by the Committee on Natural Resources. H. Rept. 119-657.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
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
      "text": "Ordered to be Reported in the Nature of a Substitute by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
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
      "actionDate": "2026-04-21",
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
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
            "date": "2026-05-20T17:51:42Z",
            "name": "Reported By"
          },
          {
            "date": "2026-04-21T17:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-27T14:06:00Z",
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
                "date": "2026-04-21T17:00:00Z",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "UT"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1687ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1687\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Fulcher (for himself, Ms. Maloy , and Ms. Boebert ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Geothermal Steam Act of 1970 to increase the frequency of lease sales, to require replacement sales, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Committing Leases for Energy Access Now Act or the CLEAN Act .\n#### 2. Geothermal leasing\n##### (a) Annual leasing\nSection 4(b) of the Geothermal Steam Act of 1970 ( 30 U.S.C. 1003(b) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking 2 years and inserting year ;\n**(2)**\nby redesignating paragraphs (3) and (4) as paragraphs (5) and (6), respectively; and\n**(3)**\nafter paragraph (2), by inserting the following:\n(3) Replacement Sales If a lease sale under paragraph (1) for a year is canceled or delayed, the Secretary of the Interior shall conduct a replacement sale during the same year. (4) Requirement In conducting a lease sale under paragraph (2) in a State described in that paragraph, the Secretary of the Interior shall offer all nominated parcels eligible for geothermal development and utilization under the resource management plan in effect for the State. .\n##### (b) Deadlines for consideration of geothermal drilling permits\nSection 4 of the Geothermal Steam Act of 1970 ( 30 U.S.C. 1003 ) is amended by adding at the end the following:\n(h) Deadlines for consideration of geothermal drilling permits (1) Notice Not later than 30 days after the date on which the Secretary receives an application for any geothermal drilling permit, the Secretary shall\u2014 (A) provide written notice to the applicant that the application is complete; or (B) notify the applicant that information is missing and specify any information that is required to be submitted for the application to be complete. (2) Issuance of decision If the Secretary determines that an application for a geothermal drilling permit is complete under paragraph (1)(A), the Secretary shall issue a final decision on the application not later than 30 days after the Secretary notifies the applicant that the application is complete. .",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr1687rh.xml",
      "text": "IB\nUnion Calendar No. 571\n119th CONGRESS\n2d Session\nH. R. 1687\n[Report No. 119\u2013657]\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Fulcher (for himself, Ms. Maloy , and Ms. Boebert ) introduced the following bill; which was referred to the Committee on Natural Resources\nMay 20, 2026 Additional sponsors: Ms. Lee of Nevada and Mr. Begich\nMay 20, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on February 27, 2025\nA BILL\nTo amend the Geothermal Steam Act of 1970 to increase the frequency of lease sales, to require replacement sales, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Committing Leases for Energy Access Now Act or the CLEAN Act .\n#### 2. Geothermal leasing\n##### (a) Annual leasing\nSection 4(b) of the Geothermal Steam Act of 1970 ( 30 U.S.C. 1003(b) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking 2 years and inserting year ;\n**(2)**\nby redesignating paragraphs (3) and (4) as paragraphs (5) and (6), respectively; and\n**(3)**\nafter paragraph (2), by inserting the following:\n(3) Replacement Sales If a lease sale under paragraph (1) for a year is canceled or delayed, the Secretary of the Interior shall conduct a replacement sale during the same year. (4) Requirement Of the nominated parcels eligible for geothermal development and utilization under the resource management plan in effect for the State, the Secretary shall, in conducting a lease sale under paragraph (2), offer for lease\u2014 (A) 75 percent of such nominated parcels; and (B) the remaining 25 percent of such nominated parcels, unless the Secretary provides a written justification that identifies a statutory, environmental, or administrative basis that prevents the Secretary from offering such nominated parcels for lease. .\n##### (b) Deadlines for consideration of geothermal drilling permits\nSection 4 of the Geothermal Steam Act of 1970 ( 30 U.S.C. 1003 ) is amended by adding at the end the following:\n(h) Deadlines for consideration of geothermal drilling permits (1) Notice Not later than 30 days after the date on which the Secretary receives an application for any geothermal drilling permit, the Secretary shall\u2014 (A) provide written notice to the applicant that the application is complete; or (B) notify the applicant that information is missing and specify any information that is required to be submitted for the application to be complete. (2) Issuance or deferral (A) In general Not later than 30 days after the Secretary has provided written notice to an applicant for a geothermal drilling permit that the application for such permit is complete pursuant to paragraph (1)(A), the Secretary shall\u2014 (i) issue the permit, if the requirements under the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) and other applicable law have been completed within such timeframe; or (ii) defer the decision on the permit and provide to the applicant a notice\u2014 (I) that specifies any steps that the applicant could take for the permit to be issued; and (II) that includes a list of actions that need to be taken by the agency to comply with applicable law, together with timelines and deadlines for taking such actions, which shall not exceed the deadlines specified in section 107(g) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336a(g) ). (B) Deadline for deferred decisions If the Secretary defers a decision on a permit under subparagraph (A)(ii), the Secretary shall issue a decision on the permit not later than 10 days after the applicant takes any steps specified pursuant to subparagraph (A)(ii)(I) and the agency takes the actions listed pursuant to subparagraph (A)(ii)(II) in accordance with any applicable timelines and deadlines. .",
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
            "updateDate": "2026-01-05T18:19:22Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-01-05T18:19:22Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2026-01-05T18:19:22Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-01-05T18:19:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-21T16:21:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1687",
          "measure-number": "1687",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2026-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1687v00",
            "update-date": "2026-05-07"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Committing Leases for Energy Access Now Act or the CLEAN Act</strong></p><p>This bill directs the Department of the Interior to increase the frequency of lease sales for developing and utilizing geothermal energy on federal land.</p><p>Specifically, Interior must hold lease sales at least once a year (rather than two years) in states with pending nominations of federal land to be leased for geothermal energy development.</p><p>In conducting such lease sales,\u00a0Interior must offer all of the pending nominated parcels eligible for geothermal development and utilization under the resource management plan in effect for the state.</p><p>If a lease sale is canceled or delayed, Interior must conduct a replacement sale during the same year.</p><p>Finally, the bill establishes deadlines for Interior to respond to applications for geothermal drilling permits.</p>"
        },
        "title": "CLEAN Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1687.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Committing Leases for Energy Access Now Act or the CLEAN Act</strong></p><p>This bill directs the Department of the Interior to increase the frequency of lease sales for developing and utilizing geothermal energy on federal land.</p><p>Specifically, Interior must hold lease sales at least once a year (rather than two years) in states with pending nominations of federal land to be leased for geothermal energy development.</p><p>In conducting such lease sales,\u00a0Interior must offer all of the pending nominated parcels eligible for geothermal development and utilization under the resource management plan in effect for the state.</p><p>If a lease sale is canceled or delayed, Interior must conduct a replacement sale during the same year.</p><p>Finally, the bill establishes deadlines for Interior to respond to applications for geothermal drilling permits.</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119hr1687"
    },
    "title": "CLEAN Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Committing Leases for Energy Access Now Act or the CLEAN Act</strong></p><p>This bill directs the Department of the Interior to increase the frequency of lease sales for developing and utilizing geothermal energy on federal land.</p><p>Specifically, Interior must hold lease sales at least once a year (rather than two years) in states with pending nominations of federal land to be leased for geothermal energy development.</p><p>In conducting such lease sales,\u00a0Interior must offer all of the pending nominated parcels eligible for geothermal development and utilization under the resource management plan in effect for the state.</p><p>If a lease sale is canceled or delayed, Interior must conduct a replacement sale during the same year.</p><p>Finally, the bill establishes deadlines for Interior to respond to applications for geothermal drilling permits.</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119hr1687"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1687ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr1687rh.xml"
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
      "title": "CLEAN Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-22T02:38:25Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Committing Leases for Energy Access Now Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-22T02:38:25Z"
    },
    {
      "title": "CLEAN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Committing Leases for Energy Access Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Geothermal Steam Act of 1970 to increase the frequency of lease sales, to require replacement sales, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:39Z"
    }
  ]
}
```
