# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3085?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3085
- Title: Firearm Access During Shutdowns Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3085
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2026-02-12T12:03:24Z
- Update date including text: 2026-02-12T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3085",
    "number": "3085",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Firearm Access During Shutdowns Act of 2025",
    "type": "S",
    "updateDate": "2026-02-12T12:03:24Z",
    "updateDateIncludingText": "2026-02-12T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-10-30T17:59:03Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-30T17:59:03Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "WV"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "LA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "ID"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "MT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "OK"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "MS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "WV"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "NE"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3085is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3085\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Risch (for himself, Mrs. Capito , Mr. Cassidy , Mr. Crapo , Mr. Daines , Mr. Lankford , Mrs. Hyde-Smith , Mr. Justice , Mr. Sheehy , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo ensure that certain operations, functions, and services of the Federal Government relating to enforcement of firearms laws and firearm export licensing continue during a lapse in appropriations.\n#### 1. Short title\nThis Act may be cited as the Firearm Access During Shutdowns Act of 2025 .\n#### 2. Continuation of certain firearm-related operations during Government shutdowns\n##### (a) In general\nThe operations, functions, and services described in subsection (b) shall be deemed to relate to an emergency involving the safety of human life or the protection of property for purposes of section 1342 of title 31, United States Code, and the employees carrying out those operations, functions, and services shall be deemed to be excepted employees, as defined in section 1341(c) of that title.\n##### (b) Operations, functions, and services\nThe operations, functions, and services described in this subsection are the operations, functions, and services of\u2014\n**(1)**\nthe National Instant Criminal Background Check System of the Federal Bureau of Investigation, including the processing of background checks in support of the operations of the Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives;\n**(2)**\nthe Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives;\n**(3)**\nthe Bureau of Industry and Security of the Department of Commerce relating to firearms and firearm-related products, including activities related to processing of applications for export licenses; and\n**(4)**\nthe Directorate of Defense Trade Controls of the Department of State relating to firearms and firearm-related products, including activities related to processing of applications for export licenses.",
      "versionDate": "2025-10-30",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-10-31",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5874",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Firearm Access During Shutdowns Act",
      "type": "HR"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-10T15:26:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-30",
    "originChamber": "Senate",
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
          "measure-id": "id119s3085",
          "measure-number": "3085",
          "measure-type": "s",
          "orig-publish-date": "2025-10-30",
          "originChamber": "SENATE",
          "update-date": "2025-11-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3085v00",
            "update-date": "2025-11-10"
          },
          "action-date": "2025-10-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Firearm Access During Shutdowns Act of 2025</strong></p><p>This bill requires various federal agencies to continue certain operations, functions, and services related to firearms during a government shutdown.</p><p>The bill applies to\u00a0</p><ul><li>the Federal Bureau of Investigation's National Instant Criminal Background Check System, including the processing of background checks in support of the operations of the Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF);</li><li>the ATF's Directorate of Enforcement Programs and Services;</li><li>the activities of the Department of Commerce's Bureau of Industry and Security relating to firearms and firearm-related products, including activities related to processing of applications for export licenses; and</li><li>the activities of the Department of State's Directorate of Defense Trade Controls relating to firearms and firearm-related products, including activities related to processing of applications for export licenses.</li></ul><p>Under the bill, (1) these operations, functions, and services are deemed to relate to an emergency involving the safety of human life or the protection of property; and (2) employees carrying out the operations, functions, and services are deemed to be excepted employees. (Under an exception in\u00a0the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown. Employees who are required to work during a government shutdown because they fall under this or other exceptions are known as excepted employees.)</p>"
        },
        "title": "Firearm Access During Shutdowns Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3085.xml",
    "summary": {
      "actionDate": "2025-10-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Firearm Access During Shutdowns Act of 2025</strong></p><p>This bill requires various federal agencies to continue certain operations, functions, and services related to firearms during a government shutdown.</p><p>The bill applies to\u00a0</p><ul><li>the Federal Bureau of Investigation's National Instant Criminal Background Check System, including the processing of background checks in support of the operations of the Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF);</li><li>the ATF's Directorate of Enforcement Programs and Services;</li><li>the activities of the Department of Commerce's Bureau of Industry and Security relating to firearms and firearm-related products, including activities related to processing of applications for export licenses; and</li><li>the activities of the Department of State's Directorate of Defense Trade Controls relating to firearms and firearm-related products, including activities related to processing of applications for export licenses.</li></ul><p>Under the bill, (1) these operations, functions, and services are deemed to relate to an emergency involving the safety of human life or the protection of property; and (2) employees carrying out the operations, functions, and services are deemed to be excepted employees. (Under an exception in\u00a0the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown. Employees who are required to work during a government shutdown because they fall under this or other exceptions are known as excepted employees.)</p>",
      "updateDate": "2025-11-10",
      "versionCode": "id119s3085"
    },
    "title": "Firearm Access During Shutdowns Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Firearm Access During Shutdowns Act of 2025</strong></p><p>This bill requires various federal agencies to continue certain operations, functions, and services related to firearms during a government shutdown.</p><p>The bill applies to\u00a0</p><ul><li>the Federal Bureau of Investigation's National Instant Criminal Background Check System, including the processing of background checks in support of the operations of the Directorate of Enforcement Programs and Services of the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF);</li><li>the ATF's Directorate of Enforcement Programs and Services;</li><li>the activities of the Department of Commerce's Bureau of Industry and Security relating to firearms and firearm-related products, including activities related to processing of applications for export licenses; and</li><li>the activities of the Department of State's Directorate of Defense Trade Controls relating to firearms and firearm-related products, including activities related to processing of applications for export licenses.</li></ul><p>Under the bill, (1) these operations, functions, and services are deemed to relate to an emergency involving the safety of human life or the protection of property; and (2) employees carrying out the operations, functions, and services are deemed to be excepted employees. (Under an exception in\u00a0the Antideficiency Act, an employee whose duties involve the safety of human life or the protection of property may be required to work during a government shutdown. Employees who are required to work during a government shutdown because they fall under this or other exceptions are known as excepted employees.)</p>",
      "updateDate": "2025-11-10",
      "versionCode": "id119s3085"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3085is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Firearm Access During Shutdowns Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Firearm Access During Shutdowns Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure that certain operations, functions, and services of the Federal Government relating to enforcement of firearms laws and firearm export licensing continue during a lapse in appropriations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:17Z"
    }
  ]
}
```
