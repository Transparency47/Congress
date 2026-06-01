# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/303?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/303
- Title: Retired Pay Restoration Act
- Congress: 119
- Bill type: HR
- Bill number: 303
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-10-29T08:05:48Z
- Update date including text: 2025-10-29T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-11 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/303",
    "number": "303",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Retired Pay Restoration Act",
    "type": "HR",
    "updateDate": "2025-10-29T08:05:48Z",
    "updateDateIncludingText": "2025-10-29T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:37:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-11T22:36:20Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:37:05Z",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "HI"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "IL"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CT"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "RI"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NV"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr303ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 303\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Bilirakis introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 10, United States Code, to permit additional retired members of the Armed Forces who have a service-connected disability to receive both disability compensation from the Department of Veterans Affairs for their disability and either retired pay by reason of their years of military service or combat-related special compensation.\n#### 1. Short title\nThis Act may be cited as the Retired Pay Restoration Act .\n#### 2. Findings and sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nFor more than 100 years before 1999, all disabled military retirees were required to fund their own veterans\u2019 disability compensation by forfeiting one dollar of earned retired pay for each dollar received in veterans\u2019 disability compensation.\n**(2)**\nSince 1999, Congress has enacted legislation to progressively expand eligibility criteria for relief of the retired pay disability offset and reduce the burden of financial sacrifice on disabled military retirees.\n**(3)**\nAbsent adequate funding to eliminate the sacrifice for all disabled retirees, Congress has given initial priority to easing financial inequities for the most severely disabled and for combat-disabled retirees.\n**(4)**\nIn the interest of maximizing eligibility within cost constraints, Congress effectively has authorized full concurrent receipt for all qualifying retirees with 100-percent disability ratings and all qualifying retirees with combat-related disability ratings, while phasing out the disability offset to retired pay over 10 years for retired members with noncombat-related, service-connected disability ratings of 50 percent to 90 percent.\n**(5)**\nIn pursuing these good-faith efforts, Congress acknowledges the regrettable necessity of creating new thresholds of eligibility that understandably are disappointing to disabled retirees who fall short of meeting those new thresholds.\n**(6)**\nCongress is not content with the status quo.\n##### (b) Sense of Congress\nIt is the sense of Congress that military retired pay earned by service and sacrifice in defending the United States should not be reduced because a military retiree is also eligible for veterans\u2019 disability compensation awarded for service-connected disability.\n#### 3. Eligibility for payment of both retired pay and veterans\u2019 disability compensation for certain additional military retirees with compensable service-connected disabilities\n##### (a) Extension of Concurrent Receipt Authority to Retirees With Service-Connected Disabilities Rated Less Than 50 Percent\nSection 1414(a) of title 10, United States Code, is amended\u2014\n**(1)**\nby striking Compensation in the subsection heading and all that follows through Subject and inserting Compensation .\u2014Subject ; and\n**(2)**\nby striking paragraph (2).\n##### (b) Amendments To reflect conclusion of Phase-In of Concurrent Receipt of Retired Pay and Veterans\u2019 Disability Compensation\nSection 1414 of title 10, United States Code, is further amended\u2014\n**(1)**\nin subsection (a), as amended by subsection (a) of this section, by striking the final sentence;\n**(2)**\nby striking subsection (c) and redesignating subsections (d) and (e) as subsections (c) and (d), respectively; and\n**(3)**\nin subsection (d), as so redesignated, by striking paragraphs (3) and (4).\n##### (c) Specification of qualified retirees for concurrent receipt purposes\nSection 1414 of title 10, United States Code, is further amended\u2014\n**(1)**\nin subsection (a), as amended by subsections (a) and (b)\u2014\n**(A)**\nby striking a member or and all that follows through is entitled and inserting an individual who is a qualified retiree for any month is entitled ; and\n**(B)**\nby inserting retired pay and veterans\u2019 disability compensation after both ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking Special Rules in the subsection heading and all that follows through is subject to and inserting Special Rules for Chapter 61 Disability Retirees .\u2014In the case of a qualified retiree who is retired under chapter 61 of this title, the retired pay of the member is subject to ; and\n**(B)**\nby striking paragraph (2); and\n**(3)**\nin subsection (d), as redesignated and amended by subsection (b), by adding at the end the following new paragraph:\n(3) Qualified retiree The term qualified retiree means a member or former member of the uniformed services who, with respect to any month\u2014 (A) is entitled to retired pay, other than in the case of a member retired under chapter 61 of this title with less than 20 years of service creditable under section 1405 of this title and less than 20 years of service computed under section 12732 of this title; and (B) is entitled to veterans\u2019 disability compensation. .\n##### (d) Clerical Amendments\n**(1) Section heading**\nThe heading of section 1414 of title 10, United States Code, is amended to read as follows:\n1414. Members eligible for retired pay who are also eligible for veterans\u2019 disability compensation: Concurrent payment of retired pay and disability compensation .\n**(2) Table of sections**\nThe item relating to such section in the table of sections at the beginning of chapter 71 of title 10, United States Code, is amended to read as follows:\n1414. Members eligible for retired pay who are also eligible for veterans\u2019 disability compensation: Concurrent payment of retired pay and disability compensation. .\n##### (e) Conforming amendment\nSection 1413a(f) of title 10, United States Code, is amended by striking Subsection (d) and inserting Subsection (c) .\n##### (f) Effective Date\nThe amendments made by this section shall take effect as of January 1, 2021, and shall apply to payments for months beginning on or after that date.",
      "versionDate": "2025-01-09",
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
            "name": "Disability and paralysis",
            "updateDate": "2025-03-05T16:10:34Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-05T16:10:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T15:40:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr303",
          "measure-number": "303",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr303v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Retired Pay Restoration Act</strong></p> <p>This bill allows the receipt of both military retired pay and veterans' disability compensation with respect to any service-connected disability. Under current law, only individuals with service-connected disabilities rated at 50% or more receive both without offset.</p> <p> Individuals who were retired or separated after at least 20 years of military service due to a service-connected disability shall be eligible for the full concurrent receipt of both veterans' disability compensation and either military retired pay or combat-related special pay.</p>"
        },
        "title": "Retired Pay Restoration Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr303.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Retired Pay Restoration Act</strong></p> <p>This bill allows the receipt of both military retired pay and veterans' disability compensation with respect to any service-connected disability. Under current law, only individuals with service-connected disabilities rated at 50% or more receive both without offset.</p> <p> Individuals who were retired or separated after at least 20 years of military service due to a service-connected disability shall be eligible for the full concurrent receipt of both veterans' disability compensation and either military retired pay or combat-related special pay.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr303"
    },
    "title": "Retired Pay Restoration Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Retired Pay Restoration Act</strong></p> <p>This bill allows the receipt of both military retired pay and veterans' disability compensation with respect to any service-connected disability. Under current law, only individuals with service-connected disabilities rated at 50% or more receive both without offset.</p> <p> Individuals who were retired or separated after at least 20 years of military service due to a service-connected disability shall be eligible for the full concurrent receipt of both veterans' disability compensation and either military retired pay or combat-related special pay.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr303"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr303ih.xml"
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
      "title": "Retired Pay Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:07Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Retired Pay Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to permit additional retired members of the Armed Forces who have a service-connected disability to receive both disability compensation from the Department of Veterans Affairs for their disability and either retired pay by reason of their years of military service or combat-related special compensation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T03:03:36Z"
    }
  ]
}
```
