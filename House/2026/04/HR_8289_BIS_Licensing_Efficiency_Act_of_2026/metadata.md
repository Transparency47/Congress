# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8289
- Title: BIS Licensing Efficiency Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8289
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-20T12:05:25Z
- Update date including text: 2026-05-20T12:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 0.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 44 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8289",
    "number": "8289",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "BIS Licensing Efficiency Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T12:05:25Z",
    "updateDateIncludingText": "2026-05-20T12:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 44 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
            "date": "2026-04-22T20:42:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-15T14:00:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "CA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8289ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8289\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Meeks (for himself and Mr. Issa ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to ensure expeditious processing of license applications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the BIS Licensing Efficiency Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSection 1756(a)(2) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4815(a)(2) ) requires the Secretary of Commerce to ensure that licensing decisions are made in an expeditious manner, with transparency to applicants on the status of license and other authorization processing and the reason for denying any license or request for authorization .\n**(2)**\nSection 1756(b) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4815(b) ) expresses the sense of Congress that the Secretary should make best efforts to ensure that an accurate, consistent, and timely evaluation and processing of licenses or other requests for authorization to export, reexport, or in-country transfer items controlled under this subchapter is generally accomplished within 30 days from the date of such license request .\n**(3)**\nExecutive Order 12981 (61 Fed. Reg. 54079; relating to administration of export controls), which was codified in Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ), stipulates that all license applications submitted under the Act and the Regulations or any renewal of, or successor to, the Export Administration Act and the Regulations, shall be resolved or referred to the President no later than 90 calendar days .\n**(4)**\nThe Export Administration Regulations (parts 730\u2013774 of title 15, Code of Federal Regulations) stipulate that license applications should be resolved or referred to the President no later than 90 calendar days from the date of BIS\u2019s registration of the license application .\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nlong license delays at the Bureau of Industry and Security of the Department of Commerce create uncertainty for United States exporters and domestic manufacturers and can lead to the loss of business to foreign companies, harming the United States economy;\n**(2)**\nefficient and predictable processing of export licenses is critical to the competitiveness of United States technology companies and the stability of global supply chains;\n**(3)**\nUnited States technology and economic leadership requires that the export controls system functions efficiently and that license decisions are made in an expeditious manner; and\n**(4)**\ntransparency regarding the efficiency and timeliness of license reviews is necessary for effective Congressional oversight of the export control system.\n#### 4. Licensing timeline; licensing reviews\nSection 1756 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4815 ) is amended\u2014\n**(1)**\nby redesignating subsection (e) as subsection (g);\n**(2)**\nin subsection (g), as so redesignated, in the header, by striking Report and inserting Annual report on end use checks ; and\n**(3)**\nby inserting after subsection (d) the following new subsections:\n(e) Licensing timeline (1) In general Not later than 90 days after the date on which an application for a license under this section is submitted, the Secretary should make a licensing decision and notify the applicant of such decision. (2) Delayed application If no licensing decision is made not later than 120 days after the date on which an application for a license under this section was submitted, the Secretary shall notify the applicant of the status of such application, the reason such a decision has not been made, and request any additional information necessary to make such a decision. (f) Licensing reviews Licensing officers with relevant subject matter expertise shall play an essential role in conducting license reviews of all applications for a license under this section. .\n#### 5. Quarterly report on license processing\nSection 1756 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4815 ), as amended by section 1, is further amended by inserting after subsection (g) the following new subsection:\n(h) Quarterly report on license processing (1) In general Not later than 90 days after the date of the enactment of this subsection, and not less frequently than quarterly thereafter, the Secretary shall submit to the appropriate congressional committees a report detailing the processing of license applications and other requests for authorization for the export, reexport, release, and in-country transfer of items controlled under this section. (2) Elements (A) Initial report The first report required by paragraph (1) shall include, with respect to the preceding one-year period, the following: (i) The total number of license applications submitted. (ii) On the date on which such report is submitted, the total number of license applications in the below statuses on the: (I) Received. (II) On hold (i.e., on hold without action). (III) Referred to another department or agency. (IV) Signed off by a Licensing Officer. (V) Countersigned. (VI) Validated. (iii) A breakdown of the total number of licenses approved, denied, and returned without action. (iv) The average and median processing time for all license applications, in calendar days from the date on which an application is first submitted to the date on which a decision on an application is communicated to the applicant. (v) The average and median processing time of license applications broken out by\u2014 (I) end-user country (for license applications with multiple end-user countries listed, such applications shall be included in the calculation of each country); (II) Export Control Classification Number ( ECCN ) (for license applications with multiple ECCNs listed, such applications shall be included in the calculation of each ECCN); and (III) whether the license application was for an export, re-export, deemed export, or in-country transfer. (vi) The total number of license applications referred to\u2014 (I) the Department of State; (II) the Department of Defense; or (III) the Department of Energy. (vii) The number of license applications that remained pending for not less than 90 calendar days and a summary of the reasons for such delays, including interagency referral, pre-license check, or administrative backlog. (B) Subsequent reports Each subsequent report required by paragraph (1) shall include, with respect to the preceding quarter, the information described in subparagraph (A)(i) through (A)(vii). (3) Definitions In this subsection\u2014 (A) the term appropriate congressional committees means\u2014 (i) the Committee on Foreign Affairs of the House of Representatives; and (ii) the Committee on Banking, Housing, and Urban Affairs of the Senate; and .\n#### 6. Audit and report by Comptroller General of the United States\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Comptroller General of the United States shall commence an audit of the license review process of the Bureau of Industry and Security of the Department of Commerce.\n##### (b) Contents\nThe audit required under subsection (a) should analyze whether licensing decisions under the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ) have been made in an expeditious manner in the preceding calendar year consistent with the procedures and timelines mandated by such Act and identify any bottlenecks that may impact the timing of licensing decisions.\n##### (c) Report\nNot later than one year after the enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\nsubmit a report with the findings from the audit required by subsection (a) to the Committee on Foreign Affairs of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(2)**\npost the report on a publicly available website of the United States Government Accountability Office.",
      "versionDate": "2026-04-15",
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
            "name": "Congressional oversight",
            "updateDate": "2026-05-01T18:33:39Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-01T18:33:34Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-01T18:33:48Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-05-01T18:33:29Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-05-01T18:33:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-20T23:17:22Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8289ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BIS Licensing Efficiency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T12:38:20Z"
    },
    {
      "title": "BIS Licensing Efficiency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T12:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Export Control Reform Act of 2018 to ensure expeditious processing of license applications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T12:33:45Z"
    }
  ]
}
```
