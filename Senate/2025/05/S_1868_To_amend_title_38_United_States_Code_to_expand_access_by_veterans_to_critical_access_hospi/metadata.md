# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1868?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1868
- Title: Critical Access for Veterans Care Act
- Congress: 119
- Bill type: S
- Bill number: 1868
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-03-26T11:03:17Z
- Update date including text: 2026-03-26T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1868",
    "number": "1868",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Critical Access for Veterans Care Act",
    "type": "S",
    "updateDate": "2026-03-26T11:03:17Z",
    "updateDateIncludingText": "2026-03-26T11:03:17Z"
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
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
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
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
            "date": "2026-03-18T20:00:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:12Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-22T16:25:36Z",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "MT"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1868is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1868\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Cramer (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to expand access by veterans to critical access hospitals and affiliated clinics under the Veterans Community Care Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Critical Access for Veterans Care Act .\n#### 2. Expansion of access by veterans to critical access hospitals and affiliated clinics under Veterans Community Care Program\n##### (a) In general\nSubsection (d)(1) of section 1703 of title 38, United States Code, is amended\u2014\n**(1)**\nin subparagraph (D), by striking ; or and inserting a semicolon;\n**(2)**\nin subparagraph (E), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(F) with respect to care or services sought by a covered veteran at a critical access hospital or provider-based rural health clinic affiliated with such hospital (including any care or services sought from a health care provider specified in subsection (c) located in the surrounding community of such hospital or clinic due to a referral from such hospital or clinic), the veteran resides within 35 miles of such hospital or clinic. .\n##### (b) Prior authorization and referral\nSuch section is further amended\u2014\n**(1)**\nin subsection (a)(3), by striking A covered veteran and inserting Except as provided in subsection (d)(5), a covered veteran ; and\n**(2)**\nin subsection (d), by adding at the end the following new paragraph:\n(5) The Secretary may not require a covered veteran to receive authorization or a referral prior to the receipt of care or services under paragraph (1)(F). .\n##### (c) Payment rate and claims for care and services\nSubsection (i) of such section is amended by adding at the end the following new paragraph:\n(7) (A) With respect to care or services furnished under this section\u2014 (i) at a critical access hospital, including pursuant to subsection (d)(1)(F), the critical access hospital rate established under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) shall apply instead of the service-based rate; and (ii) at a provider-based rural health clinic affiliated with such hospital, including pursuant to subsection (d)(1)(F), the rate specified under section 1833 of the Social Security Act ( 42 U.S.C. 1395l ) shall apply. (B) Claims for covered veterans receiving care under subsection (d)(1)(F) shall include an identifier denoting the care or services provided under such subsection and shall be reimbursed at the cost-based level under the Medicare program. (C) The Secretary, in consultation with the Administrator of the Centers for Medicare & Medicaid Services, may furnish additional guidance regarding the claims process under this paragraph in accordance with the best practices of medicare administrative contractors (as defined in section 1874A(a)(3) of the Social Security Act ( 42 U.S.C. 1395kk\u20131(a)(3) )) in processing cost-based reimbursement for services furnished at critical access hospitals or provider-based rural health clinics affiliated with such hospitals. (D) Claims for covered veterans receiving care under subsection (d)(1)(F) shall be reviewed and payment shall be issued in accordance with the findings of such review not later than 60 days after the submission of the claim. .\n##### (d) Definitions\nSubsection (o) of such section is amended\u2014\n**(1)**\nby redesignating paragraph (2) as paragraph (3); and\n**(2)**\nby inserting after paragraph (1) the following new paragraph (2):\n(2) The term critical access hospital has the meaning given that term in section 1861(mm) of the Social Security Act ( 42 U.S.C. 1395x(mm) ). .\n##### (e) Report\n**(1) In general**\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress a report on third party administrators and community care providers concerning the implementation of the amendments made by this section, including timely approval and payment of claims under section 1703(d)(1)(F), as added by subsection (a), and overall user experience associated with care or services provided pursuant to such amendments.\n**(2) Definitions**\nIn this subsection:\n**(A) Community care provider**\nThe term community care provider means a health care provider specified in paragraph (1) or (5) of section 1703(c) of title 38, United States Code.\n**(B) Third party administrator**\nThe term third party administrator means an entity that manages a provider network and performs administrative services related to such network within the Veterans Community Care Program under section 1703 of title 38, United States Code.",
      "versionDate": "2025-05-22",
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
            "name": "Congressional oversight",
            "updateDate": "2025-12-12T21:06:54Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-12-12T21:06:49Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-12-12T21:06:06Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-12-12T21:05:56Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-12-12T21:06:42Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-12-12T21:05:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-05T18:38:35Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1868is.xml"
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
      "title": "Critical Access for Veterans Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Critical Access for Veterans Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to expand access by veterans to critical access hospitals and affiliated clinics under the Veterans Community Care Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:36Z"
    }
  ]
}
```
