# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3119
- Title: Fisher House Availability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3119
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2026-03-30T20:50:19Z
- Update date including text: 2026-03-30T20:50:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3119",
    "number": "3119",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Fisher House Availability Act of 2025",
    "type": "S",
    "updateDate": "2026-03-30T20:50:19Z",
    "updateDateIncludingText": "2026-03-30T20:50:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
            "date": "2026-03-18T20:00:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:38Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-11-06T16:26:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3119is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3119\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Moran (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to make temporary lodging facilities of the Department of Veterans Affairs available for members of the Armed Forces, other individuals on active duty, and family members of such individuals on a space-available basis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fisher House Availability Act of 2025 .\n#### 2. Expansion of availability of Department of Veterans Affairs temporary lodging to certain individuals\nSection 1708 of title 38, United States Code, is amended\u2014\n**(1)**\nby amending subsection (a) to read as follows:\n(a) The Secretary may furnish persons described in subsection (b) with temporary lodging in a Fisher house or other appropriate facility in accordance with this section. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby amending paragraph (2) to read as follows:\n(2) A member of the family of a veteran described in paragraph (1) and others who accompany such veteran and provide the equivalent of familial support for such veteran. ; and\n**(B)**\nby adding at the end the following new paragraphs:\n(3) On a space-available basis\u2014 (A) an eligible individual who must travel a significant distance to receive care or services at a Department facility or non-Department facility; and (B) a member of the family of an eligible individual described in subparagraph (A) and others who accompany such eligible individual and provide the equivalent of familial support for such eligible individual during the receipt of care or services described in such subparagraph. (4) On a space-available basis\u2014 (A) a member of the family of a veteran who must travel a significant distance for such family member to receive care or services at a Department facility or non-Department facility; and (B) the veteran and others who accompany such family member and provide the equivalent of familial support for such family member during the receipt of care or services described in such subparagraph. (5) On a space-available basis\u2014 (A) a member of the family of an eligible individual who must travel a significant distance for such family member to receive care or services at a Department facility or non-Department facility; and (B) the eligible individual and others who accompany such family member and provide the equivalent of familial support for such family member during the receipt of care or services described in such subparagraph. ;\n**(3)**\nby striking subsection (c) and redesignating subsections (d) and (e) as subsections (c) and (d), respectively;\n**(4)**\nin subsection (d), as so redesignated\u2014\n**(A)**\nin paragraph (2), by striking subsection (d) and inserting subsection (c) ;\n**(B)**\nin paragraph (3), by striking a veteran under subsection (b)(2) and inserting an individual under subsection (b) ;\n**(C)**\nin paragraph (4), by striking and after the semicolon;\n**(D)**\nby redesignating paragraph (5) as paragraph (6); and\n**(E)**\nby inserting after paragraph (4) the following new paragraph (5):\n(5) establishing criteria for providing access to temporary lodging facilities on a space-available basis under paragraphs (3) through (5) of subsection (b); and ; and\n**(5)**\nby adding at the end the following new subsection:\n(e) In this section: (1) The term eligible individual means a member of the Armed Forces, regardless of duty status, or any individual on active duty. (2) The term Fisher house means a housing facility that\u2014 (A) is located at, or in proximity to, a Department medical facility; (B) is available for residential use on a temporary basis by patients of that facility and others described in subsection (b); and (C) is constructed by, and donated to the Secretary by, the Zachary and Elizabeth M. Fisher Armed Services Foundation or the Fisher House Foundation, Inc. .",
      "versionDate": "2025-11-06",
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
            "name": "Health care coverage and access",
            "updateDate": "2026-01-09T16:43:50Z"
          },
          {
            "name": "Housing supply and affordability",
            "updateDate": "2026-01-09T16:43:54Z"
          },
          {
            "name": "Military medicine",
            "updateDate": "2026-01-09T16:43:17Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2026-01-09T16:43:10Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2026-01-09T16:42:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:43:26Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3119is.xml"
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
      "title": "Fisher House Availability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fisher House Availability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T07:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to direct the Secretary of Veterans Affairs to make temporary lodging facilities of the Department of Veterans Affairs available for members of the Armed Forces, other individuals on active duty, and family members of such individuals on a space-available basis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T07:03:24Z"
    }
  ]
}
```
