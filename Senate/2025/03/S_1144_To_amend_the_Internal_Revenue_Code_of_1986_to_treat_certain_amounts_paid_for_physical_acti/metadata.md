# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1144?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1144
- Title: PHIT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1144
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-03-17T11:03:20Z
- Update date including text: 2026-03-17T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S1874)
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S1874)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1144",
    "number": "1144",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "PHIT Act of 2025",
    "type": "S",
    "updateDate": "2026-03-17T11:03:20Z",
    "updateDateIncludingText": "2026-03-17T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S1874)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
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
            "date": "2025-03-26T16:35:34Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-26T16:35:34Z",
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
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "WV"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "KS"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "GA"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1144is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1144\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Thune (for himself and Mr. Murphy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat certain amounts paid for physical activity, fitness, and exercise as amounts paid for medical care.\n#### 1. Short title\nThis Act may be cited as the Personal Health Investment Today Act of 2025 or the PHIT Act of 2025 .\n#### 2. Purpose\nThe purpose of this Act is to promote health and prevent disease, particularly diseases related to being overweight or obese, by\u2014\n**(1)**\nencouraging healthier lifestyles;\n**(2)**\nproviding financial incentives to ease the financial burden of engaging in healthy behavior; and\n**(3)**\nincreasing the ability of individuals and families to participate in physical fitness activities.\n#### 3. Certain amounts paid for physical activity, fitness, and exercise treated as amounts paid for medical care\n##### (a) In general\nParagraph (1) of section 213(d) of the Internal Revenue Code of 1986 is amended by striking or at the end of subparagraph (C), by striking the period at the end of subparagraph (D) and inserting , or , and by inserting after subparagraph (D) the following new subparagraph:\n(E) for qualified sports and fitness expenses. .\n##### (b) Qualified sports and fitness expenses\nSubsection (d) of section 213 of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(12) Qualified sports and fitness expenses (A) In general The term qualified sports and fitness expenses means amounts paid exclusively for the sole purpose of participating in a physical activity including\u2014 (i) for membership at a fitness facility, (ii) for participation or instruction in physical exercise or physical activity, or (iii) for equipment used in a program (including a self-directed program) of physical exercise or physical activity. (B) Overall dollar limitation The aggregate amount treated as qualified sports and fitness expenses with respect to any taxpayer for any taxable year shall not exceed $1,000 ($2,000 in the case of a joint return or a head of household (as defined in section 2(b))). (C) Fitness facility For purposes of subparagraph (A)(i), the term fitness facility means a facility\u2014 (i) which provides instruction in a program of physical exercise, offers facilities for the preservation, maintenance, encouragement, or development of physical fitness, or serves as the site of such a program of a State or local government or an organization described in section 501(c)(3) and exempt from tax under section 501(a), (ii) which is not a private club owned and operated by its members, (iii) which does not offer golf, hunting, sailing, or riding facilities, (iv) the health or fitness component of which is not incidental to its overall function and purpose, and (v) which is fully compliant with the State of jurisdiction and Federal anti-discrimination laws. (D) Treatment of exercise videos, etc Videos, books, and similar materials shall be treated as described in subparagraph (A)(ii) if the content of such materials constitutes instruction in a program of physical exercise or physical activity. (E) Limitations related to sports and fitness equipment Amounts paid for equipment described in subparagraph (A)(iii) shall be treated as qualified sports and fitness expenses only\u2014 (i) if such equipment is utilized exclusively for participation in fitness, exercise, sport, or other physical activity, (ii) in the case of amounts paid for apparel or footwear, if such apparel or footwear is of a type that is necessary for, and is not used for any purpose other than, a specific physical activity, and (iii) in the case of amounts paid for any single item of sports equipment (other than exercise equipment), to the extent such amounts do not exceed $250. (F) Programs which include components other than physical exercise and physical activity Rules similar to the rules of paragraph (6) shall apply in the case of any program that includes physical exercise or physical activity and also other components. For purposes of the preceding sentence, travel and accommodations shall be treated as a separate component. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-03-26",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2369",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PHIT Act of 2025",
      "type": "HR"
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
        "name": "Taxation",
        "updateDate": "2025-05-08T19:47:43Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1144is.xml"
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
      "title": "PHIT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PHIT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Personal Health Investment Today Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat certain amounts paid for physical activity, fitness, and exercise as amounts paid for medical care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:28Z"
    }
  ]
}
```
