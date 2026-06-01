# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3232?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3232
- Title: Family Caregiving Research and Innovation Act
- Congress: 119
- Bill type: S
- Bill number: 3232
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-04-16T19:20:04Z
- Update date including text: 2026-04-16T19:20:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3232",
    "number": "3232",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Family Caregiving Research and Innovation Act",
    "type": "S",
    "updateDate": "2026-04-16T19:20:04Z",
    "updateDateIncludingText": "2026-04-16T19:20:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
            "date": "2026-03-19T14:01:02Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-11-20T17:02:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3232is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3232\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Markey (for himself, Ms. Baldwin , Ms. Klobuchar , and Mr. Kim ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Older Americans Act of 1965 to authorize funding for the Research, Demonstration, and Evaluation Center for the Aging Network to engage in certain research and evaluation activities with respect to family caregivers and to revise the definition of the term family caregiver .\n#### 1. Short title\nThis Act may be cited as the Family Caregiving Research and Innovation Act .\n#### 2. Family caregivers\n##### (a) Research and evaluation activities\nSection 216(b) of the Older Americans Act of 1965 ( 42 U.S.C. 3020f(b) ) is amended\u2014\n**(1)**\nin paragraph (3), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (4), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(5) to carry out research and evaluation activities under section 201(g) that bolster data, research, and evidence-based practices with respect to family caregivers (as defined in section 302), $30,000,000 for each of fiscal years 2026 through 2030. .\n##### (b) Definition of family caregiver\n**(1) In general**\nSection 302 of the Older Americans Act of 1965 ( 42 U.S.C. 3022 ) is amended\u2014\n**(A)**\nby amending paragraph (3) to read as follows:\n(3) The term family caregiver \u2014 (A) means\u2014 (i) an adult family member, or another individual, who is an informal provider of in-home and community care to an older individual or to an individual of any age with Alzheimer's disease or a related disorder with neurological and organic brain dysfunction; or (ii) an older relative caregiver; and (B) does not include an individual providing care whose primary relationship with the individual receiving the care is based on a financial or professional agreement. ;\n**(B)**\nby redesignating paragraph (4) as paragraph (5); and\n**(C)**\nby inserting after paragraph (3) the following:\n(4) The term older relative caregiver means a caregiver who\u2014 (A) (i) is age 55 or older; and (ii) lives with, is the informal provider of in-home and community care to, and is the primary caregiver for, a child or an individual with a disability; (B) in the case of a caregiver for a child\u2014 (i) is the grandparent, stepgrandparent, or other relative (other than the parent) by blood, marriage, or adoption, of the child; (ii) is the primary caregiver of the child because the biological or adoptive parents are unable or unwilling to serve as the primary caregivers of the child; and (iii) has a legal relationship to the child, such as legal custody, adoption, or guardianship, or is raising the child informally; and (C) in the case of a caregiver for an individual with a disability, is the parent, grandparent, or other relative by blood, marriage, or adoption, of the individual with a disability. .\n**(2) National Family Caregiver Support Program**\n**(A) Definitions**\nSection 372(a) of the Older Americans Act of 1965 ( 42 U.S.C. 3030s(a) ) is amended\u2014\n**(i)**\nin paragraph (1), by striking or older relative caregiver ; and\n**(ii)**\nby striking paragraph (4).\n**(B) Program authorized**\nSection 373 of the Older Americans Act of 1965 ( 42 U.S.C. 3030s\u20131 ) is amended\u2014\n**(i)**\nin subsection (a), by striking systems and all that follows through the period and inserting systems of support services for family caregivers. ;\n**(ii)**\nby amending subsection (c)(1) to read as follows:\n(1) Population served (A) In general Subject to subparagraph (B), services under a State program under this part shall be provided to family caregivers. (B) Respite care and supplemental services With regard to the services specified in paragraphs (4) and (5) of subsection (b), in the case of a caregiver described in clause (i) of section 302(3)(A), such services shall be provided only to such a caregiver who is providing care to an older individual who meets the condition specified in subparagraph (A)(i) or (B) of section 102(22). ;\n**(iii)**\nin subsection (f)(3), by striking family caregivers, or older relative caregivers, and inserting family caregivers ; and\n**(iv)**\nin subsection (i)(1), by striking family caregivers and older relative caregivers and inserting family caregivers .\n**(3) Additional conforming amendment**\nSection 417(a)(1)(F)(i) of the Older Americans Act of 1965 ( 42 U.S.C. 3032f(a)(1)(F)(i) ) is amended by striking (as defined in section 372(a)) and inserting (as defined in section 302) .",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
            "name": "Adult day care",
            "updateDate": "2026-04-16T19:20:04Z"
          },
          {
            "name": "Aging",
            "updateDate": "2026-04-16T19:19:50Z"
          },
          {
            "name": "Family services",
            "updateDate": "2026-04-16T19:19:56Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2026-04-16T19:19:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-12-02T14:55:19Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3232is.xml"
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
      "title": "Family Caregiving Research and Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Family Caregiving Research and Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Older Americans Act to 1965 to authorize funding for the Research, Demonstration, and Evaluation Center for the Aging Network to engage in certain research and evaluation activities with respect to family caregivers and to revise the definition of the term \"family caregiver\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T05:33:19Z"
    }
  ]
}
```
