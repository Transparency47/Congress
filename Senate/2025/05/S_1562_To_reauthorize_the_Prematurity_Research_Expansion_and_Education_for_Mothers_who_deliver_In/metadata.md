# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1562?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1562
- Title: PREEMIE Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1562
- Origin chamber: Senate
- Introduced date: 2025-05-01
- Update date: 2026-01-31T13:48:18Z
- Update date including text: 2026-01-31T13:48:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in Senate
- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-01: Introduced in Senate

## Actions

- 2025-05-01 - IntroReferral: Introduced in Senate
- 2025-05-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1562",
    "number": "1562",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "PREEMIE Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-01-31T13:48:18Z",
    "updateDateIncludingText": "2026-01-31T13:48:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
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
            "date": "2025-05-01T16:19:23Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-01T16:19:23Z",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "AR"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "DE"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NM"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "MT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "WV"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "MS"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "NC"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "IL"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "VA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1562is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1562\nIN THE SENATE OF THE UNITED STATES\nMay 1, 2025 Mr. Bennet (for himself and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo reauthorize the Prematurity Research Expansion and Education for Mothers who deliver Infants Early Act.\n#### 1. Short title\nThis Act may be cited as the PREEMIE Reauthorization Act of 2025 .\n#### 2. Research relating to preterm labor and delivery and the care, treatment, and outcomes of preterm and low birthweight infants\n##### (a) In general\nSection 3(e) of the Prematurity Research Expansion and Education for Mothers who deliver Infants Early Act (42 U.S.C. 247b\u20134f(e)) is amended by striking fiscal years 2019 through 2023 and inserting fiscal years 2025 through 2029 .\n##### (b) Technical correction\nEffective as if included in the enactment of the PREEMIE Reauthorization Act of 2018 ( Public Law 115\u2013328 ), section 2 of such Act is amended, in the matter preceding paragraph (1), by striking Section 2 and inserting Section 3 .\n#### 3. Interagency working group\nSection 5(a) of the PREEMIE Reauthorization Act of 2018 ( Public Law 115\u2013328 ) is amended by striking The Secretary of Health and Human Services, in collaboration with other departments, as appropriate, may establish and inserting Not later than 18 months after the date of the enactment of the PREEMIE Reauthorization Act of 2025 , the Secretary of Health and Human Services, in collaboration with other departments, as appropriate, shall establish .\n#### 4. Study on preterm births\n##### (a) In general\nThe Secretary of Health and Human Services shall enter into appropriate arrangements with the National Academies of Sciences, Engineering, and Medicine under which the National Academies shall\u2014\n**(1)**\nnot later than 30 days after the date of enactment of this Act, convene a committee of experts in maternal health to study premature births in the United States; and\n**(2)**\nupon completion of the study under paragraph (1)\u2014\n**(A)**\napprove by consensus a report on the results of such study;\n**(B)**\ninclude in such report\u2014\n**(i)**\nan assessment of each of the topics listed in subsection (b);\n**(ii)**\nthe analysis required by subsection (c); and\n**(iii)**\nthe raw data used to develop such report; and\n**(C)**\nnot later than 24 months after the date of enactment of this Act, transmit such report to\u2014\n**(i)**\nthe Secretary of Health and Human Services;\n**(ii)**\nthe Committee on Energy and Commerce of the House of Representatives; and\n**(iii)**\nthe Committee on Finance and the Committee on Health, Education, Labor, and Pensions of the Senate.\n##### (b) Assessment topics\nThe topics listed in this subsection are each of the following:\n**(1)**\nThe financial costs of premature birth to society, including\u2014\n**(A)**\nan analysis of stays in neonatal intensive care units and the cost of such stays;\n**(B)**\nlong-term costs of stays in such units to society and the family involved post-discharge; and\n**(C)**\nhealth care costs for families post-discharge from such units (such as medications, therapeutic services, co-payments for visits, and specialty equipment).\n**(2)**\nThe factors that impact preterm birth rates.\n**(3)**\nOpportunities for earlier detection of premature birth risk factors, including\u2014\n**(A)**\nopportunities to improve maternal and infant health; and\n**(B)**\nopportunities for public health programs to provide support and resources for parents in-hospital, in non-hospital settings, and post-discharge.\n##### (c) Analysis\nThe analysis required by this subsection is an analysis of\u2014\n**(1)**\ntargeted research strategies to develop effective drugs, treatments, or interventions to bring at-risk pregnancies to term;\n**(2)**\nState and other programs\u2019 best practices with respect to reducing premature birth rates; and\n**(3)**\nprecision medicine and preventative care approaches starting early in the life course (including during pregnancy) with a focus on behavioral and biological influences on premature birth, child health, and the trajectory of such approaches into adulthood.",
      "versionDate": "2025-05-01",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-21T10:30:44Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1562is.xml"
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
      "title": "PREEMIE Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T13:48:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PREEMIE Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Prematurity Research Expansion and Education for Mothers who deliver Infants Early Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T04:18:43Z"
    }
  ]
}
```
