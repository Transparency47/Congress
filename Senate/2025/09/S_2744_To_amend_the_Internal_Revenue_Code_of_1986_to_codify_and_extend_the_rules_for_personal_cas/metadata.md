# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2744?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2744
- Title: Federal Disaster Tax Relief Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2744
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2026-05-13T11:03:32Z
- Update date including text: 2026-05-13T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2744",
    "number": "2744",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Federal Disaster Tax Relief Act of 2025",
    "type": "S",
    "updateDate": "2026-05-13T11:03:32Z",
    "updateDateIncludingText": "2026-05-13T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-09",
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
            "date": "2025-09-09T21:07:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-09T21:07:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "FL"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2744is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2744\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to codify and extend the rules for personal casualty losses arising from major disasters and the rules for the exclusion from gross income of compensation for losses or damages resulting from certain wildfires.\n#### 1. Short title\nThis Act may be cited as the Federal Disaster Tax Relief Act of 2025 .\n#### 2. Codification and extension of rules for casualty losses arising from major disasters\n##### (a) Treatment of losses\n**(1) In general**\nSection 165(h) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(6) Special rule for qualified disaster losses (A) In general If an individual has a qualified net disaster loss for any taxable year, the amount determined under paragraph (2)(A)(ii) shall be the sum of\u2014 (i) such net disaster loss, and (ii) so much of the excess referred to in the matter preceding clause (i) of paragraph (2)(A) (reduced by the amount in clause (i) of this subparagraph) as exceeds 10 percent of the adjusted gross income of the individual. (B) Qualified net disaster loss For purposes of subparagraph (A), the term qualified net disaster loss means the excess of qualified disaster-related personal casualty losses over personal casualty gains. (C) Qualified disaster-related personal casualty losses (i) In general For purposes of this subsection, the term qualified disaster-related personal casualty losses means losses described in subsection (c)(3) (determined after application of paragraph (1)) which arise in a qualified disaster area on or after the first day of the incident period of the qualified disaster to which such area relates, and which are attributable to such disaster. (ii) Qualified disaster area The term qualified disaster area means any area with respect to which a major disaster has been declared by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act if the incident period of the disaster with respect to which such declaration is made begins after July 4, 2025, and before January 1, 2027. (iii) Qualified disaster The term qualified disaster means, with respect to any qualified disaster area, the disaster by reason of which a major disaster was declared with respect to such area. (iv) Incident period For purposes of this paragraph, the term incident period means, with respect to any qualified disaster, the period specified by the Federal Emergency Management Agency as the period during which such disaster occurred. .\n**(2) Conforming amendment**\nSection 165(h)(5)(B)(ii) of such Code is amended by inserting or (6) after paragraph (2)(A) .\n##### (b) Dollar limitation\nSection 165(h)(1) of the Internal Revenue Code of 1986 is amended by striking $500 ($100 for taxable years beginning after December 31, 2009) and inserting $100 ($500 in the case of any net disaster loss to which paragraph (3) applies) .\n##### (c) Standard deduction\n**(1) In general**\nSection 63(c)(1) of the Internal Revenue Code of 1986 is amended by striking and at the end of subparagraph (A), by striking the period at the end of subparagraph (B) and inserting and , and by adding at the end the following new subparagraph:\n(C) the disaster loss deduction. .\n**(2) Disaster loss deduction**\nSection 63(c) of such Code is amended by adding at the end the following new paragraph:\n(8) Disaster loss deduction For the purposes of paragraph (1), the term disaster loss deduction means the excess of qualified net disaster losses (as defined in section 165(h)(6)(B)) over the amount of personal casualty gains (as defined in section 165(h)(3)(A)) reduced by any portion of such gains taken into account under section 165(h)(5)(B)(i). .\n##### (d) Treatment under alternative minimum tax\nSection 56(b)(1)(D) of the Internal Revenue Code of 1986 is amended by inserting (other than the disaster loss deduction) after section 63(c) .\n##### (e) Effective date\nThe amendments made by this section shall apply to losses incurred in taxable years beginning after December 31, 2024.\n#### 3. Codification and extension of exclusion from gross income of compensation for losses or damages resulting from certain wildfires\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139M. Compensation for losses or damages resulting from certain wildfires (a) In general Gross income shall not include any amount received by an individual as a qualified wildfire relief payment. (b) Definitions; qualified wildfire relief payment For purposes of this section\u2014 (1) In general The term qualified wildfire relief payment means any amount received by or on behalf of an individual as compensation for losses, expenses, or damages (including compensation for additional living expenses, lost wages (other than compensation for lost wages paid by the employer which would have otherwise paid such wages), personal injury, death, or emotional distress) incurred as a result of a qualified wildfire disaster, but only to the extent the losses, expenses, or damages compensated by such payment are not compensated for by insurance or otherwise. (2) Qualified wildfire disaster The term qualified wildfire disaster means any Federally declared disaster (as defined in section 165(i)(5)(A)) after December 31, 2014, as a result of any forest or range fire. (c) Denial of double benefit Notwithstanding any other provision of this title\u2014 (1) no deduction or credit shall be allowed (to the person for whose benefit a qualified wildfire relief payment is made) for, or by reason of, any expenditure to the extent of the amount excluded under this section with respect to such expenditure, and (2) no increase in the basis or adjusted basis of any property shall result from any amount excluded under this section with respect to such property. (d) Limitation on application This section shall only apply to qualified wildfire relief payments received by the individual during taxable years beginning after December 31, 2025, and before January 1, 2031. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting before the item related to section 140 the following new item:\nSec. 139M. Compensation for losses or damages resulting from certain wildfires. .\n##### (c) Effective date\nThe amendments made by this section shall apply to payments received in taxable years beginning after December 31, 2025.",
      "versionDate": "2025-09-09",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-09-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5225",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-28",
        "text": "Received in the Senate and Read twice and referred to the Committee on Finance."
      },
      "number": "5366",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Doug LaMalfa Federal Disaster Tax Relief Certainty Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-04",
        "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S8514)"
      },
      "number": "3372",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Innocent Victims of Taxation After Fire Extension Act",
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
            "name": "Disaster relief and insurance",
            "updateDate": "2026-04-28T13:49:05Z"
          },
          {
            "name": "Fires",
            "updateDate": "2026-04-28T13:48:52Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-04-28T13:48:58Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2026-04-28T13:48:46Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2026-04-28T13:49:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-09-18T15:49:48Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2744is.xml"
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
      "title": "Federal Disaster Tax Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Disaster Tax Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to codify and extend the rules for personal casualty losses arising from major disasters and the rules for the exclusion from gross income of compensation for losses or damages resulting from certain wildfires.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:18Z"
    }
  ]
}
```
