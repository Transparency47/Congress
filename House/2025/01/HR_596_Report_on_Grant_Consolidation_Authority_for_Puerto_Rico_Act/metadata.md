# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/596?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/596
- Title: Report on Grant Consolidation Authority for Puerto Rico Act
- Congress: 119
- Bill type: HR
- Bill number: 596
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2025-04-03T19:43:25Z
- Update date including text: 2025-04-03T19:43:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/596",
    "number": "596",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Report on Grant Consolidation Authority for Puerto Rico Act",
    "type": "HR",
    "updateDate": "2025-04-03T19:43:25Z",
    "updateDateIncludingText": "2025-04-03T19:43:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:00:45Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "IL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jos\u00e9",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "PR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr596ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 596\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Ms. Vel\u00e1zquez (for herself, Mr. Torres of New York , Ms. Ocasio-Cortez , Mrs. Ramirez , Mr. Goldman of New York , Ms. Meng , Mr. Espaillat , and Mr. Hern\u00e1ndez ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require a study relating to the consolidation of certain grant programs currently available to insular areas and the suitability of such consolidation for Puerto Rico, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Report on Grant Consolidation Authority for Puerto Rico Act .\n#### 2. Congressional findings and statement of purpose\n##### (a) Increased burden on the public sector of Puerto Rico\nThe Congress makes the following findings:\n**(1)**\nPuerto Rico faces a severe economic crisis, characterized by the largest municipal bankruptcy in the United States history, higher levels of poverty and socioeconomic inequality when compared to the rest of the United States, and a reduced labor force.\n**(2)**\nPuerto Rico is managing a large recovery and reconstruction process prompted by hurricanes Irma, Mar\u00eda, and Fiona, the 2020 earthquakes, and the COVID pandemic.\n**(3)**\nThe set of post-disaster conditions has exerted a great burden on the public sector of the Commonwealth of Puerto Rico. Public employees have had to comply with new fiscal requirements imposed by the Financial Oversight and Management Board under the Puerto Rico Oversight, Management, and Economic Stability Act ( PROMESA ), handle historic allocations of Federal funds, which involves engaging with new agencies, programs, and requirements over time, and balance fiscal constraints with the urgency to recruit specialized and full-time workforce for the best use of disaster funding.\n##### (b) Statement of Purpose\nIt is the purpose of this Act to study the suitability of grant consolidation to minimize the burden upon the public sector of the Commonwealth of Puerto Rico and maximize its available resources to access Federal funding.\n#### 3. Study required\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General of the United States shall submit to the appropriate congressional committees a report containing the results of a study on the process by which grants made available by the Federal Government are consolidated for insular areas pursuant to part 97 of title 45, Code of Federal Regulations. Such report shall also contain the following:\n**(1)**\nAn analysis, in consultation with appropriate officials of local agencies in Puerto Rico, about the manner in which such agencies currently access funding from programs that are listed in section 97.12 of such part 97.\n**(2)**\nA list of each grant or other program that such officials would recommend adding to the list of programs under such section 97.12.\n**(3)**\nAny challenges noted by the Comptroller General or by such officials relating to meeting the existing requirements for obtaining funding for Puerto Rico from such listed programs.\n**(4)**\nAn assessment by the Comptroller General whether any of the challenges described pursuant to paragraph (3) with respect to existing requirements for obtaining funding would be partially or wholly addressed by extending access to the consolidation of such funding to Puerto Rico in the same manner and to the same extent as the insular areas.\n**(5)**\nAny recommendations of such officials regarding the manner in which that current process for access to such funding should change, including recommendations relating to extending access to the consolidation of such funding to Puerto Rico.\n##### (b) Access to prompt and complete information\nAny official of Puerto Rico from whom the Comptroller General seeks information for purposes of the report required by subsection (a) shall promptly and comprehensively respond to such request for information, and in no case later than 90 days after the receipt of such a request. To the extent appropriate, the Comptroller General may interpret a lack of response, or a partial or incomplete response, to any such request for information adversely in compiling the report required by such subsection.\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Natural Resources, the Committee on Education and Labor, and the Committee on Energy and Commerce of the House of Representatives; and\n**(2)**\nthe Committee on Energy and Natural Resources and the Committee on Health, Education, Labor, and Pensions of the Senate.",
      "versionDate": "2025-01-21",
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
            "updateDate": "2025-03-03T17:44:46Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-03T17:44:40Z"
          },
          {
            "name": "Puerto Rico",
            "updateDate": "2025-03-03T17:44:28Z"
          },
          {
            "name": "U.S. territories and protectorates",
            "updateDate": "2025-03-03T17:44:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T18:41:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr596",
          "measure-number": "596",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr596v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Report on Grant Consolidation Authority for Puerto Rico Act</strong></p><p>This bill requires the Government Accountability Office (GAO) to report to Congress regarding the consolidation of certain grant programs currently available to insular areas and the suitability of such consolidation for Puerto Rico.\u00a0(At present, such consolidation allows insular areas to apply for a consolidated grant in lieu of filing an individual application for each eligible grant program.)</p><p>Further, any official of Puerto Rico from whom the GAO seeks information for purposes of that report must promptly and comprehensively respond to such request for information.</p>"
        },
        "title": "Report on Grant Consolidation Authority for Puerto Rico Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr596.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Report on Grant Consolidation Authority for Puerto Rico Act</strong></p><p>This bill requires the Government Accountability Office (GAO) to report to Congress regarding the consolidation of certain grant programs currently available to insular areas and the suitability of such consolidation for Puerto Rico.\u00a0(At present, such consolidation allows insular areas to apply for a consolidated grant in lieu of filing an individual application for each eligible grant program.)</p><p>Further, any official of Puerto Rico from whom the GAO seeks information for purposes of that report must promptly and comprehensively respond to such request for information.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr596"
    },
    "title": "Report on Grant Consolidation Authority for Puerto Rico Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Report on Grant Consolidation Authority for Puerto Rico Act</strong></p><p>This bill requires the Government Accountability Office (GAO) to report to Congress regarding the consolidation of certain grant programs currently available to insular areas and the suitability of such consolidation for Puerto Rico.\u00a0(At present, such consolidation allows insular areas to apply for a consolidated grant in lieu of filing an individual application for each eligible grant program.)</p><p>Further, any official of Puerto Rico from whom the GAO seeks information for purposes of that report must promptly and comprehensively respond to such request for information.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr596"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr596ih.xml"
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
      "title": "Report on Grant Consolidation Authority for Puerto Rico Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Report on Grant Consolidation Authority for Puerto Rico Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a study relating to the consolidation of certain grant programs currently available to insular areas and the suitability of such consolidation for Puerto Rico, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T08:18:31Z"
    }
  ]
}
```
