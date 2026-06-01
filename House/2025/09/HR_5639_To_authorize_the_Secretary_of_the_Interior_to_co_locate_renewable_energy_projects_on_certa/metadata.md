# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5639?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5639
- Title: Co-Location Energy Act
- Congress: 119
- Bill type: HR
- Bill number: 5639
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-03-31T18:04:13Z
- Update date including text: 2026-03-31T18:04:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-18 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-18 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-03-25 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5639",
    "number": "5639",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "K000403",
        "district": "3",
        "firstName": "Mike",
        "fullName": "Rep. Kennedy, Mike [R-UT-3]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Co-Location Energy Act",
    "type": "HR",
    "updateDate": "2026-03-31T18:04:13Z",
    "updateDateIncludingText": "2026-03-31T18:04:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-18",
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
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-25T14:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-18T15:00:00Z",
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
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5639ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5639\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Kennedy of Utah (for himself and Mr. Levin ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo authorize the Secretary of the Interior to co-locate renewable energy projects on certain existing Federal leased areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Co-Location Energy Act .\n#### 2. Co-location of renewable energy projects\n##### (a) Definitions\nIn this section:\n**(1) Existing Federal energy lease**\nThe term existing Federal energy lease means a lease, easement, or right-of-way, as applicable\u2014\n**(A)**\non land managed by the Secretary; and\n**(B)**\nthat was issued, granted, or renewed on or before the date of enactment of this Act under\u2014\n**(i)**\nthe Mineral Leasing Act ( 30 U.S.C. 181 et seq. ); or\n**(ii)**\nthe Geothermal Steam Act of 1970 ( 30 U.S.C. 1001 et seq. ).\n**(2) Secretary**\nThe term Secretary means the Secretary of the Interior.\n##### (b) Authorization To evaluate leased areas for renewable energy development\n**(1) In general**\nIn addition to the authority of the Secretary under section 8(p) of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1337(p) ) and section 501(a)(4) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1761(a)(4) ), the Secretary may authorize a person to evaluate an area of an existing Federal energy lease for solar or wind energy development.\n**(2) Consent of leaseholder**\nThe Secretary may not authorize a person to evaluate an area under paragraph (1) unless the applicable leaseholder consents to that authorization.\n##### (c) Permits for renewable energy development on existing oil, gas, coal, and geothermal lease areas\n**(1) In general**\nIn addition to the authority of the Secretary under section 8(p) of the Outer Continental Shelf Lands Act ( 43 U.S.C. 1337(p) ) and section 501(a)(4) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1761(a)(4) ), the Secretary may issue a permit to authorize a person to construct or operate systems or facilities for the production, transportation, storage, or transmission of energy from solar or wind resources on an area of an existing Federal energy lease.\n**(2) Consent of leaseholder**\nThe Secretary may not issue a permit for an activity described in paragraph (1) unless the applicable leaseholder consents to the issuance of that permit.\n##### (d) Categorical exclusions\nNot later than 180 days after the date of enactment of this Act, the Secretary shall determine whether any of the actions for which a permit may be issued under subsection (c)(1), or any actions that may be carried out pursuant to constructing or operating systems or facilities for the production, transportation, storage, or transmission of energy from solar or wind resources on areas not subject to an existing Federal energy lease, are a category of actions that normally do not significantly affect the quality of the human environment within the meaning of section 102(2)(C) of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4332(2)(C) ).\n##### (e) Rulemaking\nThe Secretary shall issue a rule to carry out this section.",
      "versionDate": "2025-09-30",
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
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "896",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Co-Location Energy Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2026-03-31T18:03:48Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-03-31T18:03:34Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-03-31T18:04:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-12-17T15:43:41Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5639ih.xml"
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
      "title": "Co-Location Energy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Co-Location Energy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of the Interior to co-locate renewable energy projects on certain existing Federal leased areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:21Z"
    }
  ]
}
```
