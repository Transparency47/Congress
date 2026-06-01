# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1338?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1338
- Title: REPLACE Act
- Congress: 119
- Bill type: HR
- Bill number: 1338
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-03-04T15:33:56Z
- Update date including text: 2026-03-04T15:33:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-13 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1338",
    "number": "1338",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "REPLACE Act",
    "type": "HR",
    "updateDate": "2026-03-04T15:33:56Z",
    "updateDateIncludingText": "2026-03-04T15:33:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:07:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-13T22:18:52Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "UT"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1338ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1338\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Neguse (for himself and Ms. Maloy ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Disaster Recovery Reform Act of 2018 to require the President to automatically waive certain critical document fees for individuals and households affected by major disasters for which assistance is provided under the Individuals and Households Program.\n#### 1. Short title\nThis Act may be cited as the Replacing Essential Passports and Licenses After Certain Emergencies Act or the REPLACE Act .\n#### 2. Critical document fee waiver\nSection 1238(a) of the Disaster Recovery Reform Act of 2018 ( 42 U.S.C. 5174b ) is amended\u2014\n**(1)**\nin paragraph (2), by striking applies regardless and inserting and the requirement of the President to waive fees under paragraph (4) apply regardless ;\n**(2)**\nby redesignating paragraph (4) as paragraph (8); and\n**(3)**\nby inserting after paragraph (3) the following:\n(4) Waiver The President, in consultation with the Governor of a State, shall provide a fee waiver described in paragraph (1) to any individual or household that has been adversely affected by a major disaster declared under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 )\u2014 (A) for which the President provides assistance to individuals and households under section 408 of that Act ( 42 U.S.C. 5174 ); and (B) that destroyed a critical document described in paragraph (1) of the individual or household. (5) Waiver availability The Secretary of State and the Director of the United States Citizenship and Immigration Services shall make publicly available on the website of the Department of State and the United States Citizenship and Immigration Services, respectively, a notice of the availability of fee waivers described in paragraph (4). (6) Report from USCIS Not later than 1 year after the date of enactment of this paragraph, and every year thereafter, the Director of the United States Citizenship and Immigration Services shall submit to Congress a report that includes, for the period covered by the report\u2014 (A) the number of fee waivers granted under this subsection; and (B) the cost to the United States Citizenship and Immigration Services of granting fee waivers under this subsection. (7) Report from Department of State Not later than 1 year after the date of enactment of this paragraph, and every year thereafter, the Secretary of State shall submit to Congress a report that includes, for the period covered by the report\u2014 (A) the number of fee waivers granted under this subsection; and (B) the cost to the Department of State of granting fee waivers under this subsection. .",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-13",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "566",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "REPLACE Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Emergency Management",
        "updateDate": "2025-05-13T18:50:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1338",
          "measure-number": "1338",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1338v00",
            "update-date": "2026-03-04"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Replacing Essential Passports and Licenses After Certain Emergencies Act or the REPLACE Act</strong></p><p>This bill automatically waives the fees to replace certain federal documents (e.g., passports, visas, or immigration documents) destroyed by a major disaster.</p><p>Under current law, the Department of State and U.S. Citizenship and Immigration Services (USCIS) may waive replacement fees for these critical documents for individuals or households adversely affected by a major disaster. The bill requires the State Department and\u00a0USCIS to waive these replacement fees when the documents are destroyed by a major disaster for which assistance is provided under the Federal Emergency Management Agency\u2019s Individuals and Households Program. The agencies must notify the public of the availability of these waivers on their respective\u00a0websites.</p><p>The bill also requires the State Department and\u00a0USCIS to annually report to Congress the number of such fee waivers granted and the resulting cost to the respective agencies.</p>"
        },
        "title": "REPLACE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1338.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Replacing Essential Passports and Licenses After Certain Emergencies Act or the REPLACE Act</strong></p><p>This bill automatically waives the fees to replace certain federal documents (e.g., passports, visas, or immigration documents) destroyed by a major disaster.</p><p>Under current law, the Department of State and U.S. Citizenship and Immigration Services (USCIS) may waive replacement fees for these critical documents for individuals or households adversely affected by a major disaster. The bill requires the State Department and\u00a0USCIS to waive these replacement fees when the documents are destroyed by a major disaster for which assistance is provided under the Federal Emergency Management Agency\u2019s Individuals and Households Program. The agencies must notify the public of the availability of these waivers on their respective\u00a0websites.</p><p>The bill also requires the State Department and\u00a0USCIS to annually report to Congress the number of such fee waivers granted and the resulting cost to the respective agencies.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1338"
    },
    "title": "REPLACE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Replacing Essential Passports and Licenses After Certain Emergencies Act or the REPLACE Act</strong></p><p>This bill automatically waives the fees to replace certain federal documents (e.g., passports, visas, or immigration documents) destroyed by a major disaster.</p><p>Under current law, the Department of State and U.S. Citizenship and Immigration Services (USCIS) may waive replacement fees for these critical documents for individuals or households adversely affected by a major disaster. The bill requires the State Department and\u00a0USCIS to waive these replacement fees when the documents are destroyed by a major disaster for which assistance is provided under the Federal Emergency Management Agency\u2019s Individuals and Households Program. The agencies must notify the public of the availability of these waivers on their respective\u00a0websites.</p><p>The bill also requires the State Department and\u00a0USCIS to annually report to Congress the number of such fee waivers granted and the resulting cost to the respective agencies.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1338"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1338ih.xml"
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
      "title": "REPLACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REPLACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Replacing Essential Passports and Licenses After Certain Emergencies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Disaster Recovery Reform Act of 2018 to require the President to automatically waive certain critical document fees for individuals and households affected by major disasters for which assistance is provided under the Individuals and Households Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:14Z"
    }
  ]
}
```
