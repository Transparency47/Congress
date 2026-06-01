# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4217?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4217
- Title: VA COST SAVINGS Enhancements Act
- Congress: 119
- Bill type: HR
- Bill number: 4217
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2026-03-31T11:03:18Z
- Update date including text: 2026-03-31T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4217",
    "number": "4217",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001295",
        "district": "12",
        "firstName": "Mike",
        "fullName": "Rep. Bost, Mike [R-IL-12]",
        "lastName": "Bost",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "VA COST SAVINGS Enhancements Act",
    "type": "HR",
    "updateDate": "2026-03-31T11:03:18Z",
    "updateDateIncludingText": "2026-03-31T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
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
      "actionDate": "2025-06-27",
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
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T18:59:11Z",
              "name": "Referred to"
            }
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4217ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4217\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Bost introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to use on-site regulated medical waste treatment systems at certain Department of Veterans Affairs facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Department of Veterans Affairs Creation of On-Site Treatment Systems Affording Veterans Improvements and Numerous General Safety Enhancements Act or the VA COST SAVINGS Enhancements Act .\n#### 2. Use of on-site regulated medical waste treatment systems at Department of Veterans Affairs facilities\n##### (a) Identification of facilities\nThe Secretary of Veterans Affairs shall identify Department of Veterans Affairs facilities that would benefit from cost savings associated with the use of an on-site regulated medical waste treatment system over a five-year period.\n##### (b) Regulated medical waste cost analysis model\nFor purposes of carrying out subsection (a), the Secretary shall develop a uniform regulated medical waste cost analysis model to be used to determine the cost savings associated with the use of an on-site regulated medical waste treatment system at Department facilities. Such model shall be designed to calculate savings based on\u2014\n**(1)**\nthe cost of treating regulated medical waste at an off-site location under a contract with a non-Department entity; compared to\n**(2)**\nthe cost of treating regulated medical waste on-site, based on the equipment specification of treatment system manufacturers, with capital costs amortized over a ten-year period.\n##### (c) Installation\nAt each Department facility identified under subsection (a), the Secretary shall secure, install, and operate an on-site regulated medical waste treatment system.\n##### (d) Regulated medical waste defined\nIn this section, the term regulated medical waste has the meaning given such term under section 173.134(a)(5) of title 49, Code of Federal Regulations, concerning regulated medical waste and infectious substances, or any successor regulation, except that, in the case of an applicable State law that is more expansive, the definition in the State law shall apply.\n#### 3. No additional funds authorized\nNo additional funds are authorized to be appropriated to carry out the requirements of this Act.",
      "versionDate": "2025-06-27",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-29T20:32:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-27",
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
          "measure-id": "id119hr4217",
          "measure-number": "4217",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-27",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4217v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-06-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Department of Veterans Affairs Creation of On-Site Treatment Systems Affording Veterans Improvements and Numerous General Safety Enhancements Act or the VA COST SAVINGS Enhancements Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to install and operate an on-site regulated medical waste treatment system at each VA facility that would benefit from such a system's cost savings. In order to identify which VA facilities would benefit, the VA must develop a uniform regulated medical waste cost analysis model to determine the cost savings associated with the use of an on-site regulated medical waste treatment system.</p>"
        },
        "title": "VA COST SAVINGS Enhancements Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4217.xml",
    "summary": {
      "actionDate": "2025-06-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Department of Veterans Affairs Creation of On-Site Treatment Systems Affording Veterans Improvements and Numerous General Safety Enhancements Act or the VA COST SAVINGS Enhancements Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to install and operate an on-site regulated medical waste treatment system at each VA facility that would benefit from such a system's cost savings. In order to identify which VA facilities would benefit, the VA must develop a uniform regulated medical waste cost analysis model to determine the cost savings associated with the use of an on-site regulated medical waste treatment system.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4217"
    },
    "title": "VA COST SAVINGS Enhancements Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Department of Veterans Affairs Creation of On-Site Treatment Systems Affording Veterans Improvements and Numerous General Safety Enhancements Act or the VA COST SAVINGS Enhancements Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to install and operate an on-site regulated medical waste treatment system at each VA facility that would benefit from such a system's cost savings. In order to identify which VA facilities would benefit, the VA must develop a uniform regulated medical waste cost analysis model to determine the cost savings associated with the use of an on-site regulated medical waste treatment system.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4217"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4217ih.xml"
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
      "title": "VA COST SAVINGS Enhancements Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T05:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA COST SAVINGS Enhancements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Department of Veterans Affairs Creation of On-Site Treatment Systems Affording Veterans Improvements and Numerous General Safety Enhancements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to use on-site regulated medical waste treatment systems at certain Department of Veterans Affairs facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T05:33:39Z"
    }
  ]
}
```
