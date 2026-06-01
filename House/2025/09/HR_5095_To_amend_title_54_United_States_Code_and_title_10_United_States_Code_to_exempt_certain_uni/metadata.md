# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5095?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5095
- Title: HOMEFRONT Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5095
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2026-04-28T08:06:27Z
- Update date including text: 2026-04-28T08:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-02 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-04 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-12-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-02 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-04 - Committee: Referred to the Subcommittee on Federal Lands.
- 2025-12-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5095",
    "number": "5095",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "P000622",
        "district": "1",
        "firstName": "Jimmy",
        "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
        "lastName": "Patronis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "HOMEFRONT Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:27Z",
    "updateDateIncludingText": "2026-04-28T08:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T16:02:40Z",
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
                "date": "2025-12-11T20:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-12-04T15:05:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-02T16:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5095ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5095\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Mr. Patronis introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 54, United States Code, and title 10, United States Code to exempt certain units of military housing from the requirements of the National Historic Preservation Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Our Military Effectively For Readiness, Operations, and Neutralization of Threats Act of 2025 or the HOMEFRONT Act of 2025 .\n#### 2. Inapplicability of National Historic Preservation Act to certain military housing\n##### (a) In general\nSection 307104 of title 54, United States Code is amended\u2014\n**(1)**\nin the heading\u2014\n**(A)**\nby striking or ; and\n**(B)**\nby striking Capitol and inserting Capitol, and certain military housing ;\n**(2)**\nby striking Nothing and inserting (a) White House; Supreme Court; Capitol. \u2014 Nothing ; and\n**(3)**\nby adding at the end the following new subsection:\n(b) Military housing exemptions (1) Except as provided in paragraph (2), nothing in this division applies to any facility under the jurisdiction of the Secretary of Defense that, as of the date of the enactment of the HOMEFRONT Act of 2025, has been used as\u2014 (A) military unaccompanied housing (as defined in section 2871 of title 10, United States Code); or (B) military family housing (as defined in such section). (2) (A) Subject to subparagraph (B) and subparagraph (C), the Secretary may exclude from the exemption under this subsection any unit of military unaccompanied housing or military family housing pursuant to conditions the Secretary prescribes in regulations. Any unit of military unaccompanied housing or military family housing excluded from the exemption under this subsection shall be managed in accordance with this division until the date on which the Secretary elects to revoke such exclusion. (B) The total number of units of military unaccompanied housing or military family housing excluded from the exemption under this subsection pursuant to paragraph (2) may not exceed one-tenth of one percent of the total number of units of military unaccompanied housing or military family housing under the jurisdiction of the Secretary of Defense. (C) Any facility under the jurisdiction of the Department of Defense that is listed on the National Register of Historic Places as of January 20, 2025, may not be excluded from the exemption under this subsection. .\n##### (b) Privatized military housing\n**(1) In general**\nSection 2890 of title 10, United States Code, is amended to read as follows:\n(f) Prohibition on use of Nondisclosure agreements (1) A landlord may not request that a tenant or prospective tenant of a housing unit sign a nondisclosure agreement in connection with the provision entering into, continuing, terminating a lease for the housing unit, or in connection with the provision by the landlord of services related to the housing unit. Any such agreement against the interests of the tenant is invalid. (2) Paragraph (1) shall not apply to a nondisclosure agreement executed as part of the settlement of litigation. .\n**(2) Retroactive application**\nSubsection (f) of section 2890 of title 10, United States Code (as amended by paragraph (1)), shall apply with respect to any nondisclosure agreement covered by the terms of such subsection (f) regardless of the date on which the agreement was executed.",
      "versionDate": "2025-09-02",
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
            "name": "Historic sites and heritage areas",
            "updateDate": "2026-01-09T16:31:30Z"
          },
          {
            "name": "Housing industry and standards",
            "updateDate": "2026-01-09T16:31:56Z"
          },
          {
            "name": "Military facilities and property",
            "updateDate": "2026-01-09T16:31:35Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2026-01-09T16:31:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-22T19:53:01Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5095ih.xml"
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
      "title": "HOMEFRONT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-05T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOMEFRONT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-05T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Our Military Effectively For Readiness, Operations, and Neutralization of Threats Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-05T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 54, United States Code, and title 10, United States Code to exempt certain units of military housing from the requirements of the National Historic Preservation Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-05T04:03:22Z"
    }
  ]
}
```
