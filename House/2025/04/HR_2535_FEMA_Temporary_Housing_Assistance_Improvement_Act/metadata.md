# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2535?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2535
- Title: FEMA Temporary Housing Assistance Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 2535
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-01-14T21:04:46Z
- Update date including text: 2026-01-14T21:04:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-01 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2535",
    "number": "2535",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "FEMA Temporary Housing Assistance Improvement Act",
    "type": "HR",
    "updateDate": "2026-01-14T21:04:46Z",
    "updateDateIncludingText": "2026-01-14T21:04:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-01T21:10:25Z",
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
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2535ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2535\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Ms. Brownley (for herself and Ms. Chu ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to prohibit the President from considering insurance as a duplication of benefits for certain assistance under such Act.\n#### 1. Short title\nThis Act may be cited as the FEMA Temporary Housing Assistance Improvement Act .\n#### 2. Duplication of benefits clarification\nSection 408(c)(1) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174(c)(1) ) is amended by adding at the end the following:\n(C) Duplication of benefits In determining eligibility for temporary housing assistance under this subsection, the President may not consider insurance a duplication of benefits for the purpose of applying section 312 of this Act. .",
      "versionDate": "2025-04-01",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-27T16:09:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119hr2535",
          "measure-number": "2535",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2026-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2535v00",
            "update-date": "2026-01-14"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>FEMA Temporary Housing Assistance Improvement Act</strong></p><p>This bill enables individuals or households to receive temporary housing assistance from the Federal Emergency Management Agency (FEMA) following a disaster\u00a0(i.e., funds for renting housing or housing provided by FEMA) regardless of the recipient\u2019s insurance status.</p><p>Under current law, in determining whether an individual or household is eligible for temporary housing assistance, FEMA generally must determine whether the applicant has insurance that will cover those same expenses, to avoid a duplication of benefits. The bill prohibits\u00a0FEMA from considering insurance a duplication of benefits when determining an individual or household\u2019s eligibility for temporary housing assistance, removing the need for FEMA to determine insurance coverage prior to providing the assistance.</p>"
        },
        "title": "FEMA Temporary Housing Assistance Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2535.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA Temporary Housing Assistance Improvement Act</strong></p><p>This bill enables individuals or households to receive temporary housing assistance from the Federal Emergency Management Agency (FEMA) following a disaster\u00a0(i.e., funds for renting housing or housing provided by FEMA) regardless of the recipient\u2019s insurance status.</p><p>Under current law, in determining whether an individual or household is eligible for temporary housing assistance, FEMA generally must determine whether the applicant has insurance that will cover those same expenses, to avoid a duplication of benefits. The bill prohibits\u00a0FEMA from considering insurance a duplication of benefits when determining an individual or household\u2019s eligibility for temporary housing assistance, removing the need for FEMA to determine insurance coverage prior to providing the assistance.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119hr2535"
    },
    "title": "FEMA Temporary Housing Assistance Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA Temporary Housing Assistance Improvement Act</strong></p><p>This bill enables individuals or households to receive temporary housing assistance from the Federal Emergency Management Agency (FEMA) following a disaster\u00a0(i.e., funds for renting housing or housing provided by FEMA) regardless of the recipient\u2019s insurance status.</p><p>Under current law, in determining whether an individual or household is eligible for temporary housing assistance, FEMA generally must determine whether the applicant has insurance that will cover those same expenses, to avoid a duplication of benefits. The bill prohibits\u00a0FEMA from considering insurance a duplication of benefits when determining an individual or household\u2019s eligibility for temporary housing assistance, removing the need for FEMA to determine insurance coverage prior to providing the assistance.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119hr2535"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2535ih.xml"
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
      "title": "FEMA Temporary Housing Assistance Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FEMA Temporary Housing Assistance Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to prohibit the President from considering insurance as a duplication of benefits for certain assistance under such Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:33Z"
    }
  ]
}
```
