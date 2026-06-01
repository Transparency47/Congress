# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5378?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5378
- Title: Tribal Healthcare Careers Act
- Congress: 119
- Bill type: HR
- Bill number: 5378
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2026-04-01T01:25:00Z
- Update date including text: 2026-04-01T01:25:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5378",
    "number": "5378",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "G000585",
        "district": "34",
        "firstName": "Jimmy",
        "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
        "lastName": "Gomez",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Tribal Healthcare Careers Act",
    "type": "HR",
    "updateDate": "2026-04-01T01:25:00Z",
    "updateDateIncludingText": "2026-04-01T01:25:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5378ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5378\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Mr. Gomez introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide a set-aside of funds for Indian populations under the health profession opportunity grant program under section 2008 of the Social Security Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tribal Healthcare Careers Act .\n#### 2. Set-aside of funds for Indian populations\nSection 2008(c)(1) of the Social Security Act ( 42 U.S.C. 1397g(c)(1) ) is amended by inserting 15 percent of which for each fiscal year shall be reserved for grants to Indian tribes, tribal organizations, and Tribal Colleges and Universities before the period.\n#### 3. Guarantee of grants for Indian populations\nSection 2008(a)(2)(C) of the Social Security Act ( 42 U.S.C. 1397(a)(2)(C) ) is amended to read as follows:\n(C) Guarantee of grants for Indian populations The Secretary shall award at least 10 grants under this subsection to an eligible entity that is an Indian tribe, a tribal organization, or a Tribal College or University, to the extent there are a sufficient number of applications submitted by such an eligible entity that meet the requirements of subparagraph (B). .\n#### 4. Effective date\nThe amendments made by this Act shall take effect on October 1, 2025.",
      "versionDate": "2025-09-16",
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
        "name": "Native Americans",
        "updateDate": "2025-09-25T15:32:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-16",
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
          "measure-id": "id119hr5378",
          "measure-number": "5378",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-16",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5378v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-09-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Tribal Healthcare Careers Act</b></p> <p>This bill requires the Department of Health and Human Services (HHS) to reserve a portion of Health Profession Opportunity Grants for Indian tribes, tribal organizations, and tribal colleges and universities.</p> <p>HHS must award at least 10 grants to tribal applicants.</p>"
        },
        "title": "Tribal Healthcare Careers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5378.xml",
    "summary": {
      "actionDate": "2025-09-16",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Tribal Healthcare Careers Act</b></p> <p>This bill requires the Department of Health and Human Services (HHS) to reserve a portion of Health Profession Opportunity Grants for Indian tribes, tribal organizations, and tribal colleges and universities.</p> <p>HHS must award at least 10 grants to tribal applicants.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr5378"
    },
    "title": "Tribal Healthcare Careers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-16",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Tribal Healthcare Careers Act</b></p> <p>This bill requires the Department of Health and Human Services (HHS) to reserve a portion of Health Profession Opportunity Grants for Indian tribes, tribal organizations, and tribal colleges and universities.</p> <p>HHS must award at least 10 grants to tribal applicants.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr5378"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5378ih.xml"
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
      "title": "Tribal Healthcare Careers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tribal Healthcare Careers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-24T06:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide a set-aside of funds for Indian populations under the health profession opportunity grant program under section 2008 of the Social Security Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T06:33:21Z"
    }
  ]
}
```
