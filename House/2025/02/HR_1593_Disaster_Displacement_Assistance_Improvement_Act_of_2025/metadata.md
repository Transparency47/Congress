# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1593?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1593
- Title: Disaster Displacement Assistance Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1593
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-01-17T01:42:45Z
- Update date including text: 2026-01-17T01:42:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-26 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-02-26 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1593",
    "number": "1593",
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
    "title": "Disaster Displacement Assistance Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-17T01:42:45Z",
    "updateDateIncludingText": "2026-01-17T01:42:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-26T22:27:37Z",
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
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1593ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1593\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Ms. Brownley (for herself, Mr. Garcia of California , Mr. Sherman , and Ms. Chu ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to prohibit the President from considering insurance as a duplication of benefits for certain assistance under such Act.\n#### 1. Short title\nThis Act may be cited as the Disaster Displacement Assistance Improvement Act of 2025 .\n#### 2. Duplication of benefits clarification\nSection 408 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5174 ) is amended by adding at the end the following:\n(k) Duplication of benefits (1) In general In determining eligibility for displacement assistance under this section, the President may not consider insurance a duplication of benefits for the purpose of applying section 312 of this Act. (2) Displacement assistance defined In this section, the term displacement assistance means assistance provided under this section to stay in a hotel or motel, stay with family and friends, or for any other available housing options. .",
      "versionDate": "2025-02-26",
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
        "updateDate": "2025-05-14T13:00:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1593",
          "measure-number": "1593",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2026-01-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1593v00",
            "update-date": "2026-01-17"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Disaster Displacement Assistance Improvement Act of 2025</strong></p><p>This bill enables individuals or households to receive displacement assistance from the Federal Emergency Management Agency (FEMA) following a disaster (i.e., funds to address immediate, short-term lodging needs) regardless of the recipient\u2019s insurance status.</p><p>Under current law, in determining whether an individual or household is eligible for displacement assistance,\u00a0FEMA generally must determine whether the applicant has insurance that will cover those same expenses, to avoid a duplication of benefits. The bill prohibits FEMA from considering insurance a duplication of benefits when determining an individual or household\u2019s eligibility for displacement assistance, removing the need for FEMA to determine insurance status prior to providing the assistance.</p>"
        },
        "title": "Disaster Displacement Assistance Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1593.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disaster Displacement Assistance Improvement Act of 2025</strong></p><p>This bill enables individuals or households to receive displacement assistance from the Federal Emergency Management Agency (FEMA) following a disaster (i.e., funds to address immediate, short-term lodging needs) regardless of the recipient\u2019s insurance status.</p><p>Under current law, in determining whether an individual or household is eligible for displacement assistance,\u00a0FEMA generally must determine whether the applicant has insurance that will cover those same expenses, to avoid a duplication of benefits. The bill prohibits FEMA from considering insurance a duplication of benefits when determining an individual or household\u2019s eligibility for displacement assistance, removing the need for FEMA to determine insurance status prior to providing the assistance.</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119hr1593"
    },
    "title": "Disaster Displacement Assistance Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Disaster Displacement Assistance Improvement Act of 2025</strong></p><p>This bill enables individuals or households to receive displacement assistance from the Federal Emergency Management Agency (FEMA) following a disaster (i.e., funds to address immediate, short-term lodging needs) regardless of the recipient\u2019s insurance status.</p><p>Under current law, in determining whether an individual or household is eligible for displacement assistance,\u00a0FEMA generally must determine whether the applicant has insurance that will cover those same expenses, to avoid a duplication of benefits. The bill prohibits FEMA from considering insurance a duplication of benefits when determining an individual or household\u2019s eligibility for displacement assistance, removing the need for FEMA to determine insurance status prior to providing the assistance.</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119hr1593"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1593ih.xml"
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
      "title": "Disaster Displacement Assistance Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disaster Displacement Assistance Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to prohibit the President from considering insurance as a duplication of benefits for certain assistance under such Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:23Z"
    }
  ]
}
```
