# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3576?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3576
- Title: Veterans’ Life Insurance Expansion and Integrity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3576
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-12-12T09:07:46Z
- Update date including text: 2025-12-12T09:07:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3576",
    "number": "3576",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001325",
        "district": "3",
        "firstName": "Sheri",
        "fullName": "Rep. Biggs, Sheri [R-SC-3]",
        "lastName": "Biggs",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Veterans\u2019 Life Insurance Expansion and Integrity Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:46Z",
    "updateDateIncludingText": "2025-12-12T09:07:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-05-23",
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
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T15:43:24Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-05-26",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3576ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3576\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mrs. Biggs of South Carolina introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain improvements to the laws administered by the Secretary of Veterans Affairs relating to life insurance for veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans\u2019 Life Insurance Expansion and Integrity Act of 2025 .\n#### 2. Expansion of Department of Veterans Affairs life insurance program\n##### (a) In general\nSection 1922B of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1), by striking service-disabled ;\n**(B)**\nby striking paragraph (3); and\n**(C)**\nby redesignating paragraphs (4) through (6) as paragraphs (3) through (5), respsectively; and\n**(2)**\nin subsection (b), by striking the veteran has a service-connected disability and all that follows through the period at the end of paragraph (2) and inserting the following: the veteran submits an application for such insurance before the veteran attains 81 years of age .\n##### (b) Clerical amendment\n**(1) Section heading**\nSuch section is further amended by striking the section heading and inserting the following:\n1922B. Veterans life insurance .\n**(2) Table of sections**\nThe table of sections at the beginning of chapter 19 of such title is amended by striking the item relating to section 1922B and inserting the following new item:\n1922B. Veterans life insurance. .\n##### (c) Report\nNot later than two years after the date of the enactment of this Act, the Secretary of Veterans Affairs shall complete a study on the veterans life insurance program under section 1922B of such title (as amended by this Act) and submit to the Committees on Veterans Affairs of the House of Representatives and the Senate a report that includes, with respect to the period covered by the report\u2014\n**(1)**\nthe number of\u2014\n**(A)**\nveterans enrolled in such program;\n**(B)**\nclaims filed pursuant to such program;\n**(C)**\ninsurance payments made by the Secretary to claimants pursuant to such program;\n**(D)**\nthe total amount of insurance payments described in subparagraph (C); and\n**(E)**\ncontracts or policies for insurance under chapter 19 of such title cancelled or voided by the Secretary pursuant to section 1910 of such title (as amended by this Act) due to administrative error (as defined in such section);\n**(2)**\nan evaluation of\u2014\n**(A)**\nthe solvency and financial stability of such program; and\n**(B)**\nthe sufficiency of premiums under such program; and\n**(3)**\na statement of the cost savings to the United States resulting from the cancellation or voiding by the Secretary, pursuant to section 1910 of such title (as amended by this Act), of contracts or policies of insurance due to administrative error (as defined in such section).\n##### (d) Effective date\nThe amendments made by this section shall take effect on the date that is one year after the date of the enactment of this Act.\n#### 3. Contestability of certain Department of Veterans Affairs insurance contracts or policies issued due to administrative error\nSection 1910 of such title is amended\u2014\n**(1)**\nby inserting (a) In general.\u2014 before Subject to ;\n**(2)**\nby inserting and subsection (b), after section 1911 of this title ;\n**(3)**\nby inserting administrative error, after nonpayment of premium, ; and\n**(4)**\nby adding at the end the following new subsections:\n(b) Contests due to administrative error (1) Prior notice; opportunity to submit evidence With respect to any decision of the Secretary pursuant to this section to cancel or void a contract or policy of insurance due to administrative error, the Secretary shall provide the insured\u2014 (A) prior notice of such decision that includes an explanation of the administrative error underlying such cancellation or voiding; and (B) a period of not less than 90 days to submit to the Secretary evidence that no administrative error occurred with respect to such contract or policy. (2) Evidentiary review In any case where an insured submits to the Secretary evidence described in paragraph (1)(B), the Secretary shall determine whether such evidence satisfactorily demonstrates that no administrative error occurred with respect to the contract or policy of the insured by not later than 180 days after the date on which the Secretary receives such evidence. (3) Limitation The Secretary may not, pursuant to this section, cancel or void a contract or policy of insurance due to administrative error after the date that is one year after the date of the issuance, reinstatement, or conversion of such contract or policy. (4) Applicability This subsection shall apply with respect to any contract or policy for insurance, regardless of whether such contract became effective before, on, or after the date of the enactment of this subsection. (c) Administrative error defined In this section, the term administrative error means a clerical, technical, or processing mistake on the part of the Secretary that caused the issuance, reinstatement, or conversion of a contract or policy of insurance to an individual ineligible for such contract or policy on the date of such issuance, reinstatement, or conversion. .",
      "versionDate": "2025-05-23",
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
        "updateDate": "2025-06-05T18:47:38Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3576ih.xml"
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
      "title": "Veterans\u2019 Life Insurance Expansion and Integrity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans\u2019 Life Insurance Expansion and Integrity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain improvements to the laws administered by the Secretary of Veterans Affairs relating to life insurance for veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:35Z"
    }
  ]
}
```
