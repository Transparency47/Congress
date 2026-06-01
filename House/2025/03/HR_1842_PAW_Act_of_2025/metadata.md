# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1842?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1842
- Title: PAW Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1842
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2025-09-18T08:07:13Z
- Update date including text: 2025-09-18T08:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1842",
    "number": "1842",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "PAW Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-18T08:07:13Z",
    "updateDateIncludingText": "2025-09-18T08:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:04:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "MI"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1842ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1842\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Ms. Tenney (for herself and Ms. Ross ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow certain veterinary expenses for pets and service animals to be treated as amounts paid for medical care for purposes of a health savings account or flexible savings account.\n#### 1. Short title\nThis Act may be cited as the People and Animals Well-being Act of 2025 or the PAW Act of 2025 .\n#### 2. Certain amounts paid for veterinary care treated as amounts paid for medical care\n##### (a) In general\nSection 213(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(12) Certain amounts paid for veterinary care treated as paid for medical care (A) In general An amount paid or incurred by the taxpayer during the taxable year for the following shall be treated as paid for medical care: (i) Any amount paid or incurred for veterinary care or a pet health insurance plan of a service animal of the taxpayer, the taxpayer\u2019s spouse, or a dependant of the taxpayer. (ii) In the case of a pet of the taxpayer, the taxpayer\u2019s spouse, or a dependent of the taxpayer, so much as does not exceed\u2014 (I) $1,000 of the amount paid or incurred by the taxpayer for veterinary care for such pet, and (II) $1,000 for a pet health insurance plan of such pet. (iii) Pet For purposes of this subparagraph, the term pet has the meaning given such term in section 12502(b)(9)(D) of the Agriculture Improvement Act of 2018. (iv) Service animal For purposes of this subparagraph, the term service animal has the meaning given such term in section 36.104 of title 28, Code of Federal Regulations (or any successor regulation). (v) Veterinary care For the purposes of this subparagraph, the term veterinary care means amounts paid for the diagnosis, cure, mitigation, treatment, or prevention of disease, condition, or injury, including diagnostic tests, medicine, medical equipment, nutritional products, surgery, and other services or items as authorized or prescribed by a veterinarian licensed by a State or a territory of the United States to practice veterinary medicine. (B) Inflation adjustment (i) In general In the case of any taxable year beginning after 2025, each dollar amount in subparagraph (A)(ii) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which such taxable year begins determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (ii) Rounding If any increase under clause (i) is not a multiple of $50, such increase shall be rounded to the nearest multiple of $50. .\n##### (c) Effective date\nThe amendment made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act.",
      "versionDate": "2025-03-04",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T14:08:57Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1842ih.xml"
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
      "title": "PAW Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PAW Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "People and Animals Well-being Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow certain veterinary expenses for pets and service animals to be treated as amounts paid for medical care for purposes of a health savings account or flexible savings account.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:48:29Z"
    }
  ]
}
```
